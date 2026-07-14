"""
live_chain_executor.py

Signs and broadcasts a REAL transaction on Sepolia testnet. This
replaces the parent demo's chain_executor.py mock with an actual
on-chain action -- this is what turns the demo from "console output"
into "a transaction you can look up on Etherscan."

Only ever used with a throwaway testnet wallet holding free faucet ETH.
"""

import os
from web3 import Web3


def execute_transfer(amount_eth: float) -> dict:
    rpc_url = os.environ["SEPOLIA_RPC_URL"]
    private_key = os.environ["PRIVATE_KEY"]
    sender = os.environ["WALLET_ADDRESS"]
    recipient = os.environ["RECIPIENT_ADDRESS"]

    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise ConnectionError(f"Could not connect to RPC at {rpc_url}")

    sender = Web3.to_checksum_address(sender)
    recipient = Web3.to_checksum_address(recipient)

    nonce = w3.eth.get_transaction_count(sender)
    tx = {
        "nonce": nonce,
        "to": recipient,
        "value": w3.to_wei(amount_eth, "ether"),
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
        "chainId": 11155111,  # Sepolia chain ID
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_hash_hex = tx_hash.hex()

    return {
        "status": "executed",
        "amount_eth": amount_eth,
        "tx_hash": tx_hash_hex,
        "explorer_url": f"https://sepolia.etherscan.io/tx/0x{tx_hash_hex}"
        if not tx_hash_hex.startswith("0x")
        else f"https://sepolia.etherscan.io/tx/{tx_hash_hex}",
    }
