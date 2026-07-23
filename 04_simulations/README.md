# 04_SIMULATIONS

## Models, Scenarios, and Proposed Validation

This directory contains models, simulations, stress scenarios, and proposed validation methods for Flow / M-OS-R.

It is important to understand what this directory does — and does not — claim.

---

## ⚠️ VALIDATION STATUS

**The systems described in this directory have not been presented as fully validated real-world systems unless explicitly stated otherwise.**

A model is not evidence.

A scenario is not an observation.

A proposed test is not a completed test.

A simulation is not reality.

The purpose of this directory is to make assumptions visible and make them testable.

---

## I. WHAT THIS DIRECTORY CONTAINS

### 1. Conceptual Models

Descriptions of how a system might work.

These answer:

> How could this work?

They do not answer:

> Does this work in reality?

---

### 2. Scenarios

Structured situations used to examine potential behavior under different conditions.

Examples include:

- energy shortage;
- network isolation;
- resource scarcity;
- system failure;
- regional disruption;
- node isolation;
- cascading failures.

A scenario is a question posed to a system.

It is not evidence of what will happen.

---

### 3. Proposed Simulations

Methods for testing models under controlled or computational conditions.

These may help explore:

- sensitivity;
- failure points;
- trade-offs;
- dependencies;
- and possible system behavior.

Simulation results remain dependent on:

- the model;
- the assumptions;
- the input data;
- and the implementation.

---

### 4. Proposed Real-World Tests

Methods for testing whether theoretical or simulated assumptions survive contact with reality.

These may include:

- hardware tests;
- small-scale production tests;
- Circle experiments;
- Node pilots;
- resource-flow experiments;
- and resilience tests.

---

## II. EPISTEMIC STATUS

Every claim should, where possible, be understood according to its status:

| Status | Meaning |
| :--- | :--- |
| **PROPOSED** | A design or hypothesis that has not yet been tested |
| **MODELED** | Represented in a conceptual or mathematical model |
| **SIMULATED** | Tested through a computational or controlled simulation |
| **PILOTED** | Tested in a limited real-world implementation |
| **OBSERVED** | A documented observation from a real-world test |
| **VALIDATED** | Supported by documented evidence under defined conditions |
| **INDEPENDENTLY VALIDATED** | Verified by an independent party or process |

These categories should not be treated as interchangeable.

---

## III. THE VALIDATION CHAIN

A claim should ideally move through a process such as:

```text
CLAIM
  ↓
ASSUMPTION
  ↓
FAILURE MODE
  ↓
TEST DESIGN
  ↓
SIMULATION
  ↓
PILOT
  ↓
OBSERVATION
  ↓
REPLICATION
  ↓
VALIDATION