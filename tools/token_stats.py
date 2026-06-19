"""Estimate token counts for repo context files (zero LLM cost).

Uses a simple chars/4 heuristic—good enough to catch bloated AGENTS.md
or rules files before they tax every session.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Files that load into every AI coding session should stay small.
WATCHED_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "CLAUDE.md",
    ROOT / "README.md",
)

WARN_LINES = 200
WARN_TOKENS = 2000


@dataclass(frozen=True)
class FileStats:
    path: Path
    lines: int
    chars: int
    est_tokens: int

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def stats_for(path: Path) -> FileStats | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    return FileStats(
        path=path,
        lines=len(text.splitlines()),
        chars=len(text),
        est_tokens=estimate_tokens(text),
    )


def collect(paths: list[Path]) -> list[FileStats]:
    items: list[FileStats] = []
    for path in paths:
        st = stats_for(path)
        if st:
            items.append(st)
    return sorted(items, key=lambda s: s.est_tokens, reverse=True)


def discover_prompt_files() -> list[Path]:
    prompts_dir = ROOT / "prompts"
    if not prompts_dir.is_dir():
        return []
    return sorted(
        p
        for p in prompts_dir.rglob("*.md")
        if p.name != "_template.md" and not any(part.startswith("_") for part in p.relative_to(prompts_dir).parts)
    )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Estimate token counts for context files")
    parser.add_argument(
        "--check",
        action="store_true",
        help=f"Fail if AGENTS.md exceeds {WARN_LINES} lines or ~{WARN_TOKENS} tokens",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        metavar="N",
        help="Also show the N largest prompt files by estimated tokens",
    )
    args = parser.parse_args(argv)

    watched = collect(list(WATCHED_FILES))
    if not watched:
        print("No watched context files found.", file=sys.stderr)
        return 1

    print("Context file token estimates (chars / 4 heuristic):\n")
    for st in watched:
        flags: list[str] = []
        if st.path.name == "AGENTS.md":
            if st.lines > WARN_LINES:
                flags.append(f"lines>{WARN_LINES}")
            if st.est_tokens > WARN_TOKENS:
                flags.append(f"tokens~>{WARN_TOKENS}")
        flag = f"  WARNING: {', '.join(flags)}" if flags else ""
        print(f"  {st.rel}: ~{st.est_tokens:,} tokens, {st.lines} lines, {st.chars:,} chars{flag}")

    if args.top > 0:
        prompt_stats = collect(discover_prompt_files())
        print(f"\nLargest prompt files (top {args.top}):\n")
        for st in prompt_stats[: args.top]:
            print(f"  {st.rel}: ~{st.est_tokens:,} tokens, {st.lines} lines")

    if args.check:
        agents = stats_for(ROOT / "AGENTS.md")
        if agents and (agents.lines > WARN_LINES or agents.est_tokens > WARN_TOKENS):
            print(
                f"\nAGENTS.md is too large ({agents.lines} lines, ~{agents.est_tokens} tokens). "
                f"Keep under {WARN_LINES} lines; move details to docs/agents/.",
                file=sys.stderr,
            )
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
