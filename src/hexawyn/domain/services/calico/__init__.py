"""Calico domain service — pure detection & status logic."""

from hexawyn.domain.services.calico.detection_service import (
    build_agent_phase,
    build_degraded_summary,
    build_detection_result,
    resolve_dataplane_mode,
)
from hexawyn.domain.services.calico.get_calico_status_service import (
    build_calico_status_result,
)
from hexawyn.domain.services.calico.network_policy_service import (
    parse_calico_network_policy,
    parse_global_network_policy,
)
from hexawyn.domain.services.calico.policy_audit_service import (
    build_calico_policy_audit,
)
from hexawyn.domain.services.calico.segmentation_service import (
    build_calico_segmentation_audit,
)

__all__ = [
    "build_agent_phase",
    "build_calico_policy_audit",
    "build_calico_segmentation_audit",
    "build_calico_status_result",
    "build_degraded_summary",
    "build_detection_result",
    "parse_calico_network_policy",
    "parse_global_network_policy",
    "resolve_dataplane_mode",
]
