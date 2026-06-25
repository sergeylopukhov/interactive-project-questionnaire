<div align="center">

![Interactive Project Questionnaire](assets/interactive-project-questionnaire-hero.png)

# Interactive Project Questionnaire

**Codex skill for local clickable project questionnaires.**  
**Скилл Codex для локальных кликабельных анкет по проекту.**

[Русский](#русский) · [English](#english)

</div>

---

## Русский

Этот скилл помогает Codex не задавать длинный список вопросов в чате. Вместо этого Codex запускает локальную анкету в браузере, пользователь выбирает варианты и добавляет комментарии, а ответы сохраняются в `answers.json` и `answers.md`.

### Установка

```bash
git clone --depth 1 https://github.com/sergeylopukhov/interactive-project-questionnaire.git ~/.codex/skills/interactive-project-questionnaire
```

### Использование

```text
Use $interactive-project-questionnaire to collect requirements for this project.
```

На русском:

```text
Используй $interactive-project-questionnaire и собери требования к проекту через локальную анкету.
```

### Проверка

```bash
python3 ~/.codex/skills/interactive-project-questionnaire/scripts/smoke_test.py
```

### Что делает

- запускает форму только на `127.0.0.1`;
- сохраняет ответы в JSON и Markdown;
- поддерживает русский и английский интерфейс;
- добавляет «Другое / свой вариант» и «Не уверен / порекомендуй сам»;
- сохраняет комментарии к каждому вопросу;
- не требует npm, pip, Flask, FastAPI или внешних сервисов.

### Где смотреть формат анкеты

- [`references/question_schema.md`](references/question_schema.md) — схема `questions.json`;
- [`references/usage_examples.md`](references/usage_examples.md) — примеры запросов и сценариев.

---

## English

This Codex skill replaces long chat-based question lists with a local browser questionnaire. The user selects options, adds comments, and the answers are saved as `answers.json` and `answers.md`.

### Install

```bash
git clone --depth 1 https://github.com/sergeylopukhov/interactive-project-questionnaire.git ~/.codex/skills/interactive-project-questionnaire
```

### Use

```text
Use $interactive-project-questionnaire to collect requirements for this project.
```

### Check

```bash
python3 ~/.codex/skills/interactive-project-questionnaire/scripts/smoke_test.py
```

### Features

- runs only on `127.0.0.1`;
- saves answers as JSON and Markdown;
- supports English and Russian UI labels;
- supports "Other" and "Not sure / recommend for me" choices;
- saves per-question comments;
- requires no npm, pip, Flask, FastAPI, or external service.

### Format

- [`references/question_schema.md`](references/question_schema.md) — `questions.json` schema;
- [`references/usage_examples.md`](references/usage_examples.md) — prompts and usage examples.

---

## License

No license has been selected yet.
