"""Unit tests for tool/check_docs.py — the documentation anti-drift guard."""

from __future__ import annotations

from pathlib import Path

import pytest

from tool.check_docs import (
    EXIT_USAGE,
    DocIssue,
    GuardReport,
    SymbolDrift,
    _render,
    analyze_symbols,
    build_symbol_index,
    code_use_case_keys,
    coverage_issues,
    doc_use_case_keys,
    extract_doc_symbols,
    load_allowlist,
    main,
    run_checks,
    suggest_similar,
    validate_mermaid_blocks,
)


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _mermaid(body: str) -> str:
    return f"```mermaid\n{body}\n```\n"


_MERMAID_VALID = _mermaid(
    "sequenceDiagram\n"
    "    participant User\n"
    "    participant CLI\n"
    "    User->>CLI: hello\n"
    "    CLI-->>User: ok\n"
)

_MERMAID_BAD = _mermaid("bogusDiagram\n    A-->B\n")

_MERMAID_FLOWCHART = _mermaid("flowchart TD\n    A-->B\n")

_MERMAID_NO_PARTICIPANT = _mermaid("sequenceDiagram\n    Note over User: no participants\n")

_MERMAID_EQ = _mermaid("sequenceDiagram\n    participant User\n    ===\n    User->>CLI: hello\n")


def _make_code_index(tmp_path: Path) -> Path:
    """Create a minimal src tree with a few real symbols."""
    src = tmp_path / "src" / "hexawyn"
    _write(src / "contracts" / "k8s_port.py", "class K8sPort:\n    pass\n")
    _write(src / "adapters" / "vanilla_adapter.py", "class VanillaAdapter:\n    pass\n")
    _write(
        src / "application" / "ports" / "driving" / "list_namespaces" / "command.py",
        "class Command:\n    pass\n",
    )
    _write(
        src / "application" / "ports" / "driving" / "list_pods" / "command.py",
        "class Command:\n    pass\n",
    )
    return tmp_path


@pytest.fixture
def clean_tree(tmp_path: Path) -> Path:
    _make_code_index(tmp_path)
    docs = tmp_path / "docs" / "use-cases"
    _write(docs / "08-list-namespaces.md", "References K8sPort and VanillaAdapter.\n")
    _write(docs / "09-list-pods.md", "References K8sPort only.\n")
    return tmp_path


@pytest.fixture
def allowlist_path(tmp_path: Path) -> Path:
    return _write(
        tmp_path / "docs_allowlist.txt",
        "# symbols legitimately external to the codebase\n"
        "HTTPError  # stdlib\n"
        "NodePort\n"
        "\n",
    )


class TestBuildSymbolIndex:
    def test_collects_classes_functions_and_modules(self, tmp_path: Path) -> None:
        _write(
            tmp_path / "src" / "hexawyn" / "a.py",
            "class Foo:\n    pass\n\nasync def bar() -> None:\n    pass\n",
        )
        _write(
            tmp_path / "src" / "hexawyn" / "b" / "__pycache__" / "junk.py",
            "class Junk:\n    pass\n",
        )
        index = build_symbol_index(tmp_path / "src" / "hexawyn")
        assert {"Foo", "bar", "a"} <= index
        assert "Junk" not in index

    def test_ignores_missing_root(self, tmp_path: Path) -> None:
        assert build_symbol_index(tmp_path / "nope") == set()

    def test_skips_syntax_error_files(self, tmp_path: Path) -> None:
        _write(tmp_path / "src" / "hexawyn" / "broken.py", "def nope(:\n    x = None\n")
        _write(tmp_path / "src" / "hexawyn" / "ok.py", "class Fine:\n    pass\n")
        index = build_symbol_index(tmp_path / "src" / "hexawyn")
        assert "Fine" in index
        assert "NotAClass" not in index


class TestExtractDocSymbols:
    def test_keeps_compound_code_symbols(self) -> None:
        text = "Flow: K8sPort -> VanillaAdapter, plus LogPort and ListNamespacesUseCase."
        assert extract_doc_symbols(text) == {
            "K8sPort",
            "VanillaAdapter",
            "LogPort",
            "ListNamespacesUseCase",
        }

    def test_excludes_bare_layer_nouns_and_plain_words(self) -> None:
        text = "The Adapter and the Service talk to the Port through the Node. User vs Test."
        assert extract_doc_symbols(text) == set()


class TestLoadAllowlist:
    def test_skips_comments_and_blanks(self, allowlist_path: Path) -> None:
        assert load_allowlist(allowlist_path) == {"HTTPError", "NodePort"}

    def test_missing_file_returns_empty(self, tmp_path: Path) -> None:
        assert load_allowlist(tmp_path / "nope.txt") == set()


class TestSlugMapping:
    def test_driving_slugs_from_code(self, clean_tree: Path) -> None:
        assert code_use_case_keys(clean_tree) == {"list_namespaces", "list_pods"}

    def test_no_driving_dir_returns_empty(self, tmp_path: Path) -> None:
        assert code_use_case_keys(tmp_path) == set()

    def test_no_docs_dir_returns_empty(self, clean_tree: Path) -> None:
        assert doc_use_case_keys(clean_tree / "noop") == set()

    def test_doc_slugs_are_snake_normalized(self, clean_tree: Path) -> None:
        assert doc_use_case_keys(clean_tree) == {"list_namespaces", "list_pods"}

    def test_coverage_reports_orphan_docs(self, clean_tree: Path) -> None:
        _write(clean_tree / "docs" / "use-cases" / "99-ghost.md", "orphan\n")
        issues = coverage_issues(clean_tree)
        assert any("ghost" in issue.message for issue in issues)

    def test_coverage_reports_missing_docs(self, clean_tree: Path) -> None:
        (clean_tree / "docs" / "use-cases" / "09-list-pods.md").unlink()
        issues = coverage_issues(clean_tree)
        assert any("list_pods" in issue.message for issue in issues)


class TestMermaidValidation:
    def test_valid_sequence_diagram(self) -> None:
        assert validate_mermaid_blocks("x\n\n" + _MERMAID_VALID) == []

    def test_unknown_directive_flagged(self) -> None:
        issues = validate_mermaid_blocks("x\n\n" + _MERMAID_BAD)
        assert any("directive" in i for i in issues)

    def test_flowchart_is_recognized(self) -> None:
        assert validate_mermaid_blocks("x\n\n" + _MERMAID_FLOWCHART) == []

    def test_no_participants(self) -> None:
        issues = validate_mermaid_blocks("x\n\n" + _MERMAID_NO_PARTICIPANT)
        assert any("participants" in i for i in issues)

    def test_illegal_line(self) -> None:
        issues = validate_mermaid_blocks("x\n\n" + _MERMAID_EQ)
        assert any("===" in i for i in issues)


class TestSuggestSimilar:
    def test_suggests_matching_symbols(self) -> None:
        index = {"LogsPort", "PodLogsPort", "K8sPort"}
        assert "LogsPort" in suggest_similar("LogPort", index)

    def test_returns_empty_for_unknown(self) -> None:
        assert suggest_similar("GhostPort", {"K8sPort"}) == []

    def test_returns_empty_when_root_is_a_bare_noun(self) -> None:
        assert suggest_similar("Port", {"K8sPort"}) == []


class TestAnalyzeSymbols:
    def test_flags_only_true_drifts(self, clean_tree: Path, allowlist_path: Path) -> None:
        _write(
            clean_tree / "docs" / "use-cases" / "08-list-namespaces.md",
            "References K8sPort, VanillaAdapter, HTTPError, GhostPort.\n",
        )
        index = build_symbol_index(clean_tree / "src" / "hexawyn")
        vocab = {s.lower() for s in index}
        drifts = analyze_symbols(
            list((clean_tree / "docs").rglob("*.md")), index, load_allowlist(allowlist_path), vocab
        )
        assert {d.symbol for d in drifts} == {"GhostPort"}

    def test_suggestion_is_present(self, clean_tree: Path) -> None:
        _write(clean_tree / "docs" / "use-cases" / "08-list-namespaces.md", "References LogPort.\n")
        index = build_symbol_index(clean_tree / "src" / "hexawyn")
        vocab = {s.lower() for s in index}
        drifts = analyze_symbols(list((clean_tree / "docs").rglob("*.md")), index, set(), vocab)
        assert any(d.symbol == "LogPort" and d.suggestion for d in drifts)

    def test_layer_vocabulary_is_allowed(self, clean_tree: Path) -> None:
        _write(
            clean_tree
            / "src"
            / "hexawyn"
            / "application"
            / "ports"
            / "driving"
            / "list_pods"
            / "command.py",
            "class Command:\n    pass\n",
        )
        _write(
            clean_tree / "docs" / "use-cases" / "09-list-pods.md",
            "References ListPodsService and K8sPort.\n",
        )
        index = build_symbol_index(clean_tree / "src" / "hexawyn")
        vocab = {s.lower().replace("_", "") for s in index} | {"listpods"}
        drifts = analyze_symbols(list((clean_tree / "docs").rglob("*.md")), index, set(), vocab)
        assert "ListPodsService" not in {d.symbol for d in drifts}


class TestRunChecks:
    def test_clean_tree_has_no_errors(self, clean_tree: Path, allowlist_path: Path) -> None:
        report = run_checks(clean_tree, allowlist_path, "all")
        assert report.drifts == []
        assert report.mermaid_issues == []
        assert report.coverage == []
        assert not report.has_errors()

    def test_missing_doc_is_a_hard_error(self, clean_tree: Path) -> None:
        (clean_tree / "docs" / "use-cases" / "09-list-pods.md").unlink()
        report = run_checks(clean_tree, Path("missing.txt"), "all")
        assert any("list_pods" in issue.message for issue in report.coverage)
        assert report.has_errors()

    def test_flags_drift_and_bad_mermaid(self, clean_tree: Path) -> None:
        _write(
            clean_tree / "docs" / "use-cases" / "08-list-namespaces.md",
            "References GhostPort.\n\n" + _MERMAID_BAD,
        )
        report = run_checks(clean_tree, Path("missing.txt"), "all")
        assert any(d.symbol == "GhostPort" for d in report.drifts)
        assert report.mermaid_issues
        assert report.has_errors()


class TestMain:
    def test_clean_tree_exits_zero(self, clean_tree: Path, allowlist_path: Path) -> None:
        rv = main(["--root", str(clean_tree), "--allowlist", str(allowlist_path), "--quiet"])
        assert rv == 0

    def test_drift_exits_one(self, clean_tree: Path) -> None:
        _write(
            clean_tree / "docs" / "use-cases" / "08-list-namespaces.md", "References GhostPort.\n"
        )
        rv = main(["--root", str(clean_tree), "--allowlist", str(Path("missing.txt")), "--quiet"])
        assert rv == 1

    def test_missing_docs_root_exits_two(self, clean_tree: Path) -> None:
        with pytest.raises(SystemExit) as exc:
            main(["--root", str(clean_tree / "noop")])
        assert exc.value.code == EXIT_USAGE


class TestRender:
    def test_bundles_and_truncates(self) -> None:
        report = GuardReport()
        report.drifts = [SymbolDrift("../d.md", f"S{i}Port", "-") for i in range(60)]
        report.mermaid_issues = [DocIssue("../m.md", "bad mermaid") for _ in range(40)]
        report.coverage = [DocIssue("../c.md", "use case missing doc") for _ in range(40)]
        report.warnings = [DocIssue("../w.md", "soft warning") for _ in range(5)]
        rendered = _render(report)
        assert "symbol drift (60)" in rendered
        assert "invalid mermaid (40)" in rendered
        assert "doc coverage (40)" in rendered
        assert "warnings (5)" in rendered
        assert "... 10 more" in rendered
        assert "  soft warning" in rendered


class TestMainJsonAndOutput:
    def test_json_output(
        self, clean_tree: Path, allowlist_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        rv = main(["--root", str(clean_tree), "--allowlist", str(allowlist_path), "--json"])
        assert rv == 0
        payload = capsys.readouterr().out
        assert '"drifts"' in payload
        assert '"errors_count"' in payload

    def test_prints_findings_when_not_quiet(
        self, clean_tree: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        _write(
            clean_tree / "docs" / "use-cases" / "08-list-namespaces.md", "References GhostPort.\n"
        )
        rv = main(["--root", str(clean_tree), "--allowlist", str(Path("missing.txt"))])
        assert rv == 1
        assert "symbol drift" in capsys.readouterr().out

    def test_clean_nonquiet_outputs_nothing(
        self, clean_tree: Path, allowlist_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        rv = main(["--root", str(clean_tree), "--allowlist", str(allowlist_path)])
        assert rv == 0
        assert capsys.readouterr().out == ""

    def test_report_object(self) -> None:
        report = GuardReport()
        assert report.has_errors() is False
