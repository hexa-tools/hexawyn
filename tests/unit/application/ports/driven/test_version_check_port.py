"""Unit tests for application/ports/driven/version_check_port.py."""

from __future__ import annotations

from hexawyn.application.ports.driven.version_check_port import VersionCheckPort


class _FakePort(VersionCheckPort):
    def fetch_latest_version(self) -> str:
        return "0.1.0b4"


class TestVersionCheckPort:
    def test_returns_latest_version_string(self) -> None:
        assert _FakePort().fetch_latest_version() == "0.1.0b4"

    def test_returns_empty_string_when_unavailable(self) -> None:
        class _Unavailable(VersionCheckPort):
            def fetch_latest_version(self) -> str:
                return ""

        assert _Unavailable().fetch_latest_version() == ""

    def test_abstract_cannot_instantiate(self) -> None:
        import pytest

        with pytest.raises(TypeError):
            VersionCheckPort()  # type: ignore[abstract]
