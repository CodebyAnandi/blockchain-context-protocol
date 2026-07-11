# Blockchain Context Protocol (BCP)

**Giving AI Agents a Native Interface to Blockchains**

Version: v1.0 Protocol Specification
Status: Draft Standard
Author: Anandi Sheladiya — Independent Researcher
Email: codebyanandi@gmail.com
Date: July 2026

Preprint: https://www.researchgate.net/publication/408877989_Blockchain_Context_Protocol_Giving_AI_Agents_a_Native_Interface_to_Blockchains
DOI: 10.13140/RG.2.2.16419.00807

---

## Abstract

Blockchains expose state and execution through transaction-centric interfaces such as JSON-RPC. These interfaces are optimized for deterministic execution but are poorly suited for autonomous AI agents that operate using goals, constraints, and reasoning workflows.

The Blockchain Context Protocol (BCP) proposes a standardized interface layer that allows AI agents to interact with blockchain systems using structured context, declarative intents, verifiable execution plans, and policy-based constraints.

BCP introduces an agent-native interaction model that sits above existing blockchain execution standards such as ERC-4337, ERC-6900, and emerging agent authorization proposals. Rather than replacing transaction infrastructure, BCP introduces a reasoning and coordination layer enabling safe, explainable, and programmable agent behavior.

---

## 1. Introduction

### 1.1 Motivation

Autonomous agents are increasingly performing tasks involving blockchain systems, including:

- DeFi portfolio management
- Automated trading and arbitrage
- DAO governance participation
- Treasury operations
- Cross-chain asset routing
- On-chain service orchestration

Current blockchain interfaces require agents to:

- Construct raw transactions
- Query fragmented state across RPC endpoints
- Rely on centralized indexers
- Implement proprietary safety and simulation logic

This results in:

- Poor interoperability
- Increased security risk
- Limited explainability
- High implementation complexity

**Problem Statement**

Blockchains lack a standardized machine-readable context layer suitable for AI-driven decision systems.

### 1.2 Design Goals

BCP aims to:

- Provide structured blockchain state for agent reasoning
- Enable declarative intent-based execution
- Introduce verifiable policy enforcement
- Support multi-step execution planning
- Provide execution proofs and explainability
- Remain compatible with existing blockchain standards

---

## 2. Background

### 2.1 JSON-RPC Limitations

JSON-RPC provides low-level transaction and state access. It assumes:

- Caller already knows execution steps
- Caller performs off-chain reasoning
- Execution success is binary

RPC lacks:

- Semantic context
- Policy frameworks
- Intent abstraction
- Execution planning primitives

### 2.2 Emerging Agent Infrastructure

Several standards address agent execution primitives. BCP complements these standards by providing a coordination interface.

---

## 3. System Overview

BCP introduces four primary components:

1. **Context Layer** — Provides normalized blockchain state.
2. **Intent Layer** — Defines goal-oriented agent requests.
3. **Policy Layer** — Defines constraints and safety boundaries.
4. **Execution Layer** — Plans and executes verifiable actions.

---

## 4. Architecture

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

*Figure 1. BCP layered architecture, positioned above smart-account authorization and below agent reasoning.*

---

## 5. BCP Core Concepts

### 5.1 Context Object

BCP defines standardized state objects.

Example ([`examples/context.json`](examples/context.json)):

```json
{
  "account": {
    "address": "0xAgent",
    "balances": [
      {"asset": "USDC", "amount": "5000"},
      {"asset": "ETH", "amount": "2"}
    ],
    "positions": [
      {"protocol": "Aave", "collateral": "ETH", "health": 1.8}
    ]
  },
  "network": {
    "chain": "ethereum",
    "gas": 45
  }
}
```

### 5.2 Intent Object

Intents describe desired outcomes instead of transactions.

Example ([`examples/intent.json`](examples/intent.json)):

```json
{
  "goal": "Optimize yield",
  "constraints": {
    "max_risk": "medium",
    "max_slippage": "0.5%"
  }
}
```

### 5.3 Policy Object

Policies define enforceable execution rules.

Example ([`examples/policy.json`](examples/policy.json)):

```json
{
  "rules": [
    {"max_trade_size": "20%"},
    {"allowed_protocols": ["Aave", "Uniswap"]}
  ]
}
```

### 5.4 Execution Plan

Execution plans define multi-step strategies.

Example ([`examples/execution_plan.json`](examples/execution_plan.json)):

```json
{
  "steps": [
    {"action": "withdraw", "protocol": "Aave"},
    {"action": "swap", "protocol": "Uniswap"}
  ]
}
```

---

## 6. Protocol Specification

### 6.1 BCP Core Interface — Minimal Interface

The Core Interface introduces basic primitives for agent execution.

#### 6.1.1 Endpoints

**Context Query**
```
GET /bcp/context/{account}
```
Returns normalized blockchain state.

**Intent Submission**
```
POST /bcp/intent
```
Accepts declarative goal objects.

**Policy Validation**
```
POST /bcp/policy/validate
```
Verifies constraints.

**Execution**
```
POST /bcp/execute
```
Triggers execution via smart accounts.

#### 6.1.2 Execution Flow

1. Agent → Request Context
2. Agent → Generate Intent
3. BCP → Validate Policy
4. BCP → Generate Execution Plan
5. Smart Account → Execute
6. BCP → Return Proof

### 6.2 BCP Extended Interface — Advanced Agent Coordination

The Extended Interface introduces:

- **Multi-chain Context Aggregation** — Unified cross-chain state views.
- **Simulation Engines** — Pre-execution state forecasting.
- **Route Optimization** — MEV-aware execution planning.
- **Intent Market Integration** — Third-party solver coordination.
- **Proof Framework** — Cryptographic execution attestations.

---

## 7. Security Model

BCP relies on multiple security layers:

- **Authorization** — Delegation through trustless agent standards.
- **Policy Enforcement** — Pre-execution rule validation.
- **Simulation** — Risk forecasting and rollback prevention.
- **Verifiable Proofs** — Execution attestation and auditability.

---

## 8. Interoperability

BCP is designed to integrate with existing Ethereum standards.

### 8.1 ERC-4337

BCP execution plans are translated into UserOperations.

### 8.2 ERC-6900

BCP policies can be implemented as modular account extensions.

### 8.3 ERC-8004 (Proposed)

Defines agent delegation and authorization.

---

## 9. Real-World Use Cases

### 9.1 Autonomous DeFi Portfolio Agents

Agents rebalance assets based on risk-adjusted yield metrics.

### 9.2 DAO Governance Agents

Agents vote according to predefined treasury policies.

### 9.3 Cross-Chain Payment Routing

Agents optimize transaction routes across L2s and bridges.

### 9.4 On-chain Service Automation

Agents subscribe, renew, and manage decentralized services.

---

## 10. Implementation Considerations

### 10.1 Off-chain BCP Providers

Initial implementations may run as decentralized indexing and execution networks.

### 10.2 On-chain Policy Modules

Policy engines can be deployed as verifiable smart contracts.

### 10.3 Standardization Path

BCP may evolve through:

- Ethereum Improvement Proposals
- Open agent interoperability consortiums
- Integration with AI model orchestration standards

---

## 11. Limitations

- Requires standardized indexing infrastructure
- Introduces additional coordination latency
- Policy standardization remains unsolved
- Cross-chain trust models need formal verification

---

## 12. Future Research Directions

- ZK-based context verification
- Intent auction markets
- Agent reputation scoring
- Autonomous policy learning
- Decentralized execution solvers

---

## 13. Conclusion

Blockchain Context Protocol introduces an agent-native interface for blockchain coordination. By shifting interaction from transaction construction to intent execution, BCP enables safer, more interoperable, and programmable agent ecosystems.

BCP is not a replacement for blockchain execution standards. Instead, it represents a coordination layer enabling AI systems to safely reason about and operate within decentralized environments.
