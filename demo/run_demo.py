"""
run_demo.py

Runs the same natural-language request through both paths and prints a
side-by-side comparison. This is the core proof: the naive MCP-style
path executes a policy-violating trade; the BCP layer catches and
blocks it, with a logged reason.

Usage:
    python run_demo.py
    (optionally set ANTHROPIC_API_KEY to use real Claude parsing
     instead of the offline regex fallback)
"""

import json
import mcp_naive
import bcp_layer


# This request intentionally asks for a trade larger than the demo
# policy allows (20% of balance). Wallet holds 10 ETH, so the policy
# permits at most 2 ETH per trade -- this request asks for 5.
RISKY_REQUEST = "Swap 5 ETH for USDC on Uniswap with 0.3% slippage"

# This one stays within policy limits.
SAFE_REQUEST = "Swap 1 ETH for USDC on Uniswap with 0.3% slippage"


def divider(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_scenario(label: str, request: str):
    divider(f"SCENARIO: {label}")
    print(f"Request: \"{request}\"\n")

    divider("  -> mcp_naive.py (current MCP-style behavior)")
    naive_result = mcp_naive.run(request)
    print(json.dumps(naive_result, indent=2))

    divider("  -> bcp_layer.py (Intent -> Policy -> Execution -> Proof)")
    bcp_result = bcp_layer.run(request)
    print(json.dumps(bcp_result, indent=2))


if __name__ == "__main__":
    run_scenario("Oversized trade (violates policy)", RISKY_REQUEST)
    run_scenario("Trade within policy limits", SAFE_REQUEST)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(
        "The naive MCP-style path executes both requests without question.\n"
        "The BCP layer blocks the oversized trade with a logged reason,\n"
        "and only produces a verifiable proof for the trade that passes policy."
    )
