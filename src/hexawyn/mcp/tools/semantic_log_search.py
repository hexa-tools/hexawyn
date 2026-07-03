"""MCP tool: semantic_log_search — search pod logs by pattern across all namespaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.use_case.semantic_log_search.semantic_log_search_use_case import (
    SemanticLogSearchUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def semantic_log_search(
    pattern: str,
    is_regex: bool = False,
    namespace: str | None = None,
    time_window_minutes: int = 60,
) -> dict[str, object]:
    from hexawyn.application.service.semantic_log_search_service import (
        SemanticLogSearchService,
    )
    from hexawyn.mcp.server import build_k8s_adapter, build_log_search_adapter

    try:
        service = SemanticLogSearchService(
            port=build_log_search_adapter(), k8s_port=build_k8s_adapter()
        )
        r = SemanticLogSearchUseCase(service=service).execute(
            SemanticLogSearchCommand(
                pattern=pattern,
                is_regex=is_regex,
                namespace=namespace,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "pattern": r.pattern,
            "time_window_minutes": r.time_window_minutes,
            "groups": r.groups,
            "pods_affected": r.pods_affected,
            "services_affected": r.services_affected,
            "skipped_pods": r.skipped_pods,
            "skipped_namespaces": r.skipped_namespaces,
            "scanned_namespaces": r.scanned_namespaces,
            "namespaces_total": r.namespaces_total,
            "no_matches": r.no_matches,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(semantic_log_search)
