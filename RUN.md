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
2. Upload all 21 files from `treatment-upload/` to the project knowledge (select all, drag in once). That folder is every `.md` file from `discovery-operator/`, made by `python scripts/make_upload.py`. A project stores files without folders and the operator has five files named `CONTEXT.md`, so the path is built into each name (`01-outcome/CONTEXT.md` becomes `01-outcome__CONTEXT.md`). Contents are unchanged. The `.html` and `.js` files are the visual tree and are not uploaded.
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
2. Two graders from different model makers grade separately, on the same blind files, with the same brief (`grading/GRADER-BRIEF.md`): a fresh Claude agent with no context writes `grading/blind-grades-claude.md`, and Codex (OpenAI) writes `grading/blind-grades-codex.md`. Each reads only `questions.md` and `grading/blind/`, never the other's grades or the key. Verdicts are Correct / Partly correct / Wrong, with the rubric clause and a quote.
3. Then the key is committed as `grading/key.json` and `results.md` maps both graders' verdicts back to control and treatment, question by question, including ties and losses. It reports how often the two graders agree and lists every disagreement.

Known limit: the blinding is partial. A treatment answer may name the operator's own labels or files, which can give the arm away. Answers are not redacted, because the transcripts stay raw.
