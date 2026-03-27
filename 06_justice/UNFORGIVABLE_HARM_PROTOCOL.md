# UNFORGIVABLE_HARM_PROTOCOL.md

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Provide a single, auditable, privacy‑preserving, and democratic protocol for identifying, verifying, escalating, and remediating incidents of unforgivable harm within Flow. This protocol ensures that such cases are treated with the highest priority, while preserving anonymity and maintaining system auditability.

---

## 1. Principles
* **Highest Priority:** Unforgivable harm always supersedes other reports (infrastructure, accessibility, social).
* **Victim-Centric:** The victim never moves; the perpetrator must be isolated and investigated.
* **Immediate Escalation:** All cases enter critical workflow immediately, bypassing normal triage.
* **LOTUS Oversight:** Escalation to cross-node LOTUS panel for verification and decision.
* **Privacy & Optional Anonymity:** Victim may remain anonymous; all data encrypted in transit and at rest.
* **Auditability:** Every step logged with cryptographic proofs; independent auditor access.

---

## 2. Definitions
* **Unforgivable Harm:** Intentional and systemic boundary violations via force, malice, or sustained harassment, including:
    * **Sadistic Harm:** Infliction of suffering for perpetrator satisfaction.
    * **Physical/Weaponized Violence:** Any use of weapons or force causing serious injury or threat to life.
* **Report:** Submission describing suspected unforgivable harm.
* **Verification Event:** Signed, encrypted local record of physical or digital confirmation.
* **Actionable Threshold:** Any report that meets the definition of unforgivable harm or receives corroboration from at least one independent Node verification.

---

## 3. Submission Channels
* **Digital App/Portal:** Primary intake channel for detailed reports (images, video, GPS).
* **SMS/USSD:** Low-bandwidth reporting option.
* **Assisted Node Kiosks/Hubs:** Staff-assisted intake without exposing victim PII.
* **Direct Node Contact:** Phone or in-person intake routed into the same workflow.
* **Automated Alerts/Sensors:** Environmental triggers or safety alarms can flag potential harm events.

---

## 4. Verification Workflow

### Stepwise process
1.  **Immediate Intake:** All reports flagged as potential unforgivable harm are assigned **Critical Priority**.
2.  **Automated Screening:** Node system checks for duplicates, patterns, or known perpetrators.
3.  **Sensor/Media Corroboration:** IoT sensors, CCTV metadata, and optionally uploaded media are hashed and attached to report.
4.  **Witness Attestation:** Independent witnesses (minimum 2 NodeIDs) may submit signed attestations.
5.  **Remote Verifier Triage:** If corroboration meets threshold, assign remote verifier to confirm.
6.  **On-Site Verification:** Deploy physical verifier immediately for high-risk or urgent reports.
7.  **LOTUS Escalation:** If Node cannot resolve immediately or requires cross-node authority, trigger LOTUS panel assignment.

### Verification Event JSON Example
```json
{
  "eventId": "uuid",
  "reportId": "uuid",
  "verifierNode": "node:abc",
  "timestamp": "ISO8601",
  "method": "sensor|media|witness|on-site|remote",
  "outcome": "confirmed|not_confirmed|inconclusive",
  "evidenceHashes": ["sha256:..."],
  "signature": "hex"
}
```

## 5. SLA and Escalation

| Priority | Ack Time | Required Action | Escalation if Missed |
| :--- | :--- | :--- | :--- |
| **Critical** | Immediate | Mitigation, isolation, and verification within 4 hours | Escalate to LOTUS cross-node panel |
| **High** | 1 hour | Action within 12 hours | Escalate to LOTUS panel |
| **Normal** | N/A | Not applicable for unforgivable harm | N/A |

> **Note:** SLA overrides all other priorities.
> **LOTUS Panel Mandate:** Temporary assignment max 3 months, trauma-informed training, confidential.

---

## 6. Anti-Abuse and Privacy Safeguards

* **Victim Anonymity:** Optional; PII stored encrypted off-chain.
* **Rate Limits:** Apply to reporter submission attempts; coordinated abuse triggers investigation.
* **Audit Proofs:** Verification Events hashed and stored; independent auditors can verify without exposing PII.
* **False Reporting Penalties:** Verified malicious submissions penalized via Node trust scores; appeals through LOTUS.

---

## 7. Telemetry and Auditing

* **Telemetry Schema:** `nodeIDHash`, `epoch`, `reportsReceived`, `verificationsCount`, `escalationCount`, `anomalyFlag`.
* **Retention:** Raw logs 12 months; aggregated anonymized metrics indefinitely.
* **Audit Process:** Quarterly automated scans; annual independent audit under NDA; publication of attestation hashes on-chain.

---

## 8. Operational Notes

* **Cross-Node Coordination:** Nodes can pool resources for rapid verification and mitigation.
* **Fallback Protocol:** If on-site verification fails due to access or risk, deploy temporary mitigation (barriers, signage) while alternate verification occurs.
* **Documentation:** Every step recorded in `NodePolicy` and cryptographically hashed for audit.

---

## 9. Pilot Plan

* **Duration:** 3–6 months.
* **Nodes:** 3 diverse Nodes.
* **Participants:** 500–2,000.
* **Deliverables:** Intake channels, priority scoring, anonymous verification workflow, LOTUS escalation, telemetry dashboard, audit process.
* **Metrics:** * Time to first acknowledgement.
    * Time to mitigation.
    * SLA compliance.
    * % reports resolved.
    * False positive rate.
    * User satisfaction.

---

## 10. References

* `FLOW_REPORT_WORKFLOWS.md`
* `ANONYMOUS_VERIFICATION_WORKFLOW.md`
* `CONFLICT_ESCALATION_PATHS.md`
* `LOTUS_PROTOCOL.md`
