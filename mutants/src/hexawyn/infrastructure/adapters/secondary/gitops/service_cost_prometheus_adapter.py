from __future__ import annotations

from hexawyn.application.ports.driven.service_cost_port import (
    PodResourceSnapshotData,
    ServiceCostPort,
)
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import (
    query_prometheus_instant,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut: MutantDict = {}  # type: ignore


class ServiceCostPrometheusAdapter(ServiceCostPort):
    @_mutmut_mutated(mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut)
    def fetch_pod_resources(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_orig(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_1(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = None
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_2(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = None
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_3(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = None
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_4(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(None)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_5(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = None

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_6(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(None)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_7(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = None
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_8(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = None
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_9(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get(None, '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_10(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', None)}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_11(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_12(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', )}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_13(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['XXlabelsXX'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_14(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['LABELS'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_15(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('XXnamespaceXX', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_16(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('NAMESPACE', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_17(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', 'XXXX')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_18(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get(None, '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_19(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', None)}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_20(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_21(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', )}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_22(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['XXlabelsXX'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_23(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['LABELS'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_24(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('XXpodXX', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_25(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('POD', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_26(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', 'XXXX')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_27(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = None

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_28(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["XXvalueXX"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_29(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["VALUE"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_30(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = None
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_31(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = None
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_32(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get(None, "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_33(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", None)
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_34(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_35(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", )
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_36(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["XXlabelsXX"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_37(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["LABELS"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_38(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("XXnamespaceXX", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_39(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("NAMESPACE", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_40(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "XXXX")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_41(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = None
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_42(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get(None, "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_43(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", None)
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_44(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_45(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", )
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_46(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["XXlabelsXX"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_47(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["LABELS"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_48(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("XXpodXX", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_49(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("POD", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_50(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "XXXX")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_51(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = None
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_52(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    None
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_53(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=None,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_54(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=None,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_55(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=None,
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_56(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=None,
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_57(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_58(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_59(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_60(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_61(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["XXvalueXX"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_62(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["VALUE"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_63(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(None, 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_64(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), None),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_65(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_66(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), ),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_67(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) * (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_68(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(None, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_69(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, None) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_70(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_71(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, ) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_72(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 1) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_73(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 / 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_74(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1025 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_75(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1025), 2),
                    )
                )
            return result
        except Exception:
            return []
    def xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_76(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 3),
                    )
                )
            return result
        except Exception:
            return []

mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['_mutmut_orig'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_1'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_1 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_2'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_2 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_3'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_3 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_4'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_4 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_5'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_5 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_6'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_6 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_7'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_7 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_8'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_8 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_9'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_9 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_10'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_10 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_11'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_11 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_12'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_12 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_13'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_13 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_14'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_14 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_15'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_15 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_16'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_16 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_17'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_17 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_18'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_18 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_19'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_19 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_20'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_20 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_21'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_21 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_22'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_22 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_23'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_23 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_24'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_24 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_25'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_25 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_26'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_26 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_27'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_27 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_28'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_28 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_29'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_29 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_30'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_30 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_31'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_31 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_32'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_32 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_33'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_33 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_34'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_34 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_35'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_35 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_36'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_36 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_37'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_37 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_38'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_38 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_39'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_39 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_40'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_40 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_41'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_41 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_42'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_42 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_43'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_43 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_44'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_44 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_45'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_45 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_46'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_46 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_47'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_47 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_48'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_48 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_49'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_49 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_50'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_50 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_51'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_51 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_52'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_52 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_53'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_53 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_54'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_54 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_55'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_55 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_56'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_56 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_57'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_57 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_58'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_58 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_59'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_59 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_60'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_60 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_61'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_61 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_62'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_62 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_63'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_63 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_64'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_64 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_65'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_65 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_66'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_66 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_67'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_67 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_68'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_68 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_69'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_69 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_70'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_70 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_71'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_71 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_72'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_72 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_73'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_73 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_74'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_74 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_75'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_75 # type: ignore # mutmut generated
mutants_xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut['xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_76'] = ServiceCostPrometheusAdapter.xǁServiceCostPrometheusAdapterǁfetch_pod_resources__mutmut_76 # type: ignore # mutmut generated
