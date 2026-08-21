from __future__ import annotations

import sys
from unittest.mock import patch

from hexawyn.cli.integrations.mcp.base import CommandResult
from hexawyn.cli.integrations.mcp.claude import (
    ClaudeCodeIntegration,
    _command_string,
    _parse_entry,
)

_COMMAND = f"{sys.executable} -m hexawyn.mcp.stdio"
_CONFIGURED_COMMAND = f"  Command: {sys.executable}\n"

CONFIGURED_TEXT = (
    "hexawyn:\n"
    "  Scope: User config\n"
    "  Status: ✔ Connected\n"
    "  Type: stdio\n"
    f"{_CONFIGURED_COMMAND}"
    "  Args: -m hexawyn.mcp.stdio\n"
)
NOT_CONFIGURED = CommandResult(
    1,
    "",
    'No MCP server named "hexawyn". Configured servers: Jan, topview',
)
GET_COMMAND = ["claude", "mcp", "get", "hexawyn"]
ADD_COMMAND = [
    "claude",
    "mcp",
    "add",
    "hexawyn",
    "--",
    sys.executable,
    "-m",
    "hexawyn.mcp.stdio",
]

_AVAILABLE = lambda: patch(  # noqa: E731
    "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
    return_value="/usr/local/bin/claude",
)
_MISSING = lambda: patch(  # noqa: E731
    "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
    return_value=None,
)


class FakeRunner:
    """Deterministic CommandRunner replacement — never touches subprocess."""

    def __init__(self, responses: list[CommandResult]) -> None:
        self.responses = list(responses)
        self.commands: list[list[str]] = []

    def run(self, command: list[str]) -> CommandResult:
        self.commands.append(command)
        if not self.responses:
            return NOT_CONFIGURED
        return self.responses.pop(0)


def _integration(responses: list[CommandResult]) -> ClaudeCodeIntegration:
    return ClaudeCodeIntegration(runner=FakeRunner(responses))


class TestClaudeDetection:
    def test_is_available_when_claude_on_path(self) -> None:
        integration = _integration([])
        with _AVAILABLE():
            assert integration.is_available() is True

    def test_is_available_false_when_missing(self) -> None:
        integration = _integration([])
        with _MISSING():
            assert integration.is_available() is False

    def test_is_installed_when_entry_present(self) -> None:
        integration = _integration([CommandResult(0, CONFIGURED_TEXT)])
        with _AVAILABLE():
            assert integration.is_installed() is True

    def test_is_installed_false_when_absent(self) -> None:
        integration = _integration([NOT_CONFIGURED])
        with _AVAILABLE():
            assert integration.is_installed() is False

    def test_is_installed_false_when_get_fails(self) -> None:
        integration = _integration([CommandResult(2, "", "claude exploded")])
        with _AVAILABLE():
            assert integration.is_installed() is False


class TestClaudeInstall:
    def test_install_configures_server(self) -> None:
        runner = FakeRunner(
            [
                NOT_CONFIGURED,  # check: not configured yet
                CommandResult(0, ""),  # claude mcp add
                CommandResult(0, CONFIGURED_TEXT),  # verify
            ]
        )
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.install()

        assert result.success is True
        assert result.already_configured is False
        assert runner.commands[0] == GET_COMMAND
        assert runner.commands[1] == ADD_COMMAND

    def test_install_is_idempotent(self) -> None:
        first_runner = FakeRunner(
            [
                NOT_CONFIGURED,
                CommandResult(0, ""),
                CommandResult(0, CONFIGURED_TEXT),
            ]
        )
        with _AVAILABLE():
            first = ClaudeCodeIntegration(runner=first_runner).install()
            # Second run sees the already-written configuration.
            second_runner = FakeRunner([CommandResult(0, CONFIGURED_TEXT)])
            second = ClaudeCodeIntegration(runner=second_runner).install()

        assert first.success is True
        assert second.success is True
        assert second.already_configured is True
        assert "add" not in " ".join(" ".join(c) for c in second_runner.commands)

    def test_install_when_already_configured_does_not_add(self) -> None:
        runner = FakeRunner([CommandResult(0, CONFIGURED_TEXT)])
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.install()

        assert result.success is True
        assert result.already_configured is True
        assert "add" not in " ".join(" ".join(c) for c in runner.commands)

    def test_install_when_claude_missing(self) -> None:
        integration = _integration([])
        with _MISSING():
            result = integration.install()
        assert result.success is False
        assert "not found" in result.message

    def test_install_when_add_fails(self) -> None:
        runner = FakeRunner(
            [
                NOT_CONFIGURED,
                CommandResult(1, "", "boom"),
            ]
        )
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.install()

        assert result.success is False
        assert "claude mcp add" in result.message
        assert "boom" in result.message

    def test_install_verification_failure(self) -> None:
        runner = FakeRunner(
            [
                NOT_CONFIGURED,
                CommandResult(0, ""),
                NOT_CONFIGURED,  # verify: still absent
            ]
        )
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.install()

        assert result.success is False

    def test_install_when_get_fails(self) -> None:
        runner = FakeRunner([CommandResult(2, "", "claude exploded")])
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.install()

        assert result.success is False
        assert "claude exploded" in result.message


class TestClaudeUninstall:
    def test_uninstall_removes_only_hexawyn(self) -> None:
        runner = FakeRunner(
            [
                CommandResult(0, CONFIGURED_TEXT),
                CommandResult(0, ""),  # claude mcp remove
                NOT_CONFIGURED,  # verify: gone
            ]
        )
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.uninstall()

        assert result.success is True
        assert runner.commands[1] == ["claude", "mcp", "remove", "hexawyn"]

    def test_uninstall_when_not_configured(self) -> None:
        runner = FakeRunner([NOT_CONFIGURED])
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.uninstall()

        assert result.success is True
        assert result.message == "not configured"
        assert "remove" not in " ".join(" ".join(c) for c in runner.commands)

    def test_uninstall_when_claude_missing(self) -> None:
        integration = _integration([])
        with _MISSING():
            result = integration.uninstall()
        assert result.success is False

    def test_uninstall_when_remove_fails(self) -> None:
        runner = FakeRunner(
            [
                CommandResult(0, CONFIGURED_TEXT),
                CommandResult(1, "", "cannot remove"),
            ]
        )
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.uninstall()

        assert result.success is False
        assert "claude mcp remove" in result.message

    def test_uninstall_when_still_present_after_remove(self) -> None:
        runner = FakeRunner(
            [
                CommandResult(0, CONFIGURED_TEXT),
                CommandResult(0, ""),
                CommandResult(0, CONFIGURED_TEXT),  # verify: still there
            ]
        )
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.uninstall()

        assert result.success is False

    def test_uninstall_when_get_fails(self) -> None:
        runner = FakeRunner([CommandResult(2, "", "claude exploded")])
        integration = ClaudeCodeIntegration(runner=runner)
        with _AVAILABLE():
            result = integration.uninstall()

        assert result.success is False
        assert "claude exploded" in result.message


class TestClaudeStatus:
    def test_status_configured(self) -> None:
        integration = _integration([CommandResult(0, CONFIGURED_TEXT)])
        with _AVAILABLE():
            status = integration.status()

        assert status.configured is True
        assert status.transport == "stdio"
        assert status.command == _COMMAND
        assert status.endpoint == ""
        assert status.error is None

    def test_status_not_configured(self) -> None:
        integration = _integration([NOT_CONFIGURED])
        with _AVAILABLE():
            status = integration.status()

        assert status.configured is False
        assert status.error is None

    def test_status_when_get_fails(self) -> None:
        integration = _integration([CommandResult(2, "", "claude exploded")])
        with _AVAILABLE():
            status = integration.status()

        assert status.configured is False
        assert "claude exploded" in (status.error or "")

    def test_status_when_claude_missing(self) -> None:
        integration = _integration([])
        with _MISSING():
            status = integration.status()
        assert status.configured is False
        assert "Claude Code not found" in (status.error or "")


class TestParseEntry:
    def test_parses_type_and_command(self) -> None:
        entry = _parse_entry(CONFIGURED_TEXT)
        assert entry["type"] == "stdio"
        assert entry["command"] == sys.executable
        assert entry["args"] == "-m hexawyn.mcp.stdio"

    def test_parses_url_entry(self) -> None:
        entry = _parse_entry("hexawyn:\n  Type: http\n  URL: http://localhost:8000/mcp\n")
        assert entry["type"] == "http"
        assert entry["url"] == "http://localhost:8000/mcp"

    def test_parses_unknown_text_as_empty(self) -> None:
        assert _parse_entry("unrelated output") == {}

    def test_command_string_without_args(self) -> None:
        assert _command_string({"command": "python"}) == "python"

    def test_command_string_without_command(self) -> None:
        assert _command_string({"args": "-m x"}) == ""
