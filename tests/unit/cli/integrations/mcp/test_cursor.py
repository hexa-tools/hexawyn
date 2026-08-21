from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

from hexawyn.cli.integrations.mcp.cursor import CursorIntegration


class TestCursorIntegration:
    def test_default_config_path(self) -> None:
        assert CursorIntegration.default_config_path == Path.home() / ".cursor" / "mcp.json"

    def test_config_root_key_is_mcp_servers(self) -> None:
        integration = CursorIntegration(config_path=Path("/tmp/x.json"))
        assert integration._config_root_key() == "mcpServers"

    def test_build_entry(self) -> None:
        integration = CursorIntegration(config_path=Path("/tmp/x.json"))
        assert integration._build_entry() == {
            "command": sys.executable,
            "args": ["-m", "hexawyn.mcp.stdio"],
        }

    def test_install_and_uninstall_via_config(self, tmp_path: Path) -> None:
        config_path = tmp_path / "mcp.json"
        config_path.parent.mkdir(exist_ok=True)
        config_path.write_text(
            json.dumps({"mcpServers": {"github": {"command": "gh-mcp"}}}),
            encoding="utf-8",
        )
        integration = CursorIntegration(config_path=config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value=None,
        ):
            install = integration.install()
            status = integration.status()
            uninstall = integration.uninstall()

        assert install.success is True
        assert status.configured is True
        assert uninstall.success is True
        data = json.loads(config_path.read_text(encoding="utf-8"))
        assert "github" in data["mcpServers"]
        assert "hexawyn" not in data["mcpServers"]
