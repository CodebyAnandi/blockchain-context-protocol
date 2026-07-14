"""
policy_engine.py

The piece current MCP tool-calling does not provide: a check that runs
*before* execution, using explicit, auditable rules -- not a model's
best judgement in the moment.
"""

import json


def load_policy(path: str = "policy.json") -> dict:
    with open(path) as f:
        return json.load(f)


def validate_intent(intent: dict, context: dict, policy: dict) -> dict:
    """
    Checks an Intent object against Policy rules and the current Context.
    Returns {"allowed": bool, "reason": str}.
    """
    rules = {k: v for rule in policy["rules"] for k, v in rule.items()}

    from_asset = intent["from_asset"]
    amount = intent["amount"]

    # Find current balance of the asset being spent
    balances = {b["asset"]: float(b["amount"]) for b in context["account"]["balances"]}
    balance = balances.get(from_asset)

    if balance is None:
        return {"allowed": False, "reason": f"No {from_asset} balance found in context."}

    # Rule 1: max trade size as % of balance
    max_pct = rules.get("max_trade_size_pct_of_balance")
    if max_pct is not None:
        pct_of_balance = (amount / balance) * 100
        if pct_of_balance > max_pct:
            return {
                "allowed": False,
                "reason": (
                    f"Trade size is {pct_of_balance:.1f}% of {from_asset} balance, "
                    f"exceeds policy max of {max_pct}%."
                ),
            }

    # Rule 2: allowed protocols
    allowed_protocols = rules.get("allowed_protocols")
    if allowed_protocols is not None and intent.get("protocol") not in allowed_protocols:
        return {
            "allowed": False,
            "reason": f"Protocol '{intent.get('protocol')}' is not in allowed list {allowed_protocols}.",
        }

    # Rule 3: max slippage
    max_slippage = rules.get("max_slippage_pct")
    if max_slippage is not None and intent.get("max_slippage_pct", 0) > max_slippage:
        return {
            "allowed": False,
            "reason": (
                f"Requested slippage {intent.get('max_slippage_pct')}% exceeds "
                f"policy max of {max_slippage}%."
            ),
        }

    return {"allowed": True, "reason": "Intent satisfies all policy rules."}
