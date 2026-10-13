# The Control: a Continuous Discovery folder vs no folder

Entry for Clief Notes Weekly Comp #14, "The Control", by Joshua Baker.

**Question:** does my Continuous Discovery Operator (a Claude project folder that runs Teresa Torres' Continuous Discovery Habits workflow) answer discovery questions better than plain Claude with no folder?

**Result:** no measurable difference in correctness on 8 questions. Both arms were right on all 8. The folder made the model ask for a product outcome on half the questions and pushed it toward filling a snapshot on the one question where the right answer was "there is no story here". Full write-up, including losses: [results.md](results.md).

## What's in this repo

| Path | What it is |
|---|---|
| `questions.md` | 8 questions with expected answers, grading rules and Torres sources. Committed first (`0fbe034`), before any run. |
| `SOURCES.md` | The Torres / Product Talk pages the question writer read. |
| `prompts/` | Each prompt exactly as pasted. |
| `discovery-operator/` | The folder under test. Identical to its public version (argo-continuous-discovery `6d70e8e`) during the runs; two fixes were added after the results (see results.md and git log). |
| `treatment-upload/` | The 21 files actually uploaded to the Claude project for the run (path built into the name). Not updated with the later fixes, so it stays the record of what was tested. |
| `control/` | Raw transcripts, no folder. |
| `treatment/` | Raw transcripts, with the folder. |
| `grading/` | Grader brief, blind answer files, blind grades, and the key. |
| `RUN.md` | How to re-run both arms and the grading. |
| `results.md` | What changed, question by question, including ties and losses. |
| `results-audit.md` | A self-audit of results.md for bias, and what it changed. |

## How the folder maps to the comp's five files

The operator was built for comp #7 and uses a different ICM layout. I didn't rebuild it for this comp:

- **identity.md** → `discovery-operator/CLAUDE.md` (who the operator is, what it is not)
- **rules.md** → the five `CONTEXT.md` files, one per phase (outcome, interview, opportunities, solutions, experiments)
- **examples.md** → `discovery-operator/03-opportunities/examples/babor-interviews.md`
- **reference/** → `discovery-operator/*/docs/` and `discovery-operator/reference/`
- **README.md** → `discovery-operator/README.md`

## The order things happened in (see git log)

1. Questions written cold and committed.
2. Folder snapshot and run protocol committed.
3. Blind grading method committed, then a second grader (Codex) added to the plan. The Codex grading was **not run** for lack of time; see results.md.
4. Control transcripts committed, then treatment transcripts.
5. Blind answer files committed, graded blind, then unblinded.
6. Results written.
7. Two fixes to the folder, from what the results showed. Not re-run yet.

## Credits

Method: Teresa Torres, *Continuous Discovery Habits* and producttalk.org. Folder architecture: Jake van Clief's Interpretable Context Methodology. The Larder product, Brightfold Labs and all interviews in the questions are invented.
