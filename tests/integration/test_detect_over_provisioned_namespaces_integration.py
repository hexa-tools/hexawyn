"""Integration tests: DetectOverProvisionedNamespacesUseCase → service → VanillaAdapter.

Uses a real VanillaAdapter wired with fake K8s clients — no cluster needed.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.service.detect_over_provisioned_namespaces_service import (
    DetectOverProvisionedNamespacesService,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_use_case import (  # noqa: E501
    DetectOverProvisionedNamespacesUseCase,
)
from hexawyn.domain.errors import ClusterUnreachableError, PrometheusUnavailableError


def _container(cpu: str | None = "500m", memory: str | None = "1Gi") -> MagicMock:
    c = MagicMock()
    requests: dict[str, str] = {}
    if cpu:
        requests["cpu"] = cpu
    if memory:
        requests["memory"] = memory
    c.resources.requests = requests or None
    return c


def _pod(namespace: str, cpu: str | None = "500m", memory: str | None = "1Gi") -> MagicMock:
    pod = MagicMock()
    pod.metadata.namespace = namespace
    pod.spec.containers = [_container(cpu, memory)]
    return pod


def _ns_obj(name: str, age_hours: float = 720.0) -> MagicMock:
    ns = MagicMock()
    ns.metadata.name = name
    ns.metadata.creation_timestamp = datetime.now(UTC) - timedelta(hours=age_hours)
    return ns


def _fake_core_api(pods: list[MagicMock], namespaces: list[MagicMock]) -> MagicMock:
    api = MagicMock()
    pod_list = MagicMock()
    pod_list.items = pods
    ns_list = MagicMock()
    ns_list.items = namespaces
    api.list_pod_for_all_namespaces.return_value = pod_list
    api.list_namespace.return_value = ns_list
    return api


def _build_use_case(
    api: MagicMock, prometheus_url: str = ""
) -> DetectOverProvisionedNamespacesUseCase:
    adapter = VanillaAdapter("test-cluster", api=api, prometheus_url=prometheus_url)
    service = DetectOverProvisionedNamespacesService(waste_port=adapter)
    return DetectOverProvisionedNamespacesUseCase(service=service)


class TestDetectOverProvisionedNamespacesIntegration:
    def test_vanilla_adapter_implements_waste_port(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort

        assert isinstance(VanillaAdapter("test"), NamespaceWasteAnalysisPort)

    def test_tc1_dev_flagged_production_healthy(self) -> None:
        # CPU only — avoids ambiguity from memory Prometheus response
        pods = [
            _pod("dev", cpu="8000m", memory=None),
            _pod("production", cpu="4000m", memory=None),
        ]
        ns_objs = [_ns_obj("dev"), _ns_obj("production")]
        api = _fake_core_api(pods, ns_objs)

        cpu_payload = {
            "status": "success",
            "data": {
                "resultType": "vector",
                "result": [
                    {"metric": {"namespace": "dev"}, "value": [0, "0.45"]},
                    {"metric": {"namespace": "production"}, "value": [0, "3.5"]},
                ],
            },
        }

        with patch("httpx.get") as mock_get:
            resp = MagicMock()
            resp.json.return_value = cpu_payload
            resp.raise_for_status.return_value = None
            mock_get.return_value = resp
            result = _build_use_case(api, "http://prometheus:9090").execute(
                DetectOverProvisionedNamespacesCommand()
            )

        ns_map = {ns.namespace: ns for ns in result.report.namespaces}
        assert ns_map["dev"].is_over_provisioned is True
        assert ns_map["production"].is_over_provisioned is False

    def test_tc1_dev_ranked_first(self) -> None:
        pods = [_pod("production", cpu="4000m", memory=None), _pod("dev", cpu="8000m", memory=None)]
        ns_objs = [_ns_obj("production"), _ns_obj("dev")]
        api = _fake_core_api(pods, ns_objs)

        cpu_payload = {
            "status": "success",
            "data": {
                "resultType": "vector",
                "result": [
                    {"metric": {"namespace": "dev"}, "value": [0, "0.45"]},
                    {"metric": {"namespace": "production"}, "value": [0, "3.5"]},
                ],
            },
        }
        with patch("httpx.get") as mock_get:
            resp = MagicMock()
            resp.json.return_value = cpu_payload
            resp.raise_for_status.return_value = None
            mock_get.return_value = resp
            result = _build_use_case(api, "http://prometheus:9090").execute(
                DetectOverProvisionedNamespacesCommand()
            )

        assert result.report.namespaces[0].namespace == "dev"

    def test_tc2_recently_created_namespace_excluded(self) -> None:
        pods = [_pod("new-ns", cpu="4000m")]
        ns_objs = [_ns_obj("new-ns", age_hours=6.0)]
        api = _fake_core_api(pods, ns_objs)
        use_case = _build_use_case(api)

        result = use_case.execute(DetectOverProvisionedNamespacesCommand())

        assert result.report.namespaces == []
        excluded_names = [e.namespace for e in result.report.excluded]
        assert "new-ns" in excluded_names

    def test_no_prometheus_returns_namespace_without_waste(self) -> None:
        pods = [_pod("dev", cpu="8000m")]
        ns_objs = [_ns_obj("dev")]
        api = _fake_core_api(pods, ns_objs)
        use_case = _build_use_case(api, prometheus_url="")

        result = use_case.execute(DetectOverProvisionedNamespacesCommand())

        assert result.prometheus_available is False
        assert result.report.namespaces[0].cpu_waste_pct == 0.0

    def test_k8s_unreachable_raises_error(self) -> None:
        api = MagicMock()
        api.list_namespace.side_effect = Exception("timeout")
        use_case = _build_use_case(api)

        with pytest.raises(ClusterUnreachableError):
            use_case.execute(DetectOverProvisionedNamespacesCommand())

    def test_prometheus_unavailable_raises_error(self) -> None:
        import httpx

        pods = [_pod("dev", cpu="8000m")]
        ns_objs = [_ns_obj("dev")]
        api = _fake_core_api(pods, ns_objs)
        use_case = _build_use_case(api, prometheus_url="http://prometheus:9090")

        with patch("httpx.get", side_effect=httpx.HTTPError("timeout")):
            with pytest.raises(PrometheusUnavailableError):
                use_case.execute(DetectOverProvisionedNamespacesCommand())

    def test_top_n_limits_results(self) -> None:
        pods = [_pod(f"ns-{i}", cpu=f"{(i + 1) * 1000}m") for i in range(10)]
        ns_objs = [_ns_obj(f"ns-{i}") for i in range(10)]
        api = _fake_core_api(pods, ns_objs)
        use_case = _build_use_case(api)

        result = use_case.execute(DetectOverProvisionedNamespacesCommand(top_n=3))

        assert len(result.report.namespaces) <= 3  # noqa: PLR2004

    def test_waste_ratio_formula_correct(self) -> None:
        pods = [_pod("dev", cpu="8000m", memory=None)]
        ns_objs = [_ns_obj("dev")]
        api = _fake_core_api(pods, ns_objs)

        prometheus_payload = {
            "status": "success",
            "data": {
                "resultType": "vector",
                "result": [{"metric": {"namespace": "dev"}, "value": [0, "0.5"]}],
            },
        }
        with patch("httpx.get") as mock_get:
            resp = MagicMock()
            resp.json.return_value = prometheus_payload
            resp.raise_for_status.return_value = None
            mock_get.return_value = resp
            result = _build_use_case(api, "http://prometheus:9090").execute(
                DetectOverProvisionedNamespacesCommand()
            )

        dev = result.report.namespaces[0]
        # (8.0 - 0.5) / 8.0 * 100 = 93.75%
        assert round(dev.cpu_waste_pct, 1) == pytest.approx(93.75, abs=0.1)
