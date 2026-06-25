<div align="center">

![Interactive Project Questionnaire](assets/interactive-project-questionnaire-hero.png)

# Interactive Project Questionnaire

**Codex skill for local clickable project questionnaires.**  
**Скилл Codex для локальных кликабельных анкет по проекту.**

[English](#english) · [Русский](#русский)

</div>

---

## English

This Codex skill replaces long chat-based question lists with a local browser questionnaire. The user selects options, adds comments, and the answers are saved as `answers.json` and `answers.md`.

### Install

```bash
git clone --depth 1 https://github.com/sergeylopukhov/interactive-project-questionnaire.git ~/.codex/skills/interactive-project-questionnaire
```

### Use

After installation, Codex can pick this skill automatically when the request looks like requirements gathering:

```text
Ask me questions before implementation.
```

```text
Collect requirements before you build.
```

You can also mention the skill name directly:

```text
Use interactive-project-questionnaire when you need to ask me project questions.
```

Or invoke the skill explicitly:

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

## Русский

Этот скилл помогает Codex не задавать длинный список вопросов в чате. Вместо этого Codex запускает локальную анкету в браузере, пользователь выбирает варианты и добавляет комментарии, а ответы сохраняются в `answers.json` и `answers.md`.

### Установка

```bash
git clone --depth 1 https://github.com/sergeylopukhov/interactive-project-questionnaire.git ~/.codex/skills/interactive-project-questionnaire
```

### Использование

После установки Codex может выбрать скилл сам, если запрос похож на сбор требований:

```text
Сначала задай мне вопросы по проекту.
```

```text
Собери требования перед реализацией.
```

Можно указать имя скилла напрямую:

```text
Используй interactive-project-questionnaire, чтобы задать мне вопросы по проекту.
```

Или вызвать через `$`:

```text
Use $interactive-project-questionnaire to collect requirements for this project.
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

## License

No license has been selected yet.
