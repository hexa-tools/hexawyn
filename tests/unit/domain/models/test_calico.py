"""Tests for domain/models/calico.py — pure, no infrastructure."""

from __future__ import annotations

import pytest
from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoHostEndpoint,
    CalicoIPPool,
    CalicoNetworkPolicy,
    CalicoNodeAgent,
    DataplaneMode,
)


class TestEnums:
    def test_dataplane_mode_values(self) -> None:
        assert DataplaneMode.IPIP.value == "IPIP"
        assert DataplaneMode.VXLAN.value == "VXLAN"
        assert DataplaneMode.EBPF.value == "eBPF"
        assert DataplaneMode.UNKNOWN.value == "UNKNOWN"

    def test_agent_phase_values(self) -> None:
        assert CalicoAgentPhase.READY.value == "ready"
        assert CalicoAgentPhase.RUNNING.value == "running"
        assert CalicoAgentPhase.NOT_READY.value == "not_ready"
        assert CalicoAgentPhase.UNKNOWN.value == "unknown"

    def test_detection_status_values(self) -> None:
        assert CalicoDetectionStatus.INSTALLED.value == "installed"
        assert CalicoDetectionStatus.DEGRADED.value == "degraded"
        assert CalicoDetectionStatus.NOT_INSTALLED.value == "not_installed"


class TestCalicoNodeAgent:
    def _agent(self, **overrides: object) -> CalicoNodeAgent:
        base: dict[str, object] = {
            "node": "node-1",
            "phase": CalicoAgentPhase.READY,
            "ready": True,
            "ready_replicas": 1,
            "desired_replicas": 1,
            "available_replicas": 1,
            "message": None,
        }
        base.update(overrides)
        return CalicoNodeAgent(**base)  # type: ignore[arg-type]

    def test_ready_agent_is_healthy(self) -> None:
        assert self._agent().healthy is True

    def test_ready_but_zero_desired_is_unhealthy(self) -> None:
        assert self._agent(desired_replicas=0).healthy is False

    def test_ready_but_short_replicas_is_unhealthy(self) -> None:
        assert self._agent(ready_replicas=0).healthy is False

    def test_not_ready_agent_is_unhealthy(self) -> None:
        assert self._agent(ready=False, phase=CalicoAgentPhase.NOT_READY).healthy is False

    def test_boundary_one_replica_healthy(self) -> None:
        assert self._agent(ready_replicas=1, desired_replicas=1).healthy is True

    def test_defaults_message_none(self) -> None:
        assert self._agent().message is None


class TestDetectionResultProperties:
    def _result(self, **overrides: object) -> CalicoDetectionResult:
        base: dict[str, object] = {
            "installed": True,
            "status": CalicoDetectionStatus.INSTALLED,
            "not_installed_marker": None,
            "version": "v3.26.1",
            "mode": DataplaneMode.IPIP,
            "namespace": "calico-system",
            "tigera_operator": False,
            "enterprise": False,
            "agents": [],
            "total_nodes": 1,
            "ready_agents": 1,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def test_installed_not_installed_false(self) -> None:
        result = self._result()
        assert result.not_installed is False
        assert result.marker is None

    def test_not_installed_flag_and_marker(self) -> None:
        result = self._result(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            version=None,
            namespace=None,
            mode=DataplaneMode.UNKNOWN,
            total_nodes=0,
            ready_agents=0,
            degraded_agents=0,
        )
        assert result.not_installed is True
        assert result.marker == "NOT_INSTALLED"
        assert result.marker == NOT_INSTALLED_MARKER

    def test_empty_agent_list_is_allowed(self) -> None:
        result = self._result(agents=[], total_nodes=0)
        assert result.agents == []
        assert result.total_nodes == 0

    def test_frozen(self) -> None:
        with pytest.raises(Exception):
            self._result().installed = False  # type: ignore[misc]


class TestSerieProjections:
    def test_network_policy(self) -> None:
        np = CalicoNetworkPolicy(
            name="np",
            namespace="default",
            order=100.0,
            selector="app == 'web'",
            ingress_rules=("allow-80",),
            egress_rules=(),
            apply_on_forward=False,
        )
        assert np.name == "np"
        assert np.ingress_rules == ("allow-80",)

    def test_ip_pool(self) -> None:
        pool = CalicoIPPool(
            name="pool", cidr="10.1.0.0/16", ipip_mode="Always", vxlan_mode="Never", disabled=False
        )
        assert pool.cidr == "10.1.0.0/16"

    def test_host_endpoint(self) -> None:
        he = CalicoHostEndpoint(
            name="he", node="node-1", interface_name="eth0", expected_ip="10.0.0.1"
        )
        assert he.expected_ip == "10.0.0.1"
