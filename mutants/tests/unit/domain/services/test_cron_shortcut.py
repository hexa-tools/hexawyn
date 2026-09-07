class TestCronToMinutes:
    def test_shortcut_mappings(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes

        assert cron_to_minutes("*/15 * * * *") == 15  # noqa: PLR2004
        assert cron_to_minutes("*/30 * * * *") == 30  # noqa: PLR2004
        assert cron_to_minutes("0 * * * *") == 60  # noqa: PLR2004
        assert cron_to_minutes("0 */6 * * *") == 360  # noqa: PLR2004
        assert cron_to_minutes("0 */12 * * *") == 720  # noqa: PLR2004
        assert cron_to_minutes("0 0 * * *") == 1440  # noqa: PLR2004

    def test_unknown_returns_zero(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes

        assert cron_to_minutes("0 0 1 * *") == 0
        assert cron_to_minutes("invalid") == 0
        assert cron_to_minutes("") == 0


class TestShortcutToCron:
    def test_shortcut_mappings(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("15m") == "*/15 * * * *"
        assert shortcut_to_cron("30m") == "*/30 * * * *"
        assert shortcut_to_cron("1h") == "0 * * * *"
        assert shortcut_to_cron("6h") == "0 */6 * * *"
        assert shortcut_to_cron("12h") == "0 */12 * * *"
        assert shortcut_to_cron("24h") == "0 0 * * *"

    def test_unknown_shortcut_returns_none(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("45m") is None

    def test_passes_through_cron_expression(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("0 0 * * *") == "0 0 * * *"

    def test_strips_whitespace(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("  1h  ") == "0 * * * *"
