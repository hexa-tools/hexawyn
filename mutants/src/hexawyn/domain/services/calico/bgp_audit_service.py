"""Pure Calico BGP audit — no infrastructure imports.

Combines the observed BGPConfiguration (ASN, node-to-node mesh, service
cluster IPs), the BGPPeer list and the calico-node agent health into a truthful
audit. BGP session state is never fabricated: it is derived only from the
observed calico-node agent readiness, and reported ``unknown`` when no agent
health is observable.
"""

from __future__ import annotations

from collections.abc import Sequence

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoBgpAuditResult,
    CalicoBgpConfiguration,
    CalicoBgpPeer,
    CalicoDetectionResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_bgp_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_bgp_audit__mutmut)
def build_calico_bgp_audit(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_orig(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_1(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_2(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=None,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_3(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=None,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_4(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=None,
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_5(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=None,
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_6(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=None,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_7(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state=None,
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_8(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=None,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_9(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_10(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_11(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_12(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_13(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_14(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_15(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_16(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_17(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_18(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_19(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_20(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=True,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_21(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=1,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_22(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="XXunknownXX",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_23(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="UNKNOWN",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_24(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = None
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_25(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(None)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_26(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = None
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_27(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(None)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_28(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = None
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_29(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(None)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_30(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = None
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_31(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_32(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        None,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_33(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_34(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_35(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_36(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_37(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=None,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_38(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_39(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_40(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=None,
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_41(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=None,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_42(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=None,
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_43(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=None,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_44(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=None,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_45(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=None,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_46(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=None,
    )


def x_build_calico_bgp_audit__mutmut_47(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_48(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_49(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_50(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_51(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_52(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_53(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_54(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_55(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_56(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        error=detection.error,
    )


def x_build_calico_bgp_audit__mutmut_57(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=True,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        )


def x_build_calico_bgp_audit__mutmut_58(
    *,
    configurations: Sequence[CalicoBgpConfiguration],
    peers: Sequence[CalicoBgpPeer],
    detection: CalicoDetectionResult,
) -> CalicoBgpAuditResult:
    """Compose the Calico BGP audit from config, peers and agent health."""
    if not detection.installed:
        return CalicoBgpAuditResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            as_number=None,
            node_to_node_mesh_enabled=None,
            service_cluster_ips=(),
            peers=[],
            peer_count=0,
            session_state="unknown",
            session_note=None,
            summary=None,
            error=detection.error,
        )

    config = _default_configuration(configurations)
    session_state, session_note = _session_state(detection)
    peers_list = list(peers)
    summary = _summary(
        config.as_number if config else None,
        peers_list,
        config.node_to_node_mesh_enabled if config else None,
    )
    return CalicoBgpAuditResult(
        installed=False,
        not_installed_marker=None,
        as_number=config.as_number if config else None,
        node_to_node_mesh_enabled=config.node_to_node_mesh_enabled if config else None,
        service_cluster_ips=config.service_cluster_ips if config else (),
        peers=peers_list,
        peer_count=len(peers_list),
        session_state=session_state,
        session_note=session_note,
        summary=summary,
        error=detection.error,
    )

mutants_x_build_calico_bgp_audit__mutmut['_mutmut_orig'] = x_build_calico_bgp_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_1'] = x_build_calico_bgp_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_2'] = x_build_calico_bgp_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_3'] = x_build_calico_bgp_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_4'] = x_build_calico_bgp_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_5'] = x_build_calico_bgp_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_6'] = x_build_calico_bgp_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_7'] = x_build_calico_bgp_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_8'] = x_build_calico_bgp_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_9'] = x_build_calico_bgp_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_10'] = x_build_calico_bgp_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_11'] = x_build_calico_bgp_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_12'] = x_build_calico_bgp_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_13'] = x_build_calico_bgp_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_14'] = x_build_calico_bgp_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_15'] = x_build_calico_bgp_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_16'] = x_build_calico_bgp_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_17'] = x_build_calico_bgp_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_18'] = x_build_calico_bgp_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_19'] = x_build_calico_bgp_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_20'] = x_build_calico_bgp_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_21'] = x_build_calico_bgp_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_22'] = x_build_calico_bgp_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_23'] = x_build_calico_bgp_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_24'] = x_build_calico_bgp_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_25'] = x_build_calico_bgp_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_26'] = x_build_calico_bgp_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_27'] = x_build_calico_bgp_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_28'] = x_build_calico_bgp_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_29'] = x_build_calico_bgp_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_30'] = x_build_calico_bgp_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_31'] = x_build_calico_bgp_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_32'] = x_build_calico_bgp_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_33'] = x_build_calico_bgp_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_34'] = x_build_calico_bgp_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_35'] = x_build_calico_bgp_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_36'] = x_build_calico_bgp_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_37'] = x_build_calico_bgp_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_38'] = x_build_calico_bgp_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_39'] = x_build_calico_bgp_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_40'] = x_build_calico_bgp_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_41'] = x_build_calico_bgp_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_42'] = x_build_calico_bgp_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_43'] = x_build_calico_bgp_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_44'] = x_build_calico_bgp_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_45'] = x_build_calico_bgp_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_46'] = x_build_calico_bgp_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_47'] = x_build_calico_bgp_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_48'] = x_build_calico_bgp_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_49'] = x_build_calico_bgp_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_50'] = x_build_calico_bgp_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_51'] = x_build_calico_bgp_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_52'] = x_build_calico_bgp_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_53'] = x_build_calico_bgp_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_54'] = x_build_calico_bgp_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_55'] = x_build_calico_bgp_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_56'] = x_build_calico_bgp_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_57'] = x_build_calico_bgp_audit__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_calico_bgp_audit__mutmut['x_build_calico_bgp_audit__mutmut_58'] = x_build_calico_bgp_audit__mutmut_58 # type: ignore # mutmut generated
mutants_x__default_configuration__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__default_configuration__mutmut)
def _default_configuration(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name == "default":
            return config
    return configurations[0]


def x__default_configuration__mutmut_orig(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name == "default":
            return config
    return configurations[0]


def x__default_configuration__mutmut_1(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if configurations:
        return None
    for config in configurations:
        if config.name == "default":
            return config
    return configurations[0]


def x__default_configuration__mutmut_2(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name != "default":
            return config
    return configurations[0]


def x__default_configuration__mutmut_3(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name == "XXdefaultXX":
            return config
    return configurations[0]


def x__default_configuration__mutmut_4(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name == "DEFAULT":
            return config
    return configurations[0]


def x__default_configuration__mutmut_5(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name == "default":
            return config
    return configurations[1]

mutants_x__default_configuration__mutmut['_mutmut_orig'] = x__default_configuration__mutmut_orig # type: ignore # mutmut generated
mutants_x__default_configuration__mutmut['x__default_configuration__mutmut_1'] = x__default_configuration__mutmut_1 # type: ignore # mutmut generated
mutants_x__default_configuration__mutmut['x__default_configuration__mutmut_2'] = x__default_configuration__mutmut_2 # type: ignore # mutmut generated
mutants_x__default_configuration__mutmut['x__default_configuration__mutmut_3'] = x__default_configuration__mutmut_3 # type: ignore # mutmut generated
mutants_x__default_configuration__mutmut['x__default_configuration__mutmut_4'] = x__default_configuration__mutmut_4 # type: ignore # mutmut generated
mutants_x__default_configuration__mutmut['x__default_configuration__mutmut_5'] = x__default_configuration__mutmut_5 # type: ignore # mutmut generated
mutants_x__session_state__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__session_state__mutmut)
def _session_state(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_orig(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_1(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes != 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_2(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 1:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_3(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "XXunknownXX", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_4(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "UNKNOWN", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_5(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "XXNo calico-node agents observed; BGP session state unknownXX"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_6(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "no calico-node agents observed; bgp session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_7(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "NO CALICO-NODE AGENTS OBSERVED; BGP SESSION STATE UNKNOWN"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_8(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents >= 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_9(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 1:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_10(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "XXdegradedXX", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_11(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "DEGRADED", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_12(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "XXBGP sessions may be affectedXX"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_13(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "bgp sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_14(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP SESSIONS MAY BE AFFECTED"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_15(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "XXreachableXX", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_16(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "REACHABLE", "All calico-node agents ready; BGP peer state not directly observed"


def x__session_state__mutmut_17(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "XXAll calico-node agents ready; BGP peer state not directly observedXX"


def x__session_state__mutmut_18(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "all calico-node agents ready; bgp peer state not directly observed"


def x__session_state__mutmut_19(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "ALL CALICO-NODE AGENTS READY; BGP PEER STATE NOT DIRECTLY OBSERVED"

mutants_x__session_state__mutmut['_mutmut_orig'] = x__session_state__mutmut_orig # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_1'] = x__session_state__mutmut_1 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_2'] = x__session_state__mutmut_2 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_3'] = x__session_state__mutmut_3 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_4'] = x__session_state__mutmut_4 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_5'] = x__session_state__mutmut_5 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_6'] = x__session_state__mutmut_6 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_7'] = x__session_state__mutmut_7 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_8'] = x__session_state__mutmut_8 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_9'] = x__session_state__mutmut_9 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_10'] = x__session_state__mutmut_10 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_11'] = x__session_state__mutmut_11 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_12'] = x__session_state__mutmut_12 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_13'] = x__session_state__mutmut_13 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_14'] = x__session_state__mutmut_14 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_15'] = x__session_state__mutmut_15 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_16'] = x__session_state__mutmut_16 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_17'] = x__session_state__mutmut_17 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_18'] = x__session_state__mutmut_18 # type: ignore # mutmut generated
mutants_x__session_state__mutmut['x__session_state__mutmut_19'] = x__session_state__mutmut_19 # type: ignore # mutmut generated
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
def _summary(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_orig(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_1(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = None
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_2(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_3(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(None)
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_4(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_5(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(None)
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_6(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'XXenabledXX' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_7(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'ENABLED' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_8(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'XXdisabledXX'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_9(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'DISABLED'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_10(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(None)
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_11(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_12(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "XXNo Calico BGP configuration or peers observed.XX"
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_13(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "no calico bgp configuration or peers observed."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_14(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "NO CALICO BGP CONFIGURATION OR PEERS OBSERVED."
    return "BGP: " + "; ".join(parts)


def x__summary__mutmut_15(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " - "; ".join(parts)


def x__summary__mutmut_16(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "XXBGP: XX" + "; ".join(parts)


def x__summary__mutmut_17(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "bgp: " + "; ".join(parts)


def x__summary__mutmut_18(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "; ".join(None)


def x__summary__mutmut_19(
    as_number: str | None,
    peers: list[CalicoBgpPeer],
    mesh_enabled: bool | None,
) -> str:
    parts: list[str] = []
    if as_number is not None:
        parts.append(f"ASN {as_number}")
    if mesh_enabled is not None:
        parts.append(f"node-to-node mesh {'enabled' if mesh_enabled else 'disabled'}")
    if peers:
        parts.append(f"{len(peers)} BGP peer(s)")
    if not parts:
        return "No Calico BGP configuration or peers observed."
    return "BGP: " + "XX; XX".join(parts)

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_3'] = x__summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_4'] = x__summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_5'] = x__summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_6'] = x__summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_7'] = x__summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_8'] = x__summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_9'] = x__summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_10'] = x__summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_11'] = x__summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_12'] = x__summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_13'] = x__summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_14'] = x__summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_15'] = x__summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_16'] = x__summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_17'] = x__summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_18'] = x__summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_19'] = x__summary__mutmut_19 # type: ignore # mutmut generated
