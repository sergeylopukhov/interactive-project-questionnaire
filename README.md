# Interactive Project Questionnaire

![Interactive Project Questionnaire hero](assets/interactive-project-questionnaire-hero.png)

Collect project decisions through a local clickable form instead of a long chat questionnaire.

**English description:** Interactive Project Questionnaire is a dependency-free Codex skill for AI agents that need to gather requirements, clarify project scope, and turn planning questions into a local form with saved JSON and Markdown answers.

**Описание на русском:** Interactive Project Questionnaire — скилл для Codex и других AI-агентов, который собирает требования через локальную анкету. Пользователь выбирает варианты, добавляет свои ответы и комментарии, а агент получает структурированные файлы для дальнейшей работы.

## What It Does

- Replaces long numbered question lists with a browser-based local form.
- Saves answers as `answers.json` and `answers.md`.
- Supports English and Russian UI labels.
- Supports custom "Other" answers and "Not sure / recommend for me" choices.
- Adds a comment field to every question.
- Handles required questions, recommendations, scale inputs, and simple conditional follow-ups.
- Runs only on `127.0.0.1` and uses no external dependencies.

## Why Use It

Agents often need project decisions before they can build well. Chat-based questionnaires are hard to answer and easy to misread. This skill turns those decisions into a compact local form, then gives the agent clean files to continue from.

Good fit for:

- product briefs
- feature scoping
- landing page requirements
- design direction choices
- automation specs
- bot and dashboard requirements
- implementation planning

## Repository Layout

```text
interactive-project-questionnaire/
  SKILL.md
  agents/openai.yaml
  scripts/questionnaire_server.py
  scripts/smoke_test.py
  references/question_schema.md
  references/usage_examples.md
assets/
  interactive-project-questionnaire-hero.png
```

## Install For Codex

Copy the skill folder into your Codex skills directory:

```bash
cp -R interactive-project-questionnaire ~/.codex/skills/
```

Then ask Codex to use it:

```text
Use $interactive-project-questionnaire to collect requirements for this project.
```

## Use Without Installing

You can also run the bundled server directly:

```bash
python3 interactive-project-questionnaire/scripts/questionnaire_server.py --port 0
```

Open the printed local URL:

```text
http://127.0.0.1:<port>/
```

## Typical Agent Flow

1. Create `.project-questionnaire/questions.json`.
2. Validate the questionnaire.
3. Start the local server.
4. Give the user the local URL.
5. Wait until the user saves the form.
6. Read `.project-questionnaire/answers.md` and `.project-questionnaire/answers.json`.
7. Summarize the decisions and continue the task.

## Quick Start

Validate a questionnaire:

```bash
python3 interactive-project-questionnaire/scripts/questionnaire_server.py \
  --input .project-questionnaire/questions.json \
  --validate-only
```

Run the local form:

```bash
python3 interactive-project-questionnaire/scripts/questionnaire_server.py \
  --input .project-questionnaire/questions.json \
  --out-dir .project-questionnaire \
  --port 0
```

Run smoke tests:

```bash
python3 interactive-project-questionnaire/scripts/smoke_test.py
```

Print the built-in demo questionnaire:

```bash
python3 interactive-project-questionnaire/scripts/questionnaire_server.py --print-demo
```

## Minimal Questionnaire

```json
{
  "title": "Project Brief",
  "description": "Choose the direction so the agent can continue with less back-and-forth.",
  "language": "en",
  "questions": [
    {
      "id": "goal",
      "title": "What should this project optimize for first?",
      "type": "single_choice",
      "required": true,
      "recommended": "mvp",
      "allow_other": true,
      "allow_recommend": true,
      "options": [
        {
          "value": "mvp",
          "label": "Fast MVP"
        },
        {
          "value": "polished_v1",
          "label": "Polished first version"
        }
      ]
    }
  ]
}
```

## Russian UI

Set `language` to `ru`:

```json
{
  "title": "Бриф проекта",
  "description": "Выберите направление, чтобы агент продолжил работу без длинной переписки.",
  "language": "ru",
  "questions": [
    {
      "id": "goal",
      "title": "Какой результат важнее всего?",
      "type": "single_choice",
      "required": true,
      "allow_other": true,
      "allow_recommend": true,
      "options": [
        {
          "value": "mvp",
          "label": "Быстрый MVP"
        },
        {
          "value": "polished_v1",
          "label": "Аккуратная первая версия"
        }
      ]
    }
  ]
}
```

## Output Files

After the user saves the form, the server writes:

```text
.project-questionnaire/answers.json
.project-questionnaire/answers.md
```

Existing answer files are backed up before new ones are written.

## Cleanup

Cleanup is explicit because the agent needs to read the saved answers:

```bash
python3 interactive-project-questionnaire/scripts/questionnaire_server.py \
  --out-dir .project-questionnaire \
  --cleanup
```

The cleanup command removes generated questionnaire files and keeps `.project-questionnaire/.gitignore`.

## Suggested GitHub Descriptions

English:

```text
Collect AI project requirements through a local clickable questionnaire with JSON and Markdown outputs.
```

Русский:

```text
Локальная анкета для AI-агентов: собирает требования к проекту и сохраняет ответы в JSON и Markdown.
```

## License

No license has been selected yet.
