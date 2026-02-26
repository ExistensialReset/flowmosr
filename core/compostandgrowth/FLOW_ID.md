# FLOW_ID.md

**Status:** DRAFT  
**Scope:** Global Node Protocol  
**Primary Placement:** `/core/FLOW_ID.md`  
**Purpose:** Define a secure, verifiable, and post-monetary identity system for Flow, ensuring one human = one identity while preserving privacy, decentralization, and non-coercion.

---

## 1. Principles

1. **One Human = One ID**  
   - Each ID is unique, physically bound to a single human.  
   - Duplication, theft, or forgery is structurally prevented.  

2. **Physical Initial Verification**  
   - Registration occurs at a Node with **3 randomly selected, already verified members**.  
   - Requires physical presence and validation of a Node-approved ID (not BankID or state-issued monetary IDs).  
   - One-time registration.

3. **Cryptographic Binding**  
   - Post-verification, the individual receives a **private key** only they control.  
   - Public key is used for all Flow interactions.  
   - Key is rooted in physical verification and cannot be duplicated without the original person.

4. **Rotative Verification / Social Proof**  
   - New verifications or recoveries require **a randomly selected subset of verified members**.  
   - Prevents Sybil attacks and false identities.  

5. **Theft Protection & Recovery**  
   - No central server stores private keys.  
   - Private key stored locally (hardware wallet or equivalent).  
   - Social recovery protocol: **3 of 5 verified contacts** required for recovery – no single person can hijack the ID.

6. **Audit & Transparency**  
   - All verifications are logged **anonymously** in an auditable ledger.  
   - Only verification status and date are public; no personal data is exposed.  

---

## 2. Security Features

- **Randomized human verification** = hard to fake.  
- **Cryptography** = hard to steal.  
- **Rotative verification** = hard to manipulate.  
- **Transparent, anonymized logs** = accountable but privacy-preserving.  

---

## 3. Flow Compatibility

- No reliance on banks or state authorities.  
- Minimalist, post-monetary, non-coercive.  
- Fully compatible with LxSxI principles: Calm × Spontaneity × Empathy.  
- Can be integrated directly with LOTUS-lotteries and all other decision-making organs.

---

## 4. Operational Checklist for Nodes

- [ ] Candidate presents Node-approved ID at Node registration.  
- [ ] 3 random verified members perform physical verification.  
- [ ] Private key generated and handed to individual securely.  
- [ ] Public key registered in Flow ledger (anonymized).  
- [ ] All verification events timestamped and logged.  
- [ ] Recovery contacts selected (randomized from verified members).  
- [ ] Ledger exportable for independent audit without PII.  

---

## 5. Recovery & Key Rotation

- **Key rotation** optional, requires social verification.  
- Recovery must follow the **3-of-5 verified contacts** process.  
- Logs updated for every key rotation, recovery attempt, and outcome.

---

## 6. Integration with LOTUS

- All Flow IDs are **eligible for lottery selection**.  
- IDs form the **qualified pool** for panel selection, mandate rotations, and other Flow decision organs.  
- Private key ensures identity integrity while remaining fully **anonymized in logs and audits**.  

---

## 7. Retention & Privacy

- Private key stays local; never stored in cloud or central server.  
- Ledger keeps verification metadata only; no PII.  
- Annual optional data deletion for individuals, except cryptographic proofs needed for ongoing Flow operations.

---

## 8. Mermaid Visualization of FLOW ID

```mermaid
flowchart LR
    FLOWID["Flow ID 🔑"] --> VERIFY["Physical Initial Verification 🧑‍💻"]
    FLOWID --> CRYPTO["Cryptographic Binding 🔐"]
    FLOWID --> ROTATION["Rotative Verification ♻️"]
    FLOWID --> RECOVERY["Social Recovery 🛡️"]
    FLOWID --> AUDIT["Audit & Ledger 📊"]

    VERIFY --> NODEID["Node-approved ID 🏷️"]
    VERIFY --> MEMBERS["3 Random Verified Members 🎲"]

    CRYPTO --> PRIVATE["Private Key 🔑"]
    CRYPTO --> PUBLIC["Public Key 🌐"]

    ROTATION --> RANDOMPOOL["Random Verified Members 🎲"]

    RECOVERY --> CONTACTS["3-of-5 Verified Contacts 👥"]

    AUDIT --> LOGS["Anonymized Ledger Entries 🗂️"]
    AUDIT --> EXPORT["Exportable for Audit 💾"]
