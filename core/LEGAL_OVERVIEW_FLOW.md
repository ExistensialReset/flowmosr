# LEGAL_OVERVIEW_FLOW.md

**Status:** Draft  
**Scope:** Entire M-OS-R Ecosystem  
**Purpose:** High-level overview of legal, compliance, verification, and audit flows across all Nodes and Spirals. Includes Playbooks, LOTUS coordination, and chain-of-custody relationships. Color-coded for clarity.

---

```mermaid
flowchart TB
    %% --- Class Definitions ---
    classDef node fill:#FFEEAA,stroke:#333,stroke-width:1px,color:#000
    classDef spiral fill:#AAEEFF,stroke:#333,stroke-width:1px,color:#000
    classDef playbook fill:#EEFFAA,stroke:#333,stroke-width:1px,color:#000
    classDef legal fill:#FFCCDD,stroke:#333,stroke-width:1px,color:#000
    classDef verifier fill:#DDEEFF,stroke:#333,stroke-width:1px,color:#000
    classDef audit fill:#DDFFDD,stroke:#333,stroke-width:1px,color:#000
    classDef lotus fill:#CCCCFF,stroke:#333,stroke-width:1px,color:#000

    %% --- Nodes ---
    N1[Node 1]:::node
    N2[Node 2]:::node
    N3[Node 3]:::node
    N4[Node 4]:::node
    N5[Node 5]:::node

    %% --- Spirals ---
    S1[Spiral Alpha]:::spiral
    S2[Spiral Beta]:::spiral
    S3[Spiral Gamma]:::spiral

    %% --- Playbooks ---
    P1[Unforgivable Harm Protocol]:::playbook
    P2[Complete Legal Response Playbook]:::playbook
    P3[Emergency Disclosure Playbook]:::playbook
    P4[Data Minimization Playbook]:::playbook

    %% --- Legal / Compliance Roles ---
    L1[Legal Officer]:::legal
    L2[Compliance Officer]:::legal
    L3[Node Counsel]:::legal
    L4[Regulatory Liaison]:::legal

    %% --- Verifiers / Auditors ---
    V1[Verifier / Evidence Custodian]:::verifier
    V2[Verifier / Evidence Custodian]:::verifier
    A1[Auditor Liaison]:::audit
    A2[Independent Auditor]:::audit

    %% --- LOTUS ---
    LOTUS[LOTUS Governance / Oversight]:::lotus

    %% --- Node to Spiral Relations ---
    N1 -->|participates in| S1
    N2 -->|participates in| S1
    N3 -->|participates in| S2
    N4 -->|participates in| S2
    N5 -->|participates in| S3

    %% --- Spiral to Playbook Guidance ---
    S1 -->|guided by| P1
    S2 -->|guided by| P1
    S3 -->|guided by| P3
    S1 -->|follows| P2
    S2 -->|follows| P2
    S3 -->|follows| P4

    %% --- Legal / Compliance Flow ---
    L1 -->|advises| N1
    L1 -->|advises| N2
    L2 -->|executes| N3
    L3 -->|advises| N4
    L4 -->|coordinates regulatory response| N5

    %% --- Verifier / Audit Flow ---
    V1 -->|verifies| N1
    V2 -->|verifies| N2
    A1 -->|audits| LOTUS
    A2 -->|audits| N3 & N4 & N5

    %% --- LOTUS Coordination ---
    LOTUS -->|coordinates| N1
    LOTUS -->|coordinates| N2
    LOTUS -->|coordinates| N3
    LOTUS -->|coordinates| N4
    LOTUS -->|coordinates| N5
    LOTUS -->|reviews & approves| P1
    LOTUS -->|reviews & approves| P2
    LOTUS -->|reviews & approves| P3
    LOTUS -->|reviews & approves| P4

    %% --- Playbooks to Legal ---
    P1 -->|informs| L1
    P2 -->|informs| L2
    P3 -->|informs| L3
    P4 -->|informs| L4

    %% --- Legend ---
    subgraph Legend[" "]
        direction LR
        Node[Node]:::node
        Spiral[Spiral]:::spiral
        Playbook[Playbook]:::playbook
        Legal[Legal / Compliance]:::legal
        Verifier[Verifier / Evidence Custodian]:::verifier
        Auditor[Auditor Liaison]:::audit
        LOTUS_Gov[LOTUS Governance]:::lotus
    end