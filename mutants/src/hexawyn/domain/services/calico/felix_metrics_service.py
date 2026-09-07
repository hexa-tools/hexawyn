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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_felix_metrics_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_felix_metrics_result__mutmut)
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


def x_build_calico_felix_metrics_result__mutmut_orig(
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


def x_build_calico_felix_metrics_result__mutmut_1(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if detection.installed:
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


def x_build_calico_felix_metrics_result__mutmut_2(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=None,
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


def x_build_calico_felix_metrics_result__mutmut_3(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=False,
            not_installed_marker=None,
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


def x_build_calico_felix_metrics_result__mutmut_4(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            metrics_available=None,
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


def x_build_calico_felix_metrics_result__mutmut_5(
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
            policies=None,
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


def x_build_calico_felix_metrics_result__mutmut_6(
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
            total_denies=None,
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


def x_build_calico_felix_metrics_result__mutmut_7(
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
            total_allows=None,
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


def x_build_calico_felix_metrics_result__mutmut_8(
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
            deny_policy_count=None,
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


def x_build_calico_felix_metrics_result__mutmut_9(
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
            error=None,
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


def x_build_calico_felix_metrics_result__mutmut_10(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
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


def x_build_calico_felix_metrics_result__mutmut_11(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=False,
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


def x_build_calico_felix_metrics_result__mutmut_12(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
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


def x_build_calico_felix_metrics_result__mutmut_13(
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


def x_build_calico_felix_metrics_result__mutmut_14(
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


def x_build_calico_felix_metrics_result__mutmut_15(
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


def x_build_calico_felix_metrics_result__mutmut_16(
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


def x_build_calico_felix_metrics_result__mutmut_17(
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


def x_build_calico_felix_metrics_result__mutmut_18(
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


def x_build_calico_felix_metrics_result__mutmut_19(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=True,
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


def x_build_calico_felix_metrics_result__mutmut_20(
    *,
    detection: CalicoDetectionResult,
    counters: Mapping[str, object],
) -> CalicoFelixMetricsResult:
    """Aggregate Felix per-policy counters and rank by deny volume."""
    if not detection.installed:
        return CalicoFelixMetricsResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            metrics_available=True,
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


def x_build_calico_felix_metrics_result__mutmut_21(
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
            total_denies=1,
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


def x_build_calico_felix_metrics_result__mutmut_22(
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
            total_allows=1,
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


def x_build_calico_felix_metrics_result__mutmut_23(
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
            deny_policy_count=1,
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


def x_build_calico_felix_metrics_result__mutmut_24(
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

    if counters.get("available"):
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


def x_build_calico_felix_metrics_result__mutmut_25(
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

    if not counters.get(None):
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


def x_build_calico_felix_metrics_result__mutmut_26(
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

    if not counters.get("XXavailableXX"):
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


def x_build_calico_felix_metrics_result__mutmut_27(
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

    if not counters.get("AVAILABLE"):
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


def x_build_calico_felix_metrics_result__mutmut_28(
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
            installed=None,
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


def x_build_calico_felix_metrics_result__mutmut_29(
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
            metrics_available=None,
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


def x_build_calico_felix_metrics_result__mutmut_30(
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
            metrics_message=None,
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


def x_build_calico_felix_metrics_result__mutmut_31(
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
            policies=None,
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


def x_build_calico_felix_metrics_result__mutmut_32(
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
            total_denies=None,
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


def x_build_calico_felix_metrics_result__mutmut_33(
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
            total_allows=None,
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


def x_build_calico_felix_metrics_result__mutmut_34(
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
            deny_policy_count=None,
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


def x_build_calico_felix_metrics_result__mutmut_35(
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
            error=None,
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


def x_build_calico_felix_metrics_result__mutmut_36(
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


def x_build_calico_felix_metrics_result__mutmut_37(
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


def x_build_calico_felix_metrics_result__mutmut_38(
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


def x_build_calico_felix_metrics_result__mutmut_39(
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


def x_build_calico_felix_metrics_result__mutmut_40(
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


def x_build_calico_felix_metrics_result__mutmut_41(
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


def x_build_calico_felix_metrics_result__mutmut_42(
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


def x_build_calico_felix_metrics_result__mutmut_43(
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


def x_build_calico_felix_metrics_result__mutmut_44(
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


def x_build_calico_felix_metrics_result__mutmut_45(
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
            installed=False,
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


def x_build_calico_felix_metrics_result__mutmut_46(
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
            metrics_available=True,
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


def x_build_calico_felix_metrics_result__mutmut_47(
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
            metrics_message=str(None),
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


def x_build_calico_felix_metrics_result__mutmut_48(
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
            metrics_message=str(counters.get("message") and "felix metrics unavailable"),
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


def x_build_calico_felix_metrics_result__mutmut_49(
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
            metrics_message=str(counters.get(None) or "felix metrics unavailable"),
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


def x_build_calico_felix_metrics_result__mutmut_50(
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
            metrics_message=str(counters.get("XXmessageXX") or "felix metrics unavailable"),
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


def x_build_calico_felix_metrics_result__mutmut_51(
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
            metrics_message=str(counters.get("MESSAGE") or "felix metrics unavailable"),
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


def x_build_calico_felix_metrics_result__mutmut_52(
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
            metrics_message=str(counters.get("message") or "XXfelix metrics unavailableXX"),
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


def x_build_calico_felix_metrics_result__mutmut_53(
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
            metrics_message=str(counters.get("message") or "FELIX METRICS UNAVAILABLE"),
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


def x_build_calico_felix_metrics_result__mutmut_54(
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
            total_denies=1,
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


def x_build_calico_felix_metrics_result__mutmut_55(
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
            total_allows=1,
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


def x_build_calico_felix_metrics_result__mutmut_56(
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
            deny_policy_count=1,
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


def x_build_calico_felix_metrics_result__mutmut_57(
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

    per_policy = None
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


def x_build_calico_felix_metrics_result__mutmut_58(
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

    per_policy = _aggregate(None)
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


def x_build_calico_felix_metrics_result__mutmut_59(
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

    per_policy = _aggregate(counters.get(None))
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


def x_build_calico_felix_metrics_result__mutmut_60(
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

    per_policy = _aggregate(counters.get("XXsamplesXX"))
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


def x_build_calico_felix_metrics_result__mutmut_61(
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

    per_policy = _aggregate(counters.get("SAMPLES"))
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


def x_build_calico_felix_metrics_result__mutmut_62(
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
    policies = None
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


def x_build_calico_felix_metrics_result__mutmut_63(
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
            policy=None,
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


def x_build_calico_felix_metrics_result__mutmut_64(
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
            allow_packets=None,
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


def x_build_calico_felix_metrics_result__mutmut_65(
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
            deny_packets=None,
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


def x_build_calico_felix_metrics_result__mutmut_66(
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
            allow_bytes=None,
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


def x_build_calico_felix_metrics_result__mutmut_67(
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
            deny_bytes=None,
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


def x_build_calico_felix_metrics_result__mutmut_68(
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


def x_build_calico_felix_metrics_result__mutmut_69(
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


def x_build_calico_felix_metrics_result__mutmut_70(
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


def x_build_calico_felix_metrics_result__mutmut_71(
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


def x_build_calico_felix_metrics_result__mutmut_72(
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


def x_build_calico_felix_metrics_result__mutmut_73(
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
            allow_packets=_as_int(None, "allow_packets"),
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


def x_build_calico_felix_metrics_result__mutmut_74(
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
            allow_packets=_as_int(values, None),
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


def x_build_calico_felix_metrics_result__mutmut_75(
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
            allow_packets=_as_int("allow_packets"),
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


def x_build_calico_felix_metrics_result__mutmut_76(
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
            allow_packets=_as_int(values, ),
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


def x_build_calico_felix_metrics_result__mutmut_77(
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
            allow_packets=_as_int(values, "XXallow_packetsXX"),
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


def x_build_calico_felix_metrics_result__mutmut_78(
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
            allow_packets=_as_int(values, "ALLOW_PACKETS"),
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


def x_build_calico_felix_metrics_result__mutmut_79(
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
            deny_packets=_as_int(None, "deny_packets"),
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


def x_build_calico_felix_metrics_result__mutmut_80(
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
            deny_packets=_as_int(values, None),
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


def x_build_calico_felix_metrics_result__mutmut_81(
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
            deny_packets=_as_int("deny_packets"),
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


def x_build_calico_felix_metrics_result__mutmut_82(
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
            deny_packets=_as_int(values, ),
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


def x_build_calico_felix_metrics_result__mutmut_83(
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
            deny_packets=_as_int(values, "XXdeny_packetsXX"),
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


def x_build_calico_felix_metrics_result__mutmut_84(
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
            deny_packets=_as_int(values, "DENY_PACKETS"),
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


def x_build_calico_felix_metrics_result__mutmut_85(
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
            allow_bytes=_as_int(None, "allow_bytes"),
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


def x_build_calico_felix_metrics_result__mutmut_86(
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
            allow_bytes=_as_int(values, None),
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


def x_build_calico_felix_metrics_result__mutmut_87(
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
            allow_bytes=_as_int("allow_bytes"),
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


def x_build_calico_felix_metrics_result__mutmut_88(
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
            allow_bytes=_as_int(values, ),
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


def x_build_calico_felix_metrics_result__mutmut_89(
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
            allow_bytes=_as_int(values, "XXallow_bytesXX"),
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


def x_build_calico_felix_metrics_result__mutmut_90(
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
            allow_bytes=_as_int(values, "ALLOW_BYTES"),
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


def x_build_calico_felix_metrics_result__mutmut_91(
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
            deny_bytes=_as_int(None, "deny_bytes"),
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


def x_build_calico_felix_metrics_result__mutmut_92(
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
            deny_bytes=_as_int(values, None),
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


def x_build_calico_felix_metrics_result__mutmut_93(
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
            deny_bytes=_as_int("deny_bytes"),
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


def x_build_calico_felix_metrics_result__mutmut_94(
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
            deny_bytes=_as_int(values, ),
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


def x_build_calico_felix_metrics_result__mutmut_95(
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
            deny_bytes=_as_int(values, "XXdeny_bytesXX"),
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


def x_build_calico_felix_metrics_result__mutmut_96(
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
            deny_bytes=_as_int(values, "DENY_BYTES"),
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


def x_build_calico_felix_metrics_result__mutmut_97(
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
    policies.sort(key=None)

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


def x_build_calico_felix_metrics_result__mutmut_98(
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
    policies.sort(key=lambda counter: None)

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


def x_build_calico_felix_metrics_result__mutmut_99(
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
    policies.sort(key=lambda counter: (+counter.deny_packets, -counter.allow_packets))

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


def x_build_calico_felix_metrics_result__mutmut_100(
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
    policies.sort(key=lambda counter: (-counter.deny_packets, +counter.allow_packets))

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


def x_build_calico_felix_metrics_result__mutmut_101(
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
        installed=None,
        not_installed_marker=None,
        metrics_available=True,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_102(
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
        metrics_available=None,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_103(
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
        policies=None,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_104(
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
        total_denies=None,
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_105(
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
        total_allows=None,
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_106(
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
        deny_policy_count=None,
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_107(
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
        error=None,
    )


def x_build_calico_felix_metrics_result__mutmut_108(
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
        not_installed_marker=None,
        metrics_available=True,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_109(
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
        metrics_available=True,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_110(
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
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_111(
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
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_112(
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
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_113(
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
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_114(
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
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_115(
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
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_116(
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
        )


def x_build_calico_felix_metrics_result__mutmut_117(
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
        installed=False,
        not_installed_marker=None,
        metrics_available=True,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_118(
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
        metrics_available=False,
        metrics_message=None,
        policies=policies,
        total_denies=sum(counter.deny_packets for counter in policies),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_119(
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
        total_denies=sum(None),
        total_allows=sum(counter.allow_packets for counter in policies),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_120(
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
        total_allows=sum(None),
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_121(
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
        deny_policy_count=sum(None),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_122(
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
        deny_policy_count=sum(2 for counter in policies if counter.deny_packets > 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_123(
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
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets >= 0),
        error=detection.error,
    )


def x_build_calico_felix_metrics_result__mutmut_124(
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
        deny_policy_count=sum(1 for counter in policies if counter.deny_packets > 1),
        error=detection.error,
    )

mutants_x_build_calico_felix_metrics_result__mutmut['_mutmut_orig'] = x_build_calico_felix_metrics_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_1'] = x_build_calico_felix_metrics_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_2'] = x_build_calico_felix_metrics_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_3'] = x_build_calico_felix_metrics_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_4'] = x_build_calico_felix_metrics_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_5'] = x_build_calico_felix_metrics_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_6'] = x_build_calico_felix_metrics_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_7'] = x_build_calico_felix_metrics_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_8'] = x_build_calico_felix_metrics_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_9'] = x_build_calico_felix_metrics_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_10'] = x_build_calico_felix_metrics_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_11'] = x_build_calico_felix_metrics_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_12'] = x_build_calico_felix_metrics_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_13'] = x_build_calico_felix_metrics_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_14'] = x_build_calico_felix_metrics_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_15'] = x_build_calico_felix_metrics_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_16'] = x_build_calico_felix_metrics_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_17'] = x_build_calico_felix_metrics_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_18'] = x_build_calico_felix_metrics_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_19'] = x_build_calico_felix_metrics_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_20'] = x_build_calico_felix_metrics_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_21'] = x_build_calico_felix_metrics_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_22'] = x_build_calico_felix_metrics_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_23'] = x_build_calico_felix_metrics_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_24'] = x_build_calico_felix_metrics_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_25'] = x_build_calico_felix_metrics_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_26'] = x_build_calico_felix_metrics_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_27'] = x_build_calico_felix_metrics_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_28'] = x_build_calico_felix_metrics_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_29'] = x_build_calico_felix_metrics_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_30'] = x_build_calico_felix_metrics_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_31'] = x_build_calico_felix_metrics_result__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_32'] = x_build_calico_felix_metrics_result__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_33'] = x_build_calico_felix_metrics_result__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_34'] = x_build_calico_felix_metrics_result__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_35'] = x_build_calico_felix_metrics_result__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_36'] = x_build_calico_felix_metrics_result__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_37'] = x_build_calico_felix_metrics_result__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_38'] = x_build_calico_felix_metrics_result__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_39'] = x_build_calico_felix_metrics_result__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_40'] = x_build_calico_felix_metrics_result__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_41'] = x_build_calico_felix_metrics_result__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_42'] = x_build_calico_felix_metrics_result__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_43'] = x_build_calico_felix_metrics_result__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_44'] = x_build_calico_felix_metrics_result__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_45'] = x_build_calico_felix_metrics_result__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_46'] = x_build_calico_felix_metrics_result__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_47'] = x_build_calico_felix_metrics_result__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_48'] = x_build_calico_felix_metrics_result__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_49'] = x_build_calico_felix_metrics_result__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_50'] = x_build_calico_felix_metrics_result__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_51'] = x_build_calico_felix_metrics_result__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_52'] = x_build_calico_felix_metrics_result__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_53'] = x_build_calico_felix_metrics_result__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_54'] = x_build_calico_felix_metrics_result__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_55'] = x_build_calico_felix_metrics_result__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_56'] = x_build_calico_felix_metrics_result__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_57'] = x_build_calico_felix_metrics_result__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_58'] = x_build_calico_felix_metrics_result__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_59'] = x_build_calico_felix_metrics_result__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_60'] = x_build_calico_felix_metrics_result__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_61'] = x_build_calico_felix_metrics_result__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_62'] = x_build_calico_felix_metrics_result__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_63'] = x_build_calico_felix_metrics_result__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_64'] = x_build_calico_felix_metrics_result__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_65'] = x_build_calico_felix_metrics_result__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_66'] = x_build_calico_felix_metrics_result__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_67'] = x_build_calico_felix_metrics_result__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_68'] = x_build_calico_felix_metrics_result__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_69'] = x_build_calico_felix_metrics_result__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_70'] = x_build_calico_felix_metrics_result__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_71'] = x_build_calico_felix_metrics_result__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_72'] = x_build_calico_felix_metrics_result__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_73'] = x_build_calico_felix_metrics_result__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_74'] = x_build_calico_felix_metrics_result__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_75'] = x_build_calico_felix_metrics_result__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_76'] = x_build_calico_felix_metrics_result__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_77'] = x_build_calico_felix_metrics_result__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_78'] = x_build_calico_felix_metrics_result__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_79'] = x_build_calico_felix_metrics_result__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_80'] = x_build_calico_felix_metrics_result__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_81'] = x_build_calico_felix_metrics_result__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_82'] = x_build_calico_felix_metrics_result__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_83'] = x_build_calico_felix_metrics_result__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_84'] = x_build_calico_felix_metrics_result__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_85'] = x_build_calico_felix_metrics_result__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_86'] = x_build_calico_felix_metrics_result__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_87'] = x_build_calico_felix_metrics_result__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_88'] = x_build_calico_felix_metrics_result__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_89'] = x_build_calico_felix_metrics_result__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_90'] = x_build_calico_felix_metrics_result__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_91'] = x_build_calico_felix_metrics_result__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_92'] = x_build_calico_felix_metrics_result__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_93'] = x_build_calico_felix_metrics_result__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_94'] = x_build_calico_felix_metrics_result__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_95'] = x_build_calico_felix_metrics_result__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_96'] = x_build_calico_felix_metrics_result__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_97'] = x_build_calico_felix_metrics_result__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_98'] = x_build_calico_felix_metrics_result__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_99'] = x_build_calico_felix_metrics_result__mutmut_99 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_100'] = x_build_calico_felix_metrics_result__mutmut_100 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_101'] = x_build_calico_felix_metrics_result__mutmut_101 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_102'] = x_build_calico_felix_metrics_result__mutmut_102 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_103'] = x_build_calico_felix_metrics_result__mutmut_103 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_104'] = x_build_calico_felix_metrics_result__mutmut_104 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_105'] = x_build_calico_felix_metrics_result__mutmut_105 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_106'] = x_build_calico_felix_metrics_result__mutmut_106 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_107'] = x_build_calico_felix_metrics_result__mutmut_107 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_108'] = x_build_calico_felix_metrics_result__mutmut_108 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_109'] = x_build_calico_felix_metrics_result__mutmut_109 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_110'] = x_build_calico_felix_metrics_result__mutmut_110 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_111'] = x_build_calico_felix_metrics_result__mutmut_111 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_112'] = x_build_calico_felix_metrics_result__mutmut_112 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_113'] = x_build_calico_felix_metrics_result__mutmut_113 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_114'] = x_build_calico_felix_metrics_result__mutmut_114 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_115'] = x_build_calico_felix_metrics_result__mutmut_115 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_116'] = x_build_calico_felix_metrics_result__mutmut_116 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_117'] = x_build_calico_felix_metrics_result__mutmut_117 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_118'] = x_build_calico_felix_metrics_result__mutmut_118 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_119'] = x_build_calico_felix_metrics_result__mutmut_119 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_120'] = x_build_calico_felix_metrics_result__mutmut_120 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_121'] = x_build_calico_felix_metrics_result__mutmut_121 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_122'] = x_build_calico_felix_metrics_result__mutmut_122 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_123'] = x_build_calico_felix_metrics_result__mutmut_123 # type: ignore # mutmut generated
mutants_x_build_calico_felix_metrics_result__mutmut['x_build_calico_felix_metrics_result__mutmut_124'] = x_build_calico_felix_metrics_result__mutmut_124 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__aggregate__mutmut)
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


def x__aggregate__mutmut_orig(raw: object) -> dict[str, dict[str, float]]:
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


def x__aggregate__mutmut_1(raw: object) -> dict[str, dict[str, float]]:
    if isinstance(raw, Sequence):
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


def x__aggregate__mutmut_2(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = None
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


def x__aggregate__mutmut_3(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if isinstance(sample, Mapping):
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


def x__aggregate__mutmut_4(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            break
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


def x__aggregate__mutmut_5(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = None
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


def x__aggregate__mutmut_6(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get(None)
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


def x__aggregate__mutmut_7(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("XXpolicyXX")
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


def x__aggregate__mutmut_8(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("POLICY")
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


def x__aggregate__mutmut_9(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = None
        if policy is None or kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_10(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get(None)
        if policy is None or kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_11(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("XXkindXX")
        if policy is None or kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_12(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("KIND")
        if policy is None or kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_13(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("kind")
        if policy is None and kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_14(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("kind")
        if policy is not None or kind is None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_15(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("kind")
        if policy is None or kind is not None:
            continue
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_16(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, Sequence):
        return {}
    per_policy: dict[str, dict[str, float]] = {}
    for sample in raw:
        if not isinstance(sample, Mapping):
            continue
        policy = sample.get("policy")
        kind = sample.get("kind")
        if policy is None or kind is None:
            break
        try:
            value = float(sample.get("value", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_17(raw: object) -> dict[str, dict[str, float]]:
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
            value = None
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_18(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(None)
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_19(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get(None, 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_20(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get("value", None))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_21(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get(0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_22(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get("value", ))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_23(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get("XXvalueXX", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_24(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get("VALUE", 0.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_25(raw: object) -> dict[str, dict[str, float]]:
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
            value = float(sample.get("value", 1.0))
        except (TypeError, ValueError):
            continue
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_26(raw: object) -> dict[str, dict[str, float]]:
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
            break
        entry = per_policy.setdefault(str(policy), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_27(raw: object) -> dict[str, dict[str, float]]:
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
        entry = None
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_28(raw: object) -> dict[str, dict[str, float]]:
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
        entry = per_policy.setdefault(None, {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_29(raw: object) -> dict[str, dict[str, float]]:
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
        entry = per_policy.setdefault(str(policy), None)
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_30(raw: object) -> dict[str, dict[str, float]]:
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
        entry = per_policy.setdefault({})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_31(raw: object) -> dict[str, dict[str, float]]:
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
        entry = per_policy.setdefault(str(policy), )
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_32(raw: object) -> dict[str, dict[str, float]]:
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
        entry = per_policy.setdefault(str(None), {})
        entry[str(kind)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_33(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = None
    return per_policy


def x__aggregate__mutmut_34(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(None)] = entry.get(str(kind), 0.0) + value
    return per_policy


def x__aggregate__mutmut_35(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(str(kind), 0.0) - value
    return per_policy


def x__aggregate__mutmut_36(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(None, 0.0) + value
    return per_policy


def x__aggregate__mutmut_37(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(str(kind), None) + value
    return per_policy


def x__aggregate__mutmut_38(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(0.0) + value
    return per_policy


def x__aggregate__mutmut_39(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(str(kind), ) + value
    return per_policy


def x__aggregate__mutmut_40(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(str(None), 0.0) + value
    return per_policy


def x__aggregate__mutmut_41(raw: object) -> dict[str, dict[str, float]]:
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
        entry[str(kind)] = entry.get(str(kind), 1.0) + value
    return per_policy

mutants_x__aggregate__mutmut['_mutmut_orig'] = x__aggregate__mutmut_orig # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_1'] = x__aggregate__mutmut_1 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_2'] = x__aggregate__mutmut_2 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_3'] = x__aggregate__mutmut_3 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_4'] = x__aggregate__mutmut_4 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_5'] = x__aggregate__mutmut_5 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_6'] = x__aggregate__mutmut_6 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_7'] = x__aggregate__mutmut_7 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_8'] = x__aggregate__mutmut_8 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_9'] = x__aggregate__mutmut_9 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_10'] = x__aggregate__mutmut_10 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_11'] = x__aggregate__mutmut_11 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_12'] = x__aggregate__mutmut_12 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_13'] = x__aggregate__mutmut_13 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_14'] = x__aggregate__mutmut_14 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_15'] = x__aggregate__mutmut_15 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_16'] = x__aggregate__mutmut_16 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_17'] = x__aggregate__mutmut_17 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_18'] = x__aggregate__mutmut_18 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_19'] = x__aggregate__mutmut_19 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_20'] = x__aggregate__mutmut_20 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_21'] = x__aggregate__mutmut_21 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_22'] = x__aggregate__mutmut_22 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_23'] = x__aggregate__mutmut_23 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_24'] = x__aggregate__mutmut_24 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_25'] = x__aggregate__mutmut_25 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_26'] = x__aggregate__mutmut_26 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_27'] = x__aggregate__mutmut_27 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_28'] = x__aggregate__mutmut_28 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_29'] = x__aggregate__mutmut_29 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_30'] = x__aggregate__mutmut_30 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_31'] = x__aggregate__mutmut_31 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_32'] = x__aggregate__mutmut_32 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_33'] = x__aggregate__mutmut_33 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_34'] = x__aggregate__mutmut_34 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_35'] = x__aggregate__mutmut_35 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_36'] = x__aggregate__mutmut_36 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_37'] = x__aggregate__mutmut_37 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_38'] = x__aggregate__mutmut_38 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_39'] = x__aggregate__mutmut_39 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_40'] = x__aggregate__mutmut_40 # type: ignore # mutmut generated
mutants_x__aggregate__mutmut['x__aggregate__mutmut_41'] = x__aggregate__mutmut_41 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(values: dict[str, float], kind: str) -> int:
    return int(values.get(kind, 0.0))


def x__as_int__mutmut_orig(values: dict[str, float], kind: str) -> int:
    return int(values.get(kind, 0.0))


def x__as_int__mutmut_1(values: dict[str, float], kind: str) -> int:
    return int(None)


def x__as_int__mutmut_2(values: dict[str, float], kind: str) -> int:
    return int(values.get(None, 0.0))


def x__as_int__mutmut_3(values: dict[str, float], kind: str) -> int:
    return int(values.get(kind, None))


def x__as_int__mutmut_4(values: dict[str, float], kind: str) -> int:
    return int(values.get(0.0))


def x__as_int__mutmut_5(values: dict[str, float], kind: str) -> int:
    return int(values.get(kind, ))


def x__as_int__mutmut_6(values: dict[str, float], kind: str) -> int:
    return int(values.get(kind, 1.0))

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_4'] = x__as_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_5'] = x__as_int__mutmut_5 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_6'] = x__as_int__mutmut_6 # type: ignore # mutmut generated
