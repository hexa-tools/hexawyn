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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_global_health_check__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_global_health_check__mutmut)
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


def x_global_health_check__mutmut_orig(  # noqa: PLR0913
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


def x_global_health_check__mutmut_1(  # noqa: PLR0913
    max_clusters: int = 1,
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


def x_global_health_check__mutmut_2(  # noqa: PLR0913
    max_clusters: int = 0,
    page: int = 2,
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


def x_global_health_check__mutmut_3(  # noqa: PLR0913
    max_clusters: int = 0,
    page: int = 1,
    page_size: int = 1,
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


def x_global_health_check__mutmut_4(  # noqa: PLR0913
    max_clusters: int = 0,
    page: int = 1,
    page_size: int = 0,
    max_workers: int = 6,
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


def x_global_health_check__mutmut_5(  # noqa: PLR0913
    max_clusters: int = 0,
    page: int = 1,
    page_size: int = 0,
    max_workers: int = 5,
    timeout_seconds: float = 9.0,
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


def x_global_health_check__mutmut_6(  # noqa: PLR0913
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
        adapter = None
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


def x_global_health_check__mutmut_7(  # noqa: PLR0913
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
        use_case = None
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


def x_global_health_check__mutmut_8(  # noqa: PLR0913
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
        use_case = GlobalHealthCheckUseCase(port=None)
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


def x_global_health_check__mutmut_9(  # noqa: PLR0913
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
        response = None
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


def x_global_health_check__mutmut_10(  # noqa: PLR0913
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
            None
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


def x_global_health_check__mutmut_11(  # noqa: PLR0913
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
                max_clusters=None,
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


def x_global_health_check__mutmut_12(  # noqa: PLR0913
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
                page=None,
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


def x_global_health_check__mutmut_13(  # noqa: PLR0913
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
                page_size=None,
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


def x_global_health_check__mutmut_14(  # noqa: PLR0913
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
                max_workers=None,
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


def x_global_health_check__mutmut_15(  # noqa: PLR0913
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
                timeout_seconds=None,
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


def x_global_health_check__mutmut_16(  # noqa: PLR0913
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
                previous_fleet_score=None,
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


def x_global_health_check__mutmut_17(  # noqa: PLR0913
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


def x_global_health_check__mutmut_18(  # noqa: PLR0913
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


def x_global_health_check__mutmut_19(  # noqa: PLR0913
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


def x_global_health_check__mutmut_20(  # noqa: PLR0913
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


def x_global_health_check__mutmut_21(  # noqa: PLR0913
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


def x_global_health_check__mutmut_22(  # noqa: PLR0913
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


def x_global_health_check__mutmut_23(  # noqa: PLR0913
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
        report = None

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


def x_global_health_check__mutmut_24(  # noqa: PLR0913
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

        clusters = None
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


def x_global_health_check__mutmut_25(  # noqa: PLR0913
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
            entry: dict[str, object] = None
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


def x_global_health_check__mutmut_26(  # noqa: PLR0913
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
                "XXcontext_nameXX": cr.context_name,
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


def x_global_health_check__mutmut_27(  # noqa: PLR0913
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
                "CONTEXT_NAME": cr.context_name,
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


def x_global_health_check__mutmut_28(  # noqa: PLR0913
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
                "XXreachableXX": cr.reachable,
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


def x_global_health_check__mutmut_29(  # noqa: PLR0913
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
                "REACHABLE": cr.reachable,
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


def x_global_health_check__mutmut_30(  # noqa: PLR0913
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
                "XXunreachable_reasonXX": cr.unreachable_reason,
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


def x_global_health_check__mutmut_31(  # noqa: PLR0913
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
                "UNREACHABLE_REASON": cr.unreachable_reason,
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


def x_global_health_check__mutmut_32(  # noqa: PLR0913
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
                "XXhealth_scoreXX": cr.health_score,
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


def x_global_health_check__mutmut_33(  # noqa: PLR0913
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
                "HEALTH_SCORE": cr.health_score,
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


def x_global_health_check__mutmut_34(  # noqa: PLR0913
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
                "XXhealth_statusXX": cr.health_status,
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


def x_global_health_check__mutmut_35(  # noqa: PLR0913
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
                "HEALTH_STATUS": cr.health_status,
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


def x_global_health_check__mutmut_36(  # noqa: PLR0913
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
                "XXcategoriesXX": {
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


def x_global_health_check__mutmut_37(  # noqa: PLR0913
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
                "CATEGORIES": {
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


def x_global_health_check__mutmut_38(  # noqa: PLR0913
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
                        "XXstatusXX": c.status,
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


def x_global_health_check__mutmut_39(  # noqa: PLR0913
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
                        "STATUS": c.status,
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


def x_global_health_check__mutmut_40(  # noqa: PLR0913
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
                        "XXkey_metricXX": c.key_metric,
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


def x_global_health_check__mutmut_41(  # noqa: PLR0913
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
                        "KEY_METRIC": c.key_metric,
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


def x_global_health_check__mutmut_42(  # noqa: PLR0913
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
                        "XXtop_issueXX": c.top_issue,
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


def x_global_health_check__mutmut_43(  # noqa: PLR0913
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
                        "TOP_ISSUE": c.top_issue,
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


def x_global_health_check__mutmut_44(  # noqa: PLR0913
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
                "XXchecked_atXX": cr.checked_at.isoformat(),
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


def x_global_health_check__mutmut_45(  # noqa: PLR0913
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
                "CHECKED_AT": cr.checked_at.isoformat(),
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


def x_global_health_check__mutmut_46(  # noqa: PLR0913
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
            clusters.append(None)

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


def x_global_health_check__mutmut_47(  # noqa: PLR0913
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
            "XXclustersXX": clusters,
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


def x_global_health_check__mutmut_48(  # noqa: PLR0913
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
            "CLUSTERS": clusters,
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


def x_global_health_check__mutmut_49(  # noqa: PLR0913
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
            "XXfleet_scoreXX": report.fleet_score,
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


def x_global_health_check__mutmut_50(  # noqa: PLR0913
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
            "FLEET_SCORE": report.fleet_score,
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


def x_global_health_check__mutmut_51(  # noqa: PLR0913
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
            "XXfleet_statusXX": report.fleet_status,
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


def x_global_health_check__mutmut_52(  # noqa: PLR0913
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
            "FLEET_STATUS": report.fleet_status,
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


def x_global_health_check__mutmut_53(  # noqa: PLR0913
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
            "XXreachable_countXX": report.reachable_count,
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


def x_global_health_check__mutmut_54(  # noqa: PLR0913
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
            "REACHABLE_COUNT": report.reachable_count,
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


def x_global_health_check__mutmut_55(  # noqa: PLR0913
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
            "XXunreachable_countXX": report.unreachable_count,
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


def x_global_health_check__mutmut_56(  # noqa: PLR0913
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
            "UNREACHABLE_COUNT": report.unreachable_count,
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


def x_global_health_check__mutmut_57(  # noqa: PLR0913
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
            "XXfleet_score_trendXX": response.fleet_score_trend,
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


def x_global_health_check__mutmut_58(  # noqa: PLR0913
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
            "FLEET_SCORE_TREND": response.fleet_score_trend,
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


def x_global_health_check__mutmut_59(  # noqa: PLR0913
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
            "XXtotal_contextsXX": response.total_contexts,
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


def x_global_health_check__mutmut_60(  # noqa: PLR0913
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
            "TOTAL_CONTEXTS": response.total_contexts,
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


def x_global_health_check__mutmut_61(  # noqa: PLR0913
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
            "XXpageXX": response.page,
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


def x_global_health_check__mutmut_62(  # noqa: PLR0913
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
            "PAGE": response.page,
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


def x_global_health_check__mutmut_63(  # noqa: PLR0913
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
            "XXpage_sizeXX": response.page_size,
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


def x_global_health_check__mutmut_64(  # noqa: PLR0913
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
            "PAGE_SIZE": response.page_size,
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


def x_global_health_check__mutmut_65(  # noqa: PLR0913
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
            "XXhas_moreXX": response.has_more,
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


def x_global_health_check__mutmut_66(  # noqa: PLR0913
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
            "HAS_MORE": response.has_more,
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


def x_global_health_check__mutmut_67(  # noqa: PLR0913
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
            "XXchecked_atXX": report.checked_at.isoformat(),
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


def x_global_health_check__mutmut_68(  # noqa: PLR0913
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
            "CHECKED_AT": report.checked_at.isoformat(),
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


def x_global_health_check__mutmut_69(  # noqa: PLR0913
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
            "XXerrorXX": None,
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


def x_global_health_check__mutmut_70(  # noqa: PLR0913
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
            "ERROR": None,
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


def x_global_health_check__mutmut_71(  # noqa: PLR0913
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
            "XXclustersXX": [],
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


def x_global_health_check__mutmut_72(  # noqa: PLR0913
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
            "CLUSTERS": [],
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


def x_global_health_check__mutmut_73(  # noqa: PLR0913
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
            "XXfleet_scoreXX": None,
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


def x_global_health_check__mutmut_74(  # noqa: PLR0913
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
            "FLEET_SCORE": None,
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


def x_global_health_check__mutmut_75(  # noqa: PLR0913
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
            "XXfleet_statusXX": "error",
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


def x_global_health_check__mutmut_76(  # noqa: PLR0913
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
            "FLEET_STATUS": "error",
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


def x_global_health_check__mutmut_77(  # noqa: PLR0913
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
            "fleet_status": "XXerrorXX",
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


def x_global_health_check__mutmut_78(  # noqa: PLR0913
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
            "fleet_status": "ERROR",
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


def x_global_health_check__mutmut_79(  # noqa: PLR0913
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
            "XXreachable_countXX": 0,
            "unreachable_count": 0,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_80(  # noqa: PLR0913
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
            "REACHABLE_COUNT": 0,
            "unreachable_count": 0,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_81(  # noqa: PLR0913
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
            "reachable_count": 1,
            "unreachable_count": 0,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_82(  # noqa: PLR0913
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
            "XXunreachable_countXX": 0,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_83(  # noqa: PLR0913
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
            "UNREACHABLE_COUNT": 0,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_84(  # noqa: PLR0913
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
            "unreachable_count": 1,
            "fleet_score_trend": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_85(  # noqa: PLR0913
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
            "XXfleet_score_trendXX": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_86(  # noqa: PLR0913
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
            "FLEET_SCORE_TREND": None,
            "total_contexts": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_87(  # noqa: PLR0913
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
            "XXtotal_contextsXX": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_88(  # noqa: PLR0913
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
            "TOTAL_CONTEXTS": 0,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_89(  # noqa: PLR0913
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
            "total_contexts": 1,
            "page": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_90(  # noqa: PLR0913
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
            "XXpageXX": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_91(  # noqa: PLR0913
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
            "PAGE": page,
            "page_size": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_92(  # noqa: PLR0913
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
            "XXpage_sizeXX": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_93(  # noqa: PLR0913
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
            "PAGE_SIZE": page_size,
            "has_more": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_94(  # noqa: PLR0913
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
            "XXhas_moreXX": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_95(  # noqa: PLR0913
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
            "HAS_MORE": False,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_96(  # noqa: PLR0913
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
            "has_more": True,
            "checked_at": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_97(  # noqa: PLR0913
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
            "XXchecked_atXX": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_98(  # noqa: PLR0913
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
            "CHECKED_AT": None,
            "error": str(exc),
        }


def x_global_health_check__mutmut_99(  # noqa: PLR0913
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
            "XXerrorXX": str(exc),
        }


def x_global_health_check__mutmut_100(  # noqa: PLR0913
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
            "ERROR": str(exc),
        }


def x_global_health_check__mutmut_101(  # noqa: PLR0913
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
            "error": str(None),
        }

mutants_x_global_health_check__mutmut['_mutmut_orig'] = x_global_health_check__mutmut_orig # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_1'] = x_global_health_check__mutmut_1 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_2'] = x_global_health_check__mutmut_2 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_3'] = x_global_health_check__mutmut_3 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_4'] = x_global_health_check__mutmut_4 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_5'] = x_global_health_check__mutmut_5 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_6'] = x_global_health_check__mutmut_6 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_7'] = x_global_health_check__mutmut_7 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_8'] = x_global_health_check__mutmut_8 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_9'] = x_global_health_check__mutmut_9 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_10'] = x_global_health_check__mutmut_10 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_11'] = x_global_health_check__mutmut_11 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_12'] = x_global_health_check__mutmut_12 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_13'] = x_global_health_check__mutmut_13 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_14'] = x_global_health_check__mutmut_14 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_15'] = x_global_health_check__mutmut_15 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_16'] = x_global_health_check__mutmut_16 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_17'] = x_global_health_check__mutmut_17 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_18'] = x_global_health_check__mutmut_18 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_19'] = x_global_health_check__mutmut_19 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_20'] = x_global_health_check__mutmut_20 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_21'] = x_global_health_check__mutmut_21 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_22'] = x_global_health_check__mutmut_22 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_23'] = x_global_health_check__mutmut_23 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_24'] = x_global_health_check__mutmut_24 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_25'] = x_global_health_check__mutmut_25 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_26'] = x_global_health_check__mutmut_26 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_27'] = x_global_health_check__mutmut_27 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_28'] = x_global_health_check__mutmut_28 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_29'] = x_global_health_check__mutmut_29 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_30'] = x_global_health_check__mutmut_30 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_31'] = x_global_health_check__mutmut_31 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_32'] = x_global_health_check__mutmut_32 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_33'] = x_global_health_check__mutmut_33 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_34'] = x_global_health_check__mutmut_34 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_35'] = x_global_health_check__mutmut_35 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_36'] = x_global_health_check__mutmut_36 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_37'] = x_global_health_check__mutmut_37 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_38'] = x_global_health_check__mutmut_38 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_39'] = x_global_health_check__mutmut_39 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_40'] = x_global_health_check__mutmut_40 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_41'] = x_global_health_check__mutmut_41 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_42'] = x_global_health_check__mutmut_42 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_43'] = x_global_health_check__mutmut_43 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_44'] = x_global_health_check__mutmut_44 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_45'] = x_global_health_check__mutmut_45 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_46'] = x_global_health_check__mutmut_46 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_47'] = x_global_health_check__mutmut_47 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_48'] = x_global_health_check__mutmut_48 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_49'] = x_global_health_check__mutmut_49 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_50'] = x_global_health_check__mutmut_50 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_51'] = x_global_health_check__mutmut_51 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_52'] = x_global_health_check__mutmut_52 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_53'] = x_global_health_check__mutmut_53 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_54'] = x_global_health_check__mutmut_54 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_55'] = x_global_health_check__mutmut_55 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_56'] = x_global_health_check__mutmut_56 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_57'] = x_global_health_check__mutmut_57 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_58'] = x_global_health_check__mutmut_58 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_59'] = x_global_health_check__mutmut_59 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_60'] = x_global_health_check__mutmut_60 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_61'] = x_global_health_check__mutmut_61 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_62'] = x_global_health_check__mutmut_62 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_63'] = x_global_health_check__mutmut_63 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_64'] = x_global_health_check__mutmut_64 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_65'] = x_global_health_check__mutmut_65 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_66'] = x_global_health_check__mutmut_66 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_67'] = x_global_health_check__mutmut_67 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_68'] = x_global_health_check__mutmut_68 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_69'] = x_global_health_check__mutmut_69 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_70'] = x_global_health_check__mutmut_70 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_71'] = x_global_health_check__mutmut_71 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_72'] = x_global_health_check__mutmut_72 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_73'] = x_global_health_check__mutmut_73 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_74'] = x_global_health_check__mutmut_74 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_75'] = x_global_health_check__mutmut_75 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_76'] = x_global_health_check__mutmut_76 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_77'] = x_global_health_check__mutmut_77 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_78'] = x_global_health_check__mutmut_78 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_79'] = x_global_health_check__mutmut_79 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_80'] = x_global_health_check__mutmut_80 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_81'] = x_global_health_check__mutmut_81 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_82'] = x_global_health_check__mutmut_82 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_83'] = x_global_health_check__mutmut_83 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_84'] = x_global_health_check__mutmut_84 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_85'] = x_global_health_check__mutmut_85 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_86'] = x_global_health_check__mutmut_86 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_87'] = x_global_health_check__mutmut_87 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_88'] = x_global_health_check__mutmut_88 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_89'] = x_global_health_check__mutmut_89 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_90'] = x_global_health_check__mutmut_90 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_91'] = x_global_health_check__mutmut_91 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_92'] = x_global_health_check__mutmut_92 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_93'] = x_global_health_check__mutmut_93 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_94'] = x_global_health_check__mutmut_94 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_95'] = x_global_health_check__mutmut_95 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_96'] = x_global_health_check__mutmut_96 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_97'] = x_global_health_check__mutmut_97 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_98'] = x_global_health_check__mutmut_98 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_99'] = x_global_health_check__mutmut_99 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_100'] = x_global_health_check__mutmut_100 # type: ignore # mutmut generated
mutants_x_global_health_check__mutmut['x_global_health_check__mutmut_101'] = x_global_health_check__mutmut_101 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(global_health_check)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(global_health_check)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
