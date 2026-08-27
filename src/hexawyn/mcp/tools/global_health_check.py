"""MCP tool: global_health_check — cluster fleet health overview."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.global_health_check.command import (
    GlobalHealthCheckCommand,
)
from hexawyn.application.use_case.cluster.global_health_check.global_health_check_use_case import (
    GlobalHealthCheckUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def global_health_check(  # noqa: PLR0913
    max_clusters: int = 0,
    page: int = 1,
    page_size: int = 0,
    max_workers: int = 5,
    timeout_seconds: float = 8.0,
    previous_fleet_score: float | None = None,
) -> dict[str, object]:
    """Return a global health overview for all clusters in the kubeconfig.

    Scans the kubeconfig contexts in parallel (up to ``max_workers``).
    Unreachable clusters are marked as such and excluded from the aggregate
    fleet score. ``max_clusters`` (0 = unlimited) and ``page``/``page_size``
    (0 = no pagination) let you scan hundreds of contexts in batches so each
    call stays within ``timeout_seconds``.

    Args:
        max_clusters: Max kubeconfig contexts to check. 0 = all (default).
        page: Page number (1-based) when ``page_size > 0``.
        page_size: Contexts per page. 0 = no pagination (default).
        max_workers: Parallel workers for the fleet scan.
        timeout_seconds: Per-fleet timeout in seconds (default: 8.0).
        previous_fleet_score: Previous fleet score for trend computation (optional).
    """
    from hexawyn.mcp.server import build_fleet_health_adapter

    try:
        adapter = build_fleet_health_adapter()
        use_case = GlobalHealthCheckUseCase(port=adapter)
        response = use_case.execute(
            GlobalHealthCheckCommand(
                max_clusters=max_clusters,
                page=page,
                page_size=page_size,
                max_workers=max_workers,
                timeout_seconds=timeout_seconds,
                previous_fleet_score=previous_fleet_score,
            )
        )
        report = response.report

        clusters = []
        for cr in report.cluster_reports:
            entry: dict[str, object] = {
                "context_name": cr.context_name,
                "reachable": cr.reachable,
                "unreachable_reason": cr.unreachable_reason,
                "health_score": cr.health_score,
                "health_status": cr.health_status,
                "categories": {
                    cat: {
                        "status": c.status,
                        "key_metric": c.key_metric,
                        "top_issue": c.top_issue,
                    }
                    for cat, c in cr.categories.items()
                },
                "checked_at": cr.checked_at.isoformat(),
            }
            clusters.append(entry)

        return {
            "clusters": clusters,
            "fleet_score": report.fleet_score,
            "fleet_status": report.fleet_status,
            "reachable_count": report.reachable_count,
            "unreachable_count": report.unreachable_count,
            "fleet_score_trend": response.fleet_score_trend,
            "total_contexts": response.total_contexts,
            "page": response.page,
            "page_size": response.page_size,
            "has_more": response.has_more,
            "checked_at": report.checked_at.isoformat(),
            "error": None,
        }
    except Exception as exc:
        return {
            "clusters": [],
            "fleet_score": None,
            "fleet_status": "error",
            "reachable_count": 0,
            "unreachable_count": 0,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(global_health_check)
