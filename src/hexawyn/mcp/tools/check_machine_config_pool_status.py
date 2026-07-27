"""MCP tool: check_machine_config_pool_status — Check MachineConfig pool status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (  # noqa: E501
    CheckMachineConfigPoolStatusUseCase,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.command import (
    CheckMachineConfigPoolStatusCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def check_machine_config_pool_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_machine_config_pool_adapter

    try:
        use_case = CheckMachineConfigPoolStatusUseCase(
            machine_config_pool_port=build_machine_config_pool_adapter()
        )
        response = use_case.execute(CheckMachineConfigPoolStatusCommand())
        pools_list = [
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
            for pool in response.result.pools  # type: ignore
        ]
        return {
            "total": response.result.total,  # type: ignore
            "healthy": response.result.healthy,  # type: ignore
            "degraded": response.result.degraded,  # type: ignore
            "updating": response.result.updating,  # type: ignore
            "paused": response.result.paused,  # type: ignore
            "all_healthy": response.result.all_healthy,  # type: ignore
            "pools": pools_list,
            "error": None,
        }
    except Exception as exc:
        return {
            "total": 0,
            "healthy": 0,
            "degraded": 0,
            "updating": 0,
            "paused": 0,
            "all_healthy": False,
            "pools": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_machine_config_pool_status)
