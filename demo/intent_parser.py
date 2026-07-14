"""
intent_parser.py

Converts a natural-language request into a structured BCP Intent object.

If an ANTHROPIC_API_KEY environment variable is set, this uses the real
Claude API to do the parsing -- showing how an actual agent would form
an Intent. If no key is set, it falls back to a small regex-based parser
so the demo still runs end-to-end with zero setup.

Either way, the *output shape* is what matters for the rest of the demo:

{
  "goal": str,
  "from_asset": str,
  "to_asset": str,
  "amount": float,
  "protocol": str,
  "max_slippage_pct": float
}
"""

import os
import re
import json


INTENT_SCHEMA_PROMPT = """Convert the following request into a JSON object with
exactly these fields: goal (string), from_asset (string, e.g. "ETH"),
to_asset (string, e.g. "USDC"), amount (number), protocol (string, e.g.
"Uniswap"), max_slippage_pct (number). Respond with ONLY the JSON object,
no markdown, no explanation.

Request: {request}
"""


def parse_with_claude(request: str) -> dict:
    from anthropic import Anthropic

    client = Anthropic()  # reads ANTHROPIC_API_KEY from env
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": INTENT_SCHEMA_PROMPT.format(request=request)}],
    )
    text = response.content[0].text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)


def parse_with_regex_fallback(request: str) -> dict:
    """Very small pattern matcher, just enough to drive the demo offline."""
    amount_match = re.search(r"(\d+(\.\d+)?)\s*(ETH|USDC)", request, re.IGNORECASE)
    to_match = re.search(r"for\s+(ETH|USDC)", request, re.IGNORECASE)
    protocol_match = re.search(r"on\s+(\w+)", request, re.IGNORECASE)
    slippage_match = re.search(r"(\d+(\.\d+)?)\s*%\s*slippage", request, re.IGNORECASE)

    amount = float(amount_match.group(1)) if amount_match else 0.0
    from_asset = amount_match.group(3).upper() if amount_match else "ETH"
    to_asset = to_match.group(1).upper() if to_match else "USDC"
    protocol = protocol_match.group(1) if protocol_match else "Uniswap"
    slippage = float(slippage_match.group(1)) if slippage_match else 0.3

    return {
        "goal": request,
        "from_asset": from_asset,
        "to_asset": to_asset,
        "amount": amount,
        "protocol": protocol,
        "max_slippage_pct": slippage,
    }


def parse_intent(request: str) -> dict:
    if os.environ.get("ANTHROPIC_API_KEY"):
        try:
            return parse_with_claude(request)
        except Exception as e:
            print(f"[intent_parser] Claude API call failed ({e}), falling back to regex parser.")
    return parse_with_regex_fallback(request)
