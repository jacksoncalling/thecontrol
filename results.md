# Results: does the Continuous Discovery folder beat no folder?

**Short answer: no, not on these 8 questions.** Both arms got every question right in substance. The folder did not fix a single mistake the plain chat made. It did change *how* the model answered, mostly in ways that got in the way of a one-off question. Details below, including where the folder did worse.

## Setup in one paragraph

Same model in both arms: Sonnet 5.5 on claude.ai, effort Medium, web search, memory and personal preferences off, one fresh chat per question. Control: plain chats, no files. Treatment: a Claude project with the 21 `.md` files of the Continuous Discovery Operator (`treatment-upload/`) and the operator's own project instruction. Questions were written cold from Teresa Torres' public material by an agent that never saw the folder, and committed before any run (`0fbe034`). Answers were shuffled into A and B per question and graded blind by a fresh Claude agent against the rubric in `questions.md` (`grading/blind-grades-claude.md`). The key that maps A and B back to the arms is in `grading/key.json`.

## Scores

| Q | Topic | Control | Treatment |
|---|---|---|---|
| Q01 | Opportunities vs disguised solutions | Correct, or Partly on a strict reading (see note 1) | Correct |
| Q02 | Past story vs generalisation vs speculation | Correct | Correct |
| Q03 | Strong or weak interview | Correct | Correct |
| Q04 | Outcome types | Correct | Correct (one level mix-up beyond the question, note 4) |
| Q05 | Assumption types | Correct | Correct |
| Q06 | Which assumption to test first | Correct | Correct |
| Q07 | Not enough evidence (the trap) | Correct | Correct, or Partly on a strict reading (see note 2) |
| Q08 | What belongs at the opportunity level | Correct | Correct (internal slip, note 5) |

**Total:** 8 of 8 correct in both arms on the substance reading. On the strict reading, 7 correct and 1 partly correct in both arms. **That's a tie.**

## What actually differed

| | Control | Treatment |
|---|---|---|
| Words in answers (all 8) | 3,333 | 3,145 |
| Asked for a product outcome before going on | 0 of 8 | 4 of 8 (Q01, Q03, Q05, Q07) |
| Used the folder's own labels ("Thin", "Emerging", "NEEDS MORE INTERVIEWS", "workspace") | n/a | Q03, Q06, Q07 |
| Mentioned the folder's demo data (Babor) | n/a | Q07 |
| Claims the rubric does not cover | Q01: adds "I forget what's in my fridge" to [2], which the speaker didn't say | Q03, Q07: "interview 1 of the 3-4 Torres recommends" (from the folder's `02-interview/CONTEXT.md`, not in the rubric's sources, not checked). Q05: "desirability is what Torres suggests testing first in most cases" |
| Errors beyond the question | none found | Q04, Q07, Q08 (notes 2, 4, 5) |

### Notes

1. **Q01 control.** It puts [11] under the "(b) Solutions presented as needs" heading, then says in the same place that [11] is "neither a need nor a solution". The rubric wants (b) to name exactly [8] and [10]. The grader gave both readings.
2. **Q07 treatment, the trap question.** It says plainly "I can't draw one" and invents no moments, which meets the Correct clause. But it then offers "the honest map is a single fragment" and files a new opportunity ("keeping weekly grocery spend predictable") as Emerging. The expected answer leaves the map empty and treats price sensitivity as a topic for follow-up, not an opportunity. **This is the one place where the folder pushed the model toward the wrong kind of answer.** The folder's job is to fill a snapshot, so it filled one, even where the right snapshot is empty. The control answered the same question cleanly: "If I drew a numbered sequence from these, I would be inventing moments."
3. **Outcome gating.** The operator's instruction says "Start with 01-outcome if no outcome has been defined." On single method questions, that turned into "no product outcome has been defined yet" and a question back, four times. None of them withheld the answer, but it is friction a user asking one question doesn't need.
4. **Q04 treatment.** It classifies (g) correctly as a product outcome, then suggests it "works well as a sibling or child opportunity area under (c)". That mixes tree levels: an outcome is not an opportunity.
5. **Q08 treatment.** Opens with "Four of the eight belong at the opportunity level" and then lists three. The table below is right.

## Where the folder lost or tied

- **Tied on correctness, all 8 questions.**
- **Lost on the trap question (Q07)** on the strict reading, and on cleanliness in any reading.
- **Lost on focus:** more side claims and slips beyond the question (Q04, Q05, Q07, Q08), and outcome gating on half the questions.
- **Not slower to read:** about 6% fewer words overall. I didn't time the runs.
- **Small plus:** the treatment's Q07 ends with a useful interview coaching note and three re-interview prompts. A product manager would value that, but the question didn't ask for it.

## Why the plain chat was already this good

This is Josh's reading, and it's a hypothesis we can't prove from inside this test. Teresa Torres' work is public, heavily cited and widely taught across product management, especially in the US tech industry. Her definitions are unusually structured: named outcome types, five assumption types, explicit tests like "more than one way to address it?". Material like that is very likely well represented in what the model learned. So the baseline already "knows" Torres, and a folder that restates her definitions adds little.

The control shows this directly. Asked to work "using Teresa Torres' definitions", the plain chat used her concepts correctly every time without any files: assumption mapping in Q06, all five assumption types in Q05, a "tell me about the last time" rewrite in Q03.

**What this means for the folder.** Its value is not the definitions. If it has value, it's in the parts these 8 questions don't test: keeping a tree across many interviews, counting interviews, capping confidence by interview quality, routing. Our questions were single-shot knowledge questions. A fair next test would give both arms a series of 4 to 5 interviews and check what the tree looks like at the end.

## Limits of this test

- **One run per question per arm.** No repeats, so we can't say how stable each answer is.
- **One grader, and it's a Claude model** grading Claude answers. We planned and committed a second blind grader from another vendor (Codex, see `RUN.md` and commit `e25c9a8`) but did not run it before the deadline. So there is no grader agreement figure.
- **Blinding is partial.** Treatment answers name the folder's labels and its demo data, so a grader could guess the arm. Answers were not redacted, because the transcripts stay raw.
- **The rubric was written by a Claude agent** from Torres' public pages (`SOURCES.md`). It accepts two answers in places (Q02 [12], Q05 (f)), which makes those parts less sharp.
- **The runs were done by hand** and pasted from the copy button. Times in the transcript headers are when each answer was saved to its file, not the exact send time.

## What changed in the folder because of this

See the section below once the fix is committed. Planned, from notes 2 and 3:

- In `CLAUDE.md`: if the user asks a direct method question instead of bringing work to process, answer it directly. Don't ask for an outcome first and don't mention demo data.
- In `03-opportunities/docs/snapshot-template.md` and `02-interview/CONTEXT.md`: when no specific story was told, the experience map stays empty and says so. Generalisations go to insights or follow-up questions, never to a new opportunity.

These changes have **not** been re-run against the questions.
