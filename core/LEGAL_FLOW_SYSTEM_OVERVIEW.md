# 🗂️ Legal Flow System Overview — Core Reference

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** High-level map of core and structure-in-flow documents, showing relationships between architecture, policy, operational protocols, verification, and legal flows. Designed to orient contributors quickly, highlight dependencies, and serve as a reference for pilots and audits.  

---

## 1. Core Files (`/core`)

| File | Type | Purpose / Notes |
|------|------|----------------|
| `M-OS-R_AS_AN_OPERATING_SYSTEM.md` | Architecture | System-wide OS perspective |
| `M-OS-R_SYSTEM_MAP.md` | Architecture | Map of system modules & dependencies |
| `CORE_FLOW_PROTOCOLS.md` | Protocol | Operational rules for Flows |
| `CORE_GUIDERAIL.md` | Policy | Safety & integrity guardrails |
| `FLOW_CORE_INVARIANTS.md` | Policy | Fundamental invariants to maintain |
| `FLOW_CORE_STRUCTURE_OVERVIEW.md` | Overview | High-level structure of flows |
| `FLOW_GLOBAL_IMPLEMENTATION_GUIDE.md` | Guide | Global deployment & operational guidance |
| `FLOW_ID*.md` | Schema/Policy | Identification, lifecycle, and node policy templates |
| `RESOURCE_METRIC_STANDARDS.md` | Standard | Baseline metrics for resource tracking |
| `ETHOS_SAFEGUARDS.md` | Policy | Ethical & safety measures |
| `RNG_AND_LOG_SPEC.md` | Technical | Randomization & logging standards |
| `STRATEGIC_PREPARATION_FRAMEWORK*.md` | Planning | Strategic & operational preparation |
| `STRUCTURAL_INVARIANTS.md` | Policy | Core invariants for flow integrity |
| `POWER_AND_ENFORCEMENT.md` | Governance | Enforcement powers & limits |
| `ENTRY_STRATEGIES_DOCUMENTATION.md` | Guide | Node entry & activation strategies |
| `BODY_OF_*` series | Reference / Knowledge | Human measurement, flow body reference |

---

## 2. Structure-in-Flow Files (`/structure_in_flow`)

| File | Type | Purpose / Notes |
|------|------|----------------|
| `COMPLETE_LEGAL_RESPONSE_PLAYBOOK.md` | Legal | Compelled disclosure playbook |
| `LEGAL_OVERVIEW_FLOW.md` | Legal / Overview | High-level legal flow and guidance |
| `EVIDENCE_DECISION_MATRIX_UNFORGIVABLE_HARM.md` | Policy / Protocol | Decision matrix for high-risk incidents |
| `UNFORGIVABLE_HARM_PROTOCOL.md` | Operational | Stepwise protocol for unforgivable harm |
| `ANONYMOUS_VERIFICATION_WORKFLOW.md` | Protocol | Verification workflow for anonymous reports |
| `FLOW_VERIFICATION_PROTOCOL.md` | Protocol | Verification steps & documentation |
| `FLOW_NODES_AND_TEAMS_STRUCTURE.md` | Organizational | Node roles and team mapping |
| `FLOW_MASTER_ARCHITECTURE.md` | Architecture | Master system map |
| `FLOW_MASTER_SCHEME.md` | Architecture | High-level flow scheme |
| `FLOW_SPIRAL_*.md` series | Operational / Planning | Flow spirals & timeline modeling |
| `FLOW_OVERVIEW.md` | Overview | Summary of flow structure |
| `HARM_SUMMARY.md` | Operational | Overview of harm categories & flows |
| `ANONYMOUS_RESOURCE_TRACKING_IN_FLOW.md` | Protocol | Resource tracking without revealing identities |
| `RESOURCE_TRACKING_AND_COORDINATION_IN_FLOW.md` | Operational | Coordination & flow-level resource tracking |
| `FLOW_GOVERNANCE_LOTTERIES.md` | Governance | Node lotteries & selection mechanisms |
| `FLOW_LOTTERY_PARAMETERS_AND_RNG_SPEC_visual.md` | Technical / Visual | RNG & lottery parameter visualization |
| `NODE_DEFINITION.md` | Organizational | Node definitions & responsibilities |
| `FLOW_UNIVERSAL_REPORTING.md` | Operational | Standardized reporting mechanisms |
| `NO_CURRENCY_RESOURCE_ALLOCATION_IN_FLOW.md` | Policy | Currency-free resource allocation |

---

## 3. High-Level Relationships (Mermaid)

```mermaid
flowchart TD
    style CORE fill:#f0f8ff,stroke:#333,stroke-width:2px
    style STRUCTURE_IN_FLOW fill:#fff0f5,stroke:#333,stroke-width:2px

    subgraph CORE
        A[M-OS-R_SYSTEM_MAP]
        B[CORE_FLOW_PROTOCOLS]
        C[RESOURCE_METRIC_STANDARDS]
        D[FLOW_CORE_INVARIANTS]
        E[FLOW_GLOBAL_IMPLEMENTATION_GUIDE]
        F[ETHOS_SAFEGUARDS]
    end

    subgraph STRUCTURE_IN_FLOW
        G[COMPLETE_LEGAL_RESPONSE_PLAYBOOK]
        H[LEGAL_OVERVIEW_FLOW]
        I[EVIDENCE_DECISION_MATRIX_UNFORGIVABLE_HARM]
        J[UNFORGIVABLE_HARM_PROTOCOL]
        K[ANONYMOUS_VERIFICATION_WORKFLOW]
        L[FLOW_VERIFICATION_PROTOCOL]
        M[FLOW_NODES_AND_TEAMS_STRUCTURE]
        N[FLOW_MASTER_ARCHITECTURE]
        O[FLOW_MASTER_SCHEME]
        P[FLOW_SPIRAL_*]
        Q[FLOW_OVERVIEW]
        R[HARM_SUMMARY]
        S[ANONYMOUS_RESOURCE_TRACKING_IN_FLOW]
        T[RESOURCE_TRACKING_AND_COORDINATION_IN_FLOW]
        U[FLOW_GOVERNANCE_LOTTERIES]
        V[FLOW_LOTTERY_PARAMETERS_AND_RNG_SPEC_visual]
        W[NODE_DEFINITION]
        X[FLOW_UNIVERSAL_REPORTING]
        Y[NO_CURRENCY_RESOURCE_ALLOCATION_IN_FLOW]
    end

    %% Relationships
    A --> B
    B --> D
    C --> B
    D --> E
    E --> F
    B --> G
    B --> H
    G --> I
    G --> J
    I --> L
    H --> L
    L --> M
    M --> N
    N --> O
    P --> O
    Q --> N
    R --> J
    S --> T
    U --> V
    W --> X
    Y --> X