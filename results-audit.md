# Audit of results.md

- **What was audited:** `results.md` as first committed (`2477be0`, with the folder section from `3b3fa09`).
- **Against what:** the comp brief's three bars (questions first, raw transcripts, report the losses), the grading rules in `questions.md`, and the blind grades in `grading/blind-grades-claude.md` as the source. Not against taste.
- **Method:** AuditEdit drift checks (`/audit`), run by the same Claude session that wrote `results.md`. So this is a self-audit, and that's a limit: a cold auditor would be stronger.
- **Date:** 2026-10-13

## Diagnosis

The main drift was **not** flattery toward the folder. It went the other way. To look honest, the first version was harder on the folder than the evidence allows.

1. **Selective inclusion, major.** It said "The folder did not fix a single mistake the plain chat made". But the control's one shaky answer (Q01, [11] placed under the solutions heading) was answered cleanly by the treatment. On the strict reading, each arm had exactly one partly correct answer, on different questions. The first version reported the folder's slip (Q07) in detail and left the folder's matching win out. The distinction that got lost: *a tie in totals is not the same as the same answers*.
2. **Lost contact, minor.** "Asked for a product outcome before going on: 4 of 8" overstated it. Only Q01 and Q03 raised it at the top; Q05 and Q07 raised it at the end, after answering.
3. **Metaphor as explanation, minor.** "The folder's job is to fill a snapshot, so it filled one" read as a mechanism. But the prompt asked *both* arms for a snapshot. The specific folder rule that plausibly pushed it ("Do not reject a Thin transcript ... Even opinion-based interviews contain signal") wasn't named, and the claim rests on one run.
4. **Selective inclusion, minor.** Grader notes left out of the first version: the control's speculative lead about [1], the treatment calling [9] "speculation", and a deviation both arms share (Q06, A4 rated low instead of medium).
5. **Lost contact, minor.** The training-data explanation said "very likely". We can't see the training data, so it's now "plausibly", and marked as a guess.
6. **Omission, minor.** The limits didn't say who has a stake: Josh built the folder and ran both arms, and the assistant that wrote the results also helped design the test.

Checks that came out clear: mirroring (Josh's Torres hypothesis is labelled as his and as unproven), premature abstraction (none), re-flattening (the verdict is scoped to "these 8 questions", and it names the next test).

## Repair log

| # | Drift | Patch applied to `results.md` |
|---|---|---|
| 1 | Selective inclusion | Short answer and total now say each arm had one shaky answer on different questions. Added "Won on Q01" under "Where the folder lost or tied". |
| 2 | Lost contact | Row renamed "Brought up the missing product outcome", with where it was raised. Note 3 changed to match. |
| 3 | Metaphor as explanation | Note 2 now says both arms were asked for a snapshot, names the folder rule and template, and says "from one run only". |
| 4 | Selective inclusion | Added the two missing side claims and a "Shared by both arms" row. |
| 5 | Lost contact | "very likely" changed to "plausibly", marked as a guess. |
| 6 | Omission | New limit: "The people judging have a stake". |

The verdict didn't change: a tie on correctness, with the folder adding friction on single questions. What changed is that the loss list and the win list are now held to the same standard.

## For next time (the repair to the instrument)

```json
{
  "target": "how results.md is written in a control run",
  "drift_type": "selective inclusion (anti-flattery overcorrection)",
  "what_was_lost": "a tie in totals vs. which answers each arm got wrong",
  "patch": "For every loss reported for one arm, check whether the other arm has a matching loss on a different question, and report both in the same place.",
  "test_prompt": "Write results.md for a control where both arms score 7 correct and 1 partly correct, on different questions.",
  "retest_criteria": "The short answer names both partial answers and the question each was on."
}
```
