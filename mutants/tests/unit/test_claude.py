"""Regression test: `claude mcp get` returns exit 0 even when the server is absent.

Claude Code ≥ 2.x prints ``No MCP server named "hexawyn"`` and exits 0 when the
server is not configured. hexawyn's integration must not treat an exit-0
"not found" as "configured" — otherwise `hexa claude install` never adds the
server and reports a false "already configured".
"""

from __future__ import annotations

from unittest.mock import patch

from hexawyn.cli.integrations.mcp.base import CommandResult
from hexawyn.cli.integrations.mcp.claude import ClaudeCodeIntegration

NOT_FOUND_EXIT_0 = CommandResult(
    0,
    'No MCP server named "hexawyn". Configured servers: Jan, topview\n',
    "",
)


class _FakeRunner:
    def __init__(self, result: CommandResult) -> None:
        self._result = result

    def run(self, command: list[str]) -> CommandResult:
        return self._result


class TestClaudeNotConfiguredOnExitZero:
    def test_is_installed_false_when_get_exits_zero_but_prints_not_found(self) -> None:
        integration = ClaudeCodeIntegration(runner=_FakeRunner(NOT_FOUND_EXIT_0))
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/claude",
        ):
            assert integration.is_installed() is False

    def test_status_not_configured_when_get_exits_zero_but_prints_not_found(self) -> None:
        integration = ClaudeCodeIntegration(runner=_FakeRunner(NOT_FOUND_EXIT_0))
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/claude",
        ):
            status = integration.status()

        assert status.configured is False

    def test_install_runs_add_when_get_exits_zero_but_prints_not_found(self) -> None:
        calls: list[list[str]] = []

        class _Runner:
            def __init__(self) -> None:
                self._get_calls = 0
                self._add_done: bool = False

            def run(self, command: list[str]) -> CommandResult:
                calls.append(command)
                if "add" in command:
                    self._add_done = True
                    return CommandResult(0, "")
                if "get" in command:
                    self._get_calls += 1
                    if self._get_calls == 1 and not self._add_done:
                        return NOT_FOUND_EXIT_0
                    return CommandResult(
                        0,
                        "hexawyn:\n"
                        "  Scope: User config\n"
                        "  Status: Connected\n"
                        "  Type: stdio\n"
                        "  Command: /usr/bin/python\n"
                        "  Args: -m hexawyn.mcp.stdio\n",
                    )
                return CommandResult(0, "")

        integration = ClaudeCodeIntegration(runner=_Runner())
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/claude",
        ):
            result = integration.install()

        assert result.success is True
        assert result.already_configured is False
        assert any("add" in " ".join(cmd) for cmd in calls), "install() must run claude mcp add"
