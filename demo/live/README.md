# Live Demo: Real Testnet Execution

This is the "hands dirty" version of the [`demo/`](../) folder — instead
of a simulated `execute_swap()`, this signs and broadcasts a **real
transaction on Sepolia testnet**, gated by the same Intent → Policy →
Execution → Proof pattern.

At the end, you get a real transaction hash you can look up on
[Sepolia Etherscan](https://sepolia.etherscan.io) — actual proof this
happened, not console output.

⚠️ **Testnet only. Zero real financial value. Read the safety notes below
before doing anything.**

## What's different from the main demo

- `live_context.py` fetches your **real** wallet balance from Sepolia via RPC, instead of reading a mock `context.json`.
- `live_chain_executor.py` **signs and sends a real transaction** using web3.py, instead of faking a tx hash.
- Simplified to a plain ETH transfer (not a DEX swap) — swaps need a deployed router contract + ABI + token approvals, which is a much bigger lift. A transfer proves the same thing: real signing, real broadcast, real policy gate.

## Setup

### 1. Create a throwaway testnet wallet

**Do not use a wallet that holds real funds.** In MetaMask: click your
account icon → "Add account" → create a brand new one, used only for
this. Copy its address.

Export its private key: Account Details → Show Private Key. This key
will only ever touch free testnet ETH.

### 2. Get free Sepolia ETH

Use a faucet, e.g. [sepoliafaucet.com](https://sepoliafaucet.com) or
[Alchemy's Sepolia faucet](https://www.alchemy.com/faucets/ethereum-sepolia).
Paste in your new wallet's address. This gives you free test ETH with
zero real-world value.

### 3. Get a free RPC endpoint

Sign up at [Alchemy](https://www.alchemy.com) (or [Infura](https://infura.io)),
create an app, select the **Sepolia** network, and copy the HTTPS RPC URL.

### 4. Configure your environment

```bash
cd demo/live
cp .env.example .env
```

Open `.env` and fill in:
- `SEPOLIA_RPC_URL` — from step 3
- `PRIVATE_KEY` — from step 1 (the throwaway wallet's key)
- `WALLET_ADDRESS` — the throwaway wallet's public address
- `RECIPIENT_ADDRESS` — any address to send test ETH to (can be a second account you control)

**`.env` is already in `.gitignore` — it will never be committed.**
Double-check before pushing anything: run `git status` and confirm
`.env` does not appear as a tracked file.

### 5. Install dependencies and run

```bash
pip install -r requirements.txt
python run_live_demo.py
```

## What you'll see

The script requests a 0.01 ETH transfer by default — above the demo's
0.001 ETH policy limit — so the **first run will be denied**, with no
transaction sent:

```
Policy check: {"allowed": false, "reason": "Requested 0.01 ETH exceeds policy max of 0.001 ETH."}
DENIED -- no transaction was sent.
```

Open `run_live_demo.py`, change the amount at the bottom to something
under the limit (e.g. `0.0001`), and run it again. This time it passes
policy, signs, and broadcasts a real transaction:

```
EXECUTED.
Proof: { ... "tx_hash": "0x...", ... }
View on Sepolia Etherscan: https://sepolia.etherscan.io/tx/0x...
```

Open that link. That's a real, on-chain, verifiable action — gated by
a policy check that ran before it was allowed to happen.

## Safety notes

- Never commit `.env` or paste your private key anywhere public.
- Never reuse a wallet that holds real funds for this.
- The 0.001 ETH policy cap in `policy.json` is intentionally tiny — even
  if something went wrong, you're only ever risking free testnet ETH.
