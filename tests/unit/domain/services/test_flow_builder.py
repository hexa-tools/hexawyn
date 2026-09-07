from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumFlowEntry,
    CiliumFlowQuery,
    CiliumFlowsResult,
)
from hexawyn.domain.services.cilium.flow_builder import (
    _any_namespace,
    _as_str,
    _extract_policy,
    _matches,
    _to_entry,
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
        assert result.total_flows == 0


class TestToEntryDirect:
    def test_full_tcp_entry_maps_every_field(self) -> None:
        entry = _to_entry(
            {
                "time": "2026-08-28T10:00:00Z",
                "verdict": "DROPPED",
                "drop_reason": "Policy denied",
                "direction": "egress",
                "source": {"namespace": "ns-a", "pod_name": "web-0", "identity": "100"},
                "destination": {"namespace": "ns-b", "pod_name": "db-0", "identity": "200"},
                "ip": {"source": "10.0.0.1", "destination": "10.0.0.2"},
                "l4": {"tcp": {"destination_port": 443}},
                "l7": {"protocol": "http"},
                "labels": ["k8s:io.cilium.k8s.policy.name=allow-x"],
            }
        )

        assert entry == CiliumFlowEntry(
            timestamp="2026-08-28T10:00:00Z",
            source="web-0",
            destination="db-0",
            source_namespace="ns-a",
            destination_namespace="ns-b",
            source_identity="100",
            destination_identity="200",
            verdict="DROPPED",
            drop_reason="Policy denied",
            protocol="tcp",
            destination_port="443",
            l7_protocol="http",
            direction="egress",
            policy="allow-x",
        )

    def test_udp_flow_sets_udp_protocol_and_port(self) -> None:
        entry = _to_entry(
            {
                "verdict": "FORWARDED",
                "l4": {"udp": {"destination_port": 53}},
            }
        )

        assert entry.protocol == "udp"
        assert entry.destination_port == "53"
        assert entry.verdict == "FORWARDED"

    def test_source_falls_back_to_ip_when_no_pod_name(self) -> None:
        entry = _to_entry(
            {
                "source": {"namespace": "ns-a", "identity": "100"},
                "ip": {"source": "10.0.0.1"},
            }
        )

        assert entry.source == "10.0.0.1"
        assert entry.source_namespace == "ns-a"
        assert entry.source_identity == "100"

    def test_destination_falls_back_to_ip_when_no_pod_name(self) -> None:
        entry = _to_entry(
            {
                "destination": {"namespace": "ns-b", "identity": "200"},
                "ip": {"destination": "10.0.0.2"},
            }
        )

        assert entry.destination == "10.0.0.2"
        assert entry.destination_identity == "200"

    def test_empty_pod_name_is_falsy_so_ip_wins(self) -> None:
        entry = _to_entry(
            {
                "source": {"pod_name": ""},
                "ip": {"source": "10.0.0.9"},
            }
        )

        assert entry.source == "10.0.0.9"

    def test_missing_identity_returns_none_not_zero(self) -> None:
        entry = _to_entry(
            {
                "source": {"pod_name": "web-0"},
                "destination": {"pod_name": "db-0"},
                "ip": {"source": "10.0.0.1", "destination": "10.0.0.2"},
            }
        )

        assert entry.source_identity is None
        assert entry.destination_identity is None

    def test_missing_drop_reason_returns_none(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})

        assert entry.drop_reason is None

    def test_missing_direction_returns_none(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})

        assert entry.direction is None

    def test_missing_l7_protocol_returns_none(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})

        assert entry.l7_protocol is None

    def test_no_l4_means_no_protocol_no_port(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})

        assert entry.protocol is None
        assert entry.destination_port is None

    def test_source_empty_when_no_pod_and_no_ip(self) -> None:
        entry = _to_entry({"source": {}, "verdict": "FORWARDED"})

        assert entry.source == ""

    def test_destination_empty_when_no_pod_and_no_ip(self) -> None:
        entry = _to_entry({"destination": {}, "verdict": "FORWARDED"})

        assert entry.destination == ""

    def test_both_tcp_and_udp_prefer_tcp(self) -> None:
        entry = _to_entry(
            {
                "verdict": "FORWARDED",
                "l4": {
                    "tcp": {"destination_port": 443},
                    "udp": {"destination_port": 53},
                },
            }
        )

        assert entry.protocol == "tcp"
        assert entry.destination_port == "443"

    def test_missing_time_returns_empty_string(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})

        assert entry.timestamp == ""

    def test_verdict_not_forced_when_absent(self) -> None:
        entry = _to_entry({})

        assert entry.verdict == "UNKNOWN"


class TestMatchesDirect:
    def _entry(self) -> CiliumFlowEntry:
        return _to_entry(
            {
                "verdict": "FORWARDED",
                "direction": "ingress",
                "source": {"namespace": "ns-a", "pod_name": "web-0"},
                "destination": {"namespace": "ns-b", "pod_name": "db-0"},
            }
        )

    def test_matches_when_no_filters(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery()) is True

    def test_namespace_match_on_source(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(namespace="ns-a")) is True

    def test_namespace_match_on_destination(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(namespace="ns-b")) is True

    def test_namespace_mismatch_rejected(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(namespace="ns-z")) is False

    def test_pod_match_on_destination(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(pod="db-0")) is True

    def test_pod_mismatch_rejected(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(pod="other-0")) is False

    def test_direction_case_insensitive(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(direction="INGRESS")) is True

    def test_direction_mismatch_rejected(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(direction="egress")) is False

    def test_verdict_case_insensitive(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(verdict="forwarded")) is True

    def test_verdict_mismatch_rejected(self) -> None:
        assert _matches(self._entry(), CiliumFlowQuery(verdict="dropped")) is False

    def test_empty_direction_on_entry_matches_non_empty_query(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})
        assert _matches(entry, CiliumFlowQuery(direction="ingress")) is False


class TestAnyNamespace:
    def test_source_namespace_match(self) -> None:
        entry = _to_entry({"source": {"namespace": "ns-a"}, "destination": {"namespace": "ns-b"}})
        assert _any_namespace(entry, "ns-a") is True

    def test_destination_namespace_match(self) -> None:
        entry = _to_entry({"source": {"namespace": "ns-a"}, "destination": {"namespace": "ns-b"}})
        assert _any_namespace(entry, "ns-b") is True

    def test_no_namespace_match(self) -> None:
        entry = _to_entry({"source": {"namespace": "ns-a"}, "destination": {"namespace": "ns-b"}})
        assert _any_namespace(entry, "ns-c") is False

    def test_both_namespaces_none(self) -> None:
        entry = _to_entry({"verdict": "FORWARDED"})
        assert _any_namespace(entry, "ns-a") is False


class TestExtractPolicyDirect:
    def test_non_policy_label_before_policy_is_skipped(self) -> None:
        labels = ["env=prod", "k8s:io.cilium.k8s.policy.name=allow"]

        assert _extract_policy(labels) == "allow"

    def test_label_without_equals_is_skipped(self) -> None:
        labels = ["k8s:io.cilium.policy=allow", "just-a-label"]
        assert _extract_policy(labels) == "allow"

    def test_policy_value_keeps_multiple_equals(self) -> None:
        labels = ["k8s:io.cilium.k8s.policy.name=a=b=c"]

        assert _extract_policy(labels) == "a=b=c"

    def test_empty_policy_value_returns_none(self) -> None:
        labels = ["k8s:io.cilium.k8s.policy.name="]

        assert _extract_policy(labels) is None

    def test_non_list_labels_returns_none(self) -> None:
        assert _extract_policy("k8s:policy=allow") is None

    def test_policy_keyword_uppercase_still_matches(self) -> None:
        labels = ["k8s:io.cilium.k8s.POLICY.name=deny"]

        assert _extract_policy(labels) == "deny"

    def test_label_without_equals_before_policy_is_skipped(self) -> None:
        labels = ["bare-label", "k8s:io.cilium.k8s.policy.name=allow"]

        assert _extract_policy(labels) == "allow"


class TestAsStr:
    def test_none_returns_none(self) -> None:
        assert _as_str(None) is None

    def test_value_stringified(self) -> None:
        assert _as_str(42) == "42"


class TestBuildFlowsResultShape:
    def test_result_is_cilium_flows_result(self) -> None:
        result = build_flows([_raw_flow()], CiliumFlowQuery())

        assert isinstance(result, CiliumFlowsResult)

    def test_limit_equal_to_length_is_not_clamped(self) -> None:
        flows = [_raw_flow(namespace=f"ns-{i}") for i in range(3)]
        result = build_flows(flows, CiliumFlowQuery(limit=3))  # noqa: PLR2004

        assert result.total_flows == 3  # noqa: PLR2004

    def test_zero_limit_is_falsy_and_not_enforced(self) -> None:
        result = build_flows([_raw_flow()], CiliumFlowQuery(limit=0))

        assert result.total_flows == 1  # noqa: PLR2004
