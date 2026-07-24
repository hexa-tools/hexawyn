"""MCP tool: detect_unintended_external_exposure."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_unintended_external_exposure.command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.detect_unintended_external_exposure_use_case import (
    DetectUnintendedExternalExposureUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_unintended_external_exposure() -> dict[str, object]:
    from hexawyn.mcp.server import build_external_exposure_audit_adapter

    try:
        use_case = DetectUnintendedExternalExposureUseCase(
            port=build_external_exposure_audit_adapter()
        )
        _ = use_case.execute(DetectUnintendedExternalExposureCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_unintended_external_exposure)
