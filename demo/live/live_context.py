"""
live_context.py

Fetches REAL wallet state from Sepolia testnet -- this is the Context
Layer, using an actual RPC connection instead of the mocked context.json
in the parent demo/ folder.
"""

import os
from web3 import Web3


def get_context() -> dict:
    rpc_url = os.environ["SEPOLIA_RPC_URL"]
    address = os.environ["WALLET_ADDRESS"]

    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise ConnectionError(f"Could not connect to RPC at {rpc_url}")

    balance_wei = w3.eth.get_balance(Web3.to_checksum_address(address))
    balance_eth = float(w3.from_wei(balance_wei, "ether"))
    gas_price_gwei = float(w3.from_wei(w3.eth.gas_price, "gwei"))

    return {
        "account": {
            "address": address,
            "balances": [{"asset": "ETH", "amount": str(balance_eth)}],
        },
        "network": {
            "chain": "sepolia-testnet",
            "gas": gas_price_gwei,
        },
    }
