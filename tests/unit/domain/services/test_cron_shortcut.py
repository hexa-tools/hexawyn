class TestCronToMinutes:
    def test_shortcut_mappings(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes

        assert cron_to_minutes("*/15 * * * *") == 15
        assert cron_to_minutes("*/30 * * * *") == 30
        assert cron_to_minutes("0 * * * *") == 60
        assert cron_to_minutes("0 */6 * * *") == 360
        assert cron_to_minutes("0 */12 * * *") == 720
        assert cron_to_minutes("0 0 * * *") == 1440

    def test_unknown_returns_zero(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes

        assert cron_to_minutes("0 0 1 * *") == 0
        assert cron_to_minutes("invalid") == 0
        assert cron_to_minutes("") == 0
