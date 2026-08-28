"""Pure Calico status composition — no infrastructure imports.

Turns the detection snapshot plus the (best-effort) felix metrics and
connectivity probe into a truthful ``CalicoStatusResult``. Degradation is never
hidden: agent shortfall, felix errors or a degraded connectivity probe all raise
the overall status to DEGRADED.
"""

from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoStatusResult,
)


def build_calico_status_result(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def _felix_error_total(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def _connectivity_status(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def _compose_degraded_summary(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)
