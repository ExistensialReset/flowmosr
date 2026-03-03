# LOTUS BASELINE RECOVERY CHECKLIST
## Quick Reference for Recovery Actions

**Reference:** `BASELINE_RECOVERY_PROTOCOL.md` v1.1  
**Purpose:** Ensure all Baseline violations are handled correctly, auditable, and traceable.

---

## 1. Identify Violation
- [ ] Node(s) below Global Baseline metric (energy, food, water, space, time, air, electricity)  
- [ ] Verified via: Self-declaration / Peer confirmation / Sensor validation / LOTUS dispute confirmation  
- [ ] Timestamp and log created in `/compostandgrowth/baseline_violations/`  

---

## 2. Determine Recovery Level
- [ ] **Level 1 – Node Self-Correction** (72h limit)  
  - Internal surplus reallocation  
  - Distribution adjustment  
  - Voluntary surplus window triggered  
- [ ] **Level 2 – Regional Recovery** (7-day limit)  
  - Scan regional surplus nodes & emergency pools  
  - Redistribute via `FLOW_SURPLUS_PROTOCOL.md`  
  - Report to LOTUS at day 3 and day 7  
- [ ] **Level 3 – Global Recovery**  
  - Activate only if regional insufficient or multiple regional failures  
  - Prioritize: biological needs → energy stability → infrastructure repair  
  - Audit & log full redistribution

---

## 3. Emergency Override
- [ ] Triggered by: War / Planetary Disaster / Grid Collapse / Regional Governance Failure  
- [ ] Requires: Regional LOTUS supermajority OR 66% Global LOTUS override  
- [ ] Log justification & timestamp  
- [ ] Automatic post-facto audit & ratification

---

## 4. Monitoring & Reporting
- [ ] Node: Progress report at 24/48/72h  
- [ ] Regional: KPI & audit logs at day 3 & day 7  
- [ ] Global: Full audit and ledger update  
- [ ] Metrics linked to thresholds in `RISK_MANAGEMENT.md`

---

## 5. Data Privacy
- [ ] Public: number of violations, regional recovery rates, global interventions  
- [ ] Private: individual/household-level data anonymized in all reports

---

## 6. Completion Status
- [ ] Action marked as: Mitigated / Escalated / Resolved  
- [ ] All logs linked and stored in `/compostandgrowth/baseline_violations/`  
- [ ] LOTUS confirms closure

---

✅ **All items checked → Baseline violation properly resolved and auditable**

```mermaid
flowchart TD
    %% Subgraphs
    subgraph LEVEL1["1️⃣ Node Self-Correction"]
        direction TB
        N1["🔹 Reallocate internal surplus"]:::medium
        N2["🔹 Adjust distribution priorities"]:::medium
        N3["🔹 Trigger voluntary surplus window"]:::medium
        N4["⏱ 72h Time limit"]:::high
    end

    subgraph LEVEL2["2️⃣ Regional Recovery"]
        direction TB
        R1["🔹 Scan regional surplus & emergency pools"]:::medium
        R2["🔹 Redistribute via FLOW_SURPLUS_PROTOCOL"]:::high
        R3["⏱ 7-day limit"]:::high
        R4["📊 Report to LOTUS"]:::medium
    end

    subgraph LEVEL3["3️⃣ Global Recovery"]
        direction TB
        G1["🔹 Activate only if regional insufficient OR multiple failures"]:::critical
        G2["🔹 Prioritize: biological needs → energy → infrastructure"]:::high
        G3["📋 Full audit & ledger update"]:::high
        G4["🔁 Return authority to regional layer post-stabilization"]:::medium
    end

    subgraph EMERGENCY["4️⃣ Emergency Override"]
        direction TB
        E1["⚠️ Triggered by Crisis"]:::critical
        E2["🗳️ Regional supermajority OR 66% Global LOTUS vote"]:::critical
        E3["⏳ Automatic post-facto audit & ratification"]:::high
    end

    %% Connections
    N1 --> N2 --> N3 --> N4 --> R1
    R1 --> R2 --> R3 --> R4 --> G1
    G1 --> G2 --> G3 --> G4
    E1 --> E2 --> E3 --> G3

    %% Styling
    classDef critical fill:#ff6666,stroke:#900,stroke-width:2px,color:#fff;
    classDef high fill:#ffcc66,stroke:#996600,stroke-width:2px,color:#000;
    classDef medium fill:#66ccff,stroke:#006699,stroke-width:2px,color:#000;
```