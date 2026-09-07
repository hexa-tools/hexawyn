from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

from hexawyn.cli.integrations.mcp.opencode import OpenCodeIntegration


class TestOpenCodeIntegration:
    def test_default_config_path(self) -> None:
        assert OpenCodeIntegration.default_config_path == (
            Path.home() / ".config" / "opencode" / "opencode.json"
        )

    def test_config_root_key_is_mcp(self) -> None:
        integration = OpenCodeIntegration(config_path=Path("/tmp/x.json"))
        assert integration._config_root_key() == "mcp"

    def test_build_entry(self) -> None:
        integration = OpenCodeIntegration(config_path=Path("/tmp/x.json"))
        assert integration._build_entry() == {
            "type": "local",
            "command": [sys.executable, "-m", "hexawyn.mcp.stdio"],
        }

    def test_install_and_uninstall_via_config(self, tmp_path: Path) -> None:
        config_path = tmp_path / "opencode.json"
        config_path.parent.mkdir(exist_ok=True)
        config_path.write_text(
            json.dumps({"mcp": {"other": {"type": "remote", "url": "https://x/mcp"}}}),
            encoding="utf-8",
        )
        integration = OpenCodeIntegration(config_path=config_path)
        with patch(
            "hexawyn.cli.integrations.mcp.file.shutil.which",
            return_value="/usr/local/bin/opencode",
        ):
            install = integration.install()
            status = integration.status()
            uninstall = integration.uninstall()

        assert install.success is True
        assert status.configured is True
        assert uninstall.success is True
        data = json.loads(config_path.read_text(encoding="utf-8"))
        assert "other" in data["mcp"]
        assert "hexawyn" not in data["mcp"]
