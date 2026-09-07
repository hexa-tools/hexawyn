from __future__ import annotations

from hexawyn.domain.models.cluster_health_comparison import (
    ClusterHealthSnapshot,
    ComparisonReport,
    HealthComparisonResult,
)
from hexawyn.domain.models.fleet_health import ClusterRawMetrics


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_to_snapshot__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_snapshot__mutmut)
def to_snapshot(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_orig(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_1(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = None
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_2(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total + raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_3(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=None,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_4(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=None,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_5(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=None,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_6(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=None,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_7(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=None,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_8(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=None,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_9(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=None,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_10(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=None,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_11(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status=None,
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_12(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=None,
        reachable=True,
    )


def x_to_snapshot__mutmut_13(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=None,
    )


def x_to_snapshot__mutmut_14(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_15(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_16(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_17(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_18(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_19(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_20(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_21(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_22(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_23(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        reachable=True,
    )


def x_to_snapshot__mutmut_24(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        )


def x_to_snapshot__mutmut_25(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) / 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_26(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization and 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_27(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 1.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_28(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 101,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_29(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) / 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_30(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization and 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_31(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 1.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_32(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 101,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_33(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="XXhealthyXX" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_34(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="HEALTHY" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_35(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing != 0 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_36(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 1 else "degraded",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_37(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "XXdegradedXX",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_38(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "DEGRADED",
        in_maintenance=False,
        reachable=True,
    )


def x_to_snapshot__mutmut_39(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=True,
        reachable=True,
    )


def x_to_snapshot__mutmut_40(raw: ClusterRawMetrics) -> ClusterHealthSnapshot:
    failing = raw.pods_total - raw.pods_running
    return ClusterHealthSnapshot(
        cluster_name=raw.context_name,
        failing_pods=failing,
        total_pods=raw.pods_total,
        cpu_utilization_pct=(raw.cpu_utilization or 0.0) * 100,
        memory_utilization_pct=(raw.memory_utilization or 0.0) * 100,
        node_count=raw.nodes_total,
        nodes_not_ready=raw.nodes_not_ready,
        active_incidents=raw.pipelines_failing,
        health_status="healthy" if failing == 0 else "degraded",
        in_maintenance=False,
        reachable=False,
    )

mutants_x_to_snapshot__mutmut['_mutmut_orig'] = x_to_snapshot__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_1'] = x_to_snapshot__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_2'] = x_to_snapshot__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_3'] = x_to_snapshot__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_4'] = x_to_snapshot__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_5'] = x_to_snapshot__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_6'] = x_to_snapshot__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_7'] = x_to_snapshot__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_8'] = x_to_snapshot__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_9'] = x_to_snapshot__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_10'] = x_to_snapshot__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_11'] = x_to_snapshot__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_12'] = x_to_snapshot__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_13'] = x_to_snapshot__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_14'] = x_to_snapshot__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_15'] = x_to_snapshot__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_16'] = x_to_snapshot__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_17'] = x_to_snapshot__mutmut_17 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_18'] = x_to_snapshot__mutmut_18 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_19'] = x_to_snapshot__mutmut_19 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_20'] = x_to_snapshot__mutmut_20 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_21'] = x_to_snapshot__mutmut_21 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_22'] = x_to_snapshot__mutmut_22 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_23'] = x_to_snapshot__mutmut_23 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_24'] = x_to_snapshot__mutmut_24 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_25'] = x_to_snapshot__mutmut_25 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_26'] = x_to_snapshot__mutmut_26 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_27'] = x_to_snapshot__mutmut_27 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_28'] = x_to_snapshot__mutmut_28 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_29'] = x_to_snapshot__mutmut_29 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_30'] = x_to_snapshot__mutmut_30 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_31'] = x_to_snapshot__mutmut_31 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_32'] = x_to_snapshot__mutmut_32 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_33'] = x_to_snapshot__mutmut_33 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_34'] = x_to_snapshot__mutmut_34 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_35'] = x_to_snapshot__mutmut_35 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_36'] = x_to_snapshot__mutmut_36 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_37'] = x_to_snapshot__mutmut_37 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_38'] = x_to_snapshot__mutmut_38 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_39'] = x_to_snapshot__mutmut_39 # type: ignore # mutmut generated
mutants_x_to_snapshot__mutmut['x_to_snapshot__mutmut_40'] = x_to_snapshot__mutmut_40 # type: ignore # mutmut generated
mutants_x_compare__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compare__mutmut)
def compare(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_orig(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_1(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable and not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_2(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_3(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_4(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(None, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_5(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, None)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_6(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_7(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, )

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_8(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance and cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_9(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(None, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_10(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, None)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_11(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_12(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, )

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_13(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = None
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_14(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(None)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_15(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = None
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_16(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(None)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_17(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = None
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_18(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods + cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_19(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = None
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_20(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct + cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_21(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = None

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_22(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents + cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_23(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = None
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_24(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(None)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_25(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = None

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_26(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(None)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_27(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 or delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_28(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 or delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_29(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(None) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_30(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a + score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_31(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) <= 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_32(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 1.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_33(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing != 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_34(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 1 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_35(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents != 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_36(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 1:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_37(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=None,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_38(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=None,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_39(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=None,
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_40(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_41(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_42(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_43(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason=None,
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_44(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=None,
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_45(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=None,
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_46(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_47(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_48(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_49(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_50(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="XXboth_healthyXX",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_51(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="BOTH_HEALTHY",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_52(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(None, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_53(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, None),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_54(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_55(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, ),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_56(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 2),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_57(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(None, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_58(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, None),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_59(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_60(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, ),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_61(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 2),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_62(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = None
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_63(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a >= score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_64(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=None,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_65(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=None,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_66(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=None,
    )


def x_compare__mutmut_67(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_68(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_69(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        )


def x_compare__mutmut_70(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_71(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=None,
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_72(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=None,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_73(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=None,
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_74(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=None,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_75(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=None,
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_76(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=None,
        ),
    )


def x_compare__mutmut_77(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_78(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_79(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_80(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_81(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_82(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_83(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            ),
    )


def x_compare__mutmut_84(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(None)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_85(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(None):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_86(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(None)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_87(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(None, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_88(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, None),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_89(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_90(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, ),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_91(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 2),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_92(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(None, 1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_93(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, None),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_94(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(1),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_95(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, ),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_96(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 2),
            normalized_b_failing_per_100=round(normalized_b, 1),
        ),
    )


def x_compare__mutmut_97(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(None, 1),
        ),
    )


def x_compare__mutmut_98(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, None),
        ),
    )


def x_compare__mutmut_99(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(1),
        ),
    )


def x_compare__mutmut_100(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, ),
        ),
    )


def x_compare__mutmut_101(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    if not cluster_a.reachable or not cluster_b.reachable:
        return _unreachable_result(cluster_a, cluster_b)

    if cluster_a.in_maintenance or cluster_b.in_maintenance:
        return _maintenance_result(cluster_a, cluster_b)

    normalized_a = _failing_per_100(cluster_a)
    normalized_b = _failing_per_100(cluster_b)
    delta_failing = cluster_a.failing_pods - cluster_b.failing_pods
    delta_cpu = cluster_a.cpu_utilization_pct - cluster_b.cpu_utilization_pct
    delta_incidents = cluster_a.active_incidents - cluster_b.active_incidents

    score_a = score(cluster_a)
    score_b = score(cluster_b)

    if abs(score_a - score_b) < 0.5 and delta_failing == 0 and delta_incidents == 0:  # noqa: PLR2004
        return HealthComparisonResult(
            cluster_a=cluster_a,
            cluster_b=cluster_b,
            comparison=ComparisonReport(
                worse_cluster=None,
                reason="both_healthy",
                normalized_a_failing_per_100=round(normalized_a, 1),
                normalized_b_failing_per_100=round(normalized_b, 1),
            ),
        )

    worse = cluster_a.cluster_name if score_a > score_b else cluster_b.cluster_name
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=worse,
            reason=(
                f"{worse} has {abs(delta_failing)} more failing pods, "
                f"{abs(delta_cpu):.0f}pp higher CPU, "
                f"{abs(delta_incidents)} more active incidents"
            ),
            delta_failing_pods=delta_failing,
            delta_cpu_pct=round(delta_cpu, 1),
            delta_active_incidents=delta_incidents,
            normalized_a_failing_per_100=round(normalized_a, 1),
            normalized_b_failing_per_100=round(normalized_b, 2),
        ),
    )

mutants_x_compare__mutmut['_mutmut_orig'] = x_compare__mutmut_orig # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_1'] = x_compare__mutmut_1 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_2'] = x_compare__mutmut_2 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_3'] = x_compare__mutmut_3 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_4'] = x_compare__mutmut_4 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_5'] = x_compare__mutmut_5 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_6'] = x_compare__mutmut_6 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_7'] = x_compare__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_8'] = x_compare__mutmut_8 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_9'] = x_compare__mutmut_9 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_10'] = x_compare__mutmut_10 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_11'] = x_compare__mutmut_11 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_12'] = x_compare__mutmut_12 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_13'] = x_compare__mutmut_13 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_14'] = x_compare__mutmut_14 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_15'] = x_compare__mutmut_15 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_16'] = x_compare__mutmut_16 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_17'] = x_compare__mutmut_17 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_18'] = x_compare__mutmut_18 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_19'] = x_compare__mutmut_19 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_20'] = x_compare__mutmut_20 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_21'] = x_compare__mutmut_21 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_22'] = x_compare__mutmut_22 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_23'] = x_compare__mutmut_23 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_24'] = x_compare__mutmut_24 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_25'] = x_compare__mutmut_25 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_26'] = x_compare__mutmut_26 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_27'] = x_compare__mutmut_27 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_28'] = x_compare__mutmut_28 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_29'] = x_compare__mutmut_29 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_30'] = x_compare__mutmut_30 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_31'] = x_compare__mutmut_31 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_32'] = x_compare__mutmut_32 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_33'] = x_compare__mutmut_33 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_34'] = x_compare__mutmut_34 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_35'] = x_compare__mutmut_35 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_36'] = x_compare__mutmut_36 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_37'] = x_compare__mutmut_37 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_38'] = x_compare__mutmut_38 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_39'] = x_compare__mutmut_39 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_40'] = x_compare__mutmut_40 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_41'] = x_compare__mutmut_41 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_42'] = x_compare__mutmut_42 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_43'] = x_compare__mutmut_43 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_44'] = x_compare__mutmut_44 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_45'] = x_compare__mutmut_45 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_46'] = x_compare__mutmut_46 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_47'] = x_compare__mutmut_47 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_48'] = x_compare__mutmut_48 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_49'] = x_compare__mutmut_49 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_50'] = x_compare__mutmut_50 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_51'] = x_compare__mutmut_51 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_52'] = x_compare__mutmut_52 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_53'] = x_compare__mutmut_53 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_54'] = x_compare__mutmut_54 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_55'] = x_compare__mutmut_55 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_56'] = x_compare__mutmut_56 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_57'] = x_compare__mutmut_57 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_58'] = x_compare__mutmut_58 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_59'] = x_compare__mutmut_59 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_60'] = x_compare__mutmut_60 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_61'] = x_compare__mutmut_61 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_62'] = x_compare__mutmut_62 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_63'] = x_compare__mutmut_63 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_64'] = x_compare__mutmut_64 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_65'] = x_compare__mutmut_65 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_66'] = x_compare__mutmut_66 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_67'] = x_compare__mutmut_67 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_68'] = x_compare__mutmut_68 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_69'] = x_compare__mutmut_69 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_70'] = x_compare__mutmut_70 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_71'] = x_compare__mutmut_71 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_72'] = x_compare__mutmut_72 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_73'] = x_compare__mutmut_73 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_74'] = x_compare__mutmut_74 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_75'] = x_compare__mutmut_75 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_76'] = x_compare__mutmut_76 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_77'] = x_compare__mutmut_77 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_78'] = x_compare__mutmut_78 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_79'] = x_compare__mutmut_79 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_80'] = x_compare__mutmut_80 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_81'] = x_compare__mutmut_81 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_82'] = x_compare__mutmut_82 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_83'] = x_compare__mutmut_83 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_84'] = x_compare__mutmut_84 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_85'] = x_compare__mutmut_85 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_86'] = x_compare__mutmut_86 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_87'] = x_compare__mutmut_87 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_88'] = x_compare__mutmut_88 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_89'] = x_compare__mutmut_89 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_90'] = x_compare__mutmut_90 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_91'] = x_compare__mutmut_91 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_92'] = x_compare__mutmut_92 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_93'] = x_compare__mutmut_93 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_94'] = x_compare__mutmut_94 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_95'] = x_compare__mutmut_95 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_96'] = x_compare__mutmut_96 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_97'] = x_compare__mutmut_97 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_98'] = x_compare__mutmut_98 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_99'] = x_compare__mutmut_99 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_100'] = x_compare__mutmut_100 # type: ignore # mutmut generated
mutants_x_compare__mutmut['x_compare__mutmut_101'] = x_compare__mutmut_101 # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__failing_per_100__mutmut)
def _failing_per_100(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 0.0
    return snap.failing_pods / snap.total_pods * 100


def x__failing_per_100__mutmut_orig(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 0.0
    return snap.failing_pods / snap.total_pods * 100


def x__failing_per_100__mutmut_1(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods < 0:
        return 0.0
    return snap.failing_pods / snap.total_pods * 100


def x__failing_per_100__mutmut_2(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 1:
        return 0.0
    return snap.failing_pods / snap.total_pods * 100


def x__failing_per_100__mutmut_3(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 1.0
    return snap.failing_pods / snap.total_pods * 100


def x__failing_per_100__mutmut_4(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 0.0
    return snap.failing_pods / snap.total_pods / 100


def x__failing_per_100__mutmut_5(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 0.0
    return snap.failing_pods * snap.total_pods * 100


def x__failing_per_100__mutmut_6(snap: ClusterHealthSnapshot) -> float:
    if snap.total_pods <= 0:
        return 0.0
    return snap.failing_pods / snap.total_pods * 101

mutants_x__failing_per_100__mutmut['_mutmut_orig'] = x__failing_per_100__mutmut_orig # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut['x__failing_per_100__mutmut_1'] = x__failing_per_100__mutmut_1 # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut['x__failing_per_100__mutmut_2'] = x__failing_per_100__mutmut_2 # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut['x__failing_per_100__mutmut_3'] = x__failing_per_100__mutmut_3 # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut['x__failing_per_100__mutmut_4'] = x__failing_per_100__mutmut_4 # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut['x__failing_per_100__mutmut_5'] = x__failing_per_100__mutmut_5 # type: ignore # mutmut generated
mutants_x__failing_per_100__mutmut['x__failing_per_100__mutmut_6'] = x__failing_per_100__mutmut_6 # type: ignore # mutmut generated
mutants_x_score__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_score__mutmut)
def score(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_orig(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_1(snap: ClusterHealthSnapshot) -> float:
    normalized = None
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_2(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(None)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_3(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5 - snap.nodes_not_ready * 10
    )


def x_score__mutmut_4(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01 - snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_5(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2 - snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_6(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized / 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_7(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 3
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_8(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct / 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_9(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 1.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_10(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents / 5
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_11(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 6
        + snap.nodes_not_ready * 10
    )


def x_score__mutmut_12(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready / 10
    )


def x_score__mutmut_13(snap: ClusterHealthSnapshot) -> float:
    normalized = _failing_per_100(snap)
    return (
        normalized * 2
        + snap.cpu_utilization_pct * 0.01
        + snap.active_incidents * 5
        + snap.nodes_not_ready * 11
    )

mutants_x_score__mutmut['_mutmut_orig'] = x_score__mutmut_orig # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_1'] = x_score__mutmut_1 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_2'] = x_score__mutmut_2 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_3'] = x_score__mutmut_3 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_4'] = x_score__mutmut_4 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_5'] = x_score__mutmut_5 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_6'] = x_score__mutmut_6 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_7'] = x_score__mutmut_7 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_8'] = x_score__mutmut_8 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_9'] = x_score__mutmut_9 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_10'] = x_score__mutmut_10 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_11'] = x_score__mutmut_11 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_12'] = x_score__mutmut_12 # type: ignore # mutmut generated
mutants_x_score__mutmut['x_score__mutmut_13'] = x_score__mutmut_13 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__unreachable_result__mutmut)
def _unreachable_result(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_orig(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_1(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = None
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_2(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable or not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_3(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_4(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_5(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=None,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_6(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=None,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_7(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=None,
    )


def x__unreachable_result__mutmut_8(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_9(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_10(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        )


def x__unreachable_result__mutmut_11(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=None,
        ),
    )


def x__unreachable_result__mutmut_12(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            reason="both_clusters_unreachable" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_13(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            ),
    )


def x__unreachable_result__mutmut_14(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="XXboth_clusters_unreachableXX" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_15(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="BOTH_CLUSTERS_UNREACHABLE" if both else "partial_comparison_unreachable",
        ),
    )


def x__unreachable_result__mutmut_16(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "XXpartial_comparison_unreachableXX",
        ),
    )


def x__unreachable_result__mutmut_17(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    both = not cluster_a.reachable and not cluster_b.reachable
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason="both_clusters_unreachable" if both else "PARTIAL_COMPARISON_UNREACHABLE",
        ),
    )

mutants_x__unreachable_result__mutmut['_mutmut_orig'] = x__unreachable_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_1'] = x__unreachable_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_2'] = x__unreachable_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_3'] = x__unreachable_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_4'] = x__unreachable_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_5'] = x__unreachable_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_6'] = x__unreachable_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_7'] = x__unreachable_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_8'] = x__unreachable_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_9'] = x__unreachable_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_10'] = x__unreachable_result__mutmut_10 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_11'] = x__unreachable_result__mutmut_11 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_12'] = x__unreachable_result__mutmut_12 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_13'] = x__unreachable_result__mutmut_13 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_14'] = x__unreachable_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_15'] = x__unreachable_result__mutmut_15 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_16'] = x__unreachable_result__mutmut_16 # type: ignore # mutmut generated
mutants_x__unreachable_result__mutmut['x__unreachable_result__mutmut_17'] = x__unreachable_result__mutmut_17 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__maintenance_result__mutmut)
def _maintenance_result(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_orig(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_1(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = None
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_2(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=None,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_3(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=None,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_4(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=None,
    )


def x__maintenance_result__mutmut_5(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_6(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_7(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        )


def x__maintenance_result__mutmut_8(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            reason=None,
        ),
    )


def x__maintenance_result__mutmut_9(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            reason=f"{maint.cluster_name} is in maintenance (not degraded)",
        ),
    )


def x__maintenance_result__mutmut_10(
    cluster_a: ClusterHealthSnapshot,
    cluster_b: ClusterHealthSnapshot,
) -> HealthComparisonResult:
    maint = cluster_a if cluster_a.in_maintenance else cluster_b
    return HealthComparisonResult(
        cluster_a=cluster_a,
        cluster_b=cluster_b,
        comparison=ComparisonReport(
            worse_cluster=None,
            ),
    )

mutants_x__maintenance_result__mutmut['_mutmut_orig'] = x__maintenance_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_1'] = x__maintenance_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_2'] = x__maintenance_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_3'] = x__maintenance_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_4'] = x__maintenance_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_5'] = x__maintenance_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_6'] = x__maintenance_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_7'] = x__maintenance_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_8'] = x__maintenance_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_9'] = x__maintenance_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__maintenance_result__mutmut['x__maintenance_result__mutmut_10'] = x__maintenance_result__mutmut_10 # type: ignore # mutmut generated
