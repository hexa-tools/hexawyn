from __future__ import annotations

import sys
from pathlib import Path

import yaml
from hexawyn.cli.integrations.mcp.deepseek import DeepSeekHarnessIntegration


class TestDeepSeekHarnessIntegration:
    def test_default_config_path(self) -> None:
        assert DeepSeekHarnessIntegration.default_config_path == (
            Path.home() / ".config" / "deepseek-harness" / "hexawyn.cordis.yml"
        )

    def test_client_name_is_deepseek(self) -> None:
        assert DeepSeekHarnessIntegration.client_name == "deepseek"

    def test_build_overlay_registers_hexawyn_mcp(self) -> None:
        integration = DeepSeekHarnessIntegration(config_path=Path("/tmp/x.cordis.yml"))
        data = yaml.safe_load(integration._build_overlay())
        entry = data[0]["insert"][0]
        assert entry["id"] == "hexawyn"
        assert entry["name"] == "@deepseek-ai/dsh-mcp-client"
        config = entry["config"]
        assert config["serverName"] == "hexawyn"
        assert config["transport"] == "stdio"
        assert config["command"] == sys.executable
        assert config["args"] == ["-m", "hexawyn.mcp.stdio"]

    def test_install_then_uninstall_writes_and_removes_overlay(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn.cordis.yml"
        config_path.parent.mkdir(exist_ok=True)
        integration = DeepSeekHarnessIntegration(config_path=config_path)

        assert integration.install().success is True
        assert config_path.exists() is True
        assert integration.is_installed() is True
        assert integration.status().configured is True

        assert integration.uninstall().success is True
        assert config_path.exists() is False
        assert integration.is_installed() is False

    def test_install_is_idempotent(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn.cordis.yml"
        config_path.parent.mkdir(exist_ok=True)
        integration = DeepSeekHarnessIntegration(config_path=config_path)

        first = integration.install()
        second = integration.install()

        assert first.already_configured is False
        assert second.already_configured is True
        assert second.success is True

    def test_uninstall_when_not_configured(self, tmp_path: Path) -> None:
        integration = DeepSeekHarnessIntegration(config_path=tmp_path / "none.cordis.yml")
        result = integration.uninstall()
        assert result.success is True
        assert "not configured" in result.message

    def test_is_available_is_true_for_a_config_writer(self, tmp_path: Path) -> None:
        integration = DeepSeekHarnessIntegration(config_path=tmp_path / "x.cordis.yml")
        assert integration.is_available() is True
