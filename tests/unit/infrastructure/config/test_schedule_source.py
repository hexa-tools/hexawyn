from __future__ import annotations

from unittest.mock import patch


class TestYamlScheduleSource:
    def test_load_empty_returns_empty_list(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.load_config",
            return_value={},
        ):
            from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

            source = YamlScheduleSource()
            result = source.load_checks()

            assert result == []

    def test_load_checks_from_yaml(self) -> None:
        config = {
            "schedule": {
                "certs": {
                    "schedule": "0 */6 * * *",
                    "use_case": "certs_list",
                    "params": {"namespace": "prod"},
                    "notify_policy": "on_change",
                },
                "rbac": {
                    "schedule": "0 0 * * *",
                    "use_case": "audit_excessive_rbac",
                    "enabled": False,
                },
            }
        }
        with patch(
            "hexawyn.infrastructure.config.schedule_source.load_config",
            return_value=config,
        ):
            from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

            source = YamlScheduleSource()
            result = source.load_checks()

        assert len(result) == 2
        assert result[0].name == "certs"
        assert result[0].use_case == "certs_list"
        assert result[1].enabled is False

    def test_save_checks_updates_config(self) -> None:
        from hexawyn.domain.models.schedule import CronCheck

        with (
            patch(
                "hexawyn.infrastructure.config.schedule_source.load_config",
                return_value={},
            ),
            patch(
                "hexawyn.infrastructure.config.schedule_source.save_config",
            ) as mock_save,
        ):
            from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

            source = YamlScheduleSource()
            check = CronCheck(name="test", schedule="*/15 * * * *", use_case="test")

            source.save_checks([check])

            mock_save.assert_called_once()

    def test_non_dict_entry_skipped(self) -> None:
        config = {
            "schedule": {
                "certs": {"schedule": "0 */6 * * *", "use_case": "certs_list"},
                "bad": "not-a-dict",
            }
        }
        with patch(
            "hexawyn.infrastructure.config.schedule_source.load_config", return_value=config
        ):
            from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

            source = YamlScheduleSource()
            result = source.load_checks()

        assert len(result) == 1
        assert result[0].name == "certs"

    def test_corrupted_config_returns_empty(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.load_config",
            return_value={"schedule": "not_a_dict"},
        ):
            from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

            source = YamlScheduleSource()
            result = source.load_checks()
            assert result == []
