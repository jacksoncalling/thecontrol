# Grader brief (blind)

This is the exact brief given to both grading agents: a cold Claude agent and Codex (OpenAI), run separately on the same blind files. It was written and committed before any run. The only line that differs between the two is the output file name, given as `<grader>` below (`claude` or `codex`).

---

You are grading answers to 8 questions about Teresa Torres' Continuous Discovery method. For each question there are two answers, A and B. You do not know where they came from, and you must not try to guess. Grade each answer on its own against the rubric.

## Read only these files

- `questions.md`: for each question, the prompt, the expected answer, the grading rule (Correct / Partly correct / Wrong) and the Torres sources.
- `grading/blind/q01-A.md`, `q01-B.md` through `q08-A.md`, `q08-B.md`: the answers.

Do not open any other file or folder in this repository, and do not search the web. In particular, do not open any other `grading/blind-grades-*.md` file or any key file. If an answer mentions a folder, file, framework label or company, ignore that; grade only the substance.

## How to grade

1. For each answer, apply the grading rule of that question literally. Use the grading rule, not your own view of Torres and not the answer's style or length.
2. Give the verdict: **Correct**, **Partly correct** or **Wrong**.
3. Give the reason in one or two sentences, naming the rubric clause that decided it and quoting the few words from the answer that triggered it (for example: "lists [8] as an opportunity, rubric Wrong clause").
4. If an answer adds claims that go beyond the question, note any that contradict the expected answer, even if the verdict does not change.
5. Note anything that is not about correctness but a reader would want to know: length (rough word count), whether it asked a question back instead of answering, whether it refused or hedged where the rubric expects a clear answer.
6. If the rubric is ambiguous for an answer, say so and give both readings. Do not resolve it in favour of either answer.

## Output

Write `grading/blind-grades-<grader>.md` with this structure:

```
# Blind grades

| Q | Answer | Verdict | Rubric clause | Words |
|---|---|---|---|---|
| Q01 | A | ... | ... | ... |
...

## Q01
### A
- Verdict:
- Reason (with quote):
- Contradictions beyond the question:
- Other notes:
### B
...
```

Then report back in under 150 words: the table totals per letter are not needed (the letters change per question), only any question where you found the rubric ambiguous or hard to apply.
