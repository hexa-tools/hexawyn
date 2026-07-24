"""MCP tool: certs_status_explain — Explain in natural language why a cert is failing."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.certs_status_explain.certs_status_explain_use_case import (
    CertsStatusExplainUseCase,
)
from hexawyn.application.use_case.certs_status_explain.command import CertsStatusExplainCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


def certs_status_explain(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_status_explain)
