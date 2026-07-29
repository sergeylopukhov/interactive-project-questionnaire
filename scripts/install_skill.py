#!/usr/bin/env python3
"""Install this Agent Skill for one or more compatible AI agents."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


SKILL_NAME = "interactive-project-questionnaire"
SKILL_DIR = Path(__file__).resolve().parent.parent
AGENT_CHOICES = (
    "agents",
    "claude",
    "codex",
    "cursor",
    "gemini",
    "hermes",
    "kimi",
    "qwen",
)
AGENT_COMMANDS = {
    "claude": ("claude",),
    "codex": ("codex",),
    "cursor": ("cursor", "cursor-agent"),
    "gemini": ("gemini",),
    "hermes": ("hermes",),
    "kimi": ("kimi",),
    "qwen": ("qwen",),
}
AGENT_ENV_MARKERS = {
    "claude": ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT"),
    "codex": ("CODEX_HOME", "CODEX_SANDBOX", "CODEX_THREAD_ID"),
    "cursor": ("CURSOR_AGENT", "CURSOR_SESSION_ID", "CURSOR_TRACE_ID"),
    "gemini": ("GEMINI_CLI_HOME", "GEMINI_CLI_SYSTEM_SETTINGS_PATH"),
    "hermes": ("HERMES_HOME", "HERMES_SESSION_ID"),
    "kimi": ("KIMI_CODE_HOME",),
    "qwen": ("QWEN_CODE_HOME",),
}
IGNORED_NAMES = {
    ".DS_Store",
    ".git",
    ".github",
    ".pytest_cache",
    "README.md",
    "__pycache__",
}


def agent_skill_root(agent: str, home: Path) -> Path:
    """Return the global skill root for a supported agent."""
    roots = {
        "agents": home / ".agents" / "skills",
        "claude": home / ".claude" / "skills",
        "codex": Path(os.environ.get("CODEX_HOME", home / ".codex")) / "skills",
        "cursor": home / ".cursor" / "skills",
        "gemini": home / ".gemini" / "skills",
        "hermes": home / ".hermes" / "skills",
        "kimi": Path(os.environ.get("KIMI_CODE_HOME", home / ".kimi-code")) / "skills",
        "qwen": home / ".qwen" / "skills",
    }
    return roots[agent].expanduser()


def copy_ignore(_directory: str, names: list[str]) -> set[str]:
    """Exclude repository-only and generated files from installed copies."""
    ignored = {name for name in names if name in IGNORED_NAMES}
    ignored.update(name for name in names if name.endswith(".pyc"))
    return ignored


def backup_path(destination: Path) -> Path:
    """Build a non-conflicting dated backup path next to the destination."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = destination.with_name(f"{destination.name}.backup-{timestamp}")
    suffix = 1
    while candidate.exists() or candidate.is_symlink():
        candidate = destination.with_name(f"{destination.name}.backup-{timestamp}-{suffix}")
        suffix += 1
    return candidate


def install_copy(skill_root: Path, *, force: bool, dry_run: bool) -> tuple[Path, Path | None]:
    """Install a clean copy under a skill root and optionally back up an old copy."""
    destination = skill_root.expanduser().resolve(strict=False) / SKILL_NAME
    backup = None

    if destination.exists() or destination.is_symlink():
        if not force:
            raise FileExistsError(
                f"{destination} already exists; rerun with --force to replace it with a dated backup"
            )
        backup = backup_path(destination)

    if dry_run:
        return destination, backup

    skill_root.mkdir(parents=True, exist_ok=True)
    if backup is not None:
        destination.rename(backup)

    try:
        shutil.copytree(SKILL_DIR, destination, ignore=copy_ignore)
    except Exception:
        if backup is not None and not destination.exists() and not destination.is_symlink():
            backup.rename(destination)
        raise

    return destination, backup


def verify_installation(destination: Path) -> None:
    """Run the bundled smoke test from the installed copy."""
    skill_file = destination / "SKILL.md"
    smoke_test = destination / "scripts" / "smoke_test.py"
    if not skill_file.is_file() or not smoke_test.is_file():
        raise RuntimeError(f"installed package is incomplete at {destination}")
    subprocess.run([sys.executable, str(smoke_test)], check=True)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install Interactive Project Questionnaire for compatible AI agents."
    )
    parser.add_argument(
        "--agent",
        action="append",
        choices=(*AGENT_CHOICES, "all", "auto"),
        help="Agent preset. Repeat for several agents, use 'auto' to detect clients, or 'all'.",
    )
    parser.add_argument(
        "--target",
        action="append",
        type=Path,
        default=[],
        help="Custom skills root for any other Agent Skills client. Repeatable.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installation after creating a dated backup.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print destinations without changing files.",
    )
    return parser.parse_args(argv)


def selected_roots(args: argparse.Namespace, home: Path) -> list[tuple[str, Path]]:
    agents = args.agent or []
    if "all" in agents:
        agents = list(AGENT_CHOICES)
    elif "auto" in agents:
        agents = detect_agents()

    roots: list[tuple[str, Path]] = []
    seen: set[Path] = set()

    for agent in agents:
        root = agent_skill_root(agent, home)
        normalized = root.resolve(strict=False)
        if normalized not in seen:
            roots.append((agent, root))
            seen.add(normalized)

    for target in args.target:
        root = target.expanduser()
        normalized = root.resolve(strict=False)
        if normalized not in seen:
            roots.append(("custom", root))
            seen.add(normalized)

    return roots


def detect_agents() -> list[str]:
    """Detect installed or active clients, falling back to the shared standard root."""
    active: list[str] = []

    for agent, markers in AGENT_ENV_MARKERS.items():
        if any(os.environ.get(marker) for marker in markers):
            active.append(agent)

    if active:
        return active

    detected: list[str] = []
    for agent, commands in AGENT_COMMANDS.items():
        if any(shutil.which(command) for command in commands):
            detected.append(agent)

    return detected or ["agents"]


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    roots = selected_roots(args, Path.home())

    if not roots:
        print("Choose at least one --agent or --target.", file=sys.stderr)
        return 2

    failures = 0
    for label, root in roots:
        try:
            destination, backup = install_copy(root, force=args.force, dry_run=args.dry_run)
            prefix = "WOULD INSTALL" if args.dry_run else "INSTALLED"
            print(f"{prefix} [{label}] {destination}")
            if backup is not None:
                backup_prefix = "WOULD BACK UP" if args.dry_run else "BACKED UP"
                print(f"{backup_prefix} {backup}")
            if not args.dry_run:
                verify_installation(destination)
                print(f"VERIFIED [{label}] {destination}")
        except Exception as exc:
            failures += 1
            print(f"FAILED [{label}] {exc}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
