from __future__ import annotations

from hexawyn.domain.models.fleet_health import (
    CategoryReport,
    ClusterHealthReport,
    ClusterRawMetrics,
    FleetHealthReport,
)

_STATUS_ORDER = {"OK": 0, "WARNING": 1, "CRITICAL": 2, "UNKNOWN": -1}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_health_score__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_health_score__mutmut)
def compute_health_score(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_orig(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_1(metrics: ClusterRawMetrics) -> int:
    score = None

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_2(metrics: ClusterRawMetrics) -> int:
    score = 101

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_3(metrics: ClusterRawMetrics) -> int:
    score = 100

    score = 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_4(metrics: ClusterRawMetrics) -> int:
    score = 100

    score += 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_5(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 / metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_6(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 21 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_7(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = None
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_8(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop * max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_9(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(None, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_10(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, None)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_11(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_12(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, )
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_13(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 2)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_14(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score = int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_15(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score += int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_16(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(None)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_17(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio / 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_18(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 41)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_19(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_20(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization >= 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_21(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 1.9:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_22(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score = 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_23(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score += 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_24(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 16
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_25(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization >= 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_26(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 1.8:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_27(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score = 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_28(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score += 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_29(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 9

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_30(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_31(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization >= 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_32(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 1.9:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_33(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score = 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_34(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score += 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_35(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 16
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_36(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization >= 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_37(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 1.8:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_38(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score = 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_39(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score += 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_40(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 9

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_41(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical >= 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_42(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 1:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_43(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score = 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_44(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score += 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_45(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 11
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_46(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning >= 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_47(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 1:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_48(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score = 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_49(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score += 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_50(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 6

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_51(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score = min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_52(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score += min(metrics.security_violations * 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_53(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(None, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_54(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, None)

    return max(score, 0)


def x_compute_health_score__mutmut_55(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(15)

    return max(score, 0)


def x_compute_health_score__mutmut_56(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, )

    return max(score, 0)


def x_compute_health_score__mutmut_57(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations / 3, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_58(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 4, 15)

    return max(score, 0)


def x_compute_health_score__mutmut_59(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 16)

    return max(score, 0)


def x_compute_health_score__mutmut_60(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(None, 0)


def x_compute_health_score__mutmut_61(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, None)


def x_compute_health_score__mutmut_62(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(0)


def x_compute_health_score__mutmut_63(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, )


def x_compute_health_score__mutmut_64(metrics: ClusterRawMetrics) -> int:
    score = 100

    score -= 20 * metrics.nodes_not_ready

    crash_ratio = metrics.pods_crashloop / max(metrics.pods_total, 1)
    score -= int(crash_ratio * 40)

    if metrics.cpu_utilization is not None:
        if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.cpu_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.memory_utilization is not None:
        if metrics.memory_utilization > 0.90:  # noqa: PLR2004
            score -= 15
        elif metrics.memory_utilization > 0.80:  # noqa: PLR2004
            score -= 8

    if metrics.certs_expiring_critical > 0:
        score -= 10
    elif metrics.certs_expiring_warning > 0:
        score -= 5

    score -= min(metrics.security_violations * 3, 15)

    return max(score, 1)

mutants_x_compute_health_score__mutmut['_mutmut_orig'] = x_compute_health_score__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_1'] = x_compute_health_score__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_2'] = x_compute_health_score__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_3'] = x_compute_health_score__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_4'] = x_compute_health_score__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_5'] = x_compute_health_score__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_6'] = x_compute_health_score__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_7'] = x_compute_health_score__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_8'] = x_compute_health_score__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_9'] = x_compute_health_score__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_10'] = x_compute_health_score__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_11'] = x_compute_health_score__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_12'] = x_compute_health_score__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_13'] = x_compute_health_score__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_14'] = x_compute_health_score__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_15'] = x_compute_health_score__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_16'] = x_compute_health_score__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_17'] = x_compute_health_score__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_18'] = x_compute_health_score__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_19'] = x_compute_health_score__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_20'] = x_compute_health_score__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_21'] = x_compute_health_score__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_22'] = x_compute_health_score__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_23'] = x_compute_health_score__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_24'] = x_compute_health_score__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_25'] = x_compute_health_score__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_26'] = x_compute_health_score__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_27'] = x_compute_health_score__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_28'] = x_compute_health_score__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_29'] = x_compute_health_score__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_30'] = x_compute_health_score__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_31'] = x_compute_health_score__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_32'] = x_compute_health_score__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_33'] = x_compute_health_score__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_34'] = x_compute_health_score__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_35'] = x_compute_health_score__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_36'] = x_compute_health_score__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_37'] = x_compute_health_score__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_38'] = x_compute_health_score__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_39'] = x_compute_health_score__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_40'] = x_compute_health_score__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_41'] = x_compute_health_score__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_42'] = x_compute_health_score__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_43'] = x_compute_health_score__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_44'] = x_compute_health_score__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_45'] = x_compute_health_score__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_46'] = x_compute_health_score__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_47'] = x_compute_health_score__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_48'] = x_compute_health_score__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_49'] = x_compute_health_score__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_50'] = x_compute_health_score__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_51'] = x_compute_health_score__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_52'] = x_compute_health_score__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_53'] = x_compute_health_score__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_54'] = x_compute_health_score__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_55'] = x_compute_health_score__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_56'] = x_compute_health_score__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_57'] = x_compute_health_score__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_58'] = x_compute_health_score__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_59'] = x_compute_health_score__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_60'] = x_compute_health_score__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_61'] = x_compute_health_score__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_62'] = x_compute_health_score__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_63'] = x_compute_health_score__mutmut_63 # type: ignore # mutmut generated
mutants_x_compute_health_score__mutmut['x_compute_health_score__mutmut_64'] = x_compute_health_score__mutmut_64 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__health_status_from_score__mutmut)
def _health_status_from_score(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_orig(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_1(score: int) -> str:
    if score > 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_2(score: int) -> str:
    if score >= 81:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_3(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "XXhealthyXX"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_4(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "HEALTHY"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_5(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score > 50:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_6(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 51:  # noqa: PLR2004
        return "degraded"
    return "critical"


def x__health_status_from_score__mutmut_7(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "XXdegradedXX"
    return "critical"


def x__health_status_from_score__mutmut_8(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "DEGRADED"
    return "critical"


def x__health_status_from_score__mutmut_9(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "XXcriticalXX"


def x__health_status_from_score__mutmut_10(score: int) -> str:
    if score >= 80:  # noqa: PLR2004
        return "healthy"
    if score >= 50:  # noqa: PLR2004
        return "degraded"
    return "CRITICAL"

mutants_x__health_status_from_score__mutmut['_mutmut_orig'] = x__health_status_from_score__mutmut_orig # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_1'] = x__health_status_from_score__mutmut_1 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_2'] = x__health_status_from_score__mutmut_2 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_3'] = x__health_status_from_score__mutmut_3 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_4'] = x__health_status_from_score__mutmut_4 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_5'] = x__health_status_from_score__mutmut_5 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_6'] = x__health_status_from_score__mutmut_6 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_7'] = x__health_status_from_score__mutmut_7 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_8'] = x__health_status_from_score__mutmut_8 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_9'] = x__health_status_from_score__mutmut_9 # type: ignore # mutmut generated
mutants_x__health_status_from_score__mutmut['x__health_status_from_score__mutmut_10'] = x__health_status_from_score__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_category__mutmut)
def _node_category(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = None
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = None
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = None
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total + not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready != 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 1:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status=None, key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=None, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, )
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready != 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 2:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status=None, key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=None, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=None
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="XXWARNINGXX", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="warning", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status=None, key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=None, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=None
    )


def x__node_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, )


def x__node_category__mutmut_30(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="XXCRITICALXX", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )


def x__node_category__mutmut_31(metrics: ClusterRawMetrics) -> CategoryReport:
    not_ready = metrics.nodes_not_ready
    total = metrics.nodes_total
    key_metric = f"{total - not_ready}/{total} nodes ready"
    if not_ready == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if not_ready == 1:
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{not_ready} node NotReady"
        )
    return CategoryReport(
        status="critical", key_metric=key_metric, top_issue=f"{not_ready} nodes NotReady"
    )

mutants_x__node_category__mutmut['_mutmut_orig'] = x__node_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_1'] = x__node_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_2'] = x__node_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_3'] = x__node_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_4'] = x__node_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_5'] = x__node_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_6'] = x__node_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_7'] = x__node_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_8'] = x__node_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_9'] = x__node_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_10'] = x__node_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_11'] = x__node_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_12'] = x__node_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_13'] = x__node_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_14'] = x__node_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_15'] = x__node_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_16'] = x__node_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_17'] = x__node_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_18'] = x__node_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_19'] = x__node_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_20'] = x__node_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_21'] = x__node_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_22'] = x__node_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_23'] = x__node_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_24'] = x__node_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_25'] = x__node_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_26'] = x__node_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_27'] = x__node_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_28'] = x__node_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_29'] = x__node_category__mutmut_29 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_30'] = x__node_category__mutmut_30 # type: ignore # mutmut generated
mutants_x__node_category__mutmut['x__node_category__mutmut_31'] = x__node_category__mutmut_31 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pod_category__mutmut)
def _pod_category(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = None
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = None
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = None
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash != 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 1:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status=None, key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=None, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, )
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash <= total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total / 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 1.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status=None, key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=None, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=None
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="XXWARNINGXX", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="warning", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status=None, key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=None, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, top_issue=None
    )


def x__pod_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="CRITICAL", key_metric=key_metric, )


def x__pod_category__mutmut_30(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="XXCRITICALXX", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )


def x__pod_category__mutmut_31(metrics: ClusterRawMetrics) -> CategoryReport:
    crash = metrics.pods_crashloop
    total = metrics.pods_total
    key_metric = f"{metrics.pods_running}/{total} pods running, {crash} CrashLoop"
    if crash == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if crash < total * 0.15:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
        )
    return CategoryReport(
        status="critical", key_metric=key_metric, top_issue=f"{crash} CrashLoopBackOff pods"
    )

mutants_x__pod_category__mutmut['_mutmut_orig'] = x__pod_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_1'] = x__pod_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_2'] = x__pod_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_3'] = x__pod_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_4'] = x__pod_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_5'] = x__pod_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_6'] = x__pod_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_7'] = x__pod_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_8'] = x__pod_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_9'] = x__pod_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_10'] = x__pod_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_11'] = x__pod_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_12'] = x__pod_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_13'] = x__pod_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_14'] = x__pod_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_15'] = x__pod_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_16'] = x__pod_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_17'] = x__pod_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_18'] = x__pod_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_19'] = x__pod_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_20'] = x__pod_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_21'] = x__pod_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_22'] = x__pod_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_23'] = x__pod_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_24'] = x__pod_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_25'] = x__pod_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_26'] = x__pod_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_27'] = x__pod_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_28'] = x__pod_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_29'] = x__pod_category__mutmut_29 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_30'] = x__pod_category__mutmut_30 # type: ignore # mutmut generated
mutants_x__pod_category__mutmut['x__pod_category__mutmut_31'] = x__pod_category__mutmut_31 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cpu_category__mutmut)
def _cpu_category(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is not None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status=None, key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric=None, top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", )
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="XXUNKNOWNXX", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="unknown", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="XXCPU usage unavailableXX", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="cpu usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU USAGE UNAVAILABLE", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = None
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(None)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization / 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 101)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = None
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization >= 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 1.9:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status=None, key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=None, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=None
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="XXCRITICALXX", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="critical", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization >= 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 1.8:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status=None, key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_30(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=None, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_31(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=None
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_32(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_33(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_34(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_35(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="XXWARNINGXX", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_36(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="warning", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_37(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status=None, key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_38(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=None, top_issue=None)


def x__cpu_category__mutmut_39(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_40(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", top_issue=None)


def x__cpu_category__mutmut_41(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, )


def x__cpu_category__mutmut_42(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)


def x__cpu_category__mutmut_43(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.cpu_utilization is None:
        return CategoryReport(status="UNKNOWN", key_metric="CPU usage unavailable", top_issue=None)
    pct = int(metrics.cpu_utilization * 100)
    key_metric = f"CPU {pct}% utilized"
    if metrics.cpu_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"CPU pressure at {pct}%"
        )
    if metrics.cpu_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"CPU high at {pct}%"
        )
    return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)

mutants_x__cpu_category__mutmut['_mutmut_orig'] = x__cpu_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_1'] = x__cpu_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_2'] = x__cpu_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_3'] = x__cpu_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_4'] = x__cpu_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_5'] = x__cpu_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_6'] = x__cpu_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_7'] = x__cpu_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_8'] = x__cpu_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_9'] = x__cpu_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_10'] = x__cpu_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_11'] = x__cpu_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_12'] = x__cpu_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_13'] = x__cpu_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_14'] = x__cpu_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_15'] = x__cpu_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_16'] = x__cpu_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_17'] = x__cpu_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_18'] = x__cpu_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_19'] = x__cpu_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_20'] = x__cpu_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_21'] = x__cpu_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_22'] = x__cpu_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_23'] = x__cpu_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_24'] = x__cpu_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_25'] = x__cpu_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_26'] = x__cpu_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_27'] = x__cpu_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_28'] = x__cpu_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_29'] = x__cpu_category__mutmut_29 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_30'] = x__cpu_category__mutmut_30 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_31'] = x__cpu_category__mutmut_31 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_32'] = x__cpu_category__mutmut_32 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_33'] = x__cpu_category__mutmut_33 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_34'] = x__cpu_category__mutmut_34 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_35'] = x__cpu_category__mutmut_35 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_36'] = x__cpu_category__mutmut_36 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_37'] = x__cpu_category__mutmut_37 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_38'] = x__cpu_category__mutmut_38 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_39'] = x__cpu_category__mutmut_39 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_40'] = x__cpu_category__mutmut_40 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_41'] = x__cpu_category__mutmut_41 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_42'] = x__cpu_category__mutmut_42 # type: ignore # mutmut generated
mutants_x__cpu_category__mutmut['x__cpu_category__mutmut_43'] = x__cpu_category__mutmut_43 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__memory_category__mutmut)
def _memory_category(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is not None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status=None, key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric=None, top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="XXUNKNOWNXX", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="unknown", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="XXMemory usage unavailableXX", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="MEMORY USAGE UNAVAILABLE", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = None
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(None)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization / 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 101)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = None
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization >= 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 1.9:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status=None, key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=None, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=None
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="XXCRITICALXX", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="critical", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization >= 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 1.8:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status=None, key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_30(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=None, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_31(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=None
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_32(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_33(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_34(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_35(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="XXWARNINGXX", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_36(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="warning", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_37(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status=None, key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_38(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=None, top_issue=None)


def x__memory_category__mutmut_39(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_40(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", top_issue=None)


def x__memory_category__mutmut_41(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="OK", key_metric=key_metric, )


def x__memory_category__mutmut_42(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)


def x__memory_category__mutmut_43(metrics: ClusterRawMetrics) -> CategoryReport:
    if metrics.memory_utilization is None:
        return CategoryReport(
            status="UNKNOWN", key_metric="Memory usage unavailable", top_issue=None
        )
    pct = int(metrics.memory_utilization * 100)
    key_metric = f"Memory {pct}% utilized"
    if metrics.memory_utilization > 0.90:  # noqa: PLR2004
        return CategoryReport(
            status="CRITICAL", key_metric=key_metric, top_issue=f"Memory pressure at {pct}%"
        )
    if metrics.memory_utilization > 0.80:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING", key_metric=key_metric, top_issue=f"Memory high at {pct}%"
        )
    return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)

mutants_x__memory_category__mutmut['_mutmut_orig'] = x__memory_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_1'] = x__memory_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_2'] = x__memory_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_3'] = x__memory_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_4'] = x__memory_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_5'] = x__memory_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_6'] = x__memory_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_7'] = x__memory_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_8'] = x__memory_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_9'] = x__memory_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_10'] = x__memory_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_11'] = x__memory_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_12'] = x__memory_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_13'] = x__memory_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_14'] = x__memory_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_15'] = x__memory_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_16'] = x__memory_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_17'] = x__memory_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_18'] = x__memory_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_19'] = x__memory_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_20'] = x__memory_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_21'] = x__memory_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_22'] = x__memory_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_23'] = x__memory_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_24'] = x__memory_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_25'] = x__memory_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_26'] = x__memory_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_27'] = x__memory_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_28'] = x__memory_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_29'] = x__memory_category__mutmut_29 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_30'] = x__memory_category__mutmut_30 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_31'] = x__memory_category__mutmut_31 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_32'] = x__memory_category__mutmut_32 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_33'] = x__memory_category__mutmut_33 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_34'] = x__memory_category__mutmut_34 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_35'] = x__memory_category__mutmut_35 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_36'] = x__memory_category__mutmut_36 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_37'] = x__memory_category__mutmut_37 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_38'] = x__memory_category__mutmut_38 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_39'] = x__memory_category__mutmut_39 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_40'] = x__memory_category__mutmut_40 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_41'] = x__memory_category__mutmut_41 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_42'] = x__memory_category__mutmut_42 # type: ignore # mutmut generated
mutants_x__memory_category__mutmut['x__memory_category__mutmut_43'] = x__memory_category__mutmut_43 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cert_category__mutmut)
def _cert_category(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = None
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = None
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = None
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical >= 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 1:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status=None,
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=None,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=None,
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="XXCRITICALXX",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="critical",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning >= 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 1:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status=None,
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=None,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=None,
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="XXWARNINGXX",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="warning",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status=None, key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=None, top_issue=None)


def x__cert_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", top_issue=None)


def x__cert_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="OK", key_metric=key_metric, )


def x__cert_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)


def x__cert_category__mutmut_30(metrics: ClusterRawMetrics) -> CategoryReport:
    critical = metrics.certs_expiring_critical
    warning = metrics.certs_expiring_warning
    key_metric = f"{critical} critical, {warning} warning cert(s)"
    if critical > 0:
        return CategoryReport(
            status="CRITICAL",
            key_metric=key_metric,
            top_issue=f"{critical} cert(s) expire within 7 days",
        )
    if warning > 0:
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{warning} cert(s) expire within 30 days",
        )
    return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)

mutants_x__cert_category__mutmut['_mutmut_orig'] = x__cert_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_1'] = x__cert_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_2'] = x__cert_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_3'] = x__cert_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_4'] = x__cert_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_5'] = x__cert_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_6'] = x__cert_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_7'] = x__cert_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_8'] = x__cert_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_9'] = x__cert_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_10'] = x__cert_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_11'] = x__cert_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_12'] = x__cert_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_13'] = x__cert_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_14'] = x__cert_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_15'] = x__cert_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_16'] = x__cert_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_17'] = x__cert_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_18'] = x__cert_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_19'] = x__cert_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_20'] = x__cert_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_21'] = x__cert_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_22'] = x__cert_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_23'] = x__cert_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_24'] = x__cert_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_25'] = x__cert_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_26'] = x__cert_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_27'] = x__cert_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_28'] = x__cert_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_29'] = x__cert_category__mutmut_29 # type: ignore # mutmut generated
mutants_x__cert_category__mutmut['x__cert_category__mutmut_30'] = x__cert_category__mutmut_30 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pipeline_category__mutmut)
def _pipeline_category(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = None
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = None
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing != 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 1:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status=None, key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=None, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, )
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing < 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 3:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status=None,
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=None,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=None,
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="XXWARNINGXX",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="warning",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status=None,
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=None,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=None,
    )


def x__pipeline_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        )


def x__pipeline_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="XXCRITICALXX",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )


def x__pipeline_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    failing = metrics.pipelines_failing
    key_metric = f"{failing} failing pipeline(s)"
    if failing == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if failing <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{failing} Tekton pipeline run(s) failed",
        )
    return CategoryReport(
        status="critical",
        key_metric=key_metric,
        top_issue=f"{failing} Tekton pipeline run(s) failed",
    )

mutants_x__pipeline_category__mutmut['_mutmut_orig'] = x__pipeline_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_1'] = x__pipeline_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_2'] = x__pipeline_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_3'] = x__pipeline_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_4'] = x__pipeline_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_5'] = x__pipeline_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_6'] = x__pipeline_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_7'] = x__pipeline_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_8'] = x__pipeline_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_9'] = x__pipeline_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_10'] = x__pipeline_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_11'] = x__pipeline_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_12'] = x__pipeline_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_13'] = x__pipeline_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_14'] = x__pipeline_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_15'] = x__pipeline_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_16'] = x__pipeline_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_17'] = x__pipeline_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_18'] = x__pipeline_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_19'] = x__pipeline_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_20'] = x__pipeline_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_21'] = x__pipeline_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_22'] = x__pipeline_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_23'] = x__pipeline_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_24'] = x__pipeline_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_25'] = x__pipeline_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_26'] = x__pipeline_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_27'] = x__pipeline_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_28'] = x__pipeline_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__pipeline_category__mutmut['x__pipeline_category__mutmut_29'] = x__pipeline_category__mutmut_29 # type: ignore # mutmut generated
mutants_x__security_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__security_category__mutmut)
def _security_category(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_orig(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_1(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = None
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_2(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = None
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_3(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations != 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_4(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 1:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_5(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status=None, key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_6(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=None, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_7(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_8(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_9(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, )
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_10(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="XXOKXX", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_11(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="ok", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_12(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations < 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_13(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 3:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_14(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status=None,
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_15(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=None,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_16(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=None,
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_17(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_18(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_19(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_20(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="XXWARNINGXX",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_21(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="warning",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_22(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status=None,
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_23(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=None,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_24(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        top_issue=None,
    )


def x__security_category__mutmut_25(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_26(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_27(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="CRITICAL",
        key_metric=key_metric,
        )


def x__security_category__mutmut_28(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="XXCRITICALXX",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )


def x__security_category__mutmut_29(metrics: ClusterRawMetrics) -> CategoryReport:
    violations = metrics.security_violations
    key_metric = f"{violations} security violation(s)"
    if violations == 0:
        return CategoryReport(status="OK", key_metric=key_metric, top_issue=None)
    if violations <= 2:  # noqa: PLR2004
        return CategoryReport(
            status="WARNING",
            key_metric=key_metric,
            top_issue=f"{violations} privileged/non-compliant pod(s)",
        )
    return CategoryReport(
        status="critical",
        key_metric=key_metric,
        top_issue=f"{violations} privileged/non-compliant pod(s)",
    )

mutants_x__security_category__mutmut['_mutmut_orig'] = x__security_category__mutmut_orig # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_1'] = x__security_category__mutmut_1 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_2'] = x__security_category__mutmut_2 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_3'] = x__security_category__mutmut_3 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_4'] = x__security_category__mutmut_4 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_5'] = x__security_category__mutmut_5 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_6'] = x__security_category__mutmut_6 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_7'] = x__security_category__mutmut_7 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_8'] = x__security_category__mutmut_8 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_9'] = x__security_category__mutmut_9 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_10'] = x__security_category__mutmut_10 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_11'] = x__security_category__mutmut_11 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_12'] = x__security_category__mutmut_12 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_13'] = x__security_category__mutmut_13 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_14'] = x__security_category__mutmut_14 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_15'] = x__security_category__mutmut_15 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_16'] = x__security_category__mutmut_16 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_17'] = x__security_category__mutmut_17 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_18'] = x__security_category__mutmut_18 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_19'] = x__security_category__mutmut_19 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_20'] = x__security_category__mutmut_20 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_21'] = x__security_category__mutmut_21 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_22'] = x__security_category__mutmut_22 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_23'] = x__security_category__mutmut_23 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_24'] = x__security_category__mutmut_24 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_25'] = x__security_category__mutmut_25 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_26'] = x__security_category__mutmut_26 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_27'] = x__security_category__mutmut_27 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_28'] = x__security_category__mutmut_28 # type: ignore # mutmut generated
mutants_x__security_category__mutmut['x__security_category__mutmut_29'] = x__security_category__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_categories__mutmut)
def build_categories(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_orig(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_1(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "XXnodesXX": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_2(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "NODES": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_3(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(None),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_4(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "XXpodsXX": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_5(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "PODS": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_6(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(None),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_7(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "XXcpuXX": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_8(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "CPU": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_9(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(None),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_10(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "XXmemoryXX": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_11(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "MEMORY": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_12(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(None),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_13(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "XXcertificatesXX": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_14(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "CERTIFICATES": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_15(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(None),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_16(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "XXpipelinesXX": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_17(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "PIPELINES": _pipeline_category(metrics),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_18(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(None),
        "security": _security_category(metrics),
    }


def x_build_categories__mutmut_19(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "XXsecurityXX": _security_category(metrics),
    }


def x_build_categories__mutmut_20(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "SECURITY": _security_category(metrics),
    }


def x_build_categories__mutmut_21(metrics: ClusterRawMetrics) -> dict[str, CategoryReport]:
    return {
        "nodes": _node_category(metrics),
        "pods": _pod_category(metrics),
        "cpu": _cpu_category(metrics),
        "memory": _memory_category(metrics),
        "certificates": _cert_category(metrics),
        "pipelines": _pipeline_category(metrics),
        "security": _security_category(None),
    }

mutants_x_build_categories__mutmut['_mutmut_orig'] = x_build_categories__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_1'] = x_build_categories__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_2'] = x_build_categories__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_3'] = x_build_categories__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_4'] = x_build_categories__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_5'] = x_build_categories__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_6'] = x_build_categories__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_7'] = x_build_categories__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_8'] = x_build_categories__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_9'] = x_build_categories__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_10'] = x_build_categories__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_11'] = x_build_categories__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_12'] = x_build_categories__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_13'] = x_build_categories__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_14'] = x_build_categories__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_15'] = x_build_categories__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_16'] = x_build_categories__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_17'] = x_build_categories__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_18'] = x_build_categories__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_19'] = x_build_categories__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_20'] = x_build_categories__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_categories__mutmut['x_build_categories__mutmut_21'] = x_build_categories__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cluster_report__mutmut)
def build_cluster_report(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_orig(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_1(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = None
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_2(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(None)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_3(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = None
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_4(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(None)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_5(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=None,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_6(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=None,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_7(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=None,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_8(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=None,
        categories=categories,
    )


def x_build_cluster_report__mutmut_9(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=None,
    )


def x_build_cluster_report__mutmut_10(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_11(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_12(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_13(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_14(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        categories=categories,
    )


def x_build_cluster_report__mutmut_15(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        )


def x_build_cluster_report__mutmut_16(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=False,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(score),
        categories=categories,
    )


def x_build_cluster_report__mutmut_17(metrics: ClusterRawMetrics) -> ClusterHealthReport:
    score = compute_health_score(metrics)
    categories = build_categories(metrics)
    return ClusterHealthReport(
        context_name=metrics.context_name,
        reachable=True,
        unreachable_reason=None,
        health_score=score,
        health_status=_health_status_from_score(None),
        categories=categories,
    )

mutants_x_build_cluster_report__mutmut['_mutmut_orig'] = x_build_cluster_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_1'] = x_build_cluster_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_2'] = x_build_cluster_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_3'] = x_build_cluster_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_4'] = x_build_cluster_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_5'] = x_build_cluster_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_6'] = x_build_cluster_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_7'] = x_build_cluster_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_8'] = x_build_cluster_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_9'] = x_build_cluster_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_10'] = x_build_cluster_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_11'] = x_build_cluster_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_12'] = x_build_cluster_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_13'] = x_build_cluster_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_14'] = x_build_cluster_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_15'] = x_build_cluster_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_16'] = x_build_cluster_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_cluster_report__mutmut['x_build_cluster_report__mutmut_17'] = x_build_cluster_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_make_unreachable_report__mutmut)
def make_unreachable_report(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_orig(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_1(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=None,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_2(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=None,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_3(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=None,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_4(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status=None,
        categories={},
    )


def x_make_unreachable_report__mutmut_5(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories=None,
    )


def x_make_unreachable_report__mutmut_6(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_7(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_8(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_9(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_10(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        categories={},
    )


def x_make_unreachable_report__mutmut_11(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        )


def x_make_unreachable_report__mutmut_12(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=True,
        unreachable_reason=reason,
        health_score=None,
        health_status="unreachable",
        categories={},
    )


def x_make_unreachable_report__mutmut_13(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="XXunreachableXX",
        categories={},
    )


def x_make_unreachable_report__mutmut_14(context_name: str, reason: str) -> ClusterHealthReport:
    return ClusterHealthReport(
        context_name=context_name,
        reachable=False,
        unreachable_reason=reason,
        health_score=None,
        health_status="UNREACHABLE",
        categories={},
    )

mutants_x_make_unreachable_report__mutmut['_mutmut_orig'] = x_make_unreachable_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_1'] = x_make_unreachable_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_2'] = x_make_unreachable_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_3'] = x_make_unreachable_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_4'] = x_make_unreachable_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_5'] = x_make_unreachable_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_6'] = x_make_unreachable_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_7'] = x_make_unreachable_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_8'] = x_make_unreachable_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_9'] = x_make_unreachable_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_10'] = x_make_unreachable_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_11'] = x_make_unreachable_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_12'] = x_make_unreachable_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_13'] = x_make_unreachable_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_make_unreachable_report__mutmut['x_make_unreachable_report__mutmut_14'] = x_make_unreachable_report__mutmut_14 # type: ignore # mutmut generated


_SIGNIFICANT_TREND_PCT = 0.10
mutants_x_compute_fleet_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_fleet_trend__mutmut)
def compute_fleet_trend(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_orig(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_1(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None and previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_2(previous: float | None, current: float | None) -> str | None:
    if previous is None and current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_3(previous: float | None, current: float | None) -> str | None:
    if previous is not None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_4(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is not None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_5(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous != 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_6(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 1:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_7(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = None
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_8(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) * previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_9(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current + previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_10(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct >= _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_11(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "XXimprovingXX"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_12(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "IMPROVING"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_13(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct <= -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_14(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < +_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "stable"


def x_compute_fleet_trend__mutmut_15(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "XXdegradingXX"
    return "stable"


def x_compute_fleet_trend__mutmut_16(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "DEGRADING"
    return "stable"


def x_compute_fleet_trend__mutmut_17(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "XXstableXX"


def x_compute_fleet_trend__mutmut_18(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "improving"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "degrading"
    return "STABLE"

mutants_x_compute_fleet_trend__mutmut['_mutmut_orig'] = x_compute_fleet_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_1'] = x_compute_fleet_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_2'] = x_compute_fleet_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_3'] = x_compute_fleet_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_4'] = x_compute_fleet_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_5'] = x_compute_fleet_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_6'] = x_compute_fleet_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_7'] = x_compute_fleet_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_8'] = x_compute_fleet_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_9'] = x_compute_fleet_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_10'] = x_compute_fleet_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_11'] = x_compute_fleet_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_12'] = x_compute_fleet_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_13'] = x_compute_fleet_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_14'] = x_compute_fleet_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_15'] = x_compute_fleet_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_16'] = x_compute_fleet_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_17'] = x_compute_fleet_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_fleet_trend__mutmut['x_compute_fleet_trend__mutmut_18'] = x_compute_fleet_trend__mutmut_18 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_aggregate_fleet__mutmut)
def aggregate_fleet(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_orig(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_1(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = None
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_2(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = None

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_3(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_4(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = ""
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_5(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = None

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_6(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "XXunknownXX"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_7(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "UNKNOWN"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_8(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = None
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_9(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_10(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = None

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_11(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(None)

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_12(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) * len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_13(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(None) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_14(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = None
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_15(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status(None)
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_16(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = None

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_17(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "XXno_cluster_reachableXX"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_18(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "NO_CLUSTER_REACHABLE"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_19(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=None,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_20(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=None,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_21(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=None,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_22(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=None,
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_23(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=None,
    )


def x_aggregate_fleet__mutmut_24(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_25(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_26(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        reachable_count=len(reachable),
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_27(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        unreachable_count=len(unreachable),
    )


def x_aggregate_fleet__mutmut_28(reports: list[ClusterHealthReport]) -> FleetHealthReport:
    reachable = [r for r in reports if r.reachable]
    unreachable = [r for r in reports if not r.reachable]

    fleet_score: int | None = None
    fleet_status = "unknown"

    if reachable:
        scores = [r.health_score for r in reachable if r.health_score is not None]
        if scores:
            fleet_score = round(sum(scores) / len(scores))

        fleet_status = _worst_status([r.health_status for r in reachable])
    elif reports:
        fleet_status = "no_cluster_reachable"

    return FleetHealthReport(
        cluster_reports=reports,
        fleet_score=fleet_score,
        fleet_status=fleet_status,
        reachable_count=len(reachable),
        )

mutants_x_aggregate_fleet__mutmut['_mutmut_orig'] = x_aggregate_fleet__mutmut_orig # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_1'] = x_aggregate_fleet__mutmut_1 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_2'] = x_aggregate_fleet__mutmut_2 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_3'] = x_aggregate_fleet__mutmut_3 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_4'] = x_aggregate_fleet__mutmut_4 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_5'] = x_aggregate_fleet__mutmut_5 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_6'] = x_aggregate_fleet__mutmut_6 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_7'] = x_aggregate_fleet__mutmut_7 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_8'] = x_aggregate_fleet__mutmut_8 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_9'] = x_aggregate_fleet__mutmut_9 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_10'] = x_aggregate_fleet__mutmut_10 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_11'] = x_aggregate_fleet__mutmut_11 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_12'] = x_aggregate_fleet__mutmut_12 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_13'] = x_aggregate_fleet__mutmut_13 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_14'] = x_aggregate_fleet__mutmut_14 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_15'] = x_aggregate_fleet__mutmut_15 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_16'] = x_aggregate_fleet__mutmut_16 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_17'] = x_aggregate_fleet__mutmut_17 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_18'] = x_aggregate_fleet__mutmut_18 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_19'] = x_aggregate_fleet__mutmut_19 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_20'] = x_aggregate_fleet__mutmut_20 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_21'] = x_aggregate_fleet__mutmut_21 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_22'] = x_aggregate_fleet__mutmut_22 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_23'] = x_aggregate_fleet__mutmut_23 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_24'] = x_aggregate_fleet__mutmut_24 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_25'] = x_aggregate_fleet__mutmut_25 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_26'] = x_aggregate_fleet__mutmut_26 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_27'] = x_aggregate_fleet__mutmut_27 # type: ignore # mutmut generated
mutants_x_aggregate_fleet__mutmut['x_aggregate_fleet__mutmut_28'] = x_aggregate_fleet__mutmut_28 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__worst_status__mutmut)
def _worst_status(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_orig(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_1(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("XXcriticalXX", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_2(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("CRITICAL", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_3(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "XXdegradedXX", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_4(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "DEGRADED", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_5(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "XXhealthyXX"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_6(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "HEALTHY"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_7(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "healthy"):
        if status not in statuses:
            return status
    return statuses[0] if statuses else "unknown"


def x__worst_status__mutmut_8(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[1] if statuses else "unknown"


def x__worst_status__mutmut_9(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "XXunknownXX"


def x__worst_status__mutmut_10(statuses: list[str]) -> str:
    """Pick the most severe status: critical > degraded > healthy > anything else."""
    for status in ("critical", "degraded", "healthy"):
        if status in statuses:
            return status
    return statuses[0] if statuses else "UNKNOWN"

mutants_x__worst_status__mutmut['_mutmut_orig'] = x__worst_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_1'] = x__worst_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_2'] = x__worst_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_3'] = x__worst_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_4'] = x__worst_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_5'] = x__worst_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_6'] = x__worst_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_7'] = x__worst_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_8'] = x__worst_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_9'] = x__worst_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__worst_status__mutmut['x__worst_status__mutmut_10'] = x__worst_status__mutmut_10 # type: ignore # mutmut generated
