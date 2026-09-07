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
from hexawyn.domain.services.calico.bgp_audit_service import (
    _default_configuration,
    _session_state,
    _summary,
    build_calico_bgp_audit,
)


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

    def _config(self, **overrides: object) -> CalicoBgpConfiguration:
        base: dict[str, object] = {
            "name": "default",
            "as_number": "64512",
            "node_to_node_mesh_enabled": True,
            "service_cluster_ips": ("10.96.0.0/16",),
        }
        base.update(overrides)
        return CalicoBgpConfiguration(**base)  # type: ignore[arg-type]

    def _peer(self, name: str = "p1", ip: str = "10.0.0.2") -> CalicoBgpPeer:
        return CalicoBgpPeer(
            name=name,
            peer_ip=ip,
            as_number="64513",
            node_selector="all()",
        )

    def test_not_installed_full_payload(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_nodes=0,
            ready_agents=0,
            error="kube api unreachable",
        )
        result = build_calico_bgp_audit(
            configurations=[self._config()], peers=[self._peer()], detection=detection
        )
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.as_number is None
        assert result.node_to_node_mesh_enabled is None
        assert result.service_cluster_ips == ()
        assert result.peers == []
        assert result.peer_count == 0
        assert result.session_state == "unknown"
        assert result.session_note is None
        assert result.summary is None
        assert result.error == "kube api unreachable"

    def test_configured_with_peers_full_payload(self) -> None:
        configs = [self._config()]
        peers = [self._peer()]
        result = build_calico_bgp_audit(
            configurations=configs, peers=peers, detection=self._detection()
        )
        assert result.installed is True
        assert result.not_installed_marker is None
        assert result.as_number == "64512"
        assert result.node_to_node_mesh_enabled is True
        assert result.service_cluster_ips == ("10.96.0.0/16",)
        assert result.peers == peers
        assert result.peer_count == 1  # noqa: PLR2004
        assert result.session_state == "reachable"
        assert result.session_note == (
            "All calico-node agents ready; BGP peer state not directly observed"
        )
        assert result.summary == ("BGP: ASN 64512; node-to-node mesh enabled; 1 BGP peer(s)")
        assert result.error is None

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
        assert result.as_number is None
        assert result.node_to_node_mesh_enabled is True
        assert result.peer_count == 0
        assert result.summary == "BGP: node-to-node mesh enabled"

    def test_no_configuration_full_defaults(self) -> None:
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=self._detection())
        assert result.as_number is None
        assert result.node_to_node_mesh_enabled is None
        assert result.service_cluster_ips == ()
        assert result.peers == []
        assert result.peer_count == 0
        assert result.summary == "No Calico BGP configuration or peers observed."

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
        assert result.summary == "BGP: ASN 64550"

    def test_error_forwarded_when_installed(self) -> None:
        detection = self._detection(error="partial bgp discovery")
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=detection)
        assert result.error == "partial bgp discovery"
        assert result.installed is True

    def test_session_degraded_note_exact(self) -> None:
        detection = self._detection(total_nodes=2, ready_agents=1, degraded_agents=1)
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=detection)
        assert result.session_state == "degraded"
        assert result.session_note == (
            "1 calico-node agent(s) degraded; BGP sessions may be affected"
        )

    def test_session_unknown_note_exact(self) -> None:
        detection = self._detection(total_nodes=0, ready_agents=0)
        result = build_calico_bgp_audit(configurations=[], peers=[], detection=detection)
        assert result.session_state == "unknown"
        assert result.session_note == ("No calico-node agents observed; BGP session state unknown")

    def test_malformed_asn_preserved_in_summary(self) -> None:
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
        assert result.summary == "BGP: ASN not-a-number"


class TestDefaultConfigurationDirect:
    def _config(self, name: str) -> CalicoBgpConfiguration:
        return CalicoBgpConfiguration(
            name=name,
            as_number="64512",
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
        )

    def test_empty_returns_none(self) -> None:
        assert _default_configuration([]) is None

    def test_default_picked_over_first(self) -> None:
        configs = [self._config("node/a"), self._config("default")]
        result = _default_configuration(configs)
        assert result is not None
        assert result.name == "default"

    def test_first_when_no_default(self) -> None:
        configs = [self._config("node/a"), self._config("node/b")]
        result = _default_configuration(configs)
        assert result is not None
        assert result.name == "node/a"

    def test_single_default(self) -> None:
        result = _default_configuration([self._config("default")])
        assert result is not None
        assert result.name == "default"

    def test_default_not_first_still_wins(self) -> None:
        configs = [self._config("global"), self._config("default"), self._config("node/b")]
        result = _default_configuration(configs)
        assert result is not None
        assert result.name == "default"


class TestSessionStateDirect:
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

    def test_unknown_when_no_nodes(self) -> None:
        state, note = _session_state(self._detection(total_nodes=0, ready_agents=0))
        assert state == "unknown"
        assert note == "No calico-node agents observed; BGP session state unknown"

    def test_degraded_when_agents_degraded(self) -> None:
        state, note = _session_state(
            self._detection(total_nodes=2, ready_agents=1, degraded_agents=1)
        )
        assert state == "degraded"
        assert note == "1 calico-node agent(s) degraded; BGP sessions may be affected"

    def test_degraded_multiple_agents_exact(self) -> None:
        state, note = _session_state(
            self._detection(total_nodes=5, ready_agents=2, degraded_agents=3)
        )
        assert state == "degraded"
        assert note == "3 calico-node agent(s) degraded; BGP sessions may be affected"

    def test_reachable_when_all_ready(self) -> None:
        state, note = _session_state(
            self._detection(total_nodes=3, ready_agents=3, degraded_agents=0)
        )
        assert state == "reachable"
        assert note == "All calico-node agents ready; BGP peer state not directly observed"

    def test_reachable_when_no_degraded_but_not_all_ready(self) -> None:
        state, _ = _session_state(self._detection(total_nodes=3, ready_agents=2, degraded_agents=0))
        assert state == "reachable"


class TestSummaryDirect:
    def _peer(self, name: str = "p1", ip: str = "10.0.0.2") -> CalicoBgpPeer:
        return CalicoBgpPeer(
            name=name,
            peer_ip=ip,
            as_number="64513",
            node_selector="all()",
        )

    def test_empty_returns_no_configuration(self) -> None:
        assert _summary(None, [], None) == "No Calico BGP configuration or peers observed."

    def test_asn_only(self) -> None:
        assert _summary("64512", [], None) == "BGP: ASN 64512"

    def test_mesh_enabled_exact(self) -> None:
        assert _summary(None, [], True) == "BGP: node-to-node mesh enabled"

    def test_mesh_disabled_exact(self) -> None:
        assert _summary(None, [], False) == "BGP: node-to-node mesh disabled"

    def test_mesh_none_omitted_with_asn(self) -> None:
        assert _summary("64512", [], None) == "BGP: ASN 64512"

    def test_peers_count_exact(self) -> None:
        assert _summary(None, [self._peer()], None) == "BGP: 1 BGP peer(s)"

    def test_multi_peer_count(self) -> None:
        peers = [self._peer(), self._peer("p2", "10.0.0.3")]
        assert _summary(None, peers, None) == "BGP: 2 BGP peer(s)"

    def test_asn_mesh_peers_combined(self) -> None:
        summary = _summary("64512", [self._peer()], True)
        assert summary == "BGP: ASN 64512; node-to-node mesh enabled; 1 BGP peer(s)"
