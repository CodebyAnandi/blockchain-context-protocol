# Blockchain Context Protocol (BCP)

**Giving AI Agents a Native Interface to Blockchains**

Version: v1.0 Protocol Specification · Status: Draft Standard
Author: [Anandi Sheladiya](https://www.researchgate.net/profile/Anandi-Sheladiya) · Independent Researcher
Email: codebyanandi@gmail.com
License: [CC BY 4.0](LICENSE)

Preprint: [ResearchGate](https://www.researchgate.net/publication/408877989_Blockchain_Context_Protocol_Giving_AI_Agents_a_Native_Interface_to_Blockchains) · DOI: [10.13140/RG.2.2.16419.00807](https://doi.org/10.13140/RG.2.2.16419.00807)

---

## Abstract

Blockchains expose state and execution through transaction-centric interfaces such as JSON-RPC. These interfaces are optimized for deterministic execution but are poorly suited for autonomous AI agents that operate using goals, constraints, and reasoning workflows.

The Blockchain Context Protocol (BCP) proposes a standardized interface layer that allows AI agents to interact with blockchain systems using structured context, declarative intents, verifiable execution plans, and policy-based constraints.

BCP introduces an agent-native interaction model that sits above existing blockchain execution standards such as ERC-4337, ERC-6900, and emerging agent authorization proposals. Rather than replacing transaction infrastructure, BCP introduces a reasoning and coordination layer enabling safe, explainable, and programmable agent behavior.

## Why BCP?

Current blockchain interfaces require AI agents to construct raw transactions, query fragmented state across RPC endpoints, rely on centralized indexers, and implement proprietary safety logic. This results in poor interoperability, increased security risk, limited explainability, and high implementation complexity.

BCP addresses this by introducing four coordination layers above existing execution infrastructure:

| Layer | Purpose |
|---|---|
| **Context Layer** | Provides normalized blockchain state |
| **Intent Layer** | Defines goal-oriented agent requests |
| **Policy Layer** | Defines constraints and safety boundaries |
| **Execution Layer** | Plans and executes verifiable actions |

```
+------------------------------------------------------+
|                     AI AGENT                          |
|  Planning . Reasoning . Learning                      |
+-----------------------^--------------------------------+
                         |
+------------------------------------------------------+
|        Blockchain Context Protocol (BCP)              |
|                                                        |
|  Context Engine     -> State Normalization            |
|  Intent Engine      -> Goal Translation                |
|  Policy Engine      -> Constraint Verification         |
|  Execution Planner  -> Action Strategy                 |
+-----------------------^--------------------------------+
                         |
+------------------------------------------------------+
|        Smart Account / Agent Authorization             |
|   ERC-4337 . ERC-6900 . ERC-8004                       |
+-----------------------^--------------------------------+
                         |
+------------------------------------------------------+
|                    BLOCKCHAIN                          |
+------------------------------------------------------+
```

## Repository Contents

- [`SPEC.md`](SPEC.md) — Full protocol specification (v1.0 draft)
- [`demo/`](demo/) — Minimal runnable proof of the core gap: Intent → Policy → Execution → Proof, side by side with naive MCP-style execution
- [`examples/`](examples/) — Reference JSON objects for Context, Intent, Policy, and Execution Plan
- [`CHANGELOG.md`](CHANGELOG.md) — Version history
- [`LICENSE`](LICENSE) — CC BY 4.0

## Protocol Interfaces

- **BCP Core Interface** — minimal primitives: context query, intent submission, policy validation, execution
- **BCP Extended Interface** — multi-chain context aggregation, simulation engines, MEV-aware route optimization, intent market integration, cryptographic proof framework

See [`SPEC.md`](SPEC.md) Section 6 for full endpoint definitions.

## Interoperability

BCP is designed to sit above, not replace, existing Ethereum standards:

- **ERC-4337** — BCP execution plans translate into UserOperations
- **ERC-6900** — BCP policies can be implemented as modular account extensions
- **ERC-8004** (proposed) — defines agent delegation and authorization

## Status

This is a **draft standard (v1.0)**, not peer-reviewed. Feedback, issues, and discussion are welcome — open an issue or start a discussion in this repo.

## Citation

If you reference BCP in your own work, please cite:

```
Sheladiya, A. (2026). Blockchain Context Protocol: Giving AI Agents a Native
Interface to Blockchains. DOI: 10.13140/RG.2.2.16419.00807
```

## License

This work is licensed under [CC BY 4.0](LICENSE) — you're free to share and adapt it, including commercially, with attribution.
