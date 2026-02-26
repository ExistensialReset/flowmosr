# FLOW_ID_LIFECYCLE.md

**Status:** DRAFT  
**Scope:** Global Node Protocol  
**Primary Placement:** `/core/FLOW_ID_LIFECYCLE.md`  
**Purpose:** Define the full lifecycle of a Flow ID, ensuring unique human binding, auditability, privacy, and operational rules for activation, use, rotation, and deactivation.

---

## 1. Core Principles

- **One Human = One ID:** Each Flow ID corresponds to a single, verifiable human.  
- **Impossibility to Forge:** ID generation relies on multi-factor biometric + cryptographic proof to make forgery infeasible.  
- **Non-transferable:** IDs cannot be shared, sold, or assigned.  
- **Privacy by Default:** Minimal PII stored; all sensitive info is encrypted locally.  
- **Auditability:** Every action is timestamped, verifiable, and exportable.  
- **User Control:** The human can request deactivation or rotation, respecting security and governance rules.

---

## 2. Flow ID Lifecycle

### 2.1 Registration / Issuance
1. **Identity Proofing:** Human provides verifiable proof of existence (biometric scan, live verification, community attestation).  
2. **ID Generation:** System creates a unique cryptographic identity bound to the human.  
3. **Initial Signing Keys:** Generate private/public key pair stored securely on user device; public key registered in Node ledger.  
4. **Audit Log Entry:** Log issuance with timestamp, verifier ID, and hash of initial credential (no PII exposed).

---

### 2.2 Activation
- ID becomes active once verification and ledger registration are complete.  
- Associated public key is used for signing Flow transactions and decisions.  
- Activation event logged with timestamp, Node ID, and auditor hash.

---

### 2.3 Normal Use
- ID used for:
  - Voting in lotteries (LOTUS / governance panels)  
  - Decision logging  
  - Accessing Flow Baseline knowledge and services  
- All actions are **signed** by ID's private key.  
- Logs include:
  - `event_type`, `timestamp`, `node_id`, `action_summary`, `signature_hash`, `auditor_hash`  
- Exports: CSV / JSON for audit.

---

### 2.4 Rotation of Signatures / Keys
**Purpose:** Limit risk of key compromise and maintain long-term integrity.  
- Rotation interval: configurable (e.g., quarterly).  
- Steps:
  1. Generate new key pair offline.  
  2. Verify new public key and register in ledger.  
  3. Sign rotation event with old key (if available).  
  4. Log rotation: timestamp, responsible Node, key hash before/after.  
- Rotation can be **user-triggered** in case of suspected compromise.  
- Rotation does **not** change human binding.

---

### 2.5 Temporary Deactivation
**Reasons for deactivation:**
- Human requests privacy break (e.g., sabbatical, withdrawal from Flow).  
- Security concern: suspected key compromise.  
- Node-wide operational freeze.  

**Process:**
1. ID flagged as inactive in Node ledger.  
2. All new actions requiring signature are rejected.  
3. Temporary deactivation logged: timestamp, reason, responsible Node.

**Constraints:**
- Deactivation is reversible unless the human chooses full deletion.  
- Deactivation does **not** erase prior audit logs (only prevents new activity).

---

### 2.6 Permanent Deletion / Anonymization
**Allowed once per year** per human.  
- Only PII and biometric proofs deleted; cryptographic proof of past actions may remain hashed for integrity.  
- Special case: medical or legally required records may remain encrypted.  
- Logged with timestamp, responsible Node, and confirmation hash.

---

### 2.7 Verification & Audit
- Any Node or auditor can verify:
  - ID authenticity  
  - Current status (active, deactivated, deleted)  
  - Key rotation history  
  - Signed actions integrity  
- Logs are exportable for CSV/JSON audit.  
- All audit actions logged with timestamp, auditor ID, and hash.

---

### 2.8 Security Notes
- **Offline storage of private keys** preferred.  
- **No cloud dependency** required; all verification can be done peer-to-peer in Node network.  
- Multi-party verification possible for extra resilience.  
- Compromise or theft triggers rotation and potential temporary deactivation automatically.

---

## 3. Mermaid Diagram (Flow ID Lifecycle)

```mermaid
flowchart LR
    ID["Flow ID 🌱"] --> REG["Registration / Issuance 📝"]
    REG --> ACT["Activation ✅"]
    ACT --> USE["Normal Use 🖋️"]
    USE --> ROT["Rotation of Keys 🔄"]
    USE --> TEMP["Temporary Deactivation ⏸️"]
    TEMP --> USE
    USE --> DEL["Permanent Deletion / Anonymization 🗑️"]
    ROT --> USE
    ID --> AUDIT["Verification & Audit 🔍"]

    REG --> LOG1["Audit Log Entry 📊"]
    ACT --> LOG2["Activation Log 📊"]
    ROT --> LOG3["Rotation Log 📊"]
    TEMP --> LOG4["Deactivation Log 📊"]
    DEL --> LOG5["Deletion Log 📊"]
    USE --> LOG6["Action Logs 📊"]