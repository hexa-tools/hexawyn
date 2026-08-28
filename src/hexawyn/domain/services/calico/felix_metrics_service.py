"""Pure Calico Felix metrics aggregation — no infrastructure imports.

Turns the observed Felix per-policy counter samples (allow/deny packets &
bytes) into a truthful per-policy ranking by deny volume. Counters are never
invented: only observed samples are aggregated, and an unreachable metrics
endpoint degrades to an honest ``metrics_available: False`` message.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoFelixMetricsResult,
    CalicoFelixPolicyCounter,
)


def build_calico_felix_metrics_result(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            metrics_available=False,
            metrics_message=None,
            policies=[],
            total_denies=0,
            total_allows=0,
            deny_policy_count=0,
            error=detection.error,
        )

    if not counters.get("available"):
        return CalicoFelixMetricsResult(
            installed=True,
            not_installed_marker=None,
            metrics_available=False,
            metrics_message=str(counters.get("message") or "felix metrics unavailable"),
            policies=[],
            total_denies=0,
            total_allows=0,
            deny_policy_count=0,
            error=detection.error,
        )

    per_policy = _aggregate(counters.get("samples"))
    policies = [
        CalicoFelixPolicyCounter(
            policy=policy,
            allow_packets=_as_int(values, "allow_packets"),
            deny_packets=_as_int(values, "deny_packets"),
            allow_bytes=_as_int(values, "allow_bytes"),
            deny_bytes=_as_int(values, "deny_bytes"),
        )
        for policy, values in per_policy.items()
    ]
    policies.sort(key=lambda counter: (-counter.deny_packets, -counter.allow_packets))

    return CalicoFelixMetricsResult(
        installed=True,
        not_installed_marker=None,
        metrics_available=True,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def _aggregate(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("kind")
        if policy is None or kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def _as_int(values: dict[str, float], kind: str) -> int:
    return int(values.get(kind, 0.0))
