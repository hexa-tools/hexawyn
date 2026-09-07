from __future__ import annotations

from hexawyn.application.ports.driven.namespace_overview_port import (
    DeploymentStatusRaw,
    PodStatusRaw,
)
from hexawyn.domain.models.namespace_overview import NamespaceCounts


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_aggregate_counts__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_aggregate_counts__mutmut)
def aggregate_counts(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_orig(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_1(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = None
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_2(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(None)
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_3(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(2 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_4(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["XXstatusXX"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_5(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["STATUS"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_6(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] != "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_7(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "XXRunningXX")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_8(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_9(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "RUNNING")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_10(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = None

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_11(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        None
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_12(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        2
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_13(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["XXready_replicasXX"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_14(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["READY_REPLICAS"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_15(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] > deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_16(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["XXdesired_replicasXX"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_17(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["DESIRED_REPLICAS"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_18(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=None,
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_19(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=None,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_20(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=None,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_21(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=None,
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_22(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=None,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_23(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=None,
    )


def x_aggregate_counts__mutmut_24(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_25(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_26(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_27(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_ready=ready_deployments,
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_28(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        services_total=services_count,
    )


def x_aggregate_counts__mutmut_29(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) - running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        )


def x_aggregate_counts__mutmut_30(
    pods: list[PodStatusRaw], deployments: list[DeploymentStatusRaw], services_count: int
) -> NamespaceCounts:
    running = sum(1 for pod in pods if pod["status"] == "Running")
    ready_deployments = sum(
        1
        for deployment in deployments
        if deployment["ready_replicas"] >= deployment["desired_replicas"]
    )

    return NamespaceCounts(
        pods_total=len(pods),
        pods_running=running,
        pods_failed=len(pods) + running,
        deployments_total=len(deployments),
        deployments_ready=ready_deployments,
        services_total=services_count,
    )

mutants_x_aggregate_counts__mutmut['_mutmut_orig'] = x_aggregate_counts__mutmut_orig # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_1'] = x_aggregate_counts__mutmut_1 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_2'] = x_aggregate_counts__mutmut_2 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_3'] = x_aggregate_counts__mutmut_3 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_4'] = x_aggregate_counts__mutmut_4 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_5'] = x_aggregate_counts__mutmut_5 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_6'] = x_aggregate_counts__mutmut_6 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_7'] = x_aggregate_counts__mutmut_7 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_8'] = x_aggregate_counts__mutmut_8 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_9'] = x_aggregate_counts__mutmut_9 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_10'] = x_aggregate_counts__mutmut_10 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_11'] = x_aggregate_counts__mutmut_11 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_12'] = x_aggregate_counts__mutmut_12 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_13'] = x_aggregate_counts__mutmut_13 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_14'] = x_aggregate_counts__mutmut_14 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_15'] = x_aggregate_counts__mutmut_15 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_16'] = x_aggregate_counts__mutmut_16 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_17'] = x_aggregate_counts__mutmut_17 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_18'] = x_aggregate_counts__mutmut_18 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_19'] = x_aggregate_counts__mutmut_19 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_20'] = x_aggregate_counts__mutmut_20 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_21'] = x_aggregate_counts__mutmut_21 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_22'] = x_aggregate_counts__mutmut_22 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_23'] = x_aggregate_counts__mutmut_23 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_24'] = x_aggregate_counts__mutmut_24 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_25'] = x_aggregate_counts__mutmut_25 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_26'] = x_aggregate_counts__mutmut_26 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_27'] = x_aggregate_counts__mutmut_27 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_28'] = x_aggregate_counts__mutmut_28 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_29'] = x_aggregate_counts__mutmut_29 # type: ignore # mutmut generated
mutants_x_aggregate_counts__mutmut['x_aggregate_counts__mutmut_30'] = x_aggregate_counts__mutmut_30 # type: ignore # mutmut generated
