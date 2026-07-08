from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PipelineForServiceCommand:
    service_name: str
