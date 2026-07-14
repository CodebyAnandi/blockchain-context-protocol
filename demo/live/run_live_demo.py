"""
run_live_demo.py

The real version of the demo: fetches actual wallet state from Sepolia,
checks a requested transfer against policy, and -- only if it passes --
signs and broadcasts a real transaction. Prints a link you can open on
Sepolia Etherscan as proof.

Setup (see README.md in this folder for full details):
    1. cp .env.example .env
    2. Fill in .env with your testnet RPC URL, wallet, and private key
    3. pip install -r requirements.txt
    4. python run_live_demo.py
"""

import os
import json
import time
from dotenv import load_dotenv

load_dotenv()

from live_context import get_context
from live_chain_executor import execute_transfer


def load_policy() -> dict:
    with open("policy.json") as f:
        return json.load(f)


def check_policy(amount_eth: float, policy: dict) -> dict:
    rules = {k: v for rule in policy["rules"] for k, v in rule.items()}
    max_amount = rules.get("max_amount_eth")
    if max_amount is not None and amount_eth > max_amount:
        return {
            "allowed": False,
            "reason": f"Requested {amount_eth} ETH exceeds policy max of {max_amount} ETH.",
        }
    return {"allowed": True, "reason": "Amount within policy limit."}


def run(amount_eth: float):
    print("Fetching real context from Sepolia testnet...")
    context = get_context()
    print(json.dumps(context, indent=2))

    balance = float(context["account"]["balances"][0]["amount"])
    if balance == 0:
        print(
            "\nWallet balance is 0. Get free Sepolia ETH from a faucet "
            "(e.g. https://sepoliafaucet.com) before running this demo."
        )
        return

    policy = load_policy()
    intent = {"goal": f"Transfer {amount_eth} ETH", "amount_eth": amount_eth}
    check = check_policy(amount_eth, policy)

    print(f"\nIntent: {json.dumps(intent)}")
    print(f"Policy check: {json.dumps(check)}")

    if not check["allowed"]:
        proof = {"status": "denied", "intent": intent, "reason": check["reason"], "timestamp": time.time()}
        print(f"\nDENIED -- no transaction was sent.\nProof: {json.dumps(proof, indent=2)}")
        return

    print("\nPolicy passed. Signing and broadcasting real transaction...")
    result = execute_transfer(amount_eth)
    proof = {
        "status": "executed",
        "intent": intent,
        "reason": check["reason"],
        "tx_hash": result["tx_hash"],
        "timestamp": time.time(),
    }
    print(f"\nEXECUTED.\nProof: {json.dumps(proof, indent=2)}")
    print(f"\nView on Sepolia Etherscan: {result['explorer_url']}")


if __name__ == "__main__":
    # Try an amount ABOVE the 0.001 ETH policy limit first to see it get
    # blocked, then edit this value to something under the limit (e.g.
    # 0.0001) and re-run to see a real transaction go through.
    run(amount_eth=0.01)
