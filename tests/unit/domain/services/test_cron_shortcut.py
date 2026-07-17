from __future__ import annotations


class TestCronShortcut:
    def test_six_hours(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("6h") == "0 */6 * * *"

    def test_fifteen_minutes(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("15m") == "*/15 * * * *"

    def test_twenty_four_hours(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("24h") == "0 0 * * *"

    def test_one_hour(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("1h") == "0 * * * *"

    def test_thirty_minutes(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("30m") == "*/30 * * * *"

    def test_invalid_shortcut_returns_none(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("5x") is None

    def test_full_cron_passed_through(self) -> None:
        from hexawyn.domain.services.schedule.cron_shortcut import shortcut_to_cron

        assert shortcut_to_cron("0 2 * * 1") == "0 2 * * 1"
