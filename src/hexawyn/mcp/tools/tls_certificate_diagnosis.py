"""MCP tool: tls_certificate_diagnosis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command import (  # type: ignore
    TlsCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.tls_certificate_diagnosis_use_case import (  # noqa: E501
    TLSCertificateDiagnosisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def tls_certificate_diagnosis(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(TlsCertificateDiagnosisCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(tls_certificate_diagnosis)
