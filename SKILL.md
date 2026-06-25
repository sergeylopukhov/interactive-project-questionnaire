---
name: interactive-project-questionnaire
description: >-
  Automatically use this when an AI agent should ask questions before implementation, collect project requirements, clarify a product or feature, prepare a brief, gather a landing page or UI/UX brief, choose between answer options, or interview the user through a local clickable questionnaire instead of a long chat question list. Trigger on requests like "ask me questions first", "collect requirements", "prepare a brief", "clarify the project", "help me choose options", and Russian phrases such as "задай вопросы по проекту", "собери требования", "подготовь бриф", "уточни детали", "сначала спроси", "дай варианты ответов", "хочу выбрать варианты", "опроси меня перед реализацией". Supports saved JSON/Markdown answers, custom "other" answers, recommendation requests, comments, and conditional questions.
---

# Interactive Project Questionnaire

Use this skill to replace long chat-based planning prompts with a local clickable questionnaire. The goal is to let a user choose options, add custom answers and comments, save the result locally, then let the agent continue from the saved decisions.

## Core Rules

- Use `scripts/questionnaire_server.py`; do not hand-build a one-off HTML form.
- Bind only to `127.0.0.1`.
- Do not use external dependencies, package managers, CDNs, internet access, Flask, FastAPI, npm, or pip.
- Keep questions practical and decision-oriented.
- Prefer 5-12 questions unless the project clearly needs more.
- Use the user's language for the questionnaire. Set top-level `language` to `"en"` or `"ru"` when using built-in UI labels.
- Use `ui` overrides only when built-in labels are not enough.
- Include `allow_other: true` on important choice questions when the supplied options may be incomplete.
- Include `allow_recommend: true` when the agent can reasonably choose or recommend a direction.
- Expect every question in the UI to include an optional per-question comment field.
- Never overwrite existing answer files without backups; the server handles backups automatically.
- Do not delete generated questionnaire files until the agent has read the saved answers.

## Workflow

1. Understand the project or decision context from the user request and local files.
2. Read `references/question_schema.md` before writing `questions.json`.
3. Create a project-local questionnaire file, preferably:

   ```bash
   .project-questionnaire/questions.json
   ```

4. Validate it:

   ```bash
   python3 <skill-dir>/scripts/questionnaire_server.py --input .project-questionnaire/questions.json --validate-only
   ```

5. Start the local server:

   ```bash
   python3 <skill-dir>/scripts/questionnaire_server.py --input .project-questionnaire/questions.json --out-dir .project-questionnaire --port 0
   ```

6. Give the user the printed `http://127.0.0.1:<port>/` URL.
7. Ask the user to open the URL, answer the questions, save the form, and then tell the agent they are done.
8. Read both files:

   ```text
   .project-questionnaire/answers.md
   .project-questionnaire/answers.json
   ```

9. Summarize the collected decisions in the user's language.
10. Continue the requested task using those answers.

## Questionnaire Authoring

- Use concise option labels; put explanation in `help_text`.
- Use stable lowercase `id` values with letters, numbers, `_`, or `-`.
- Put agent-only details in `metadata`, not user-facing option text.
- Use `show_if` only for simple follow-up dependencies.
- Use `language: "en"` for English UI labels and `language: "ru"` for Russian UI labels.
- Use `ui` for project-specific label overrides such as a different "Other" label or save-button text.

## Manual Commands

Print the built-in demo questionnaire:

```bash
python3 <skill-dir>/scripts/questionnaire_server.py --print-demo
```

Run with a project-local questionnaire:

```bash
python3 <skill-dir>/scripts/questionnaire_server.py --input .project-questionnaire/questions.json --out-dir .project-questionnaire --port 0
```

Use a fixed port:

```bash
python3 <skill-dir>/scripts/questionnaire_server.py --input .project-questionnaire/questions.json --out-dir .project-questionnaire --port 8765
```

Validate without starting the server:

```bash
python3 <skill-dir>/scripts/questionnaire_server.py --input .project-questionnaire/questions.json --validate-only
```

Run smoke tests:

```bash
python3 <skill-dir>/scripts/smoke_test.py
```

Clean generated questionnaire files only when the user explicitly asks:

```bash
python3 <skill-dir>/scripts/questionnaire_server.py --out-dir .project-questionnaire --cleanup
```

## References

- Schema: `references/question_schema.md`
- Usage examples: `references/usage_examples.md`
- Server: `scripts/questionnaire_server.py`
