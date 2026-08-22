"""Unit tests for scripts/sync_intent_examples.py."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from scripts.sync_intent_examples import (
    _EXTRA_USE_CASES,
    _HEXAWYN_ONLY_DESCRIPTIONS,
    sync,
)


@pytest.fixture
def control_plane_file(tmp_path: Path) -> Path:
    path = tmp_path / "intent_examples.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "shared_use_case": {
                    "tool": "shared_use_case",
                    "description": "Description from control-plane",
                    "questions": ["q1", "q2", "q3", "q4", "q5"],
                },
                "another": {
                    "tool": "another",
                    "description": "Control-plane description",
                    "questions": ["q1", "q2", "q3", "q4", "q5"],
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return path


@pytest.fixture
def local_file(tmp_path: Path) -> Path:
    path = tmp_path / "local_intents.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "shared_use_case": {
                    "tool": "shared_use_case",
                    "questions": ["q1", "q2", "q3", "q4", "q5"],
                },
                "another": {
                    "tool": "another",
                    "description": "stale local description",
                    "questions": ["q1", "q2", "q3", "q4", "q5"],
                },
                "container_image_vulnerability_scanning": {
                    "tool": "container_image_vulnerability_scanning",
                    "questions": ["q1", "q2", "q3", "q4", "q5"],
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return path


@pytest.fixture
def control_plane_with_extra(control_plane_file: Path) -> Path:
    path = control_plane_file
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["snapshots_list"] = {
        "tool": "snapshots_list",
        "description": "List all VolumeSnapshots",
        "questions": ["q1", "q2", "q3", "q4", "q5"],
    }
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path


@pytest.fixture
def patched_paths(control_plane_file: Path, local_file: Path, monkeypatch) -> None:
    monkeypatch.setattr("scripts.sync_intent_examples.CONTROL_PLANE_PATH", control_plane_file)
    monkeypatch.setattr("scripts.sync_intent_examples.HEXAWYN_PATH", local_file)


class TestSyncIntentExamples:
    def test_copies_control_plane_descriptions(self, patched_paths, local_file: Path) -> None:
        sync()

        data = yaml.safe_load(local_file.read_text(encoding="utf-8"))
        assert data["shared_use_case"]["description"] == "Description from control-plane"

    def test_overwrites_stale_local_description(self, patched_paths, local_file: Path) -> None:
        sync()

        data = yaml.safe_load(local_file.read_text(encoding="utf-8"))
        assert data["another"]["description"] == "Control-plane description"

    def test_hexawyn_only_use_case_gets_hand_description(
        self, patched_paths, local_file: Path
    ) -> None:
        sync()

        data = yaml.safe_load(local_file.read_text(encoding="utf-8"))
        assert (
            data["container_image_vulnerability_scanning"]["description"]
            == (_HEXAWYN_ONLY_DESCRIPTIONS["container_image_vulnerability_scanning"])
        )

    def test_preserves_questions_and_tool(self, patched_paths, local_file: Path) -> None:
        sync()

        data = yaml.safe_load(local_file.read_text(encoding="utf-8"))
        assert data["shared_use_case"]["tool"] == "shared_use_case"
        assert data["shared_use_case"]["questions"] == ["q1", "q2", "q3", "q4", "q5"]

    def test_returns_number_of_updates(self, patched_paths) -> None:
        expected_updates = 3 + len(_EXTRA_USE_CASES)
        assert sync() == expected_updates

    def test_copies_missing_use_cases_from_control_plane(
        self, control_plane_with_extra: Path, local_file: Path, monkeypatch
    ) -> None:
        monkeypatch.setattr(
            "scripts.sync_intent_examples.CONTROL_PLANE_PATH", control_plane_with_extra
        )
        monkeypatch.setattr("scripts.sync_intent_examples.HEXAWYN_PATH", local_file)

        sync()

        data = yaml.safe_load(local_file.read_text(encoding="utf-8"))
        assert "snapshots_list" in data
        assert data["snapshots_list"]["tool"] == "snapshots_list"
        assert data["snapshots_list"]["description"] == "List all VolumeSnapshots"
        expected_questions = 5
        assert len(data["snapshots_list"]["questions"]) == expected_questions

    def test_adds_extra_use_cases_for_unregistered_tools(
        self, patched_paths, local_file: Path
    ) -> None:
        sync()

        data = yaml.safe_load(local_file.read_text(encoding="utf-8"))
        min_questions = 5
        for use_case, entry in _EXTRA_USE_CASES.items():
            assert use_case in data
            assert data[use_case]["tool"] == entry["tool"]
            assert data[use_case]["description"] == entry["description"]
            assert len(data[use_case]["questions"]) >= min_questions
