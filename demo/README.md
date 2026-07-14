# BCP Demo: The Missing Policy/Proof Layer

A minimal, runnable proof of the gap this repo's [`SPEC.md`](../SPEC.md) describes:
**current MCP tool-calling executes what it's told; it has no built-in
concept of checking an action against rules before running it, or
producing a verifiable record of why an action was allowed or denied.**

This demo is intentionally small. It does not reimplement blockchain
context-fetching (that's already solved — see [Base MCP](https://docs.base.org)
and [1inch's MCP server](https://portal.1inch.dev)) and it does not touch a
real chain (no funds, no RPC keys, no risk). It isolates and demonstrates
only the piece that's missing: **Intent → Policy → Execution → Proof.**

## What it shows

The same natural-language request — *"Swap 5 ETH for USDC on Uniswap"* —
run through two paths:

| | `mcp_naive.py` | `bcp_layer.py` |
|---|---|---|
| Parses request into structured intent | ✅ | ✅ |
| Checks intent against policy before acting | ❌ | ✅ |
| Executes | Always | Only if policy check passes |
| Produces a verifiable proof of *why* | ❌ (just a tx hash) | ✅ (reason + tx hash, or denial + reason) |

The demo wallet holds 10 ETH. The policy caps any single trade at 20% of
balance (2 ETH). A request for 5 ETH:

- **`mcp_naive.py` executes it anyway** — no check exists to stop it.
- **`bcp_layer.py` blocks it**, logging: *"Trade size is 50.0% of ETH
  balance, exceeds policy max of 20%."*

A second, smaller request (1 ETH) passes policy and executes on both
paths — showing the BCP layer doesn't block everything, only what
violates its explicit rules.

## Running it

No blockchain connection, RPC key, or funds required — execution is
simulated (see [`chain_executor.py`](chain_executor.py)).

```bash
pip install anthropic   # optional — only needed for real NLP intent parsing
python run_demo.py
```

By default, intent parsing uses a small offline regex fallback so the
demo runs with zero setup. To see a real LLM doing the natural-language
→ structured-intent conversion instead, set an API key first:

```bash
export ANTHROPIC_API_KEY=your_key_here
python run_demo.py
```

## Files

- `context.json` — mock wallet state (10 ETH, 2000 USDC)
- `policy.json` — mock policy rules (max trade size, allowed protocols, max slippage)
- `intent_parser.py` — natural language → structured Intent object (Claude API or offline fallback)
- `policy_engine.py` — validates an Intent against Policy + Context
- `chain_executor.py` — simulated swap execution (swap for a real MCP tool call to run against a live testnet)
- `mcp_naive.py` — the "problem": parse → execute, no check
- `bcp_layer.py` — the "solution": parse → check → execute-or-deny → log proof
- `run_demo.py` — runs both paths side by side and prints the comparison

## What this does *not* claim to prove

This is a small, honest demo, not a production system. It doesn't:

- Connect to a real chain (execution is mocked)
- Implement the Extended Interface (multi-chain aggregation, simulation
  engines, MEV-aware routing, intent markets)
- Solve identity/trust (that's [ERC-8004](https://eips.ethereum.org)'s job, not BCP's)

It exists to make one narrow point concrete: **the policy/proof layer
described in SPEC.md Section 5–7 doesn't exist in current MCP tooling,
and this is what it looks like when it does.**
