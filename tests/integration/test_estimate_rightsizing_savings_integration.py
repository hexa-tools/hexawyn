"""Integration tests: EstimateRightsizingSavingsUseCase → service → VanillaAdapter.

Uses a real VanillaAdapter wired with fake K8s clients — no cluster needed.
"""

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.use_case.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.service.estimate_rightsizing_savings_service import (
    EstimateRightsizingSavingsService,
)
from hexawyn.application.use_case.estimate_rightsizing_savings.estimate_rightsizing_savings_use_case import (
    EstimateRightsizingSavingsUseCase,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.rightsizing import RightsizingType


def _container(cpu: str | None = "2000m", memory: str | None = "4Gi") -> MagicMock:
    c = MagicMock()
    requests: dict[str, str] = {}
    if cpu:
        requests["cpu"] = cpu
    if memory:
        requests["memory"] = memory
    c.resources.requests = requests or None
    return c


def _deployment(
    name: str, namespace: str, cpu: str | None = "2000m", memory: str | None = "4Gi"
) -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.metadata.namespace = namespace
    dep.spec.replicas = 1
    dep.spec.template.spec.containers = [_container(cpu, memory)]
    return dep


def _pod_metric(
    deployment_name: str, namespace: str, cpu: str = "400m", mem_bytes: str = "1073741824"
) -> dict[str, object]:
    return {
        "metadata": {"name": f"{deployment_name}-7d6b8-x4m2p", "namespace": namespace},
        "containers": [{"usage": {"cpu": cpu, "memory": mem_bytes}}],
    }


def _fake_apps_api(deployments: list[MagicMock]) -> MagicMock:
    api = MagicMock()
    dep_list = MagicMock()
    dep_list.items = deployments
    api.list_deployment_for_all_namespaces.return_value = dep_list
    sts_list = MagicMock()
    sts_list.items = []
    api.list_stateful_set_for_all_namespaces.return_value = sts_list
    return api


def _fake_metrics_api(pod_metrics: list[dict[str, object]]) -> MagicMock:
    api = MagicMock()
    api.list_cluster_custom_object.return_value = {"items": pod_metrics}
    return api


def _build_use_case(
    apps_api: MagicMock, metrics_api: MagicMock | None = None
) -> EstimateRightsizingSavingsUseCase:
    adapter = VanillaAdapter("test", apps_api=apps_api, metrics_api=metrics_api)
    service = EstimateRightsizingSavingsService(rightsizing_port=adapter)
    return EstimateRightsizingSavingsUseCase(service=service)


class TestEstimateRightsizingSavingsIntegration:
    # TC1 — over-provisioned deployment detected (CPU at 20% of requests)
    def test_tc1_over_provisioned_deployment_flagged(self) -> None:
        # 2 cores requested, 400m = 0.4 cores actual → 20% utilisation
        deps = [_deployment("ml-worker", "production", cpu="2000m", memory="4Gi")]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api(
            [_pod_metric("ml-worker", "production", cpu="400m", mem_bytes="858993459")]
        )  # 819 Mi ≈ 20% of 4Gi
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=5))

        assert response.metrics_server_available is True
        recs = response.report.recommendations
        assert len(recs) == 1
        assert recs[0].resource_name == "ml-worker"
        assert recs[0].rightsizing_type == RightsizingType.OVER_PROVISIONED

    # TC2 — monthly savings positive for over-provisioned
    def test_tc2_savings_are_positive_for_over_provisioned(self) -> None:
        deps = [_deployment("ml-worker", "production", cpu="2000m", memory="4Gi")]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api(
            [_pod_metric("ml-worker", "production", cpu="400m", mem_bytes="858993459")]
        )
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand())

        assert response.report.total_monthly_savings_usd > 0

    # TC3 — metrics-server unavailable → flag, no actual, skipped
    def test_tc3_no_metrics_server_metrics_unavailable(self) -> None:
        deps = [_deployment("api", "production")]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api([])
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand())

        assert response.metrics_server_available is False
        assert response.report.recommendations == []

    # TC4 — under-provisioned deployment (RAM at 90% of requests)
    def test_tc4_under_provisioned_flagged(self) -> None:
        # 1 GiB requested, 972 MiB actual = 95%
        deps = [_deployment("cache", "production", cpu="1000m", memory="1Gi")]
        apps_api = _fake_apps_api(deps)
        mem_bytes = str(int(972 * 1024 * 1024))
        metrics_api = _fake_metrics_api(
            [_pod_metric("cache", "production", cpu="800m", mem_bytes=mem_bytes)]
        )
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand())

        recs = response.report.recommendations
        assert any(r.rightsizing_type == RightsizingType.UNDER_PROVISIONED for r in recs)

    # TC5 — top_n limits results
    def test_tc5_top_n_limits_recommendations(self) -> None:
        deps = [_deployment(f"svc-{i}", "ns", cpu="4000m", memory="8Gi") for i in range(10)]
        apps_api = _fake_apps_api(deps)
        pod_metrics = [
            _pod_metric(f"svc-{i}", "ns", cpu="400m", mem_bytes="858993459") for i in range(10)
        ]
        metrics_api = _fake_metrics_api(pod_metrics)
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand(top_n=3))

        assert len(response.report.recommendations) <= 3

    # TC6 — K8s unreachable raises ClusterUnreachableError
    def test_tc6_cluster_unreachable_raises(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("connection refused")
        use_case = _build_use_case(apps_api)

        with pytest.raises(ClusterUnreachableError):
            use_case.execute(EstimateRightsizingSavingsCommand())

    # TC7 — optimal workload not included in recommendations
    def test_tc7_optimal_workload_excluded(self) -> None:
        # CPU at 60% (above 30% over threshold), RAM at 60% (above 40% over, below 85% under) → OPTIMAL
        deps = [_deployment("web", "production", cpu="1000m", memory="2Gi")]
        apps_api = _fake_apps_api(deps)
        mem_bytes = str(int(0.6 * 2048 * 1024 * 1024))
        metrics_api = _fake_metrics_api(
            [_pod_metric("web", "production", cpu="600m", mem_bytes=mem_bytes)]
        )
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand())

        assert response.report.recommendations == []

    # TC8 — deployment with no resource requests → zero requested cores, skipped
    def test_tc8_deployment_without_resource_requests_skipped(self) -> None:
        deps = [_deployment("bare", "ns", cpu=None, memory=None)]
        apps_api = _fake_apps_api(deps)
        metrics_api = _fake_metrics_api(
            [_pod_metric("bare", "ns", cpu="100m", mem_bytes="104857600")]
        )
        use_case = _build_use_case(apps_api, metrics_api)

        response = use_case.execute(EstimateRightsizingSavingsCommand())

        # No recommendations when there are no resource requests to compare against
        assert response.report.recommendations == []
