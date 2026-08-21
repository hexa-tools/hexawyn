from __future__ import annotations

import sys
from unittest.mock import patch

from hexawyn.cli.integrations.mcp.base import CommandResult
from hexawyn.cli.integrations.mcp.cli_mcp import CliIntegrationStatus, CliMcpIntegration

CONFIGURED = CliIntegrationStatus(
    configured=True,
    transport="stdio",
    command=f"{sys.executable} -m hexawyn.mcp.stdio",
)
NOT_CONFIGURED = CliIntegrationStatus(configured=False)
ERROR_STATUS = CliIntegrationStatus(configured=False, error="fakebin exploded")


class FakeRunner:
    def __init__(self, responses: list[CommandResult]) -> None:
        self.responses = list(responses)
        self.commands: list[list[str]] = []

    def run(self, command: list[str]) -> CommandResult:
        self.commands.append(command)
        if not self.responses:
            return CommandResult(returncode=0, stdout="")
        return self.responses.pop(0)


class FakeCliIntegration(CliMcpIntegration):
    client_name = "fake"
    binary = "fakebin"
    display_name = "Fake Agent"

    def __init__(self, runner: FakeRunner, statuses: list[CliIntegrationStatus]) -> None:
        super().__init__(runner=runner)
        self._statuses = list(statuses)

    def _read_status(self) -> CliIntegrationStatus:
        if not self._statuses:
            return NOT_CONFIGURED
        return self._statuses.pop(0)

    def _add_command(self) -> list[str]:
        return [
            "fakebin",
            "mcp",
            "add",
            "hexawyn",
            "--",
            sys.executable,
            "-m",
            "hexawyn.mcp.stdio",
        ]

    def _remove_command(self) -> list[str]:
        return ["fakebin", "mcp", "remove", "hexawyn"]


def _available(integration: CliMcpIntegration) -> None:
    patch(
        "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
        return_value="/usr/local/bin/fakebin",
    ).start()


class TestCliMcpAvailability:
    def test_is_available_when_binary_present(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/fakebin",
        ):
            assert integration.is_available() is True

    def test_is_available_false_when_missing(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value=None,
        ):
            assert integration.is_available() is False

    def test_is_installed_from_status(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [CONFIGURED])
        with patch(
            "hexawyn.cli.integrations.mcp.cli_mcp.shutil.which",
            return_value="/usr/local/bin/fakebin",
        ):
            assert integration.is_installed() is True


class TestCliMcpInstall:
    def test_install_adds_server(self) -> None:
        runner = FakeRunner([CommandResult(0, "")])
        integration = FakeCliIntegration(runner, [NOT_CONFIGURED, CONFIGURED])
        _available(integration)

        result = integration.install()

        assert result.success is True
        assert result.already_configured is False
        assert runner.commands[0] == [
            "fakebin",
            "mcp",
            "add",
            "hexawyn",
            "--",
            sys.executable,
            "-m",
            "hexawyn.mcp.stdio",
        ]

    def test_install_when_already_configured(self) -> None:
        runner = FakeRunner([])
        integration = FakeCliIntegration(runner, [CONFIGURED])
        _available(integration)

        result = integration.install()

        assert result.success is True
        assert result.already_configured is True
        assert runner.commands == []

    def test_install_when_status_error(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [ERROR_STATUS])
        _available(integration)

        result = integration.install()

        assert result.success is False
        assert "fakebin exploded" in result.message

    def test_install_when_add_fails(self) -> None:
        runner = FakeRunner([CommandResult(1, "", "boom")])
        integration = FakeCliIntegration(runner, [NOT_CONFIGURED])
        _available(integration)

        result = integration.install()

        assert result.success is False
        assert "fakebin mcp add" in result.message
        assert "boom" in result.message

    def test_install_verification_failure(self) -> None:
        runner = FakeRunner([CommandResult(0, "")])
        integration = FakeCliIntegration(runner, [NOT_CONFIGURED, NOT_CONFIGURED])
        _available(integration)

        result = integration.install()

        assert result.success is False


class TestCliMcpUninstall:
    def test_uninstall_removes_server(self) -> None:
        runner = FakeRunner([CommandResult(0, "")])
        integration = FakeCliIntegration(runner, [CONFIGURED, NOT_CONFIGURED])
        _available(integration)

        result = integration.uninstall()

        assert result.success is True
        assert runner.commands[0] == ["fakebin", "mcp", "remove", "hexawyn"]

    def test_uninstall_when_not_configured(self) -> None:
        runner = FakeRunner([])
        integration = FakeCliIntegration(runner, [NOT_CONFIGURED])
        _available(integration)

        result = integration.uninstall()

        assert result.success is True
        assert result.message == "not configured"
        assert runner.commands == []

    def test_uninstall_when_remove_fails(self) -> None:
        runner = FakeRunner([CommandResult(1, "", "boom")])
        integration = FakeCliIntegration(runner, [CONFIGURED])
        _available(integration)

        result = integration.uninstall()

        assert result.success is False
        assert "fakebin mcp remove" in result.message

    def test_uninstall_when_still_present(self) -> None:
        runner = FakeRunner([CommandResult(0, "")])
        integration = FakeCliIntegration(runner, [CONFIGURED, CONFIGURED])
        _available(integration)

        result = integration.uninstall()

        assert result.success is False

    def test_uninstall_when_status_error(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [ERROR_STATUS])
        _available(integration)

        result = integration.uninstall()

        assert result.success is False


class TestCliMcpStatus:
    def test_status_configured(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [CONFIGURED])
        _available(integration)

        status = integration.status()

        assert status.configured is True
        assert status.transport == "stdio"
        assert status.command == f"{sys.executable} -m hexawyn.mcp.stdio"
        assert status.error is None

    def test_status_not_configured(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [NOT_CONFIGURED])
        _available(integration)

        status = integration.status()

        assert status.configured is False
        assert status.error is None

    def test_status_error(self) -> None:
        integration = FakeCliIntegration(FakeRunner([]), [ERROR_STATUS])
        _available(integration)

        status = integration.status()

        assert status.configured is False
        assert status.error == "fakebin exploded"
