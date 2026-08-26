#!/usr/bin/env python3
"""Anti-drift guard for hexawyn documentation.

Checks that ``docs/`` does not drift from ``src/hexawyn/``:

- symbols: every code-like identifier referenced in a doc must exist in
  ``src/hexawyn`` or ``tests/``, or be blessed in the allowlist manifest.
- mermaid: every ```mermaid sequenceDiagram block must be structurally valid.
- coverage: every driving use-case must have a doc and every doc must map to a
  real use case. A use case without a doc (or an orphan doc) fails the guard.

Usage:
    python tool/check_docs.py [--check {all,symbols,mermaid,coverage} | --all]
                              [--root DIR] [--allowlist FILE]
                              [--fail-warnings] [--quiet] [--json]

Exit codes:
    0  clean (warnings allowed unless --fail-warnings)
    1  errors found (drift / invalid mermaid / use case without doc)
    2  usage error
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, TypeVar

T = TypeVar("T")

CODE_SUFFIXES: tuple[str, ...] = (
    "UseCase",
    "Port",
    "Adapter",
    "Service",
    "Repository",
    "Node",
    "Error",
    "Manager",
    "Client",
    "Registry",
    "Engine",
    "Factory",
    "Toolset",
    "Ranker",
    "Store",
    "Loader",
    "Builder",
)
BARE_NOUNS: frozenset[str] = frozenset(CODE_SUFFIXES)

LAYER_SUFFIX_RE: str = (
    "(UseCase|Port|Adapter|Service|Repository|Node|Error|Manager|Client|Registry|Engine|Factory|Toolset|Ranker|Store|Loader|Builder)"
    "$"
)

MIN_PARTICIPANTS: int = 2
DRIFT_LIMIT: int = 50
ISSUE_LIMIT: int = 30

_DIRECTIVES: tuple[str, ...] = (
    "sequenceDiagram",
    "flowchart",
    "graph",
    "classDiagram",
    "stateDiagram",
    "erDiagram",
    "journey",
    "gantt",
    "pie",
    "mindmap",
    "C4Context",
    "quadrantChart",
    "timeline",
)

EXIT_OK: int = 0
EXIT_FAIL: int = 1
EXIT_USAGE: int = 2

CheckName = Literal["all", "symbols", "mermaid", "coverage"]


@dataclass(frozen=True)
class SymbolDrift:
    """A doc references a symbol that exists neither in code nor in the manifest."""

    file: str
    symbol: str
    suggestion: str


@dataclass(frozen=True)
class DocIssue:
    """A structural problem in a doc (mermaid) or a coverage gap."""

    file: str
    message: str


@dataclass
class GuardReport:
    """Aggregated findings across every check."""

    drifts: list[SymbolDrift] = field(default_factory=list)
    mermaid_issues: list[DocIssue] = field(default_factory=list)
    coverage: list[DocIssue] = field(default_factory=list)
    warnings: list[DocIssue] = field(default_factory=list)

    def errors(self) -> list[SymbolDrift | DocIssue]:
        """Hard failures: symbol drift, invalid mermaid and doc coverage gaps."""
        return [*self.drifts, *self.mermaid_issues, *self.coverage]

    def has_errors(self) -> bool:
        return bool(self.errors())


def iter_py_files(root: Path) -> list[Path]:
    """Every Python file under a root, skipping bytecode caches."""
    if not root.is_dir():
        return []
    return [p for p in sorted(root.rglob("*.py")) if "__pycache__" not in p.parts]


def build_symbol_index(*roots: Path) -> set[str]:
    """Set of code symbols: module stems, class, function and async names."""
    index: set[str] = set()
    for root in roots:
        for path in iter_py_files(root):
            index.add(path.stem)
            try:
                tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef):
                    index.add(node.name)
    return index


def extract_doc_symbols(text: str) -> set[str]:
    """Compound PascalCase identifiers that look like code symbols.

    Bare layer nouns (``Adapter``, ``Service``, ``Port``...) and ordinary
    capitalised words are ignored, because they are prose, not code.
    """
    found: set[str] = set()
    for match in re.finditer(r"\b([A-Z][A-Za-z0-9_]+)\b", text):
        token = match.group(1)
        if token in BARE_NOUNS:
            continue
        if token.endswith(CODE_SUFFIXES):
            found.add(token)
    return found


def to_snake(prefix: str) -> str:
    """CamelCase identifier to a snake_case key."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", prefix).lower()


def is_layer_vocabulary(symbol: str, vocab: set[str]) -> bool:
    """A ``XxxPort``/``XxxService`` is acceptable as layer vocabulary when its
    base name (``Xxx``) maps to a real use case, tool or code symbol."""
    if not symbol.endswith(CODE_SUFFIXES):
        return False
    base = re.sub(LAYER_SUFFIX_RE, "", symbol)
    key = to_snake(base).replace("_", "")
    if not key:
        return False
    return key in vocab or key.rstrip("s") in vocab


def suggest_similar(token: str, index: set[str], limit: int = 3) -> list[str]:
    """Best-match suggestions for an unknown symbol, based on its root."""
    root = re.sub(LAYER_SUFFIX_RE, "", token).lower()
    if not root:
        return []
    return sorted((s for s in index if root in s.lower()), key=len)[:limit]


def load_allowlist(path: Path) -> set[str]:
    """Manifest of symbols legitimately referenced but not defined in code."""
    if not path.is_file():
        return set()
    allowed: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        allowed.add(line.split()[0])
    return allowed


def normalize_slug(slug: str) -> str:
    """Kebab-case doc slugs and snake-case code slugs share one key."""
    return slug.replace("-", "_")


def code_use_case_keys(root: Path) -> set[str]:
    """Snake-case keys of every driving use case folder."""
    base = root / "src" / "hexawyn" / "application" / "ports" / "driving"
    if not base.is_dir():
        return set()
    return {
        entry.name for entry in base.iterdir() if entry.is_dir() and not entry.name.startswith("__")
    }


def doc_use_case_keys(root: Path) -> set[str]:
    """Normalised keys of every use-case doc filename."""
    base = root / "docs" / "use-cases"
    if not base.is_dir():
        return set()
    keys: set[str] = set()
    for path in base.glob("*.md"):
        stem = path.stem
        slug = stem.split("-", 1)[1] if "-" in stem else stem
        keys.add(normalize_slug(slug))
    return keys


def coverage_issues(root: Path) -> list[DocIssue]:
    """Coverage gaps between driving use cases and use-case docs."""
    code = code_use_case_keys(root)
    docs = doc_use_case_keys(root)
    issues: list[DocIssue] = []
    for key in sorted(code - docs):
        issues.append(
            DocIssue(file="(code)", message=f"use case '{key}' has no doc in docs/use-cases/")
        )
    for key in sorted(docs - code):
        issues.append(
            DocIssue(file="(doc)", message=f"orphan doc for non-existent use case '{key}'")
        )
    return issues


def validate_mermaid_blocks(text: str) -> list[str]:
    """Structural checks on every mermaid block embedded in a use-case doc.

    ``sequenceDiagram`` blocks must declare participants and avoid the ``===``
    separator; any other recognised diagram type passes through untouched.
    """
    issues: list[str] = []
    for match in re.finditer(r"```mermaid\s*\n(.*?)```", text, re.DOTALL):
        lines = [ln.strip() for ln in match.group(1).splitlines() if ln.strip()]
        directive = _mermaid_directive(lines)
        if directive is None:
            issues.append("mermaid block: missing a recognised mermaid directive")
            continue
        if directive != "sequenceDiagram":
            continue
        participants = [ln for ln in lines if ln.startswith("participant ")]
        arrows = [ln for ln in lines if re.search(r"-{2,}>>", ln)]
        if not participants:
            issues.append("mermaid block: no participants")
        elif len(participants) < MIN_PARTICIPANTS and not arrows:
            issues.append("mermaid block: fewer than 2 participants and no arrows")
        for ln in lines:
            if ln == "===":
                issues.append("mermaid block: illegal '===' line")
    return issues


def _mermaid_directive(lines: list[str]) -> str | None:
    """First recognised mermaid diagram directive in a block, or ``None``."""
    for ln in lines:
        for directive in _DIRECTIVES:
            if ln == directive or ln.startswith(directive + " "):
                return directive
    return None


def analyze_symbols(
    docs: list[Path], index: set[str], allowlist: set[str], vocab: set[str]
) -> list[SymbolDrift]:
    """Flag doc-referenced symbols that exist neither in code nor in the manifest."""
    drifts: list[SymbolDrift] = []
    for path in docs:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for symbol in sorted(extract_doc_symbols(text)):
            if symbol in index or symbol in allowlist:
                continue
            if is_layer_vocabulary(symbol, vocab):
                continue
            suggestion = ", ".join(suggest_similar(symbol, index)) or "-"
            drifts.append(SymbolDrift(file=str(path), symbol=symbol, suggestion=suggestion))
    return drifts


def run_checks(root: Path, allowlist_path: Path, check: CheckName) -> GuardReport:
    """Run the selected checks and return a GuardReport."""
    report = GuardReport()
    docs = list((root / "docs").rglob("*.md")) if (root / "docs").is_dir() else []
    uc_docs = (
        list((root / "docs" / "use-cases").glob("*.md"))
        if (root / "docs" / "use-cases").is_dir()
        else []
    )

    if check in ("symbols", "all"):
        index = build_symbol_index(root / "src" / "hexawyn", root / "tests")
        vocab = {symbol.lower().replace("_", "") for symbol in index}
        vocab |= {slug.lower().replace("_", "") for slug in code_use_case_keys(root)}
        tools_dir = root / "src" / "hexawyn" / "mcp" / "tools"
        if tools_dir.is_dir():
            vocab |= {path.stem.lower().replace("_", "") for path in tools_dir.glob("*.py")}
        report.drifts = analyze_symbols(docs, index, load_allowlist(allowlist_path), vocab)

    if check in ("mermaid", "all"):
        for path in uc_docs:
            for message in validate_mermaid_blocks(
                path.read_text(encoding="utf-8", errors="ignore")
            ):
                report.mermaid_issues.append(DocIssue(file=str(path), message=message))

    if check in ("coverage", "all"):
        report.coverage = coverage_issues(root)

    return report


def _section(title: str, items: list[T], limit: int, fmt: Callable[[T], str]) -> list[str]:
    """Render one findings section, truncating beyond ``limit``."""
    if not items:
        return []
    lines = [f"{title} ({len(items)}):"]
    for item in items[:limit]:
        lines.append(fmt(item))
    if len(items) > limit:
        lines.append(f"  ... {len(items) - limit} more")
    return lines


def _render_drift(item: SymbolDrift) -> str:
    return f"  {item.symbol}  ← {item.file}  (suggest: {item.suggestion})"


def _render_issue_with_file(item: DocIssue) -> str:
    return f"  {item.message}  ← {item.file}"


def _render_issue(item: DocIssue) -> str:
    return f"  {item.message}"


def _render(report: GuardReport) -> str:
    """Human-readable summary of the findings."""
    lines: list[str] = []
    lines += _section("symbol drift", report.drifts, DRIFT_LIMIT, _render_drift)
    lines += _section(
        "invalid mermaid", report.mermaid_issues, ISSUE_LIMIT, _render_issue_with_file
    )
    lines += _section("doc coverage", report.coverage, ISSUE_LIMIT, _render_issue)
    lines += _section("warnings", report.warnings, ISSUE_LIMIT, _render_issue)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Anti-drift guard for hexawyn docs.")
    parser.add_argument("--check", choices=["all", "symbols", "mermaid", "coverage"], default="all")
    parser.add_argument("--all", action="store_true", help="shorthand for --check all")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    parser.add_argument(
        "--allowlist", type=Path, default=Path(__file__).parent / "docs_allowlist.txt"
    )
    parser.add_argument("--fail-warnings", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if args.all:
        args.check = "all"

    if not (args.root / "docs").is_dir():
        parser.error("no docs/ directory under --root")

    report = run_checks(args.root, args.allowlist, args.check)
    has_errors = report.has_errors() or (bool(report.warnings) and args.fail_warnings)

    if args.json:
        payload = {
            "drifts": [
                {"file": d.file, "symbol": d.symbol, "suggestion": d.suggestion}
                for d in report.drifts
            ],
            "mermaid_issues": [
                {"file": i.file, "message": i.message} for i in report.mermaid_issues
            ],
            "coverage": [{"file": i.file, "message": i.message} for i in report.coverage],
            "warnings": [{"file": i.file, "message": i.message} for i in report.warnings],
            "errors_count": len(report.errors())
            + (len(report.warnings) if args.fail_warnings else 0),
            "warnings_count": len(report.warnings),
        }
        print(json.dumps(payload, indent=2))
    elif not args.quiet:
        rendered = _render(report)
        if rendered:
            print(rendered)

    return EXIT_FAIL if has_errors else EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
