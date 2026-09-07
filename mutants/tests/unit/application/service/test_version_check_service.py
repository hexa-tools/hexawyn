"""Unit tests for version_check_service — update detection for the hexa CLI."""

from __future__ import annotations

from hexawyn.application.ports.driven.version_check_port import VersionCheckPort
from hexawyn.application.service.version_check_service import check_for_update


class _FakeVersionPort(VersionCheckPort):
    def __init__(self, latest: str) -> None:
        self._latest = latest

    def fetch_latest_version(self) -> str:
        return self._latest


class TestCheckForUpdate:
    def test_up_to_date_when_same_version(self) -> None:
        result = check_for_update("0.1.0b4", _FakeVersionPort("0.1.0b4"))

        assert result.status == "up_to_date"
        assert result.current_version == "0.1.0b4"
        assert result.latest_version == "0.1.0b4"
        assert result.error is None

    def test_update_available_when_latest_newer(self) -> None:
        result = check_for_update("0.1.0b3", _FakeVersionPort("0.1.0b4"))

        assert result.status == "update_available"
        assert result.current_version == "0.1.0b3"
        assert result.latest_version == "0.1.0b4"

    def test_update_available_on_newer_release(self) -> None:
        result = check_for_update("0.1.0b4", _FakeVersionPort("0.2.0"))

        assert result.status == "update_available"

    def test_unknown_when_latest_unreachable(self) -> None:
        result = check_for_update("0.1.0b4", _FakeVersionPort(""))

        assert result.status == "unknown"
        assert result.error is not None

    def test_unknown_when_latest_invalid(self) -> None:
        result = check_for_update("0.1.0b4", _FakeVersionPort("not-a-version"))

        assert result.status == "unknown"


class TestVersionComparisons:
    def test_stable_release_is_newer_than_beta(self) -> None:
        result = check_for_update("0.1.0b4", _FakeVersionPort("0.1.0"))

        assert result.status == "update_available"
        assert result.latest_version == "0.1.0"

    def test_beta_is_not_newer_than_its_own_stable_release(self) -> None:
        result = check_for_update("0.1.0", _FakeVersionPort("0.1.0b4"))

        assert result.status == "up_to_date"

    def test_beta_newer_when_identical_base_and_higher_beta(self) -> None:
        result = check_for_update("0.1.0b3", _FakeVersionPort("0.1.0b4"))

        assert result.status == "update_available"

    def test_current_newer_than_latest(self) -> None:
        result = check_for_update("0.2.0", _FakeVersionPort("0.1.0b4"))

        assert result.status == "up_to_date"
