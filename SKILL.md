---
name: koda-youtube-video-structure
description: Design, audit, or rebuild Koda's evidence-grounded YouTube long-form video structure before scripting. Use for viewer payoff, packaging hypotheses, Commentary or Educational routing, section design, claim-to-proof mapping, and approval gating. Do not use to write a full script, invent Koda facts, or perform unsupported retention diagnosis.
---

# Koda YouTube Video Structure

Use this skill only for the editorial judgment layer before a full script.

## Choose one mode

- `DESIGN`: turn a topic or brief into a draft structure packet.
- `AUDIT`: independently run the three structural reviews on an existing structure packet without editing it.
- `REBUILD`: decompose an outline, transcript, or draft and produce a new draft structure packet without line editing.

`HANDOFF` is never a mode. A handoff artifact exists only after `APPROVED_FOR_HANDOFF`.

## Required loading order

1. Read the current request and task packet.
2. Read [runtime contract](references/00_runtime_contract.md).
3. Read the four Koda setup files: [channel contract](references/01_koda_channel_contract.md), [audience map](references/02_audience_and_content_map.md), [voice boundaries](references/03_koda_voice_boundaries.md), and [facts ledger](references/04_koda_facts.md).
4. Read [routing, payoff, and packaging](references/05_router_payoff_and_packaging.md).
5. Load only the pattern needed from [video patterns and Section Cards](references/06_video_patterns_and_section_cards.md).
6. Read [claims, evidence, and fact gate](references/07_claims_evidence_and_fact_gate.md).
7. Follow the selected mode in [workflows and output templates](references/08_workflows_and_output_templates.md).
8. In `AUDIT`, apply [review, approval, and data preconditions](references/09_review_approval_and_data_preconditions.md).
9. For a season-start experiment, use only the [Public Experiment preregistration](references/10_public_experiment_preregistration.md).

## Non-negotiable behavior

- Never write a complete long-form script.
- Never treat model memory as a Koda fact or Koda view.
- Mark missing channel, audience, voice, or fact inputs as `UNCONFIRMED` and list each missing item as `SETUP_REQUIRED`.
- Use only these main statuses: `DRAFT`, `NEEDS_KODA_DECISION`, `READY_FOR_KODA_APPROVAL`, `APPROVED_FOR_HANDOFF`, `REJECTED`.
- Keep blockers in `blockers[]`; never turn a blocker into a new main status.
- `DATA_PRECONDITION_CHECK_ONLY` is an operation-scope overlay, not a fourth mode. Accept it from any input mode, skip ordinary mode prerequisites, keep status `DRAFT`, and never upgrade structure rules.
- Route in this order: preregistered experiment, executable teaching action, viewpoint.
- Public Experiment is preregistration-only in v0.1.1; Case Study, Trend Judgment, full experiment-result structure, and retention review are deferred.
- `Commentary` may set `personal_evidence: true`; this is a subtype flag, not a new video-type enum.
- Generate payoff and core-judgment candidates before asking Koda to decide. A purely negative proposition is only a direction; propose affirmative, falsifiable candidates and use `NEEDS_KODA_DECISION`.
- Packaging may be `HYPOTHESIS` during drafting. Only Koda can make it `LOCKED`. Facts override packaging; a conflict returns packaging to `HYPOTHESIS` and adds `PACKAGING_CONFLICT`.
- Every Section Card chooses exactly one internal organization: `STP`, `PEIL`, `VALUE_LOOP`, or `PLAIN`.
- Evidence roles are `PROOF` and `ILLUSTRATION`; only `PROOF` satisfies an evidence gate.
- Allow at most one pure-logic section per video. Mark it `INFERENCE`; it cannot independently carry the core judgment.
- Without a retention curve, do not attribute opening or section-level causes. Output `UNDETERMINED`.
- In `AUDIT`, independently recompute all review rounds. Never trust supplied `review_rounds` or `review_inputs_complete` as proof of compliance.
- Only `AUDIT` can reach `READY_FOR_KODA_APPROVAL`, and only after all three independently rerun review rounds pass.
- Only an explicit Koda approval event can reach `APPROVED_FOR_HANDOFF`. Only an explicit Koda rejection event can reach `REJECTED`.

## Output

Return one Markdown `structure_packet` in the fixed order defined in [workflows and output templates](references/08_workflows_and_output_templates.md). State facts, inferences, missing data, and unresolved decisions separately. Do not claim that a structure will produce high retention or high views.
