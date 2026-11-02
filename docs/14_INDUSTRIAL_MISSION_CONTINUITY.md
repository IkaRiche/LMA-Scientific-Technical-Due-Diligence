# STASYS TMC — Mission continuity for remote industrial autonomy

**Industrial opportunity brief · Public scientific and technical due diligence · 2 November 2026**

## Position within the LMA technology portfolio

Lomidze Morphological Algebra is a broader formal and experimental research program. **TMC is one candidate application of that research, not its sole purpose or its commercial limit.** Other distinct directions include native Morphic AI, Morphic Vision, distributed Guardian Veil mechanisms and DRC/SRC runtime assurance. Each has its own evidence maturity and potential buyer. The present brief concentrates on TMC because this particular industrial discussion identified a concrete mission-continuity problem; it does not imply that the entire LMA portfolio, patents or future applications are being offered for transfer.

## The operational problem

A remote geological survey, pipeline inspection or autonomous field mission may lose contact with its operator or access to trustworthy GNSS positioning before reaching its assigned endpoint. Aborting every interrupted task is costly; continuing without sufficient reliable observations can be unsafe.

**The opportunity:** preserve the assigned mission, evaluate permissible alternatives as conditions change, and continue when the onboard evidence remains sufficient — or explicitly refuse when it does not.

The specific industrial question is whether this can ultimately help a robot, drone or other autonomous platform reach **a mission-defined destination** through GNSS or communications degradation, with completion confirmed independently. **GNSS-denied physical arrival has not yet been demonstrated by the TMC research package.**

## What STASYS TMC contributes

**STASYS Terminal Mission Core (TMC)** is an independently mounted, MCU-class **mission-conduct core** derived from Lomidze Morphological Algebra research. Its proposed responsibility is to preserve an externally assigned objective, consume admitted typed context and verified execution results, and derive the next permissible mission intent through its own operative morphology and acquired experience (scars and epochs).

TMC is **not a replacement for the existing autopilot, motor controller, localization system or sensors**. It does not calculate a position from absent observations, fly an aircraft, authorize actuation or directly command actuators. The expected integration is through **existing documented interface contracts**, without redesigning other onboard subsystems:

1. **Existing platform systems** provide local observation, position-quality information where available, capability/health status and execution outcomes.
2. **TMC** retains the mission goal and computes a bounded, non-actuating continuation or a principled refusal.
3. **Existing independent authority, autopilot/controller and executor** decide admissibility and carry out permitted actions.
4. **Independent feedback** confirms actual consequences and, where relevant, arrival at the mission-defined endpoint.

Compatibility with a platform's existing safety/failsafe behavior is an **integration prerequisite**. A TMC intent cannot override an independent controller's safety restriction. Neither GPS loss nor communications loss automatically proves that useful navigation remains possible.

## Industrial situations worth qualifying

| Application | Costly interruption | Candidate value, if proven | Essential dependency |
|---|---|---|---|
| **Remote geological surveying** | An unmanned survey leg is interrupted by loss of operator communications or untrusted satellite positioning. | Continue a permitted survey leg toward a defined survey waypoint with fewer avoidable restarts. | Sufficient valid onboard localization, terrain/obstacle constraints and independent waypoint confirmation. |
| **Pipeline / linear-asset patrol** | A long inspection route crosses communication gaps and areas with degraded positioning. | Preserve inspection intent and re-evaluate a valid remaining segment instead of requiring a new remote plan at every disturbance. | Compatible existing robot/autopilot interfaces, observation quality and inspection-completion evidence. |
| **Unattended industrial mobile robots** | A remote mission must react to route or sensor degradation without an active operator. | Keep the assigned task and choose another allowed continuation, or stop with a traceable reason. | Accepted local state, bounded alternatives and independent execution feedback. |

These are **use-case hypotheses**, not validated customer savings, contracts or field deployments.

## Evidence already available

| Evidence tier | Owner-reported finding | Qualification boundary |
|---|---|---|
| **Scoped software — PASS_SCOPED** | A bounded fixed-goal experiment survived sequential failures, invalidated a stale continuation, selected other admissible continuations and ended with typed completion or principled refusal. | A controlled software mission, not real GNSS-denied arrival or an arbitrary route. |
| **Scoped causal research — PASS_SCOPED** | Coupled Conduct/Experience Prints produced a history-conditioned mission phenotype absent under key single-Print/uncoupled controls; structural and experience cuts changed the result. | Does not establish universal advantage over a fair conventional controller. |
| **STM32H723 laboratory — OBSERVED_IN_SCOPE** | Frozen decision traces were reproduced in two reported platform-facing on-target runs; separate two-Print physical evidence awaits independent raw-data adjudication. | The demonstrated telemetry interface was limited; **no autonomous navigation through a GPS-denied field mission** was tested. |
| **Integrated endpoint reach — NOT_ESTABLISHED** | No qualified TMC-supported real-platform test independently confirms reaching a designated location without GNSS. | A targeted industrial qualification question, not an available product specification. |

The accepted conventional full-information comparator reproduced bounded mission decisions. The proposed value is a *testable architectural and industrial hypothesis*, not a claim that conventional finite-state or robotics systems cannot do the same job.

## Proposed first industrial feasibility gate

Use a **civilian remote-inspection profile**, a real existing controller (unmodified internally), a compatible TMC interface and an equal-information conventional mission executive as baseline.

**Pre-register the following outcomes:** assigned-goal retention; use of admissible mission continuation after operator-link loss; the response when GNSS becomes unavailable but *independent trustworthy local localization* remains; the response when reliable localization is insufficient; stale/intentionally conflicting input refusal; independently verified arrival or task completion; and no TMC actuator-authority leakage.

**Compare:** completion versus justified refusal, unnecessary-abort rate, unsupported-continue rate, recovery from a degraded segment, deterministic trace, resource cost and interface compatibility. Preserve negative results. Do not infer arrival from mission-intent emission or synthetic completion flags.

**Go / no-go:** if a complete trusted local state cannot be supplied without GNSS, or an existing controller's safety contract prevents the proposed continuation, no claim of destination reach follows. Scope the pilot down or record **EVIDENCE_INSUFFICIENT** rather than relaxing the required outcome.

## Business and IP boundary

Potential participants are industrial autonomy OEMs, robotics integrators, remote-survey firms and infrastructure inspection operators. A logical first transaction is a **paid, bounded feasibility/qualification engagement**, followed — only after results — by a platform-specific license or OEM arrangement.

The underlying TMC implementation, canonical proofs, detailed morphology, firmware and original experimental records remain under **KOHI BG EOOD's controlled IP custody**. This public document supplies no implementation license or source access, including under NDA.

[Scientific TMC scope](03_TMC_VISION.md) · [Reviewer protocol](05_REVIEW_PROTOCOL.md) · [Public evidence register](../evidence/CLAIMS_REGISTER.csv) · [Disclosure boundary](07_DISCLOSURE_BOUNDARY.md)
