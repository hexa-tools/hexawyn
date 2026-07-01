from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AdminEndpointAuditCommand:
    endpoint_pattern: str = "/admin*"
    time_window_minutes: int = 30
    flag_threshold: int = 5
