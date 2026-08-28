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


def _default_configuration(
    configurations: Sequence[CalicoBgpConfiguration],
) -> CalicoBgpConfiguration | None:
    if not configurations:
        return None
    for config in configurations:
        if config.name == "default":
            return config
    return configurations[0]


def _session_state(detection: CalicoDetectionResult) -> tuple[str, str | None]:
    if detection.total_nodes == 0:
        return "unknown", "No calico-node agents observed; BGP session state unknown"
    if detection.degraded_agents > 0:
        return "degraded", (
            f"{detection.degraded_agents} calico-node agent(s) degraded; "
            "BGP sessions may be affected"
        )
    return "reachable", "All calico-node agents ready; BGP peer state not directly observed"


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
