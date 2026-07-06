"""MCP tool: detect_unintended_external_exposure — flags Kubernetes Services
of type LoadBalancer or NodePort that are not in a configurable allowlist,
classifying each by risk level based on port severity, namespace, and IP
restrictions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.detect_unintended_external_exposure_use_case import (
    DetectUnintendedExternalExposureUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_unintended_external_exposure(
    allowlist: list[str] | None = None,
    namespaces: list[str] | None = None,
) -> dict[str, object]:
    from hexawyn.application.service.unintended_external_exposure_service import (
        UnintendedExternalExposureService,
    )
    from hexawyn.mcp.server import build_external_exposure_audit_adapter

    try:
        service = UnintendedExternalExposureService(
            external_exposure_port=build_external_exposure_audit_adapter()
        )
        r = DetectUnintendedExternalExposureUseCase(service=service).execute(
            DetectUnintendedExternalExposureCommand(
                allowlist=allowlist,
                namespaces=namespaces,
            )
        )
        return {
            "findings": r.findings,
            "excluded_exposures": r.excluded_exposures,
            "total_external_services_checked": r.total_external_services_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_unintended_external_exposure)
