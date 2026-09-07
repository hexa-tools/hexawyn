from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.token_input import _format_expiry, _get_current_plan


class TestFormatExpiry:
    def test_empty_string(self) -> None:
        assert _format_expiry("") == "unknown"

    def test_iso_format(self) -> None:
        result = _format_expiry("2099-12-31T23:59:59Z")
        assert "2099" in result
        assert "days" in result

    def test_unix_timestamp(self) -> None:
        result = _format_expiry("4102444799")
        assert "31 Dec 2099" in result

    def test_parse_error_returns_raw(self) -> None:
        assert _format_expiry("not-a-date") == "not-a-date"


class TestGetCurrentPlan:
    def test_active_plan(self) -> None:
        mock_state = MagicMock()
        mock_state.state = "active"
        mock_state.plan = "team"
        with patch(
            "hexawyn.infrastructure.license.license_reader.read_license_state",
            return_value=mock_state,
        ):
            assert _get_current_plan() == "team"

    def test_missing_state(self) -> None:
        mock_state = MagicMock()
        mock_state.state = "missing"
        mock_state.plan = None
        with patch(
            "hexawyn.infrastructure.license.license_reader.read_license_state",
            return_value=mock_state,
        ):
            assert _get_current_plan() is None

    def test_invalid_state(self) -> None:
        mock_state = MagicMock()
        mock_state.state = "invalid"
        mock_state.plan = None
        with patch(
            "hexawyn.infrastructure.license.license_reader.read_license_state",
            return_value=mock_state,
        ):
            assert _get_current_plan() is None
