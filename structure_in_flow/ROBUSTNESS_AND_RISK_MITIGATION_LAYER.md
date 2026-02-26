# 🛡️ Robustness & Risk Mitigation Layer — v2

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Sammanställer identifierade svagheter och föreslagna motåtgärder med ägarskap och prioritet. Ska fungera som levande lager för självkorrigerande system.

---

## 1. Core Identity & Verification Risks

| Risk | Severity | Owner | Status | Mitigation |
|------|---------|-------|--------|------------|
| Randomized social verification | Critical | Node Leads / LOTUS | Not started | Multi-layer verification; verifier training; periodic audits; reputation weighting |
| Recovery Set without incentive | High | Node Leads / Dev Team | Not started | Introduce clear incentives (reputation points, eligibility for privileges) |
| Reduced privileges for non-secure devices | High | Node Leads | Not started | Define restricted actions explicitly; communicate to participants |
| Community Membership Card discrimination | Medium | LOTUS | Not started | Standardization guidelines; LOTUS review respecting local sovereignty |

---

## 2. Lifecycle & Policy Gaps

| Risk | Severity | Owner | Status | Mitigation |
|------|---------|-------|--------|------------|
| Multi-party verification undefined | High | Dev Team / Node Leads | Not started | SOP detailing initiator, steps, logging |
| Temporary deactivation / reactivation unclear | Medium | Node Leads | Not started | Define reactivation protocol, approval process, and reference FLOW_ID_LIFECYCLE.md |
| Permanent deletion / anonymization | Medium | LOTUS | Not started | Legal review per jurisdiction; clear retention policy |
| ID type cultural limitations | Medium | Node Leads | Not started | Include regional alternatives and examples |
| Verifier conflict of interest | High | Node Leads / LOTUS | Not started | Mandatory relationship declaration system |

---

## 3. Governance & LOTUS Protocol Risks

| Risk | Severity | Owner | Status | Mitigation |
|------|---------|-------|--------|------------|
| Undefined supermajority / veto rules | Critical | LOTUS | Not started | Specify ratios, eligible veto actors |
| Exclusion of local node in incident review | Medium | LOTUS | Not started | Allow advisory input; document rationale |
| Panel support & short training | Medium | LOTUS | Not started | Provide extended onboarding and debriefing support |

---

## 4. RNG, Logs & Resource Risks

| Risk | Severity | Owner | Status | Mitigation |
|------|---------|-------|--------|------------|
| Private seed security | Critical | Node Leads / Dev Team | Not started | Multi-party seed generation; public randomness supplement |
| Seed loss recovery | High | Node Leads | Not started | Backup protocols with encrypted, distributed storage |
| Retention periods | Medium | Node Leads | Not started | Configurable retention with justification per case |

---

## 5. Structural & Operational Risks

| Risk | Severity | Owner | Status | Mitigation |
|------|---------|-------|--------|------------|
| Transparency vs privacy | High | LOTUS / Node Leads | Not started | Minimal necessary data; hash sensitive fields |
| Self-containment challenges | Medium | Node Leads | Not started | Incremental self-sufficiency milestones |
| Soft social nudges | Medium | Node Leads / LOTUS | Not started | Define limits; whistleblower channels; audits |
| Role assignment & hierarchies | Medium | Node Leads | Not started | Transparent, documented process; training & rotation |

---

## 6. Optional Top-to-Bottom Risk Flow Diagram

```mermaid
flowchart TB
    %% Top-to-bottom risk & mitigation integration
    A[Receive Request / Event] --> B[Initial Logging]
    B --> C[Risk Assessment / Prioritization]
    C --> D[Legal / Compliance Review]
    D --> E[Mitigation Applied]
    E --> F[LOTUS Attestation / Notification]
    F --> G[Audit & Follow-up]

    %% Node colors
    classDef green fill:#d4f8d4,stroke:#333,stroke-width:2px,color:#000,font-size:14px,padding:10px;
    classDef yellow fill:#fff3b0,stroke:#333,stroke-width:2px,color:#000,font-size:14px,padding:10px;
    classDef red fill:#ffcccc,stroke:#333,stroke-width:2px,color:#000,font-size:14px,padding:10px;
    classDef blue fill:#cce0ff,stroke:#333,stroke-width:2px,color:#000,font-size:14px,padding:10px;

    class A,C,D,E green
    class B yellow
    class F blue
    class G red

    %% Node width
    style A width:250px
    style B width:250px
    style C width:250px
    style D width:250px
    style E width:250px
    style F width:250px
    style G width:250px
