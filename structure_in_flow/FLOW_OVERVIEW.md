# FLOW Overview 🌿🌀

**Purpose:** Provide a visual overview of the Flow system, including decision-making bodies, the LOTUS protocol, and baseline knowledge.

**Scope:** Covers all main components of Flow, including Nodes, Spirals, Baseline Knowledge, and the LOTUS lottery process.

---

## Components

- **Nodes & Teams** – physical or organized groups that verify and participate in Flow processes.  
- **LOTUS Protocol** – democratic lottery for decision-making bodies and recovery sets.  
- **Flow Baseline Knowledge** – non-coercion, post-monetary, LxSxI: Calm × Spontaneity × Empathy.  
- **RNG & Logs** – verifiable, auditable, and privacy-preserving.  
- **Decision Documentation & Audit** – anonymized, exportable, and reviewable.  
- **Spiral Structure** – real-time, realistic, and maximal spirals for project timelines.

---

## Key Principles

1. **Decentralized & Democratic** – all decision bodies and Mirrors are selected by lottery.  
2. **Mandate of Nine Moons** – maximum 9 months for mandates; other mandates run until decision is reached.  
3. **Flow Baseline** – LxSxI, non-coercion, post-monetary, anonymized data storage, deletable once per year.  
4. **Sustainability** – devices can be repaired and reused; no forced hardware upgrades for Flow services.  
5. **Privacy & Security** – no PII stored on-chain; verification and recovery follow encrypted, auditable procedures.

---

## Mermaid Diagram

```mermaid
flowchart LR
    %% MAIN FLOW NODE
    FLOW["FLOW 🌿"]:::flow_main

    %% SUBGRAPHS
    subgraph NODES_Group["Nodes & Teams 🏢"]
        NODES["Participating Nodes"]:::nodes
    end

    subgraph LOTUS_Group["LOTUS Protocol 🌸"]
        LOTUS["LOTUS Core"]:::lotus
        LOTTERY["Lottery Selection 🎲"]:::lotus
        MANDATE["Mandate Rules 📜"]:::lotus
        RECOVERY["Recovery & Social Attestation 🔄"]:::lotus
        LOTUS --> LOTTERY
        LOTUS --> MANDATE
        LOTUS --> RECOVERY
        LOTTERY --> POOL["Qualified Pool 🧑‍💻"]
        LOTTERY --> CONFLICT["Conflict Screening 🤝"]
        LOTTERY --> TRAINING["Post-Selection Training 🏫"]
        MANDATE --> DURATION["Mandate Duration ⏳"]
        MANDATE --> EXTENSIONS["Interim Extensions 🔄"]
    end

    subgraph RNG_Group["RNG & Verification 🔑"]
        RNG["RNG Core"]:::rng
        SEED["Seed & Nonce 🗝️"]:::rng
        VERIFY["Deterministic Verification ✔️"]:::rng
        RNG --> SEED
        RNG --> VERIFY
    end

    subgraph DECISION_Group["Decision & Audit 📝📊"]
        DECISION["Decision Logs & Anonymized Votes"]:::decision
        LOGS["Decision Logs 🗂️"]:::decision
        ANON["Anonymized Votes 🕵️‍♀️"]:::decision
        DECISION --> LOGS
        DECISION --> ANON
    end

    subgraph BASELINE_Group["Flow Baseline Knowledge 🌱"]
        BASELINE["Core Principles"]:::baseline
        NONCOERCION["Non-Coercion 💛"]:::baseline
        LxSxI["LxSxI: Calm×Spontaneity×Empathy 🧘"]:::baseline
        POSTMONEY["Post-Monetary 🌍"]:::baseline
        BASELINE --> NONCOERCION
        BASELINE --> LxSxI
        BASELINE --> POSTMONEY
    end

    subgraph SPIRAL_Group["Spiral Structure 🌀"]
        SPIRALS["Project Spirals"]:::spiral
    end

    %% CONNECTIONS TO MAIN FLOW
    FLOW --> NODES
    FLOW --> LOTUS
    FLOW --> BASELINE
    FLOW --> SPIRALS
    FLOW --> DECISION
    FLOW --> RNG

    %% STYLES
    classDef flow_main fill:#A3E4D7,stroke:#2C3E50,stroke-width:3px,color:#2C3E50
    classDef nodes fill:#F7DC6F,stroke:#B9770E,stroke-width:2px,color:#2C3E50
    classDef lotus fill:#F5B7B1,stroke:#C0392B,stroke-width:2px,color:#2C3E50
    classDef baseline fill:#ABEBC6,stroke:#196F3D,stroke-width:2px,color:#2C3E50
    classDef decision fill:#AED6F1,stroke:#1B4F72,stroke-width:2px,color:#2C3E50
    classDef rng fill:#D2B4DE,stroke:#6C3483,stroke-width:2px,color:#2C3E50
    classDef spiral fill:#F9E79F,stroke:#B7950B,stroke-width:2px,color:#2C3E50```