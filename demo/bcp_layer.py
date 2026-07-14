"""
bcp_layer.py

The same request, run through the missing layer: Intent -> Policy check
-> Execution -> Proof. If the intent violates policy, execution never
happens, and the reason is logged instead of a transaction.
"""

import json
import time

from intent_parser import parse_intent
from policy_engine import load_policy, validate_intent
from chain_executor import execute_swap


def run(request: str, context_path: str = "context.json", policy_path: str = "policy.json") -> dict:
    with open(context_path) as f:
        context = json.load(f)
    policy = load_policy(policy_path)

    intent = parse_intent(request)
    check = validate_intent(intent, context, policy)

    if not check["allowed"]:
        proof = {
            "status": "denied",
            "intent": intent,
            "reason": check["reason"],
            "timestamp": time.time(),
        }
        return {"intent": intent, "policy_check": check, "result": None, "proof": proof}

    result = execute_swap(intent["from_asset"], intent["to_asset"], intent["amount"])
    proof = {
        "status": "executed",
        "intent": intent,
        "reason": check["reason"],
        "tx_hash": result["tx_hash"],
        "timestamp": time.time(),
    }
    return {"intent": intent, "policy_check": check, "result": result, "proof": proof}
