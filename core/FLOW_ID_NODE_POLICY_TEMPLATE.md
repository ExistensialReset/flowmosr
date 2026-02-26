# FLOW_ID_NODE_POLICY_TEMPLATE.md

## Purpose
**Objective:** Provide a standardized, auditable, and privacy-preserving Node Policy that all Flow Nodes must publish and adhere to when performing FLOW_ID verifications.  
**Scope:** Applies to initial verifications, recovery attestations, audits, dispute resolution, and local data handling.

---

## Node Identification and Contact
- **Node Name:**  
- **Node ID (on‑chain hash):**  
- **Physical Location:** City; Region; Country.  
- **Primary Contact Role:** Title or role (no personal PII on-chain).  
- **Published NodePolicy Hash:** **SHA256** of this policy file published to the Flow ledger.

---

## Accepted ID Types and Proof Requirements
**Minimal standardized ID list:**  
- **Community Membership Card** — issued by recognized local organization; must include issuer stamp and expiry date.  
- **Non‑state Photo ID** — printed photo, signature, and issuer contact; issuer must be locally verifiable.  
- **Utility Bill / Proof of Residence** — dated within last 3 months; must match applicant’s claimed residence.  
- **Self-attestation with Witness** — only allowed in remote or emergency contexts with two independent witnesses from different Nodes.

**Verification checks for every ID:**  
- **Physical authenticity check** (paper quality, holograms, stamps where applicable).  
- **Photo match** to applicant in person.  
- **Issuer validation** via local contact or published registry when feasible.  
- **Document timestamp** within acceptable window defined by Node.

**Process for adding/removing ID types:**  
- Proposal submitted to LOTUS governance or Node consortium.  
- Trial period at pilot Nodes with audit results.  
- On-chain update of NodePolicy hash after approval.

---

## Verifier Roles and Qualifications
- **Verifier Eligibility:** Must be a verified FLOW_ID holder in good standing.  
- **Training Requirements:** Complete Node verifier training module and pass a practical assessment. Training completion timestamped and logged (no PII).  
- **Conflict of Interest Rules:** Verifier must recuse if related to applicant within defined degree (household, direct family).  
- **Rotation and Limits:** Verifiers rotate duties; no single verifier may perform >20 initial verifications/month without cross-node attest.  

---

## Initial Verification Procedure
1. **Session Initiation:** Node issues ephemeral session token to applicant.  
2. **Random Verifier Selection:** Node selects three verifiers using verifiable RNG; selection proof recorded.  
3. **Face-to-Face Check:** Verifiers perform checks per Accepted ID Types and sign verification statement.  
4. **Key Generation Confirmation:** Applicant generates private key on device; Node verifies challenge/response without receiving private key.  
5. **Ledger Publication:** Node publishes anonymized verification hash, verifier signature hashes, NodeID, timestamp, and selectionProofHash.  
6. **Recovery Set Enrollment:** Protocol selects five recovery candidates across Nodes; applicant consents and selection proof recorded.

**Mandatory artifacts:** minimal encrypted local notes; retention limited and deletable on request except cryptographic proofs.

---

## Key Handling and Device Policy
- **Key Generation:** Must occur on applicant’s device by default; Node may provide air-gapped assistance (QR/USB) but never store private keys.  
- **Supported Devices:** Hardware wallets, secure enclave devices, or defined mobile OS versions.  
- **Fallback Policy:** Devices without secure enclave receive reduced privileges; recovery set enlarged to 7 members for extra security; mandatory re-attestation.  
- **Key Rotation:** Allowed via k-of-n recovery; rotation events logged with anonymized metadata and timelock.

---

## Recovery and Social Attestation
- **Recovery Set Size:** Standard 5 candidates; fallback 7 candidates for devices with reduced security.  
- **Recovery Threshold:** 3-of-5 (or 4-of-7 fallback) signatures required.  
- **Verifier Confirmation Channels:** Each signer must confirm via at least two channels (in-person token + app push or recorded phrase).  
- **Timelock:** Default 72 hours; adaptive extension for anomalous patterns.  
- **Veto Mechanism:** Original keyholder may veto within short window if reachable; veto event logged anonymously.

---

## Logging, Ledger, and Privacy
- **On-chain Ledger Fields:** `publicKeyHash | verificationHash | NodeID | timestamp | statusFlag | selectionProofHash`.  
- **Off-chain Local Logs:** Encrypted, minimal, purged per retention policy; used only for dispute resolution and audits.  
- **PII Prohibition:** No names, photos, government IDs, or contact info stored on-chain.  
- **Anonymized Audit Export:** Support export proving counts, timelines, and distribution without exposing PII.

---

## Audits, Compliance, and Reporting
- **Annual Audit:** Independent audit of anonymized ledger exports; attestation published on-chain.  
- **Cross-Node Attestation Thresholds:** Nodes performing >20 verifications/month must obtain attestations from ≥2 other Nodes before IDs reach full activation.  
- **Trust Score:** Computed from audit history, anomaly flags, and dispute outcomes; published as anonymized metric.  
- **Reporting Obligations:** Report suspected infiltration, collusion, or systemic anomalies to LOTUS governance and participate in coordinated response.

---

## Dispute Resolution and Incident Response
- **Local Dispute Panel:** Randomly drawn from verified members; handles contested verifications and recovery disputes.  
- **Escalation Path:** Local panel → Regional Node consortium → LOTUS governance.  
- **Incident Playbook:**  
  - Temporary suspension of new verifications  
  - Cross-node freeze of affected IDs  
  - Emergency audit with timeline <48h  
  - Public anonymized alert to LOTUS governance

---

## Retention, Deletion, and Portability
- **Retention Policy:** Minimal local notes retained only as needed; cryptographic proofs retained for validity.  
- **Annual Deletion Option:** Individuals may request deletion of local notes annually; Node must comply except where retention required.  
- **Portability:** Key migration via recovery or re-attestation preserving identity integrity.

---

## Incentives and Anti-Corruption Rules
- **Incentives:** Non-monetary reputation rewards; public recognition.  
- **Prohibitions:** No paid verification; strict penalties for bribery/collusion.  
- **Enforcement:** Violations trigger trust score penalties, temporary suspension, possible removal.

---

## Onboarding and Offboarding Nodes
- **Onboarding:** Publish NodePolicy hash on-chain; complete verifier training; pass compliance audit; register physical location.  
- **Offboarding:** For repeated violations or capture; includes audit, data export, public attestation.

---

## Appendix and Templates
- **Verification Statement Template:** Standardized text for verifier signatures (hash stored on-chain).  
- **NodePolicy Change Log:** Versioned history with on-chain hash.  
- **RNG Selection Proof Format:** See `/core/RNG_AND_LOG_SPEC.md`.  
- **Audit Checklist:** Minimal items auditors must verify (verifications, timelock compliance, RNG proofs, recovery attempts).

---

## Governance and Amendments
- **Policy Amendments:** Documented proposal, pilot testing, on-chain publication of new NodePolicy hash.  
- **LOTUS Oversight:** Provides governance for cross-node standards, dispute arbitration, and emergency coordination.

**Usage Note:** Publish human-readable Node Policy and commit hash to Flow ledger. Policy must be publicly available at Node physical location and directory.