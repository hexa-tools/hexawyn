"""Unit tests for CLI presentation constants."""

from __future__ import annotations

from hexawyn.cli.presentation.constants import _LOGO_BANNER, _POD_STATUS_COLORS


class TestConstants:
    def test_pod_status_colors_is_non_empty(self) -> None:
        assert isinstance(_POD_STATUS_COLORS, dict)
        assert len(_POD_STATUS_COLORS) > 0

    def test_logo_banner_is_non_empty(self) -> None:
        assert isinstance(_LOGO_BANNER, list)
        assert len(_LOGO_BANNER) > 0
