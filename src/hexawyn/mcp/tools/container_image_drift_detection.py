"""MCP tool: container_image_drift_detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
    DetectContainerImageDriftUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_container_image_drift(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_container_image_drift)
