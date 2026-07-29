from __future__ import annotations

from unittest.mock import patch

from hexawyn.cli.presentation.license_display import (
    format_license_aside_lines,
    format_license_footer_hint,
)
from hexawyn.domain.services.license_state import LicenseState


class TestFormatLicenseAsideLines:
    def test_state_missing_returns_not_configured(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            lines = format_license_aside_lines()

        assert len(lines) == 2  # noqa: PLR2004
        assert "not configured" in lines[1]

    def test_state_invalid_returns_invalid(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="invalid", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            lines = format_license_aside_lines()

        assert len(lines) == 2  # noqa: PLR2004
        assert "Invalid" in lines[1] or "invalid" in lines[1]

    def test_state_expired_shows_expired_label(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="expired",
                plan="team",
                days_remaining=-5,
                expiry_date="01 Jan 2025",
            ),
        ):
            lines = format_license_aside_lines()

        assert len(lines) == 3  # noqa: PLR2004
        assert "License" in lines[1]
        assert "expired" in lines[2]

    def test_state_active_with_days_remaining(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="active",
                plan="team",
                days_remaining=30,
                expiry_date="28 Aug 2026",
            ),
        ):
            lines = format_license_aside_lines()

        assert len(lines) == 3  # noqa: PLR2004
        assert "Team" in lines[1]
        assert "30d" in lines[2]
        assert "28 Aug 2026" in lines[2]

    def test_state_active_zero_days_excluded(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="active",
                plan="starter",
                days_remaining=0,
                expiry_date="01 Jan 2025",
            ),
        ):
            lines = format_license_aside_lines()

        assert len(lines) == 3  # noqa: PLR2004
        assert "Starter" in lines[1]

    def test_state_warning_shows_days(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="warning",
                plan="scale_up",
                days_remaining=5,
                expiry_date="02 Aug 2026",
            ),
        ):
            lines = format_license_aside_lines()

        assert len(lines) == 3  # noqa: PLR2004
        assert "Scale_Up" in lines[1]
        assert "5d" in lines[2]


class TestFormatLicenseFooterHint:
    def test_expired_returns_upgrade(self) -> None:
        result = format_license_footer_hint("expired")
        assert "upgrade" in result

    def test_warning_returns_muted_upgrade(self) -> None:
        result = format_license_footer_hint("warning")
        assert "upgrade" in result
        assert "dim" in result

    def test_other_returns_manage(self) -> None:
        result = format_license_footer_hint("active")
        assert "manage" in result

    def test_missing_returns_manage(self) -> None:
        result = format_license_footer_hint("missing")
        assert "manage" in result
