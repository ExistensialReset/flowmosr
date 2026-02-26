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
    %% Main FLOW system
    FLOW["FLOW 🌿"]:::flow
    FLOW --> NODES["Nodes & Teams 🏢"]:::nodes
    FLOW --> LOTUS["LOTUS Protocol 🌸"]:::lotus
    FLOW --> BASELINE["Flow Baseline Knowledge 🌱"]:::baseline
    FLOW --> SPIRALS["Spiral Structure 🌀"]:::spirals
    FLOW --> DECISION["Decision & Audit 📝📊"]:::decision
    FLOW --> RNG["RNG & Verification 🔑"]:::rng

    %% LOTUS subcomponents
    LOTUS --> LOTTERY["Lottery Selection 🎲"]:::lotus
    LOTUS --> MANDATE["Mandate Rules 📜"]:::lotus
    LOTUS --> RECOVERY["Recovery & Social Attestation 🔄"]:::lotus

    LOTTERY --> POOL["Qualified Pool 🧑‍💻"]:::lotus
    LOTTERY --> CONFLICT["Conflict Screening 🤝"]:::lotus
    LOTTERY --> TRAINING["Post-Selection Training 🏫"]:::lotus

    MANDATE --> DURATION["Mandate Duration ⏳"]:::lotus
    MANDATE --> EXTENSIONS["Interim Extensions 🔄"]:::lotus

    %% Decision & RNG interactions
    DECISION --> LOGS["Decision Logs 🗂️"]:::decision
    DECISION --> ANON["Anonymized Votes 🕵️‍♀️"]:::decision
    DECISION --> RNG
    RNG --> DECISION

    RNG --> SEED["Seed & Nonce 🗝️"]:::rng
    RNG --> VERIFY["Deterministic Verification ✔️"]:::rng
    SEED --> LOTTERY
    VERIFY --> LOTTERY
    RNG --> RECOVERY

    %% Baseline influence
    BASELINE --> NONCOERCION["Non-Coercion 💛"]:::baseline
    BASELINE --> LxSxI["LxSxI: Calm×Spontaneity×Empathy 🧘"]:::baseline
    BASELINE --> POSTMONEY["Post-Monetary 🌍"]:::baseline
    BASELINE --> NODES
    BASELINE --> LOTUS

    %% Spirals connections
    SPIRALS --> NODES
    SPIRALS --> DECISION
    SPIRALS --> LOTUS

    %% Feedback loops
    LOGS --> LOTUS
    POOL --> NODES
    TRAINING --> NODES
    RECOVERY --> NODES
    EXTENSIONS --> LOTUS

    %% Styling
    classDef flow fill:#2a9d8f,stroke:#264653,stroke-width:2px,color:#ffffff;
    classDef nodes fill:#457b9d,stroke:#1d3557,stroke-width:2px,color:#ffffff;
    classDef lotus fill:#9b5de5,stroke:#6a0dad,stroke-width:2px,color:#ffffff;
    classDef spirals fill:#f08a5d,stroke:#d35d00,stroke-width:2px,color:#ffffff;
    classDef baseline fill:#52b788,stroke:#1b4332,stroke-width:2px,color:#ffffff;
    classDef decision fill:#6c757d,stroke:#343a40,stroke-width:2px,color:#ffffff;
    classDef rng fill:#f94144,stroke:#7f0000,stroke-width:2px,color:#ffffff; ```
