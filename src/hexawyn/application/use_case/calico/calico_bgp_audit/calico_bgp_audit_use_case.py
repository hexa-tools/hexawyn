"""CalicoBgpAuditUseCase — Calico BGP config, peers and session state."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_bgp_audit.command import CalicoBgpAuditCommand
from hexawyn.application.use_case.calico.calico_bgp_audit.response import CalicoBgpAuditResponse
from hexawyn.domain.services.calico.bgp_audit_service import build_calico_bgp_audit


class CalicoBgpAuditUseCase:
    """Orchestrates the Calico BGP audit — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
                session_state="unknown",
                error=detection.error,
            )
        configurations = self._port.list_bgp_configurations()
        peers = self._port.list_bgp_peers()
        result = build_calico_bgp_audit(
            configurations=configurations, peers=peers, detection=detection
        )
        return CalicoBgpAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            as_number=result.as_number,
            node_to_node_mesh_enabled=result.node_to_node_mesh_enabled,
            service_cluster_ips=list(result.service_cluster_ips),
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )
