"""
chain_executor.py

Simulated blockchain execution.

In a real deployment, this function would be replaced by an actual
MCP tool call (e.g. Base MCP's swap tool, or a direct web3.py call to a
testnet DEX). It is mocked here so this demo runs anywhere with zero
setup, zero API keys, and zero financial risk -- the point of this repo
is to demonstrate the *missing policy/proof layer*, not to re-build a
working DEX integration.

Swap this function's body for a real MCP tool call when you're ready to
run against a live testnet.
"""

import random
import time


def execute_swap(from_asset: str, to_asset: str, amount: float) -> dict:
    """Simulates executing a swap on-chain and returns a fake tx receipt."""
    time.sleep(0.2)  # pretend this takes a moment, like a real tx would
    fake_tx_hash = "0x" + "".join(random.choices("0123456789abcdef", k=64))
    return {
        "status": "executed",
        "from_asset": from_asset,
        "to_asset": to_asset,
        "amount": amount,
        "tx_hash": fake_tx_hash,
    }
