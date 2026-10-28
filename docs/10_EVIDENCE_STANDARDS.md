# Evidence standards and interpretation

This document defines how to read the **public index**; it does not modify the canonical source repositories or independently certify their results.

| Term in this repository | What it means | What it does not mean |
|:--|:--|:--|
| Formal definition | The referenced owner defines typed objects and semantics | General mathematical novelty or universal adequacy |
| Finite-model theorem | A stated proposition was established within specified finite-model assumptions | The proposition applies to every computational system |
| Scoped software result | A selected behavior was observed and adjudicated in bounded software fixtures | A real-world platform or different fixture will perform identically |
| Hardware observation | A specific MCU-based experiment was executed or documented | Flight qualification, reliable production deployment or certified safety |
| Digital-twin result | A result within the stated simulation model and scenarios | Verified physical effectiveness |
| Candidate integration | An interface or combined product worthy of investigation | Successful end-to-end integration |
| Internal provenance | Maintained privately by the rights holder | Accessible or independently verified in this public package |
| Documentation CI | Checks the consistency of the public documentation package | Validates the underlying science |

## Evidence hierarchy

1. **Established in scope:** named model or test and its stated conditions.
2. **Reported / pending review:** observed by an operator but awaiting independent evidence adjudication.
3. **Specified:** architectural or formal contract, not necessarily experimentally demonstrated.
4. **Hypothesis:** open causal, engineering or commercial question.
5. **Not established:** unsupported for the referenced claim or environment.

Negative and inconclusive results remain part of the restricted scientific record, even where the public summary focuses on the practical research program.

## Reviewer output

Each reviewed claim should carry: an ID, explicit source commit, assumptions, setup, control/comparator, procedure, raw result, limitations, reproducibility status and one of **PASS**, **FAIL**, **INCONCLUSIVE** or **EVIDENCE_INSUFFICIENT**.

[Review protocol](05_REVIEW_PROTOCOL.md) · [Claims register](../evidence/CLAIMS_REGISTER.csv)
