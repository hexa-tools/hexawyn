from __future__ import annotations

from collections import defaultdict
from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
    NodeUtilizationSeries,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import (
    HotNodeAnalysisPort,
    PodUsageRaw,
)
from hexawyn.application.use_case.cluster.hot_node_analysis.command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.use_case.cluster.hot_node_analysis.response import (
    HotNodeAnalysisResponse,
    HotNodeResultDict,
    TopConsumerDict,
)
from hexawyn.domain.models.hot_node_analysis import (
    ClusterNodeSnapshot,
    HotNodeAnalysisReport,
    HotNodeAnalysisRequest,
    HotNodeResult,
    TopConsumer,
)
from hexawyn.domain.services.hot_node_analysis.node_analysis_builder import analyze_hot_nodes

_QUERY_TIMEOUT_SECONDS = 15.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHotNodeAnalysisUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class HotNodeAnalysisUseCase:
    @_mutmut_mutated(mutants_xǁHotNodeAnalysisUseCaseǁ__init____mutmut)
    def __init__(
        self, metrics_port: ClusterResourceMetricsPort, node_port: HotNodeAnalysisPort
    ) -> None:
        self._metrics_port = metrics_port
        self._node_port = node_port
    def xǁHotNodeAnalysisUseCaseǁ__init____mutmut_orig(
        self, metrics_port: ClusterResourceMetricsPort, node_port: HotNodeAnalysisPort
    ) -> None:
        self._metrics_port = metrics_port
        self._node_port = node_port
    def xǁHotNodeAnalysisUseCaseǁ__init____mutmut_1(
        self, metrics_port: ClusterResourceMetricsPort, node_port: HotNodeAnalysisPort
    ) -> None:
        self._metrics_port = None
        self._node_port = node_port
    def xǁHotNodeAnalysisUseCaseǁ__init____mutmut_2(
        self, metrics_port: ClusterResourceMetricsPort, node_port: HotNodeAnalysisPort
    ) -> None:
        self._metrics_port = metrics_port
        self._node_port = None

    @_mutmut_mutated(mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut)
    def execute(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_orig(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_1(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = None
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_2(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(None)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_3(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = None

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_4(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end + timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_5(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=None)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_6(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = None

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_7(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            None, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_8(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, None, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_9(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=None
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_10(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_11(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_12(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_13(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = None
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_14(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = None

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_15(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(None)

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_16(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = None

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_17(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=None,
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_18(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=None,
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_19(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=None,
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_20(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=None,
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_21(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=None,
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_22(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=None,
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_23(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=None,
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_24(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_25(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_26(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_27(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_28(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_29(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_30(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_31(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["XXnameXX"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_32(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["NAME"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_33(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["XXcordonedXX"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_34(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["CORDONED"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_35(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["XXallocatable_cpu_coresXX"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_36(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["ALLOCATABLE_CPU_CORES"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_37(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["XXallocatable_memory_gbXX"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_38(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["ALLOCATABLE_MEMORY_GB"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_39(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(None, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_40(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, None)[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_41(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_42(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, )[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_43(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["XXnameXX"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_44(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["NAME"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_45(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "XXcpu_percent_seriesXX"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_46(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "CPU_PERCENT_SERIES"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_47(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(None, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_48(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, None)[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_49(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_50(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, )[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_51(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["XXnameXX"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_52(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["NAME"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_53(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "XXmemory_percent_seriesXX"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_54(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "MEMORY_PERCENT_SERIES"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_55(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(None, []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_56(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], None),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_57(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get([]),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_58(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], ),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_59(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["XXnameXX"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_60(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["NAME"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_61(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = None
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_62(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            None, snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_63(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), None
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_64(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_65(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_66(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=None), snapshots
        )
        return _to_response(report)

    def xǁHotNodeAnalysisUseCaseǁexecute__mutmut_67(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(None)

mutants_xǁHotNodeAnalysisUseCaseǁ__init____mutmut['_mutmut_orig'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁ__init____mutmut['xǁHotNodeAnalysisUseCaseǁ__init____mutmut_1'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁ__init____mutmut['xǁHotNodeAnalysisUseCaseǁ__init____mutmut_2'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['_mutmut_orig'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_1'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_2'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_3'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_4'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_5'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_6'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_7'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_8'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_9'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_10'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_11'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_12'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_13'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_14'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_15'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_16'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_17'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_18'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_19'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_20'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_21'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_22'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_23'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_24'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_25'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_26'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_27'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_28'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_29'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_30'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_31'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_32'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_33'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_34'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_35'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_36'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_37'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_38'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_39'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_40'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_41'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_42'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_43'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_44'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_45'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_46'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_47'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_48'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_49'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_50'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_51'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_52'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_53'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_54'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_55'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_56'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_57'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_58'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_59'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_60'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_61'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_62'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_63'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_64'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_65'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_66'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHotNodeAnalysisUseCaseǁexecute__mutmut['xǁHotNodeAnalysisUseCaseǁexecute__mutmut_67'] = HotNodeAnalysisUseCase.xǁHotNodeAnalysisUseCaseǁexecute__mutmut_67 # type: ignore # mutmut generated
mutants_x__node_series__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_series__mutmut)
def _node_series(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x__node_series__mutmut_orig(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x__node_series__mutmut_1(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) and {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x__node_series__mutmut_2(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(None) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x__node_series__mutmut_3(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "XXcpu_percent_seriesXX": [],
        "memory_percent_series": [],
    }


def x__node_series__mutmut_4(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "CPU_PERCENT_SERIES": [],
        "memory_percent_series": [],
    }


def x__node_series__mutmut_5(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "XXmemory_percent_seriesXX": [],
    }


def x__node_series__mutmut_6(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "MEMORY_PERCENT_SERIES": [],
    }

mutants_x__node_series__mutmut['_mutmut_orig'] = x__node_series__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_series__mutmut['x__node_series__mutmut_1'] = x__node_series__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_series__mutmut['x__node_series__mutmut_2'] = x__node_series__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_series__mutmut['x__node_series__mutmut_3'] = x__node_series__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_series__mutmut['x__node_series__mutmut_4'] = x__node_series__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_series__mutmut['x__node_series__mutmut_5'] = x__node_series__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_series__mutmut['x__node_series__mutmut_6'] = x__node_series__mutmut_6 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__group_non_daemonset_pods__mutmut)
def _group_non_daemonset_pods(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_orig(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_1(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = None
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_2(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(None)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_3(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["XXis_daemonsetXX"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_4(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["IS_DAEMONSET"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_5(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            break
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_6(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            None
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_7(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["XXnode_nameXX"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_8(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["NODE_NAME"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_9(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=None,
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_10(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=None,
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_11(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=None,
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_12(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=None,
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_13(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_14(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_15(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_16(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_17(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["XXpod_nameXX"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_18(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["POD_NAME"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_19(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["XXnamespaceXX"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_20(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["NAMESPACE"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_21(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["XXcpu_usage_coresXX"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_22(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["CPU_USAGE_CORES"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_23(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["XXmemory_usage_gbXX"],
            )
        )
    return pods_by_node


def x__group_non_daemonset_pods__mutmut_24(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["MEMORY_USAGE_GB"],
            )
        )
    return pods_by_node

mutants_x__group_non_daemonset_pods__mutmut['_mutmut_orig'] = x__group_non_daemonset_pods__mutmut_orig # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_1'] = x__group_non_daemonset_pods__mutmut_1 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_2'] = x__group_non_daemonset_pods__mutmut_2 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_3'] = x__group_non_daemonset_pods__mutmut_3 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_4'] = x__group_non_daemonset_pods__mutmut_4 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_5'] = x__group_non_daemonset_pods__mutmut_5 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_6'] = x__group_non_daemonset_pods__mutmut_6 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_7'] = x__group_non_daemonset_pods__mutmut_7 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_8'] = x__group_non_daemonset_pods__mutmut_8 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_9'] = x__group_non_daemonset_pods__mutmut_9 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_10'] = x__group_non_daemonset_pods__mutmut_10 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_11'] = x__group_non_daemonset_pods__mutmut_11 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_12'] = x__group_non_daemonset_pods__mutmut_12 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_13'] = x__group_non_daemonset_pods__mutmut_13 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_14'] = x__group_non_daemonset_pods__mutmut_14 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_15'] = x__group_non_daemonset_pods__mutmut_15 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_16'] = x__group_non_daemonset_pods__mutmut_16 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_17'] = x__group_non_daemonset_pods__mutmut_17 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_18'] = x__group_non_daemonset_pods__mutmut_18 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_19'] = x__group_non_daemonset_pods__mutmut_19 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_20'] = x__group_non_daemonset_pods__mutmut_20 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_21'] = x__group_non_daemonset_pods__mutmut_21 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_22'] = x__group_non_daemonset_pods__mutmut_22 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_23'] = x__group_non_daemonset_pods__mutmut_23 # type: ignore # mutmut generated
mutants_x__group_non_daemonset_pods__mutmut['x__group_non_daemonset_pods__mutmut_24'] = x__group_non_daemonset_pods__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_orig(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_1(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=None,
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_2(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=None,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_3(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=None,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_4(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=None,
        summary=report.summary,
    )


def x__to_response__mutmut_5(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=None,
    )


def x__to_response__mutmut_6(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_7(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_8(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        warnings=report.warnings,
        summary=report.summary,
    )


def x__to_response__mutmut_9(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        summary=report.summary,
    )


def x__to_response__mutmut_10(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        )


def x__to_response__mutmut_11(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(None) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_hot_node_dict__mutmut)
def _to_hot_node_dict(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_orig(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_1(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=None,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_2(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=None,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_3(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=None,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_4(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=None,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_5(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=None,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_6(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=None,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_7(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=None,  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_8(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=None,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_9(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=None,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_10(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=None,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_11(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=None,
    )


def x__to_hot_node_dict__mutmut_12(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_13(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_14(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_15(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_16(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_17(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_18(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_19(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_20(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_21(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        business_hours_pattern=result.business_hours_pattern,
    )


def x__to_hot_node_dict__mutmut_22(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        )


def x__to_hot_node_dict__mutmut_23(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(None) for consumer in result.top_consumers],  # type: ignore
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )

mutants_x__to_hot_node_dict__mutmut['_mutmut_orig'] = x__to_hot_node_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_1'] = x__to_hot_node_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_2'] = x__to_hot_node_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_3'] = x__to_hot_node_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_4'] = x__to_hot_node_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_5'] = x__to_hot_node_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_6'] = x__to_hot_node_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_7'] = x__to_hot_node_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_8'] = x__to_hot_node_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_9'] = x__to_hot_node_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_10'] = x__to_hot_node_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_11'] = x__to_hot_node_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_12'] = x__to_hot_node_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_13'] = x__to_hot_node_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_14'] = x__to_hot_node_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_15'] = x__to_hot_node_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_16'] = x__to_hot_node_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_17'] = x__to_hot_node_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_18'] = x__to_hot_node_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_19'] = x__to_hot_node_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_20'] = x__to_hot_node_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_21'] = x__to_hot_node_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_22'] = x__to_hot_node_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_hot_node_dict__mutmut['x__to_hot_node_dict__mutmut_23'] = x__to_hot_node_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_consumer_dict__mutmut)
def _to_consumer_dict(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_orig(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_1(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=None,
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_2(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=None,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_3(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        cpu_usage_cores=None,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_4(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=None,
    )


def x__to_consumer_dict__mutmut_5(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_6(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_7(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        memory_usage_gb=consumer.memory_usage_gb,
    )


def x__to_consumer_dict__mutmut_8(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        )

mutants_x__to_consumer_dict__mutmut['_mutmut_orig'] = x__to_consumer_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_1'] = x__to_consumer_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_2'] = x__to_consumer_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_3'] = x__to_consumer_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_4'] = x__to_consumer_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_5'] = x__to_consumer_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_6'] = x__to_consumer_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_7'] = x__to_consumer_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_consumer_dict__mutmut['x__to_consumer_dict__mutmut_8'] = x__to_consumer_dict__mutmut_8 # type: ignore # mutmut generated
