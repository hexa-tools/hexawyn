"""Tests for resource_parsers module-level functions."""

# ruff: noqa: PLR2004

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _BYTES_TO_MI,
    _CPU_COST_PER_CORE_DAY,
    _CPU_MILLI_FACTOR,
    _MEM_COST_PER_GIB_DAY,
    _MEM_GIB_FACTOR,
    _NANOCORES_FACTOR,
    _build_daily_cost_entries,
    _compute_namespace_daily_costs,
    _compute_pod_resources,
    _container_request,
    _deployment_key_from_pod,
    _extract_container_data,
    _extract_init_container_data,
    _get_workload_type,
    _parse_cpu,
    _parse_memory,
    _parse_memory_to_mi,
    _parse_nanocores,
    _parse_prometheus_pod_vector,
    _parse_prometheus_vector,
    _pod_containers,
    _pod_namespace,
    _pod_requests_and_limits,
    _sum_container_metrics,
    _workload_key_from_pod_name,
    _workload_resource_requests,
)


class TestConstants:
    def test_constants_are_defined(self) -> None:
        assert _CPU_MILLI_FACTOR == 1000.0
        assert _NANOCORES_FACTOR == 1_000_000_000.0
        assert _CPU_COST_PER_CORE_DAY == 21.6 / 30.0
        assert _MEM_COST_PER_GIB_DAY == 2.88 / 30.0
        assert _MEM_GIB_FACTOR == 1024**3
        assert _BYTES_TO_MI == 1024.0 * 1024.0


class TestParseCpu:
    def test_parse_millicores(self) -> None:
        assert _parse_cpu("500m") == 0.5

    def test_parse_cores(self) -> None:
        assert _parse_cpu("2") == 2.0

    def test_parse_zero(self) -> None:
        assert _parse_cpu("0") == 0.0

    def test_parse_float_cores(self) -> None:
        assert _parse_cpu("0.5") == 0.5

    def test_parse_large_millicores(self) -> None:
        assert _parse_cpu("2000m") == 2.0


class TestParseMemory:
    def test_parse_gib(self) -> None:
        result = _parse_memory("1Gi")
        assert abs(result - 1.0) < 0.001

    def test_parse_mib(self) -> None:
        result = _parse_memory("512Mi")
        assert abs(result - 0.5) < 0.001

    def test_parse_kib(self) -> None:
        result = _parse_memory("1048576Ki")
        assert abs(result - 1.0) < 0.001

    def test_parse_decimal_g(self) -> None:
        result = _parse_memory("1G")
        assert abs(result - 0.931) < 0.001

    def test_parse_decimal_m(self) -> None:
        result = _parse_memory("1000M")
        expected = 1000.0 / (1.073741824 * 1024)
        assert abs(result - expected) < 0.001

    def test_parse_decimal_k(self) -> None:
        result = _parse_memory("1000K")
        expected = 1000.0 / (1.073741824 * 1024 * 1024)
        assert abs(result - expected) < 0.001

    def test_parse_bytes_fallback(self) -> None:
        result = _parse_memory("1073741824")
        assert abs(result - 1.0) < 0.001


class TestParseNanocores:
    def test_parse_nanocores_input(self) -> None:
        assert _parse_nanocores("500000000n") == 0.5, "nanocores should convert to cores"

    def test_parse_millicores_input(self) -> None:
        result = _parse_nanocores("500m")
        assert abs(result - 0.5) < 0.001

    def test_parse_cores_input(self) -> None:
        assert _parse_nanocores("0.5") == 0.5


class TestParseMemoryToMi:
    def test_parse_ki(self) -> None:
        result = _parse_memory_to_mi("1024Ki")
        assert result == 1.0

    def test_parse_mi(self) -> None:
        result = _parse_memory_to_mi("512Mi")
        assert result == 512.0

    def test_parse_gi(self) -> None:
        result = _parse_memory_to_mi("1Gi")
        assert result == 1024.0

    def test_parse_ti(self) -> None:
        result = _parse_memory_to_mi("1Ti")
        assert result == 1024.0 * 1024.0

    def test_parse_bytes(self) -> None:
        result = _parse_memory_to_mi(str(int(1024.0 * 1024.0)))
        assert abs(result - 1.0) < 0.001

    def test_parse_k(self) -> None:
        result = _parse_memory_to_mi("1000000K")
        assert result > 0.0


class TestPodNamespace:
    def test_extract_namespace(self) -> None:
        pod = MagicMock()
        pod.metadata = MagicMock()
        pod.metadata.namespace = "default"
        assert _pod_namespace(pod) == "default"

    def test_no_metadata_returns_empty(self) -> None:
        pod = MagicMock()
        pod.metadata = None
        assert _pod_namespace(pod) == ""

    def test_namespace_none_returns_empty(self) -> None:
        pod = MagicMock()
        pod.metadata = MagicMock()
        pod.metadata.namespace = None
        assert _pod_namespace(pod) == ""


class TestPodContainers:
    def test_extract_containers(self) -> None:
        c1 = "container1"
        c2 = "container2"
        pod = MagicMock()
        pod.spec = MagicMock()
        pod.spec.containers = [c1, c2]
        result = _pod_containers(pod)
        assert result == [c1, c2]

    def test_no_spec_returns_empty(self) -> None:
        pod = MagicMock()
        pod.spec = None
        assert _pod_containers(pod) == []

    def test_no_containers_returns_empty(self) -> None:
        pod = MagicMock()
        pod.spec = MagicMock()
        pod.spec.containers = None
        assert _pod_containers(pod) == []


class TestContainerRequest:
    def test_cpu_request(self) -> None:
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = {"cpu": "500m"}
        result = _container_request(container, "cpu")
        assert result == 0.5

    def test_memory_request(self) -> None:
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = {"memory": "1Gi"}
        result = _container_request(container, "memory")
        assert abs(result - 1.0) < 0.001

    def test_no_resources(self) -> None:
        container = MagicMock()
        container.resources = None
        assert _container_request(container, "cpu") is None

    def test_no_requests_dict(self) -> None:
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = None
        assert _container_request(container, "cpu") is None

    def test_request_key_missing(self) -> None:
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = {"memory": "1Gi"}
        assert _container_request(container, "cpu") is None

    def test_unknown_resource_returns_none(self) -> None:
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = {"disk": "10G"}
        assert _container_request(container, "disk") is None


class TestComputePodResources:
    def test_sum_cpu_and_memory(self) -> None:
        c1 = MagicMock()
        c1.resources = MagicMock()
        c1.resources.requests = {"cpu": "500m", "memory": "1Gi"}
        c2 = MagicMock()
        c2.resources = MagicMock()
        c2.resources.requests = {"cpu": "1000m", "memory": "2Gi"}
        cpu, mem = _compute_pod_resources([c1, c2])
        assert cpu == 1.5
        assert mem == 3.0

    def test_missing_requests_ignored(self) -> None:
        c1 = MagicMock()
        c1.resources = None
        cpu, mem = _compute_pod_resources([c1])
        assert cpu == 0.0
        assert mem == 0.0

    def test_partial_requests(self) -> None:
        c = MagicMock()
        c.resources = MagicMock()
        c.resources.requests = {"cpu": "1"}
        cpu, mem = _compute_pod_resources([c])
        assert cpu == 1.0
        assert mem == 0.0


class TestComputeNamespaceDailyCosts:
    def test_single_deployment(self) -> None:
        dep = MagicMock()
        dep.metadata = MagicMock()
        dep.metadata.namespace = "default"
        spec = MagicMock()
        dep.spec = spec
        template = MagicMock()
        spec.template = template
        pod_spec = MagicMock()
        template.spec = pod_spec
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = {"cpu": "1", "memory": "2Gi"}
        pod_spec.containers = [container]
        result = _compute_namespace_daily_costs([dep])
        assert "default" in result
        assert result["default"] > 0.0

    def test_multiple_deployments_same_namespace(self) -> None:
        d1 = MagicMock()
        d1.metadata = MagicMock()
        d1.metadata.namespace = "ns1"
        spec1 = MagicMock()
        d1.spec = spec1
        t1 = MagicMock()
        spec1.template = t1
        ps1 = MagicMock()
        t1.spec = ps1
        c1 = MagicMock()
        c1.resources = MagicMock()
        c1.resources.requests = {"cpu": "1", "memory": "1Gi"}
        ps1.containers = [c1]

        d2 = MagicMock()
        d2.metadata = MagicMock()
        d2.metadata.namespace = "ns1"
        spec2 = MagicMock()
        d2.spec = spec2
        t2 = MagicMock()
        spec2.template = t2
        ps2 = MagicMock()
        t2.spec = ps2
        c2 = MagicMock()
        c2.resources = MagicMock()
        c2.resources.requests = {"cpu": "1", "memory": "1Gi"}
        ps2.containers = [c2]

        result = _compute_namespace_daily_costs([d1, d2])
        expected = 2.0 * _CPU_COST_PER_CORE_DAY + 2.0 * _MEM_COST_PER_GIB_DAY
        assert abs(result["ns1"] - expected) < 0.001

    def test_empty_deployments(self) -> None:
        result = _compute_namespace_daily_costs([])
        assert result == {}


class TestBuildDailyCostEntries:
    def test_creates_correct_count(self) -> None:
        ns_costs = {"default": 10.0, "kube-system": 5.0}
        entries = _build_daily_cost_entries(ns_costs, 15.0, 7)
        assert len(entries) == 7

    def test_each_entry_has_required_fields(self) -> None:
        ns_costs = {"default": 5.0}
        entries = _build_daily_cost_entries(ns_costs, 5.0, 3)
        for entry in entries:
            assert "date" in entry
            assert "total_usd" in entry
            assert "namespace_costs" in entry

    def test_namespace_costs_sorted_desc(self) -> None:
        ns_costs = {"small": 1.0, "large": 10.0, "medium": 5.0}
        entries = _build_daily_cost_entries(ns_costs, 16.0, 1)
        ns_list = entries[0]["namespace_costs"]
        costs = [ns["cost_usd"] for ns in ns_list]
        assert costs == sorted(costs, reverse=True)


class TestWorkloadResourceRequests:
    def test_single_container(self) -> None:
        dep = MagicMock()
        spec = MagicMock()
        dep.spec = spec
        template = MagicMock()
        spec.template = template
        pod_spec = MagicMock()
        template.spec = pod_spec
        container = MagicMock()
        container.resources = MagicMock()
        container.resources.requests = {"cpu": "1", "memory": "2Gi"}
        pod_spec.containers = [container]
        cpu, mem = _workload_resource_requests(dep)
        assert cpu == 1.0
        assert mem == 2048.0

    def test_no_spec_returns_zero(self) -> None:
        dep = MagicMock()
        dep.spec = None
        cpu, mem = _workload_resource_requests(dep)
        assert cpu == 0.0
        assert mem == 0.0

    def test_no_template_returns_zero(self) -> None:
        dep = MagicMock()
        dep.spec = MagicMock()
        dep.spec.template = None
        cpu, mem = _workload_resource_requests(dep)
        assert cpu == 0.0
        assert mem == 0.0


class TestSumContainerMetrics:
    def test_single_container(self) -> None:
        containers = [{"usage": {"cpu": "500m", "memory": "512Mi"}}]
        cpu, mem = _sum_container_metrics(containers)
        assert cpu == 0.5
        assert mem == 512.0

    def test_multiple_containers(self) -> None:
        containers = [
            {"usage": {"cpu": "500m", "memory": "512Mi"}},
            {"usage": {"cpu": "500m", "memory": "256Mi"}},
        ]
        cpu, mem = _sum_container_metrics(containers)
        assert cpu == 1.0
        assert mem == 768.0

    def test_non_list_returns_zero(self) -> None:
        cpu, mem = _sum_container_metrics("not_a_list")
        assert cpu == 0.0
        assert mem == 0.0

    def test_missing_usage(self) -> None:
        containers = [{"no_usage": {}}]
        cpu, mem = _sum_container_metrics(containers)
        assert cpu == 0.0
        assert mem == 0.0

    def test_usage_not_dict(self) -> None:
        containers = [{"usage": "not_a_dict"}]
        cpu, mem = _sum_container_metrics(containers)
        assert cpu == 0.0
        assert mem == 0.0

    def test_non_dict_container_skipped(self) -> None:
        containers = ["not_a_dict", {"usage": {"cpu": "500m", "memory": "512Mi"}}]
        cpu, mem = _sum_container_metrics(containers)
        assert cpu == 0.5
        assert mem == 512.0


class TestWorkloadKeyFromPodName:
    def test_replicaset_suffix(self) -> None:
        result = _workload_key_from_pod_name("myapp-abc123-x9k2l", "default")
        assert result == "default/myapp"

    def test_single_suffix(self) -> None:
        result = _workload_key_from_pod_name("mypod-x9k2l", "default")
        assert result == "default/mypod"

    def test_no_suffix_returns_none(self) -> None:
        result = _workload_key_from_pod_name("mysolo", "default")
        assert result is None


class TestParsePrometheusVector:
    def test_parse_valid_payload(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "default"},
                        "value": [1234567890, "1.5"],
                    }
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {"default": 1.5}

    def test_multiple_namespaces(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "ns1"}, "value": [1, "10.0"]},
                    {"metric": {"namespace": "ns2"}, "value": [1, "5.0"]},
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {"ns1": 10.0, "ns2": 5.0}

    def test_empty_data_returns_empty(self) -> None:
        assert _parse_prometheus_vector({}) == {}
        assert _parse_prometheus_vector({"data": {}}) == {}
        assert _parse_prometheus_vector({"data": {"result": []}}) == {}

    def test_invalid_value_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "default"}, "value": [1, "not_a_number"]},
                    {"metric": {"namespace": "good"}, "value": [1, "5.0"]},
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {"good": 5.0}

    def test_missing_namespace_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {}, "value": [1, "5.0"]},
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_non_dict_entry_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    "not_a_dict",
                    {"metric": {"namespace": "ns1"}, "value": [1, "5.0"]},
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {"ns1": 5.0}

    def test_non_dict_metric_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": "not_a_dict", "value": [1, "5.0"]},
                    {"metric": {"namespace": "ns1"}, "value": [1, "2.0"]},
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {"ns1": 2.0}

    def test_non_list_value_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "ns1"}, "value": "not_a_list"},
                    {"metric": {"namespace": "ns2"}, "value": [1, "2.0"]},
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {"ns2": 2.0}


class TestParsePrometheusPodVector:
    def test_parse_valid_payload(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "default", "pod": "myapp-123"},
                        "value": [1234567890, "0.75"],
                    }
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {"default/myapp-123": 0.75}

    def test_multiple_pods(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "ns1", "pod": "pod1"}, "value": [1, "1.0"]},
                    {"metric": {"namespace": "ns1", "pod": "pod2"}, "value": [1, "2.0"]},
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {"ns1/pod1": 1.0, "ns1/pod2": 2.0}

    def test_missing_pod_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "ns1"}, "value": [1, "5.0"]},
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {}

    def test_non_dict_entry_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    "not_a_dict",
                    {"metric": {"namespace": "ns1", "pod": "pod1"}, "value": [1, "5.0"]},
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {"ns1/pod1": 5.0}

    def test_invalid_value_type_skipped(self) -> None:
        payload = {
            "data": {
                "result": [
                    {"metric": {"namespace": "ns1", "pod": "pod1"}, "value": [1, "bad"]},
                    {"metric": {"namespace": "ns2", "pod": "pod2"}, "value": [1, "2.0"]},
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {"ns2/pod2": 2.0}


class TestPodRequestsAndLimits:
    def test_requests_and_limits(self) -> None:
        c = MagicMock()
        c.resources = MagicMock()
        c.resources.requests = {"cpu": "500m", "memory": "1Gi"}
        c.resources.limits = {"cpu": "1", "memory": "2Gi"}
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c])
        assert cpu_req == 0.5
        assert mem_req == 1024.0
        assert cpu_lim == 1.0
        assert mem_lim == 2048.0

    def test_requests_only(self) -> None:
        c = MagicMock()
        c.resources = MagicMock()
        c.resources.requests = {"cpu": "500m"}
        c.resources.limits = None
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c])
        assert cpu_req == 0.5
        assert mem_req is None
        assert cpu_lim is None
        assert mem_lim is None

    def test_no_resources_returns_none(self) -> None:
        c = MagicMock()
        c.resources = None
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c])
        assert cpu_req is None
        assert mem_req is None
        assert cpu_lim is None
        assert mem_lim is None

    def test_empty_containers_returns_none(self) -> None:
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([])
        assert cpu_req is None
        assert mem_req is None
        assert cpu_lim is None
        assert mem_lim is None


class TestDeploymentKeyFromPod:
    def test_replicaset_suffix(self) -> None:
        result = _deployment_key_from_pod("myapp-abc123-x9k2l", "default")
        assert result == "default/myapp"

    def test_single_suffix(self) -> None:
        result = _deployment_key_from_pod("mypod-x9k2l", "default")
        assert result == "default/mypod"

    def test_no_suffix_returns_none(self) -> None:
        result = _deployment_key_from_pod("myapp", "default")
        assert result is None


class TestGetWorkloadType:
    def test_replicaset_ref_defaults_to_deployment(self) -> None:
        assert _get_workload_type([]) == "Deployment"
        assert _get_workload_type(None) == "Deployment"

    def test_statefulset_detected(self) -> None:
        ref = MagicMock()
        ref.kind = "StatefulSet"
        assert _get_workload_type([ref]) == "StatefulSet"

    def test_daemonset_detected(self) -> None:
        ref = MagicMock()
        ref.kind = "DaemonSet"
        assert _get_workload_type([ref]) == "DaemonSet"

    def test_job_detected(self) -> None:
        ref = MagicMock()
        ref.kind = "Job"
        assert _get_workload_type([ref]) == "Job"

    def test_cronjob_detected(self) -> None:
        ref = MagicMock()
        ref.kind = "CronJob"
        assert _get_workload_type([ref]) == "CronJob"

    def test_non_object_ref_skipped(self) -> None:
        ref_good = MagicMock()
        ref_good.kind = "StatefulSet"
        assert _get_workload_type(["not_an_object", ref_good]) == "StatefulSet"


class TestExtractContainerData:
    def test_basic_container(self) -> None:
        c = MagicMock()
        c.name = "mycontainer"
        c.ports = None
        c.liveness_probe = None
        c.readiness_probe = None
        result = _extract_container_data(c)
        assert result["container_name"] == "mycontainer"
        assert result["is_init_container"] is False
        assert result["exposed_ports"] == []
        assert result["has_liveness_probe"] is False
        assert result["has_readiness_probe"] is False

    def test_ports_extraction(self) -> None:
        p1 = MagicMock()
        p1.container_port = 8080
        p2 = MagicMock()
        p2.container_port = 9090
        c = MagicMock()
        c.name = "webserver"
        c.ports = [p1, p2]
        c.liveness_probe = None
        c.readiness_probe = None
        result = _extract_container_data(c)
        assert result["exposed_ports"] == [8080, 9090]

    def test_http_probes(self) -> None:
        c = MagicMock()
        c.name = "web"
        c.ports = None
        liveness = MagicMock()
        liveness.http_get = MagicMock()
        liveness.http_get.path = "/healthz"
        liveness.http_get.port = 8080
        readiness = MagicMock()
        readiness.http_get = MagicMock()
        readiness.http_get.path = "/ready"
        readiness.http_get.port = 8080
        c.liveness_probe = liveness
        c.readiness_probe = readiness
        result = _extract_container_data(c)
        assert result["has_liveness_probe"] is True
        assert result["has_readiness_probe"] is True
        assert result["liveness_probe_type"] == "httpGet"
        assert result["readiness_probe_type"] == "httpGet"
        assert result["liveness_http_path"] == "/healthz"
        assert result["readiness_http_path"] == "/ready"
        assert result["liveness_port"] == 8080
        assert result["readiness_port"] == 8080

    def test_tcp_probes(self) -> None:
        c = MagicMock()
        c.name = "db"
        c.ports = None
        liveness = MagicMock()
        liveness.http_get = None
        liveness.tcp_socket = MagicMock()
        liveness.tcp_socket.port = 5432
        readiness = MagicMock()
        readiness.http_get = None
        readiness.tcp_socket = MagicMock()
        readiness.tcp_socket.port = 5432
        c.liveness_probe = liveness
        c.readiness_probe = readiness
        result = _extract_container_data(c)
        assert result["liveness_probe_type"] == "tcpSocket"
        assert result["readiness_probe_type"] == "tcpSocket"
        assert result["liveness_port"] == 5432
        assert result["readiness_port"] == 5432

    def test_extract_init_container(self) -> None:
        c = MagicMock()
        c.name = "init-db"
        c.ports = None
        c.liveness_probe = None
        c.readiness_probe = None
        result = _extract_init_container_data(c)
        assert result["container_name"] == "init-db"
        assert result["is_init_container"] is True

    def test_init_container_with_http_probes(self) -> None:
        c = MagicMock()
        c.name = "init-web"
        c.ports = None
        liveness = MagicMock()
        liveness.http_get = MagicMock()
        liveness.http_get.path = "/health"
        liveness.http_get.port = 8080
        readiness = MagicMock()
        readiness.http_get = MagicMock()
        readiness.http_get.path = "/ready"
        readiness.http_get.port = 8080
        c.liveness_probe = liveness
        c.readiness_probe = readiness
        result = _extract_init_container_data(c)
        assert result["has_liveness_probe"] is True
        assert result["has_readiness_probe"] is True
        assert result["liveness_probe_type"] == "httpGet"
        assert result["readiness_probe_type"] == "httpGet"

    def test_container_with_exec_probe_type(self) -> None:
        c = MagicMock()
        c.name = "exec-container"
        c.ports = None
        liveness = MagicMock()
        liveness.http_get = None
        liveness.tcp_socket = None
        c.liveness_probe = liveness
        c.readiness_probe = None
        result = _extract_container_data(c)
        assert result["liveness_probe_type"] == "exec"
        assert result["readiness_probe_type"] == ""

    def test_pod_requests_and_limits_partial(self) -> None:
        c = MagicMock()
        c.resources = MagicMock()
        c.resources.requests = None
        c.resources.limits = {"memory": "2Gi"}
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c])
        assert cpu_req is None
        assert mem_req is None
        assert cpu_lim is None
        assert mem_lim == 2048.0
