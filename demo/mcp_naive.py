"""
mcp_naive.py

Represents how a typical MCP tool-calling agent behaves today: parse the
request, call the tool, done. No policy check, no structured proof --
just a transaction hash. This is deliberately how current blockchain
MCP servers (e.g. Base MCP) work: they execute what they're told.
"""

from intent_parser import parse_intent
from chain_executor import execute_swap


def run(request: str) -> dict:
    intent = parse_intent(request)
    result = execute_swap(intent["from_asset"], intent["to_asset"], intent["amount"])
    return {"intent": intent, "result": result}
