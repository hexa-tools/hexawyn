"""MCP tool: check_machine_config_pool_status — Check MachineConfig pool status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (
    CheckMachineConfigPoolStatusUseCase,
)
from hexawyn.application.use_case.check_machine_config_pool_status.command import (
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
        _ = use_case.execute(CheckMachineConfigPoolStatusCommand())
        return {"pools": [], "error": None}
    except Exception as exc:
        return {"pools": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_machine_config_pool_status)
