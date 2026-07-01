from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TraceK8sEventsCommand:
    trace_id: str
