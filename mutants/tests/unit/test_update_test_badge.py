"""Unit tests for scripts/update_test_badge.py."""

from __future__ import annotations

from pathlib import Path

from scripts import update_test_badge as mod


class TestBadgePattern:
    def test_matches_url_encoded_plus_form(self) -> None:
        url = "https://img.shields.io/badge/tests-8500%2B_passed-brightgreen.svg"
        assert mod.BADGE_PATTERN.search(url) is not None

    def test_matches_plain_digits_form(self) -> None:
        url = "https://img.shields.io/badge/tests-8372_passed-brightgreen.svg"
        assert mod.BADGE_PATTERN.search(url) is not None


class TestRenderBadgeUrl:
    def test_renders_exact_count(self) -> None:
        assert mod.render_badge_url(8372) == (
            "https://img.shields.io/badge/tests-8372_passed-brightgreen.svg"
        )


class TestUpdateBadge:
    def test_replaces_hardcoded_plus_form(self, tmp_path: Path, monkeypatch) -> None:
        readme = tmp_path / "README.md"
        readme.write_text(
            "[![Tests](https://img.shields.io/badge/tests-8500%2B_passed-brightgreen.svg)]()\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(mod, "README", readme)

        changed = mod.update_badge(8372)

        assert changed is True
        assert "tests-8372_passed" in readme.read_text(encoding="utf-8")
        assert "%2B" not in readme.read_text(encoding="utf-8")

    def test_returns_false_when_already_up_to_date(self, tmp_path: Path, monkeypatch) -> None:
        readme = tmp_path / "README.md"
        readme.write_text(
            "[![Tests](https://img.shields.io/badge/tests-8372_passed-brightgreen.svg)]()\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(mod, "README", readme)

        assert mod.update_badge(8372) is False
