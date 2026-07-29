<p align="center">
  <img src="assets/interactive-project-questionnaire-hero.png" alt="Interactive Project Questionnaire" width="100%">
</p>

<h1 align="center">Interactive Project Questionnaire</h1>

<p align="center">
  Portable Agent Skill for local clickable project questionnaires.<br>
  Универсальный Agent Skill для локальных кликабельных анкет по проекту.
</p>

<p align="center">
  <a href="https://agentskills.io/"><img src="https://img.shields.io/badge/Agent_Skills-open_standard-1f6feb" alt="Agent Skills open standard"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/network-127.0.0.1-0b8f60" alt="Localhost only">
  <img src="https://img.shields.io/badge/dependencies-zero-6b7280" alt="No external dependencies">
</p>

<p align="center">
  <a href="#english">English</a> · <a href="#русский">Русский</a>
</p>

---

## English

Long requirement interviews are awkward in chat. This [Agent Skills](https://agentskills.io/) package opens a local browser form instead, then saves the answers for the agent to use.

The installer includes paths for OpenCode, Claude Code, Gemini CLI, Qwen Code, Kimi Code CLI, Cursor, Codex, and Hermes Agent. It can also install to `~/.agents/skills/` or any directory passed with `--target`.

> [!NOTE]
> OpenCode, Claude Code, Gemini CLI, Qwen Code, Kimi Code CLI, and Cursor are supported directly. The installer detects them automatically and verifies the installed copy.

### How it works

1. The agent turns unresolved project decisions into a local questionnaire.
2. The user selects options, adds custom answers or comments, and saves the form.
3. The skill writes `answers.json` and `answers.md`.
4. The agent reads the saved decisions and continues the original task.

### Quick start

Send the repository URL to your coding agent:

```text
Install this skill for yourself and verify that it works:
https://github.com/sergeylopukhov/interactive-project-questionnaire
```

> [!TIP]
> Agent instructions: clone the repository to a temporary directory and inspect `SKILL.md`. Run `python3 scripts/install_skill.py --agent auto`. The command copies the package and runs the smoke test from the installed location. If detection fails, find the client's global Agent Skills directory and pass it with `--target`.

<details>
<summary><strong>Manual installation and agent presets</strong></summary>

```bash
git clone --depth 1 https://github.com/sergeylopukhov/interactive-project-questionnaire.git
cd interactive-project-questionnaire
python3 scripts/install_skill.py --agent auto
```

Choose another agent or install for several:

```bash
python3 scripts/install_skill.py --agent claude
python3 scripts/install_skill.py --agent opencode
python3 scripts/install_skill.py --agent gemini
python3 scripts/install_skill.py --agent qwen
python3 scripts/install_skill.py --agent kimi
python3 scripts/install_skill.py --agent cursor
python3 scripts/install_skill.py --agent all
```

For any other Agent Skills client, pass its global skills directory:

```bash
python3 scripts/install_skill.py --target /path/to/agent/skills
```

Presets install to:

| Preset | Global directory |
| --- | --- |
| `codex` | `${CODEX_HOME:-~/.codex}/skills/` |
| `claude` | `~/.claude/skills/` |
| `opencode` | `${XDG_CONFIG_HOME:-~/.config}/opencode/skills/` |
| `gemini` | `~/.gemini/skills/` |
| `qwen` | `~/.qwen/skills/` |
| `kimi` | `${KIMI_CODE_HOME:-~/.kimi-code}/skills/` |
| `cursor` | `~/.cursor/skills/` |
| `hermes` | `~/.hermes/skills/` |
| `agents` | `~/.agents/skills/` |

Existing installations are preserved unless `--force` is passed. Forced updates create a dated backup first.

</details>

### Use

After installation, a compatible agent can pick this skill automatically when the request looks like requirements gathering:

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
python3 scripts/smoke_test.py
```

### Features

- runs only on `127.0.0.1`;
- saves answers as JSON and Markdown;
- supports English and Russian UI labels;
- supports "Other" and "Not sure / recommend for me" choices;
- saves per-question comments;
- requires no npm, pip, Flask, FastAPI, or external service.

### Documentation

| Document | Contents |
| --- | --- |
| [`references/question_schema.md`](references/question_schema.md) | `questions.json` schema |
| [`references/usage_examples.md`](references/usage_examples.md) | Prompts and usage examples |
| [`SKILL.md`](SKILL.md) | Agent workflow and operating rules |

---

## Русский

Длинный опрос по проекту неудобно проводить в чате. Скилл открывает локальную анкету в браузере, сохраняет ответы и возвращает их агенту.

В установщике есть готовые пути для OpenCode, Claude Code, Gemini CLI, Qwen Code, Kimi Code CLI, Cursor, Codex и Hermes Agent. Для других клиентов можно выбрать `~/.agents/skills/` или передать нужный каталог через `--target`.

> [!NOTE]
> OpenCode, Claude Code, Gemini CLI, Qwen Code, Kimi Code CLI и Cursor поддерживаются напрямую. Установщик определяет их автоматически и проверяет установленную копию.

### Как это работает

1. Агент собирает нерешённые вопросы по проекту в локальную анкету.
2. Пользователь выбирает варианты, добавляет свои ответы или комментарии и сохраняет форму.
3. Скилл записывает результат в `answers.json` и `answers.md`.
4. Агент читает сохранённые решения и продолжает исходную задачу.

### Быстрый старт

Отправьте агенту ссылку на репозиторий:

```text
Установи этот скилл для себя и проверь, что он работает:
https://github.com/sergeylopukhov/interactive-project-questionnaire
```

> [!TIP]
> Инструкция для агента: клонируйте репозиторий во временную папку и проверьте `SKILL.md`. Выполните `python3 scripts/install_skill.py --agent auto`. Команда скопирует пакет и запустит smoke-тест из установленной папки. Если автоматическое определение не сработало, найдите глобальный каталог Agent Skills своего клиента и передайте путь через `--target`.

<details>
<summary><strong>Ручная установка и профили агентов</strong></summary>

```bash
git clone --depth 1 https://github.com/sergeylopukhov/interactive-project-questionnaire.git
cd interactive-project-questionnaire
python3 scripts/install_skill.py --agent auto
```

Для другого агента или сразу нескольких:

```bash
python3 scripts/install_skill.py --agent claude
python3 scripts/install_skill.py --agent opencode
python3 scripts/install_skill.py --agent gemini
python3 scripts/install_skill.py --agent qwen
python3 scripts/install_skill.py --agent kimi
python3 scripts/install_skill.py --agent cursor
python3 scripts/install_skill.py --agent all
```

Для любого другого клиента Agent Skills укажите его каталог:

```bash
python3 scripts/install_skill.py --target /путь/к/каталогу/skills
```

Готовые профили:

| Профиль | Глобальный каталог |
| --- | --- |
| `codex` | `${CODEX_HOME:-~/.codex}/skills/` |
| `claude` | `~/.claude/skills/` |
| `opencode` | `${XDG_CONFIG_HOME:-~/.config}/opencode/skills/` |
| `gemini` | `~/.gemini/skills/` |
| `qwen` | `~/.qwen/skills/` |
| `kimi` | `${KIMI_CODE_HOME:-~/.kimi-code}/skills/` |
| `cursor` | `~/.cursor/skills/` |
| `hermes` | `~/.hermes/skills/` |
| `agents` | `~/.agents/skills/` |

Установщик не перезаписывает существующую копию без `--force`. При принудительном обновлении он сначала создаёт резервную копию с датой.

</details>

### Использование

После установки агент сам выберет скилл, когда запрос потребует собрать требования:

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
Используй $interactive-project-questionnaire, чтобы собрать требования к проекту.
```

### Проверка

```bash
python3 scripts/smoke_test.py
```

### Что делает

- запускает форму только на `127.0.0.1`;
- сохраняет ответы в JSON и Markdown;
- поддерживает русский и английский интерфейс;
- добавляет «Другое / свой вариант» и «Не уверен / порекомендуй сам»;
- сохраняет комментарии к каждому вопросу;
- не требует npm, pip, Flask, FastAPI или внешних сервисов.

### Документация

| Документ | Содержание |
| --- | --- |
| [`references/question_schema.md`](references/question_schema.md) | Схема `questions.json` |
| [`references/usage_examples.md`](references/usage_examples.md) | Примеры запросов и сценариев |
| [`SKILL.md`](SKILL.md) | Порядок работы и правила для агента |

---

## License

No license has been selected yet.
