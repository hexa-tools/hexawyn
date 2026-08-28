"""Calico domain service — pure detection logic."""

from hexawyn.domain.services.calico.detection_service import (
    build_agent_phase,
    build_degraded_summary,
    build_detection_result,
    resolve_dataplane_mode,
)

__all__ = [
    "build_agent_phase",
    "build_degraded_summary",
    "build_detection_result",
    "resolve_dataplane_mode",
]
