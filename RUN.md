# How the two arms are run

Anyone (including a mod) can repeat this. Same model, same settings, same prompts, same order.

## Settings for both arms

- claude.ai in the browser. Same model in both arms; write the exact name in each transcript.
- Extended thinking: same setting in both arms.
- Web search: **off** (otherwise the control can read producttalk.org and the test is about search, not the folder).
- Memory and "search past chats": **off**. Personal preferences / styles: **empty or default** for the duration of the runs.
- One **fresh conversation per question**. Paste the text of `prompts/qNN.txt` exactly, nothing before or after it.
- Copy the answer with the copy button under the response and paste it into `control/qNN.md` or `treatment/qNN.md` under "Response". Do not edit. If a run errors or gets cut off, keep it and note it; do not rerun silently.

## Control arm

- A normal chat, **not** inside any project. No files attached.

## Treatment arm

1. Create a new Claude project, for example "comp14 treatment".
2. Upload every `.md` file from `discovery-operator/` to the project knowledge (21 files: `CLAUDE.md`, `README.md`, the five `CONTEXT.md` files, everything under `docs/`, `examples/`, `reference/`, and the `.md` files under `output/`). The `.html` and `.js` files are the visual tree and are not uploaded.
3. **Never upload `questions.md`.** It holds the expected answers.
4. Project instructions, exactly as the operator's README says:

   ```
   Read CLAUDE.md first. You are this operator. Follow the workspace
   routing in the navigation table. Start with 01-outcome if no
   outcome has been defined.
   ```

5. Run Q01 to Q08, each in a new chat inside the project.

## Grading

Grading is blind, and the method was committed before any run.

1. `python scripts/blind.py --key <somewhere outside grading/>/key.json` copies only the response text of each answer into `grading/blind/qNN-A.md` and `qNN-B.md`, shuffled per question. The key stays outside `grading/` until grading is done.
2. A fresh agent with no context gets `grading/GRADER-BRIEF.md` as its prompt. It reads only `questions.md` and `grading/blind/`, and writes `grading/blind-grades.md` (Correct / Partly correct / Wrong, with the rubric clause and a quote).
3. Then the key is committed as `grading/key.json` and `results.md` maps the grades back to control and treatment, question by question, including ties and losses.

Known limit: the blinding is partial. A treatment answer may name the operator's own labels or files, which can give the arm away. Answers are not redacted, because the transcripts stay raw.
