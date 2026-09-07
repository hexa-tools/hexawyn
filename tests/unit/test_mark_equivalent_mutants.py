"""Unit tests for tool/mark_equivalent_mutants.py — cache marking of
structurally-equivalent mutants as skipped (exit code 34)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tool.mark_equivalent_mutants import mark_mutants, module_to_meta_path

_SAMPLE_KEY = (
    "hexawyn.domain.services.cost_forecast.cost_forecast_engine" ".x__compute_trend__mutmut_1"
)
_SKIPPED_EXIT_CODE = 34


def _write_meta(root: Path, module_key: str, exit_codes: dict[str, int]) -> Path:
    meta = module_to_meta_path(root, module_key)
    meta.parent.mkdir(parents=True, exist_ok=True)
    meta.write_text(
        json.dumps(
            {
                "exit_code_by_key": exit_codes,
                "hash_by_function_name": {},
                "type_check_error_by_key": {},
                "durations_by_key": {},
                "estimated_durations_by_key": {},
            }
        ),
        encoding="utf-8",
    )
    return meta


class TestModuleToMetaPath:
    def test_builds_meta_path_from_mutant_key(self, tmp_path: Path) -> None:
        path = module_to_meta_path(tmp_path, _SAMPLE_KEY)
        assert (
            path == tmp_path / "hexawyn/domain/services/cost_forecast/cost_forecast_engine.py.meta"
        )


class TestMarkMutants:
    def test_marks_existing_mutant_as_skipped(self, tmp_path: Path) -> None:
        _write_meta(tmp_path, _SAMPLE_KEY, {_SAMPLE_KEY: 0})
        count, errors = mark_mutants(tmp_path, [_SAMPLE_KEY])
        data = json.loads(
            (
                tmp_path / "hexawyn/domain/services/cost_forecast/cost_forecast_engine.py.meta"
            ).read_text()
        )
        assert count == 1
        assert errors == []
        assert data["exit_code_by_key"][_SAMPLE_KEY] == _SKIPPED_EXIT_CODE

    def test_preserves_other_mutant_statuses(self, tmp_path: Path) -> None:
        other = _SAMPLE_KEY.replace("x__compute_trend__mutmut_1", "x__compute_trend__mutmut_2")
        _write_meta(tmp_path, _SAMPLE_KEY, {_SAMPLE_KEY: 0, other: 1})
        mark_mutants(tmp_path, [_SAMPLE_KEY])
        data = json.loads(
            (
                tmp_path / "hexawyn/domain/services/cost_forecast/cost_forecast_engine.py.meta"
            ).read_text()
        )
        assert data["exit_code_by_key"][other] == 1

    def test_missing_meta_reports_error(self, tmp_path: Path) -> None:
        count, errors = mark_mutants(tmp_path, [_SAMPLE_KEY])
        assert count == 0
        assert len(errors) == 1
        assert "missing meta" in errors[0]

    def test_unknown_key_reports_error(self, tmp_path: Path) -> None:
        _write_meta(tmp_path, _SAMPLE_KEY, {})
        unknown = _SAMPLE_KEY.replace("mutmut_1", "mutmut_999")
        count, errors = mark_mutants(tmp_path, [unknown])
        assert count == 0
        assert len(errors) == 1
        assert "key not in cache" in errors[0]

    def test_empty_list_marks_nothing(self, tmp_path: Path) -> None:
        count, errors = mark_mutants(tmp_path, [])
        assert count == 0
        assert errors == []

    def test_multiple_keys_marked(self, tmp_path: Path) -> None:
        second = _SAMPLE_KEY.replace("cost_forecast_engine", "budget_intelligence_service")
        _write_meta(tmp_path, _SAMPLE_KEY, {_SAMPLE_KEY: 0})
        _write_meta(tmp_path, second, {second: 0})
        count, errors = mark_mutants(tmp_path, [_SAMPLE_KEY, second])
        assert count == 2  # noqa: PLR2004
        assert errors == []


class TestMain:
    def test_main_returns_zero_and_marks(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        _write_meta(tmp_path, _SAMPLE_KEY, {_SAMPLE_KEY: 0})
        list_file = tmp_path / "equivalents.txt"
        list_file.write_text(_SAMPLE_KEY + "\n", encoding="utf-8")
        monkeypatch.setattr("tool.mark_equivalent_mutants._MUTANTS_ROOT", tmp_path)
        from tool.mark_equivalent_mutants import main as main_fn

        monkeypatch.setattr("sys.argv", ["mark", "--list", str(list_file)])
        assert main_fn() == 0
