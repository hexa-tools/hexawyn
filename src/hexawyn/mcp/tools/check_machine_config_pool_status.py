"""MCP tool: check_machine_config_pool_status — OpenShift MachineConfigPool health."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (  # noqa: E501
    CheckMachineConfigPoolStatusUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def check_machine_config_pool_status() -> dict[str, object]:
    """Report the status of all OpenShift MachineConfigPools.

    Lists every MachineConfigPool with its derived state (ready, updating,
    degraded, degraded+updating, paused), the machine counts, the current vs
    desired MachineConfig, the degraded machine count and reason, flags pools
    stuck updating for more than 30 minutes, and returns a summary (total,
    healthy, degraded, updating, paused).
    """
    from hexawyn.application.service.check_machine_config_pool_status_service import (
        CheckMachineConfigPoolStatusService,
    )
    from hexawyn.mcp.server import build_machine_config_pool_adapter

    try:
        adapter = build_machine_config_pool_adapter()
        service = CheckMachineConfigPoolStatusService(machine_config_pool_port=adapter)
        use_case = CheckMachineConfigPoolStatusUseCase(service=service)
        response = use_case.execute(CheckMachineConfigPoolStatusCommand())
        report = response.result
        return {
            "all_healthy": report.all_healthy,
            "total": report.total,
            "healthy": report.healthy,
            "degraded": report.degraded,
            "updating": report.updating,
            "paused": report.paused,
            "pools": [
                {
                    "name": pool.name,
                    "state": pool.state,
                    "machine_count": pool.machine_count,
                    "ready_machine_count": pool.ready_machine_count,
                    "updated_machine_count": pool.updated_machine_count,
                    "degraded_machine_count": pool.degraded_machine_count,
                    "current_config": pool.current_config,
                    "desired_config": pool.desired_config,
                    "config_mismatch": pool.config_mismatch,
                    "paused": pool.paused,
                    "reason": pool.reason,
                    "updating_duration_minutes": pool.updating_duration_minutes,
                    "is_stuck": pool.is_stuck,
                }
                for pool in report.pools
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "all_healthy": False,
            "total": 0,
            "healthy": 0,
            "degraded": 0,
            "updating": 0,
            "paused": 0,
            "pools": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_machine_config_pool_status)
