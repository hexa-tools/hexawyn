"""Tests for domain/services/calico/bgp_audit_service — BGP audit composition."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoBgpConfiguration,
    CalicoBgpPeer,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)
from hexawyn.domain.services.calico.bgp_audit_service import build_calico_bgp_audit


class TestBuildCalicoBgpAudit:
    def _detection(self, **overrides: object) -> CalicoDetectionResult:
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
            "total_nodes": 3,
            "ready_agents": 3,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def test_configured_with_peers(self) -> None:
        configs = [
            CalicoBgpConfiguration(
                name="default",
                as_number="64512",
                node_to_node_mesh_enabled=True,
                service_cluster_ips=("10.96.0.0/16",),
            )
        ]
        peers = [
            CalicoBgpPeer(name="p1", peer_ip="10.0.0.2", as_number="64513", node_selector="all()"),
        ]
        result = build_calico_bgp_audit(
            configurations=configs, peers=peers, detection=self._detection()
        )
        assert result.installed is True
        assert result.as_number == "64512"
        assert result.node_to_node_mesh_enabled is True
        assert result.service_cluster_ips == ("10.96.0.0/16",)
        assert result.peer_count == 1  # noqa: PLR2004
        assert result.session_state == "reachable"

    def test_mesh_only(self) -> None:
        configs = [
            CalicoBgpConfiguration(
                name="default",
                as_number=None,
                node_to_node_mesh_enabled=True,
                service_cluster_ips=(),
            )
        ]
        result = build_calico_bgp_audit(
            configurations=configs, peers=[], detection=self._detection()
        )
        assert result.node_to_node_mesh_enabled is True
        assert result.peer_count == 0

    def test_no_configuration_defaults_as_is(self) -> None:
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=self._detection())
        assert result.as_number is None
        assert result.node_to_node_mesh_enabled is None
        assert result.service_cluster_ips == ()
        assert result.peer_count == 0

    def test_non_default_configuration_used(self) -> None:
        configs = [
            CalicoBgpConfiguration(
                name="node/a",
                as_number="64550",
                node_to_node_mesh_enabled=None,
                service_cluster_ips=(),
            ),
        ]
        result = build_calico_bgp_audit(
            configurations=configs, peers=[], detection=self._detection()
        )
        assert result.as_number == "64550"

    def test_not_installed(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_nodes=0,
            ready_agents=0,
        )
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=detection)
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"

    def test_session_degraded(self) -> None:
        detection = self._detection(total_nodes=2, ready_agents=1, degraded_agents=1)
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=detection)
        assert result.session_state == "degraded"

    def test_session_unknown_when_no_agents(self) -> None:
        detection = self._detection(total_nodes=0, ready_agents=0)
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=detection)
        assert result.session_state == "unknown"

    def test_malformed_asn_preserved(self) -> None:
        configs = [
            CalicoBgpConfiguration(
                name="default",
                as_number="not-a-number",
                node_to_node_mesh_enabled=None,
                service_cluster_ips=(),
            )
        ]
        result = build_calico_bgp_audit(
            configurations=configs, peers=[], detection=self._detection()
        )
        assert result.as_number == "not-a-number"

    def test_summary_reflects_as_and_peers(self) -> None:
        configs = [
            CalicoBgpConfiguration(
                name="default",
                as_number="64512",
                node_to_node_mesh_enabled=False,
                service_cluster_ips=(),
            )
        ]
        peers = [
            CalicoBgpPeer(name="p1", peer_ip="10.0.0.2", as_number="64513", node_selector="all()")
        ]
        result = build_calico_bgp_audit(
            configurations=configs, peers=peers, detection=self._detection()
        )
        assert result.summary is not None
        assert "64512" in result.summary
