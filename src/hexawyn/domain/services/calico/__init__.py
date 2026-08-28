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

__all__ = [
    "build_agent_phase",
    "build_calico_status_result",
    "build_degraded_summary",
    "build_detection_result",
    "resolve_dataplane_mode",
]
