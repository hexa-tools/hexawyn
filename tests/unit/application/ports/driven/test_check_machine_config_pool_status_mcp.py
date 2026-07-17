"""RED → GREEN — MCP tool: check_machine_config_pool_status."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
    MachineConfigPoolRawData,
)
from hexawyn.domain.errors import MachineConfigPoolCRDNotFoundError


def _raw(
    name: str,
    updating: bool = False,
    degraded: bool = False,
    since: str | None = None,
) -> MachineConfigPoolRawData:
    return MachineConfigPoolRawData(
        name=name,
        machine_count=5 if updating else 3,
        ready_machine_count=3 if updating else 3,
        updated_machine_count=2 if updating else 3,
        degraded_machine_count=1 if degraded else 0,
        updating=updating,
        degraded=degraded,
        paused=False,
        current_config="rendered-old" if updating else "rendered-abc",
        desired_config="rendered-new" if updating else "rendered-abc",
        reason="failed to apply MachineConfig" if degraded else "",
        updating_since=since,
    )


class TestCheckMachineConfigPoolStatusTool:
    def test_delegates_and_returns_summary(self) -> None:
        mock_port = MagicMock(spec=MachineConfigPoolPort)
        mock_port.list_machine_config_pools.return_value = [
            _raw("master"),
            _raw("worker", updating=True, since="2026-06-16T01:00:00Z"),
            _raw("infra", degraded=True),
        ]

        with patch(
            "hexawyn.mcp.server.build_machine_config_pool_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.check_machine_config_pool_status import (
                check_machine_config_pool_status,
            )

            result = check_machine_config_pool_status()

        assert result["total"] == 3
        assert result["degraded"] == 1
        assert result["updating"] == 1
        assert result["all_healthy"] is False
        assert result["error"] is None
        worker = next(pool for pool in result["pools"] if pool["name"] == "worker")
        assert worker["state"] == "updating"
        assert worker["config_mismatch"] is True

    def test_handles_crd_absent_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_machine_config_pool_adapter",
            side_effect=MachineConfigPoolCRDNotFoundError(),
        ):
            from hexawyn.mcp.tools.check_machine_config_pool_status import (
                check_machine_config_pool_status,
            )

            result = check_machine_config_pool_status()

        assert result["all_healthy"] is False
        assert result["total"] == 0
        assert "OpenShift" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.check_machine_config_pool_status import register

        assert callable(register)
