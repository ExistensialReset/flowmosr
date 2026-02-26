# FLOW_ID.md

**Status:** DRAFT  
**Scope:** Global Node Protocol  
**Purpose:** Define FLOW_ID_v3, a decentralized, privacy-preserving identity protocol that guarantees one human = one ID without reliance on state or banking authorities. Incorporates device sustainability principles and long-lived user hardware.  

---

## Overview and Goals

**Core guarantees:**  
- Uniqueness: one human = one ID.  
- Physical binding to cryptographic control.  
- Recovery without central PII.  
- Auditable anonymized logs.  
- Resistance to Sybil and coordinated attacks.  
- Compatibility with post-monetary Flow principles.  

**Design principles:**  
- Physical initial verification.  
- Local private key ownership.  
- Randomized social verification.  
- Minimal ledger metadata.  
- Non-coercion.  
- Sustainable, repairable hardware compatibility.  

---

## Terminology and Core Components

- **Node** — a physical location or organized verifier group authorized to perform initial verifications.  
- **Verifier** — a previously verified member authorized to sign verification events.  
- **FLOW_ID record** — ledger entry containing public key hash, verification hash, NodeID, timestamp, and status flag; contains no PII.  
- **Verification event** — cryptographically signed attestations by verifier(s) that a physical check occurred.  
- **Recovery Set** — randomly selected group of verified members (standard size 5) for social recovery; recovery requires k-of-n signatures (standard 3/5).  
- **Node Policy** — local, published rules that define acceptable ID types, verification steps, and verifier training requirements.  

---

## Protocol Flow and Operational Procedures

### Initial registration

1. **Session initiation:** Applicant requests registration at a Node; Node issues an ephemeral session token.  
2. **Physical check:** Three randomly selected verifiers at the Node perform face-to-face validation against Node Policy and sign verification statements.  
3. **Key generation:** Private key is generated on the individual’s device (hardware wallet, secure enclave, or supported mobile device). Node never receives the private key. Transfer of challenges/responses uses air-gapped methods (QR, USB) if needed.  
4. **Ledger publication:** Individual publishes public key and anonymized verification hash to the Flow ledger; verifier signatures and NodeID are hashed only.  
5. **Recovery set selection:** Protocol randomly selects five verified members across nodes; applicant consents before finalization.  

### Normal operation

- All Flow actions are signed by the private key. Ledger validates the public key is active and not flagged.  

### Recovery and key rotation

- **Trigger:** User reports loss or requests rotation.  
- **Process:** k-of-n (3/5) recovery signatures produce an on-chain recovery transaction with timelock (default 72 hours). Anonymous ledger alert is published during timelock.  
- **Safeguards:** Original keyholder veto if reachable; multi-channel verifier confirmations; full audit trail.  

---

## Threat Model and Mitigations

- **Primary threats:** Node infiltration, coordinated Sybil campaigns, social engineering, coercion, private key extraction.  
- **Mitigations:**  
  - Cross-node randomization for verifier selection.  
  - Rate limits and quorum constraints for Nodes.  
  - Behavioral anomaly detection via anonymized metadata.  
  - Multi-channel verifier confirmation (physical + app/token).  
  - Timelocks and public anonymous alerts.  
  - Device security guidance: hardware wallets, secure enclaves, or supported mobile devices with clear instructions.  
  - Auditability without PII: ledger exports enable independent verification.  

---

## Node Governance, Compliance, and Privacy

- **Node requirements:** Publish Node Policy listing accepted ID types, verification steps, verifier training, incident response, retention rules.  
- Maintain minimal local notes; support annual deletion requests except for cryptographic proofs.  
- **Audits and dispute resolution:** Annual independent audits of anonymized ledger exports; local dispute panels randomly drawn from verified members handle contested verifications.  
- **Privacy guarantees:** Ledger stores only hashes, NodeIDs, timestamps, and status flags. No names, photos, or government identifiers. Verification hashes are one-way; correlation requires local data.  

---

## Device Sustainability & Compatibility

FLOW_ID_v3 explicitly supports **long-lived, repairable hardware**:  

- **Legacy device support:** SDK runs on standard smartphones (e.g., Samsung S23) and other non-specialized hardware.  
- **Fallback security levels:** Devices without secure enclaves use “soft” security with reduced privileges and extra social recovery.  
- **Migration & portability:** Keys and data can be restored on the same device, or moved to a new device without breaking identity integrity.  
- **Repairable hardware:** No mandatory device replacement, no remote kills, all recovery can occur locally.  
- **Sustainability principle:** Identity and verification are tied to the human, not the hardware lifecycle.  

---

## Implementation Roadmap and Next Steps

### Pilot (6 months)

- Deploy 3 pilot Nodes in diverse regions; enroll 500–2,000 participants.  
- Run red-team attack simulations, recovery drills, usability testing. Track verification latency, false positives, recovery success, anomalies.  

### Technical deliverables

- Client SDK: key generation, signing, recovery flows, UI patterns.  
- Reference hardware workflow and open documentation for secure key custody.  
- Ledger schema (JSON-LD) and multisig recovery transaction spec (k-of-n with timelock).  

### Governance deliverables

- Node Policy template, verifier training curriculum, audit checklist.  
- Incentives and anti-corruption rules: non-monetary reputation rewards, strict prohibition on paid verification.  

### Migration

- Re-attestation path for existing FLOW_ID holders: short physical re-check and signature with legacy key, or limited grandfathering with reduced privileges until re-attested.  

### Validation

- Independent security review and privacy impact assessment before full rollout.  

---

## Key Risks and Gaps

1. **Node-approved ID ambiguity:** define minimal ID types and addition/removal process.  
2. **Local Node capture / collusion:** enforce cross-node attest thresholds; sliding trust scores.  
3. **Recovery social engineering:** multi-channel verifier confirmation; anomaly detection; timelock escalation.  
4. **Key generation UX:** ensure SDK enforces on-device generation; fallback guidance for devices without enclaves.  
5. **Randomness integrity:** verifiable RNG (commit-reveal, on-chain seed); document audit procedures.  

---

## References

- FLOW principles: post-monetary, non-coercion, baseline human knowledge.  
- RNG & Logging Spec: `/core/RNG_AND_LOG_SPEC.md`  
- Harm Boundaries Protocol: `/ethos/THE_HARM_BOUNDARY_PROTOCOL.md`  

---