"""MCP tool: tls_certificate_diagnosis — Diagnose TLS certificate issues on ingress."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.tls_certificate_diagnosis.tls_certificate_diagnosis_use_case import (
    TLSCertificateDiagnosisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def tls_certificate_diagnosis(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.application.service.tls_certificate_diagnosis_service import (
        TLSCertificateDiagnosisService,
    )
    from hexawyn.mcp.server import build_certificate_investigation_adapter

    try:
        a = build_certificate_investigation_adapter()
        r = TLSCertificateDiagnosisUseCase(service=TLSCertificateDiagnosisService(port=a)).execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {
            "ingress_name": r.ingress_name,
            "namespace": r.namespace,
            "status": r.status,
            "diagnosis": r.diagnosis,
            "expiry_date": r.expiry_date,
            "days_remaining": r.days_remaining,
            "cipher_info": r.cipher_info,
            "san_list": r.san_list,
            "error": r.error,
        }
    except Exception as exc:
        return {"ingress_name": ingress_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(tls_certificate_diagnosis)
