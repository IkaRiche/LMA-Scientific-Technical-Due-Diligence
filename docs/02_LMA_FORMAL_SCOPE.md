# 02 — LMA: formal scope and falsification

## Public orientation (not full specification)

In the current reference, a Lomidze Print is described abstractly as:

$$
P = (D, R, V, A, B, I)
$$

where:

- `D`: bounded dimensions / site domain;
- `R`: role-bearing positions;
- `V`: typed void positions;
- `A`: adjacency and contact relations;
- `B`: boundaries;
- `I`: interface positions.

This tuple is a **public conceptual description**, not an executable proprietary representation. A Tissue is a causally interacting composition of Prints; an arbitrary list of modules is not enough to establish Tissue-level behavior.

A useful abstract semantics is:

$$
(S_{t+1},Y_t) = \mathcal{T}(P,\,S_t,\,U_t,\,C_t)
$$

with bounded internal state `S`, admitted input `U`, context `C`, output `Y` and structural object `P`. This is an **explanatory notation**, not a claim that the displayed transition law is the canonical complete ALG-L0 model.

## Specific mathematical standing

The reference identifies laws `L1`–`L8` as **specified**, including well-formedness, compatibility, order/association semantics, typed voids and boundaries, context/epoch, resources/replay and equivalence. It records three **existence theorems proved inside the explicitly bounded finite model** `M-ALG-L0-FINITE-001`:

1. **T1:** a typed void can be non-eliminable under the stated finite-model semantics.
2. **T2:** reassociation can change denotation; the association tree may be semantic.
3. **T3:** operand order can change denotation through typed interactions.

This package does **not** reproduce the canonical proof scripts or full witness constructions, under permanent external disclosure restrictions. Reviewers must not treat these summaries as independent verification of proof correctness.

## Relevant comparisons, without overclaiming

| Known category | Relevant overlap | Fair question for diligence |
|---|---|---|
| Finite-state machines | All finite digital executions can be encoded | Does the LMA representation preserve useful structure with better composition or verification economics? |
| Cellular automata | Spatial/local transitions | Which claimed operations, typed interfaces and memory effects are independently established? |
| Graph rewriting / spatial computation | Structured operators and local relations | Is a concrete LMA mechanism more than alternate syntax for an existing construction? |
| Runtime assurance / supervisory control | Bounded execution restrictions | What does morphology add beyond established enforcement or policy methods? |

**Scope of comparison:** the tested bounded digital behavior is representable in conventional finite computation. The public results establish specific causal structural effects, not computational irreducibility or universal superiority over standard controllers.

The current Morphic AI ontology distinguishes a Print's own retained acquired morphology from **Tissue-level acquired shared operative structure**. In later bounded digital experiments the source-native acquired Tissue supports a jointly acquired functional result, causal reuse over changed same-family tasks and a separately applied digital-world consequence with own-observation feedback. These are **scoped empirical causal interventions**, not additional algebraic theorems or proof of novel complexity. The underlying internal research record is maintained separately. See [Morphic AI review](13_MORPHIC_AI_REVIEW.md).

No general computational irreducibility or superiority claim is warranted by either comparator or by the finite-model theorems.

## Reviewer acceptance criteria

- Terms, domains, operators, admissibility and observables can be uniquely defined.
- At least one claimed nontrivial property has a publicly discussable theorem scope and a non-sensitive owner-operated illustration.
- Claims are distinguished from unproved novelty and from alternative known representations.
- The reviewer can explicitly record `PASS`, `FAIL` or `INCONCLUSIVE` for each proposed mathematical assertion.

This public index does not contain executable theorem witnesses or the canonical formal-model implementation; these remain internal and are not made available to external reviewers.