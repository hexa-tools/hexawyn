from pathlib import Path


class TestScheduleRefactored:
    def test_no_build_registry_in_schedule_command(self) -> None:
        source = Path("src/hexawyn/cli/commands/schedule_command.py").read_text()
        assert (
            "def _build_registry" not in source
        ), "_build_registry should be in infrastructure/config/schedule_registry.py"

    def test_no_certs_list_in_schedule_command(self) -> None:
        source = Path("src/hexawyn/cli/commands/schedule_command.py").read_text()
        assert (
            "def _certs_list" not in source
        ), "_certs_list wrapper should be in schedule_registry.py"

    def test_no_global_health_in_schedule_command(self) -> None:
        source = Path("src/hexawyn/cli/commands/schedule_command.py").read_text()
        assert (
            "def _global_health" not in source
        ), "_global_health wrapper should be in schedule_registry.py"

    def test_registry_contains_expected_keys(self) -> None:
        from hexawyn.infrastructure.config.schedule_registry import build_registry

        registry = build_registry()
        assert "certs_list" in registry
        assert "global_health_check" in registry
        assert callable(registry["certs_list"])
        assert callable(registry["global_health_check"])
