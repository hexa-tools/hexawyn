from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RedundantCallsCommand:
    flow: str
    trace_id: str | None = None
