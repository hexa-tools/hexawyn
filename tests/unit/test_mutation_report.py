"""Unit tests for scripts/mutation_report.py — mutmut stats aggregation into
docs/mutation/report.json and the README mutation badge."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.mutation_report import (
    _badge_url,
    _color,
    _load,
    _score,
    print_table,
    summarize,
    update_badge,
    write_report,
)


def _stats(
    killed: int = 9,
    total: int = 10,
    survived: int = 1,
    no_tests: int = 0,
    timeout: int = 0,
) -> dict[str, int]:
    return {
        "killed": killed,
        "total": total,
        "survived": survived,
        "no_tests": no_tests,
        "timeout": timeout,
    }


class TestScore:
    def test_full_kill_scores_100(self) -> None:
        assert _score(10, 10) == 100.0  # noqa: PLR2004

    def test_partial_kill_rounds_to_one_decimal(self) -> None:
        assert _score(9, 10) == 90.0  # noqa: PLR2004
        assert _score(2, 3) == 66.7  # noqa: PLR2004

    def test_zero_total_scores_zero(self) -> None:
        assert _score(0, 0) == 0.0
        assert _score(5, 0) == 0.0


class TestColor:
    @pytest.mark.parametrize(
        ("score", "expected"),
        [
            (100.0, "brightgreen"),
            (90.0, "brightgreen"),
            (80.0, "yellowgreen"),
            (70.0, "yellow"),
            (50.0, "orange"),
            (30.0, "red"),
            (0.0, "red"),
        ],
    )
    def test_color_thresholds(self, score: float, expected: str) -> None:
        assert _color(score) == expected


class TestBadgeUrl:
    def test_default_color_from_score(self) -> None:
        assert _badge_url("mutation", 100.0) == (
            "https://img.shields.io/badge/mutation-100.0%25-brightgreen.svg"
        )

    def test_low_score_red(self) -> None:
        assert _badge_url("mutation", 0.0) == (
            "https://img.shields.io/badge/mutation-0.0%25-red.svg"
        )

    def test_double_dash_label_kept_literal(self) -> None:
        assert _badge_url("mutation--python", 96.6) == (
            "https://img.shields.io/badge/mutation--python-96.6%25-brightgreen.svg"
        )


class TestLoad:
    def test_missing_file_returns_none(self, tmp_path: Path) -> None:
        assert _load(tmp_path / "absent.json") is None

    def test_loads_valid_json(self, tmp_path: Path) -> None:
        path = tmp_path / "stats.json"
        path.write_text(json.dumps({"killed": 9}), encoding="utf-8")
        assert _load(path) == {"killed": 9}

    def test_invalid_json_raises(self, tmp_path: Path) -> None:
        path = tmp_path / "bad.json"
        path.write_text("not json", encoding="utf-8")
        with pytest.raises(json.JSONDecodeError):
            _load(path)


class TestSummarize:
    def test_no_report_disables_python(self) -> None:
        summary = summarize(None)
        assert summary["python"] == {"enabled": False}
        assert summary["overall"] == {"total": 0, "killed": 0, "score": 0.0}

    def test_full_stats_are_folded(self) -> None:
        summary = summarize(_stats(killed=9, total=10, survived=1, timeout=2))
        python = summary["python"]
        assert isinstance(python, dict)
        assert python["killed"] == 9  # noqa: PLR2004
        assert python["total"] == 10  # noqa: PLR2004
        assert python["survived"] == 1
        assert python["no_tests"] == 0
        assert python["timeout"] == 2  # noqa: PLR2004
        assert python["score"] == 90.0  # noqa: PLR2004
        overall = summary["overall"]
        assert isinstance(overall, dict)
        assert overall == {"total": 10, "killed": 9, "score": 90.0}

    def test_missing_optional_keys_default_to_zero(self) -> None:
        summary = summarize({"killed": 7, "total": 7, "survived": 0})
        python = summary["python"]
        assert isinstance(python, dict)
        assert python["no_tests"] == 0
        assert python["timeout"] == 0
        assert python["score"] == 100.0  # noqa: PLR2004

    def test_zero_total_overall(self) -> None:
        summary = summarize(_stats(killed=0, total=0, survived=0))
        assert summary["overall"] == {"total": 0, "killed": 0, "score": 0.0}


class TestPrintTable:
    def test_enabled_prints_counts(self, capsys: pytest.CaptureFixture[str]) -> None:
        print_table(summarize(_stats(killed=9, total=10)))
        out = capsys.readouterr().out
        assert "python: 9/10 killed" in out
        assert "overall: 9/10" in out

    def test_disabled_prints_hint(self, capsys: pytest.CaptureFixture[str]) -> None:
        print_table(summarize(None))
        assert "no report found" in capsys.readouterr().out


class TestWriteReport:
    def test_writes_sorted_json_with_parents(self, tmp_path: Path) -> None:
        target = tmp_path / "nested" / "report.json"
        summary = summarize(_stats(killed=9, total=10))
        write_report(summary, target)
        written = json.loads(target.read_text(encoding="utf-8"))
        assert written == summary
        assert target.read_text(encoding="utf-8").endswith("\n")


class TestUpdateBadge:
    def _badge_readme(self, python: str = "0.0%25-red") -> str:
        return (
            "[![Mutation Python](https://img.shields.io/badge/mutation--python-"
            f"{python}.svg)](docs/mutation/PROGRES.md)\n"
        )

    def test_updates_python_badge_score(self, tmp_path: Path) -> None:
        readme = tmp_path / "README.md"
        readme.write_text(self._badge_readme(), encoding="utf-8")
        summary = summarize(_stats(killed=966, total=1000))
        assert update_badge(summary, readme) is True
        content = readme.read_text(encoding="utf-8")
        assert "mutation--python-96.6%25-brightgreen" in content

    def test_ignores_unrelated_badges(self, tmp_path: Path) -> None:
        readme = tmp_path / "README.md"
        readme.write_text(
            "[![Tests](https://img.shields.io/badge/tests-1_passed-brightgreen.svg)]()\n"
            + self._badge_readme(),
            encoding="utf-8",
        )
        summary = summarize(_stats(killed=966, total=1000))
        update_badge(summary, readme)
        content = readme.read_text(encoding="utf-8")
        assert "tests-1_passed-brightgreen.svg" in content

    def test_disabled_python_badge_resets_to_zero(self, tmp_path: Path) -> None:
        readme = tmp_path / "README.md"
        readme.write_text(self._badge_readme(), encoding="utf-8")
        update_badge(summarize(None), readme)
        content = readme.read_text(encoding="utf-8")
        assert "mutation--python-0.0%25-red" in content

    def test_unchanged_readme_returns_false(self, tmp_path: Path) -> None:
        readme = tmp_path / "README.md"
        readme.write_text(self._badge_readme(), encoding="utf-8")
        summary = summarize(_stats(killed=966, total=1000))
        assert update_badge(summary, readme) is True
        assert update_badge(summary, readme) is False

    def test_no_badge_line_returns_false(self, tmp_path: Path) -> None:
        readme = tmp_path / "README.md"
        readme.write_text("# plain readme\n", encoding="utf-8")
        assert update_badge(summarize(_stats()), readme) is False
