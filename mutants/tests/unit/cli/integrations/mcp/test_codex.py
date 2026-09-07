from __future__ import annotations

import sys
from unittest.mock import patch

from hexawyn.cli.integrations.mcp.base import CommandResult
from hexawyn.cli.integrations.mcp.codex import CodexIntegration

_COMMAND = f"{sys.executable} -m hexawyn.mcp.stdio"

LIST_CONFIGURED = f"name: hexawyn\ncommand: {_COMMAND}\nanother-server\n"
LIST_EMPTY = "another-server\n"
LIST_COMMAND = ["codex", "mcp", "list"]
ADD_COMMAND = [
    "codex",
    "mcp",
    "add",
    "hexawyn",
    "--",
    sys.executable,
    "-m",
    "hexawyn.mcp.stdio",
]
REMOVE_COMMAND = ["codex", "mcp", "remove", "hexawyn"]


class FakeRunner:
    def __init__(self, responses: list[CommandResult]) -> None:
        self.responses = list(responses)
        self.commands: list[list[str]] = []

    def run(self, command: list[str]) -> CommandResult:
        self.commands.append(command)
        if not self.responses:
            return CommandResult(returncode=0, stdout="")
        return self.responses.pop(0)


def _integration(responses: list[CommandResult]) -> CodexIntegration:
    return CodexIntegration(runner=FakeRunner(responses))


class TestCodexIntegration:
    def test_is_available_when_codex_on_path(self) -> None:
        integration = _integration([])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/codex",
        ):
            assert integration.is_available() is True

    def test_is_available_false_when_missing(self) -> None:
        integration = _integration([])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value=None,
        ):
            assert integration.is_available() is False

    def test_read_status_configured(self) -> None:
        integration = _integration([CommandResult(0, LIST_CONFIGURED)])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/codex",
        ):
            status = integration._read_status()

        assert status.configured is True
        assert status.command == _COMMAND

    def test_read_status_not_configured(self) -> None:
        integration = _integration([CommandResult(0, LIST_EMPTY)])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/codex",
        ):
            status = integration._read_status()

        assert status.configured is False

    def test_read_status_when_list_fails(self) -> None:
        integration = _integration([CommandResult(1, "", "codex exploded")])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/codex",
        ):
            status = integration._read_status()

        assert status.configured is False
        assert "codex exploded" in status.error

    def test_read_status_when_codex_missing(self) -> None:
        integration = _integration([])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value=None,
        ):
            status = integration._read_status()

        assert status.configured is False
        assert "Codex not found" in status.error

    def test_add_and_remove_commands(self) -> None:
        integration = _integration([])
        assert integration._add_command() == ADD_COMMAND
        assert integration._remove_command() == REMOVE_COMMAND

    def test_install_through_base(self) -> None:
        runner = FakeRunner(
            [
                CommandResult(0, LIST_EMPTY),  # check
                CommandResult(0, ""),  # add
                CommandResult(0, LIST_CONFIGURED),  # verify
            ]
        )
        integration = CodexIntegration(runner=runner)
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/codex",
        ):
            result = integration.install()

        assert result.success is True
        assert runner.commands[1] == ADD_COMMAND

    def test_uninstall_through_base(self) -> None:
        runner = FakeRunner(
            [
                CommandResult(0, LIST_CONFIGURED),  # check
                CommandResult(0, ""),  # remove
                CommandResult(0, LIST_EMPTY),  # verify
            ]
        )
        integration = CodexIntegration(runner=runner)
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/codex",
        ):
            result = integration.uninstall()

        assert result.success is True
        assert runner.commands[1] == REMOVE_COMMAND
