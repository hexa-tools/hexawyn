from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumFlowQuery
from hexawyn.domain.services.cilium.flow_builder import (
    build_flows,
    not_installed_flows_result,
)


def _raw_flow(verdict: str = "FORWARDED", namespace: str = "payments") -> dict:
    return {
        "time": "2026-08-28T10:00:00Z",
        "verdict": verdict,
        "direction": "ingress",
        "source": {"namespace": namespace, "pod_name": "web-0", "identity": 100},
        "destination": {"namespace": namespace, "pod_name": "db-0", "identity": 200},
        "ip": {"source": "10.0.0.1", "destination": "10.0.0.2"},
        "l4": {"tcp": {"destination_port": 443}},
        "l7": {"protocol": "http"},
    }


class TestBuildFlows:
    def test_maps_flow_fields(self) -> None:
        result = build_flows([_raw_flow()], CiliumFlowQuery())

        assert result.installed is True
        assert result.status == "present"
        assert result.total_flows == 1  # noqa: PLR2004
        flow = result.flows[0]
        assert flow.source == "web-0"
        assert flow.destination == "db-0"
        assert flow.source_namespace == "payments"
        assert flow.destination_namespace == "payments"
        assert flow.source_identity == "100"
        assert flow.verdict == "FORWARDED"
        assert flow.protocol == "tcp"
        assert flow.destination_port == "443"
        assert flow.l7_protocol == "http"

    def test_missing_verdict_reported_unknown(self) -> None:
        raw = _raw_flow()
        raw.pop("verdict")
        result = build_flows([raw], CiliumFlowQuery())

        assert result.flows[0].verdict == "UNKNOWN"

    def test_extracts_policy_from_labels(self) -> None:
        raw = _raw_flow()
        raw["labels"] = ["k8s:io.cilium.k8s.policy.name=default/deny-all"]
        result = build_flows([raw], CiliumFlowQuery())

        assert result.flows[0].policy == "default/deny-all"

    def test_policy_none_when_no_label(self) -> None:
        result = build_flows([_raw_flow()], CiliumFlowQuery())

        assert result.flows[0].policy is None

    def test_policy_none_for_non_policy_labels(self) -> None:
        raw = _raw_flow()
        raw["labels"] = ["env=prod", "not-policy"]
        result = build_flows([raw], CiliumFlowQuery())

        assert result.flows[0].policy is None

    def test_filters_by_namespace(self) -> None:
        flows = [_raw_flow(namespace="payments"), _raw_flow(namespace="checkout")]
        result = build_flows(flows, CiliumFlowQuery(namespace="payments"))

        assert result.total_flows == 1  # noqa: PLR2004
        assert result.flows[0].destination == "db-0"

    def test_filters_by_verdict(self) -> None:
        flows = [_raw_flow(verdict="FORWARDED"), _raw_flow(verdict="DROPPED")]
        result = build_flows(flows, CiliumFlowQuery(verdict="dropped"))

        assert result.total_flows == 1  # noqa: PLR2004
        assert result.flows[0].verdict == "DROPPED"

    def test_filters_by_pod(self) -> None:
        other = _raw_flow()
        other["source"]["pod_name"] = "checkout-0"
        result = build_flows([_raw_flow(), other], CiliumFlowQuery(pod="web-0"))

        assert result.total_flows == 1  # noqa: PLR2004

    def test_filters_by_direction(self) -> None:
        other = _raw_flow()
        other["direction"] = "egress"
        result = build_flows([_raw_flow(), other], CiliumFlowQuery(direction="ingress"))

        assert result.total_flows == 1  # noqa: PLR2004

    def test_limit_clamps_volume(self) -> None:
        flows = [_raw_flow(namespace=f"ns-{i}") for i in range(5)]
        result = build_flows(flows, CiliumFlowQuery(limit=2))  # noqa: PLR2004

        assert result.total_flows == 2  # noqa: PLR2004

    def test_empty_flows(self) -> None:
        result = build_flows([], CiliumFlowQuery())

        assert result.status == "empty"
        assert result.total_flows == 0
        assert result.flows == []


class TestNotInstalledFlowsResult:
    def test_returns_marker(self) -> None:
        result = not_installed_flows_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.flows == []
        assert result.note is not None
