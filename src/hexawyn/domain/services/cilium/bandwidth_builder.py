"""Pure Cilium bandwidth-manager audit — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumBandwidthAuditResult,
    CiliumBandwidthEntry,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_NOT_AVAILABLE_NOTE = "Cilium bandwidth manager is disabled (no bandwidth annotations found)"

_NEAR_LIMIT_THRESHOLD = 0.9


def build_bandwidth_entry(  # noqa: PLR0913
    namespace: str,
    pod: str,
    ingress_limit: str | None,
    egress_limit: str | None,
    usage_ratio: float | None,
    throttled: bool,
) -> CiliumBandwidthEntry:
    """Build one per-pod bandwidth entry with an observed state."""
    return CiliumBandwidthEntry(
        namespace=namespace,
        pod=pod,
        ingress_limit=ingress_limit,
        egress_limit=egress_limit,
        usage_ratio=usage_ratio,
        state=classify_bandwidth(usage_ratio, throttled),
        note=_note_for(usage_ratio, throttled),
    )


def classify_bandwidth(usage_ratio: float | None, throttled: bool) -> str:
    """Classify a pod's bandwidth state from observed inputs."""
    if throttled:
        return "throttled"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return "near_limit"
    if usage_ratio is not None:
        return "ok"
    return "UNKNOWN"


def build_bandwidth_audit(entries: list[CiliumBandwidthEntry]) -> CiliumBandwidthAuditResult:
    """Wrap the entries with an overall status, anomalies first."""
    anomalies = [entry for entry in entries if entry.state in ("throttled", "near_limit")]
    ordered = [*anomalies, *[entry for entry in entries if entry not in anomalies]]
    return CiliumBandwidthAuditResult(
        installed=True,
        status="anomalies" if anomalies else "ok",
        total_pods=len(entries),
        entries=ordered,
        note=None,
    )


def not_installed_bandwidth_audit() -> CiliumBandwidthAuditResult:
    """Honest NOT_INSTALLED marker — no fabricated bandwidth data."""
    return CiliumBandwidthAuditResult(
        installed=False,
        status="not_installed",
        total_pods=0,
        entries=[],
        note=_NOT_INSTALLED_NOTE,
    )


def not_available_bandwidth_audit() -> CiliumBandwidthAuditResult:
    """Bandwidth manager enabled on Cilium but no bandwidth annotations found."""
    return CiliumBandwidthAuditResult(
        installed=True,
        status="not_available",
        total_pods=0,
        entries=[],
        note=_NOT_AVAILABLE_NOTE,
    )


def _note_for(usage_ratio: float | None, throttled: bool) -> str | None:
    if throttled:
        return "Pod is being throttled by the Cilium bandwidth manager"
    if usage_ratio is not None and usage_ratio >= _NEAR_LIMIT_THRESHOLD:
        return f"Pod at {usage_ratio * 100:.0f}% of its bandwidth limit"
    return None
