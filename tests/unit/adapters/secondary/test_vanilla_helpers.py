"""Tests for vanilla_adapter module-level helpers — lines 1598-1733."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _deployment_key_from_pod,
    _get_workload_type,
    _parse_prometheus_pod_vector,
    _parse_prometheus_vector,
    _pod_requests_and_limits,
)


class TestParsePrometheusVector:
    """Cover _parse_prometheus_vector (lines 1566-1595)."""

    def test_valid_payload(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns", "pod": "pod-a"},
                        "value": [None, "42.5"],
                    }
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result["ns"] == 42.5  # noqa: PLR2004

    def test_empty_result(self) -> None:
        payload = {"data": {"result": []}}
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_non_dict_payload(self) -> None:
        result = _parse_prometheus_vector("not_a_dict")  # type: ignore[arg-type]
        assert result == {}

    def test_non_dict_data(self) -> None:
        result = _parse_prometheus_vector({"data": "not_dict"})
        assert result == {}

    def test_non_list_result(self) -> None:
        result = _parse_prometheus_vector({"data": {"result": "not_list"}})
        assert result == {}

    def test_entry_not_dict(self) -> None:
        payload: dict[str, object] = {"data": {"result": ["not_dict"]}}
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_metric_not_dict(self) -> None:
        payload = {"data": {"result": [{"metric": "not_dict", "value": [None, "1.0"]}]}}
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_value_pair_not_list(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns"},
                        "value": "not_a_list",
                    }
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_value_pair_too_short(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns"},
                        "value": [None],
                    }
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_namespace_not_string(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": 123, "pod": "p"},
                        "value": [None, "1.0"],
                    }
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {}

    def test_unparseable_value(self) -> None:
        payload = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns"},
                        "value": [None, "not_a_number"],
                    }
                ]
            }
        }
        result = _parse_prometheus_vector(payload)
        assert result == {}


class TestParsePrometheusPodVector:
    """Cover _parse_prometheus_pod_vector (lines 1598-1622)."""

    def test_valid_payload(self) -> None:
        payload: dict[str, object] = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns", "pod": "pod-a"},
                        "value": [None, "99.9"],
                    }
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {"ns/pod-a": 99.9}

    def test_non_dict_payload(self) -> None:
        result = _parse_prometheus_pod_vector(42)  # type: ignore[arg-type]
        assert result == {}

    def test_non_dict_data(self) -> None:
        result = _parse_prometheus_pod_vector({"data": 123})
        assert result == {}

    def test_non_list_result(self) -> None:
        result = _parse_prometheus_pod_vector({"data": {"result": None}})
        assert result == {}

    def test_entry_not_dict(self) -> None:
        payload: dict[str, object] = {"data": {"result": ["string_entry"]}}
        result = _parse_prometheus_pod_vector(payload)
        assert result == {}

    def test_metric_not_dict(self) -> None:
        payload: dict[str, object] = {
            "data": {"result": [{"metric": "bad", "value": [None, "1.0"]}]}
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {}

    def test_value_not_list(self) -> None:
        payload: dict[str, object] = {
            "data": {"result": [{"metric": {"namespace": "ns", "pod": "p"}, "value": "bad"}]}
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {}

    def test_pod_not_string(self) -> None:
        payload: dict[str, object] = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns", "pod": 123},
                        "value": [None, "1.0"],
                    }
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert result == {}

    def test_unparseable_literal_value_is_float_nan(self) -> None:
        import math

        payload: dict[str, object] = {
            "data": {
                "result": [
                    {
                        "metric": {"namespace": "ns", "pod": "p"},
                        "value": [None, "NaN"],
                    }
                ]
            }
        }
        result = _parse_prometheus_pod_vector(payload)
        assert math.isnan(result["ns/p"])


class TestPodRequestsAndLimits:
    """Cover _pod_requests_and_limits (lines 1625-1649)."""

    def test_with_full_requests_and_limits(self) -> None:
        c1 = MagicMock()
        c1.resources = MagicMock()
        c1.resources.requests = {"cpu": "500m", "memory": "1Gi"}
        c1.resources.limits = {"cpu": "1", "memory": "2Gi"}

        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c1])
        assert cpu_req == 0.5  # noqa: PLR2004
        assert mem_req == 1024.0  # noqa: PLR2004
        assert cpu_lim == 1.0  # noqa: PLR2004
        assert mem_lim == 2048.0  # noqa: PLR2004

    def test_no_resources(self) -> None:
        c1 = MagicMock()
        c1.resources = None
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c1])
        assert cpu_req is None
        assert mem_req is None

    def test_no_requests(self) -> None:
        c1 = MagicMock()
        c1.resources = MagicMock()
        c1.resources.requests = None
        c1.resources.limits = None
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c1])
        assert cpu_req is None

    def test_partial_limits(self) -> None:
        c1 = MagicMock()
        c1.resources = MagicMock()
        c1.resources.requests = {"cpu": "200m"}
        c1.resources.limits = {"memory": "512Mi"}
        cpu_req, mem_req, cpu_lim, mem_lim = _pod_requests_and_limits([c1])
        assert cpu_req == 0.2  # noqa: PLR2004
        assert mem_req is None
        assert cpu_lim is None
        assert mem_lim == 512.0  # noqa: PLR2004


class TestDeploymentKey:
    """Cover _deployment_key_from_pod (lines 1652-1659)."""

    def test_three_parts(self) -> None:
        key = _deployment_key_from_pod("myapp-7b9f4c5d6-x8k2l", "ns")
        assert key == "ns/myapp"

    def test_two_parts(self) -> None:
        key = _deployment_key_from_pod("myapp-x8k2l", "ns")
        assert key == "ns/myapp"

    def test_one_part(self) -> None:
        key = _deployment_key_from_pod("myapp", "ns")
        assert key is None


class TestGetWorkloadType:
    """Cover _get_workload_type (lines 1662-1669)."""

    def test_deployment_default_for_non_list(self) -> None:
        assert _get_workload_type("not_a_list") == "Deployment"

    def test_empty_list_returns_deployment(self) -> None:
        assert _get_workload_type([]) == "Deployment"

    def test_identifies_statefulset(self) -> None:
        ref = MagicMock()
        ref.kind = "StatefulSet"
        assert _get_workload_type([ref]) == "StatefulSet"

    def test_identifies_daemonset(self) -> None:
        ref = MagicMock()
        ref.kind = "DaemonSet"
        assert _get_workload_type([ref]) == "DaemonSet"

    def test_identifies_job(self) -> None:
        ref = MagicMock()
        ref.kind = "Job"
        assert _get_workload_type([ref]) == "Job"

    def test_skips_non_object_refs(self) -> None:
        assert _get_workload_type(["not_an_object"]) == "Deployment"
