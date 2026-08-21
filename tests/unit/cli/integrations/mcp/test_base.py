from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.cli.integrations.mcp.base import (
    MCP_SERVER_NAME,
    MCP_TRANSPORT,
    CommandResult,
    IntegrationResult,
    IntegrationStatus,
    MCPClientIntegration,
    SubprocessRunner,
)


class TestBaseContracts:
    def test_abstract_integration_cannot_be_instantiated(self) -> None:
        with pytest.raises(TypeError):
            MCPClientIntegration()  # type: ignore[abstract]

    def test_server_name_is_hexawyn(self) -> None:
        assert MCP_SERVER_NAME == "hexawyn"

    def test_transport_is_stdio(self) -> None:
        assert MCP_TRANSPORT == "stdio"


class TestCommandResult:
    def test_captures_fields(self) -> None:
        result = CommandResult(returncode=0, stdout="ok")
        assert result.returncode == 0
        assert result.stdout == "ok"

    def test_stderr_defaults_to_empty(self) -> None:
        result = CommandResult(returncode=1, stdout="")
        assert result.stderr == ""


class TestIntegrationResult:
    def test_not_already_configured_by_default(self) -> None:
        result = IntegrationResult(success=True, message="configured")
        assert result.already_configured is False


class TestIntegrationStatus:
    def test_error_defaults_to_none(self) -> None:
        status = IntegrationStatus(configured=True)
        assert status.error is None
        assert status.transport == MCP_TRANSPORT


class TestSubprocessRunner:
    def test_run_returns_command_result(self) -> None:
        proc = MagicMock()
        proc.returncode = 0
        proc.stdout = "hello"
        proc.stderr = ""
        with patch("subprocess.run", return_value=proc) as mock_run:
            result = SubprocessRunner().run(["echo", "hello"])

        mock_run.assert_called_once()
        assert result.returncode == 0
        assert result.stdout == "hello"

    def test_run_maps_file_not_found(self) -> None:
        with patch("subprocess.run", side_effect=FileNotFoundError("no such binary")):
            result = SubprocessRunner().run(["missing"])

        assert result.returncode == 127  # noqa: PLR2004
        assert "no such binary" in result.stderr

    def test_run_maps_timeout(self) -> None:
        import subprocess

        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="x", timeout=30)):
            result = SubprocessRunner().run(["sleep", "99"])

        assert result.returncode == 124  # noqa: PLR2004
