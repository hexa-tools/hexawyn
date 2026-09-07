"""CalicoBgpAuditUseCase — Calico BGP config, peers and session state."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_bgp_audit.command import CalicoBgpAuditCommand
from hexawyn.application.use_case.calico.calico_bgp_audit.response import CalicoBgpAuditResponse
from hexawyn.domain.services.calico.bgp_audit_service import build_calico_bgp_audit


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoBgpAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoBgpAuditUseCase:
    """Orchestrates the Calico BGP audit — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoBgpAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoBgpAuditUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoBgpAuditUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut)
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_orig(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_1(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = None
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_2(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if detection.installed:
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_3(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_4(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_5(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_6(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_7(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
                session_state=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_8(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
                session_state="unknown",
                error=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_9(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_10(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_11(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_12(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_13(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_14(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
                session_state="unknown",
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_15(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=True,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_16(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=1,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_17(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
                session_state="XXunknownXX",
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_18(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoBgpAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                peer_count=0,
                peers=[],
                session_state="UNKNOWN",
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_19(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
        configurations = None
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_20(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
        peers = None
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_21(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
        result = None
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_22(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            configurations=None, peers=peers, detection=detection
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_23(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            configurations=configurations, peers=None, detection=detection
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_24(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            configurations=configurations, peers=peers, detection=None
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_25(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            peers=peers, detection=detection
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_26(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            configurations=configurations, detection=detection
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_27(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            configurations=configurations, peers=peers, )
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_28(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            installed=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_29(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            not_installed_marker=None,
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_30(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            as_number=None,
            node_to_node_mesh_enabled=result.node_to_node_mesh_enabled,
            service_cluster_ips=list(result.service_cluster_ips),
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_31(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            node_to_node_mesh_enabled=None,
            service_cluster_ips=list(result.service_cluster_ips),
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_32(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            service_cluster_ips=None,
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_33(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            peer_count=None,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_34(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            peers=None,
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_35(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            session_state=None,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_36(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            session_note=None,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_37(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            summary=None,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_38(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            error=None,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_39(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_40(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_41(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            node_to_node_mesh_enabled=result.node_to_node_mesh_enabled,
            service_cluster_ips=list(result.service_cluster_ips),
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_42(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            service_cluster_ips=list(result.service_cluster_ips),
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_43(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_44(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_45(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_46(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_47(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_48(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_49(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_50(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            service_cluster_ips=list(None),
            peer_count=result.peer_count,
            peers=list(result.peers),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoBgpAuditUseCaseǁexecute__mutmut_51(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse:
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
            peers=list(None),
            session_state=result.session_state,
            session_note=result.session_note,
            summary=result.summary,
            error=result.error,
        )

mutants_xǁCalicoBgpAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁ__init____mutmut['xǁCalicoBgpAuditUseCaseǁ__init____mutmut_1'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_1'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_2'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_3'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_4'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_5'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_6'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_7'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_8'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_9'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_10'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_11'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_12'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_13'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_14'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_15'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_16'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_17'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_18'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_19'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_20'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_21'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_22'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_23'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_24'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_25'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_26'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_27'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_28'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_29'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_30'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_31'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_32'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_33'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_34'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_35'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_36'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_37'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_38'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_39'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_40'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_41'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_42'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_43'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_44'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_45'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_46'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_47'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_48'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_49'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_50'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCalicoBgpAuditUseCaseǁexecute__mutmut['xǁCalicoBgpAuditUseCaseǁexecute__mutmut_51'] = CalicoBgpAuditUseCase.xǁCalicoBgpAuditUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
