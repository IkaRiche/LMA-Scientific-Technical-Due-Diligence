# 08 — Mathematical review protocol

## Objective

Assess whether specific LMA mathematical claims are well-defined, internally correct and substantively distinguishable from known formal systems. Do **not** treat the existence of an executable toy as proof of novelty.

## Review sequence

1. **Definitions** — distinguish formal Print primitives from domain-specific implementation objects. Record sorts, operations, partiality, context, interfaces, resources and observables.
2. **Statements** — examine the exact T1–T3 finite-model theorems and enumerate their quantifiers, assumptions and stated scope.
3. **Proof and witnesses** — review public assumptions and theorem scopes; canonical proofs and executable witnesses remain internal.
4. **Countermodels** — inspect cases where a claimed distinction disappears or is captured by simpler semantics.
5. **Reduction** — compare against a full-information FSM encoding, graph rewriting and spatial computation without hiding morphology inside payloads.
6. **Engineering relevance** — determine whether differences yield a useful compositional contract or measurable cost/assurance benefit; do not assume superiority.
7. **Verdict** — assign PASS, FAIL or INCONCLUSIVE to *each* scoped claim. Record limitations and what evidence would change the verdict.

## Required recorded evidence

| Item | Reviewer record |
|---|---|
| Assertion ID | LMA-01 / LMA-02 / specific theorem |
| Source | Repository, immutable commit, path |
| Definitions | Exact version under review |
| Alternative model | Best fair comparator and information parity |
| Procedure | Public statement or owner-operated explanation |
| Observation | Publicly discussable observation or issue |
| Verdict | PASS / FAIL / INCONCLUSIVE |
| Disclosure | Public summary only |

## Important boundaries

The finite-model results do not establish a generally new complexity class, universal irreducibility, better efficiency or freedom to operate. The public repository does not include the canonical mathematical witnesses; external independent proof verification is not offered; reviewers must record INCONCLUSIVE where underlying proof artifacts would be essential.

[Public evidence index](../evidence/INDEX.md) · [LMA scope](02_LMA_FORMAL_SCOPE.md)
