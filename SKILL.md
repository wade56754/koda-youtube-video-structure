---
name: koda-youtube-video-structure
description: Design, audit, or rebuild Koda's evidence-grounded YouTube long-form video structure before scripting. Diagnose subject matter and theme, compare suitable structures with traceable sources, and return a plain-language transcript outline by default. Do not use to write a full script, invent Koda facts, or perform unsupported retention diagnosis.
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
4. Read [subject matter, theme, routing, payoff, and packaging](references/05_router_payoff_and_packaging.md).
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
- Before routing, identify what material carries the video and state its theme as one plain-language question or judgment. Then confirm the audience and viewer takeaway, compare the relevant structures, and explain why one is selected.
- Public Experiment is preregistration-only in v0.2.0; Case Study, Trend Judgment, full experiment-result structure, and retention review are deferred.
- `Commentary` may set `personal_evidence: true`; this is a subtype flag, not a new video-type enum.
- Generate payoff and core-judgment candidates before asking Koda to decide. A purely negative proposition is only a direction; propose affirmative, falsifiable candidates and use `NEEDS_KODA_DECISION`.
- Packaging may be `HYPOTHESIS` during drafting. Only Koda can make it `LOCKED`. Facts override packaging; a conflict returns packaging to `HYPOTHESIS` and adds `PACKAGING_CONFLICT`.
- Every Section Card chooses exactly one internal organization: `STP`, `PEIL`, `VALUE_LOOP`, or `PLAIN`.
- Treat `STP`, `PEIL`, and `VALUE_LOOP` as project adaptations, not universal academic models. Keep their acronyms in the internal packet; use their Chinese names and explain their purpose in the creator-facing reply.
- Evidence roles are `PROOF` and `ILLUSTRATION`; only `PROOF` satisfies an evidence gate.
- Allow at most one pure-logic section per video. Mark it `INFERENCE`; it cannot independently carry the core judgment.
- Without a retention curve, do not attribute opening or section-level causes. Output `UNDETERMINED`.
- In `AUDIT`, independently recompute all review rounds. Never trust supplied `review_rounds` or `review_inputs_complete` as proof of compliance.
- Only `AUDIT` can reach `READY_FOR_KODA_APPROVAL`, and only after all three independently rerun review rounds pass.
- Only an explicit Koda approval event can reach `APPROVED_FOR_HANDOFF`. Only an explicit Koda rejection event can reach `REJECTED`.

## Output

Build the internal `structure_packet` needed for validation and state continuity, but do not print it by default. The normal reply is exactly the four-part plain-language creator view defined in [workflows and output templates](references/08_workflows_and_output_templates.md): what the video is, why this structure fits, a transcript outline, and only the missing information that matters. Start directly with the first required heading, add no preamble and no fifth level-two heading. Never expose YAML, fixed field names, internal status enums, internal paths, or unexplained acronyms unless the user explicitly asks for a technical packet, audit details, or debug output.

The transcript outline is not a complete script. It gives each natural-language section's purpose, 2–5 speaking points, evidence or visuals, transition, and estimated duration. State facts, inferences, missing data, and unresolved decisions separately in ordinary Chinese. If the request also asks for a full script, approval, or early handoff, place the plain-language refusal inside the fourth required part; do not add a new heading or cite internal fields to justify it. Do not claim that a structure will produce high retention or high views, and never treat system success as Koda approval.
