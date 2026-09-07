from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration


class FakeFileIntegration(McpConfigFileIntegration):
    client_name = "fakefile"
    binary = "fakefile"
    display_name = "Fake File Agent"

    def _config_root_key(self) -> str:
        return "servers"

    def _build_entry(self) -> dict[str, object]:
        return {"command": [sys.executable, "-m", "hexawyn.mcp.stdio"]}


def _integration(config_path: Path) -> FakeFileIntegration:
    return FakeFileIntegration(config_path=config_path)


def _write(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


class TestFileAvailability:
    def test_available_when_binary_on_path(self, tmp_path: Path) -> None:
        integration = _integration(tmp_path / "config.json")
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            assert integration.is_available() is True

    def test_available_when_config_dir_exists(self, tmp_path: Path) -> None:
        integration = _integration(tmp_path / "config.json")
        tmp_path.mkdir(exist_ok=True)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value=None,
        ):
            assert integration.is_available() is True

    def test_unavailable_when_neither_present(self, tmp_path: Path) -> None:
        integration = _integration(tmp_path / "nested" / "config.json")
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value=None,
        ):
            assert integration.is_available() is False

    def test_is_installed_delegates_to_status(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(config_path, {"servers": {"hexawyn": {"command": ["x"]}}})
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            assert integration.is_installed() is True


class TestFileInstall:
    def test_install_writes_entry_and_preserves_others(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(config_path, {"servers": {"other": {"command": "other"}}})
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.install()

        assert result.success is True
        data = json.loads(config_path.read_text(encoding="utf-8"))
        servers = data["servers"]
        assert "other" in servers
        assert servers["hexawyn"] == {"command": [sys.executable, "-m", "hexawyn.mcp.stdio"]}

    def test_install_when_already_configured_is_idempotent(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(
            config_path,
            {"servers": {"hexawyn": {"command": ["old"]}, "other": {"command": "x"}}},
        )
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.install()

        assert result.success is True
        assert result.already_configured is True
        data = json.loads(config_path.read_text(encoding="utf-8"))
        assert data["servers"]["hexawyn"] == {"command": ["old"]}

    def test_install_creates_config_when_missing(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.install()

        assert result.success is True
        data = json.loads(config_path.read_text(encoding="utf-8"))
        assert "hexawyn" in data["servers"]

    def test_install_fails_on_malformed_config(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text("{broken", encoding="utf-8")
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.install()

        assert result.success is False
        assert "not valid JSON" in result.message

    def test_install_when_client_unavailable(self, tmp_path: Path) -> None:
        integration = _integration(tmp_path / "nested" / "config.json")
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value=None,
        ):
            result = integration.install()

        assert result.success is False
        assert "not found on PATH" in result.message

    def test_install_verification_failure(self, tmp_path: Path, monkeypatch) -> None:
        config_path = tmp_path / "config.json"
        config_path.parent.mkdir(exist_ok=True)
        integration = _integration(config_path)
        calls = {"n": 0}

        def flaky_read(self_obj: McpConfigFileIntegration) -> tuple[dict[str, object] | None, str]:
            calls["n"] += 1
            if calls["n"] == 2:  # noqa: PLR2004
                return None, "read back failed"
            return {}, ""

        monkeypatch.setattr(type(integration), "_read_config", flaky_read)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.install()

        assert result.success is False
        assert "read back failed" in result.message


class TestFileUninstall:
    def test_uninstall_removes_only_hexawyn(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(
            config_path,
            {
                "servers": {
                    "a": {"command": "a"},
                    "hexawyn": {"command": "hex"},
                    "b": {"command": "b"},
                }
            },
        )
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.uninstall()

        assert result.success is True
        data = json.loads(config_path.read_text(encoding="utf-8"))
        servers = data["servers"]
        assert "hexawyn" not in servers
        assert set(servers) == {"a", "b"}

    def test_uninstall_when_not_configured(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(config_path, {"servers": {"a": {"command": "a"}}})
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.uninstall()

        assert result.success is True
        assert result.message == "not configured"

    def test_uninstall_when_client_unavailable(self, tmp_path: Path) -> None:
        integration = _integration(tmp_path / "nested" / "config.json")
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value=None,
        ):
            result = integration.uninstall()

        assert result.success is False

    def test_uninstall_when_read_fails(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        config_path.parent.mkdir(exist_ok=True)
        config_path.write_text("{broken", encoding="utf-8")
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            result = integration.uninstall()

        assert result.success is False
        assert "not valid JSON" in result.message


class TestFileStatus:
    def test_status_configured(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(
            config_path,
            {"servers": {"hexawyn": {"command": [sys.executable, "-m", "hexawyn.mcp.stdio"]}}},
        )
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            status = integration.status()

        assert status.configured is True
        assert status.command == f"{sys.executable} -m hexawyn.mcp.stdio"
        assert status.error is None

    def test_status_not_configured(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(config_path, {"servers": {"a": {}}})
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            status = integration.status()

        assert status.configured is False
        assert status.error is None

    def test_status_malformed_config(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(config_path, "{broken")
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            status = integration.status()

        assert status.configured is False
        assert status.error is not None

    def test_status_when_client_unavailable(self, tmp_path: Path) -> None:
        integration = _integration(tmp_path / "nested" / "config.json")
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value=None,
        ):
            status = integration.status()

        assert status.configured is False
        assert "not found on PATH" in (status.error or "")

    def test_status_when_config_is_directory(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        config_path.mkdir()
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            status = integration.status()

        assert status.configured is False
        assert status.error is not None

    def test_status_when_config_not_an_object(self, tmp_path: Path) -> None:
        config_path = tmp_path / "config.json"
        _write(config_path, ["not", "an", "object"])
        integration = _integration(config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/fakefile",
        ):
            status = integration.status()

        assert status.configured is False
        assert "not a JSON object" in (status.error or "")
