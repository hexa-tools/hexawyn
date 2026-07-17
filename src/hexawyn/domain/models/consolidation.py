"""Memory consolidation domain models."""

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class ConsolidationConfig:
    min_occurrences: int = 2
    similarity_threshold: float = 0.85
    max_age_days: int = 90
    run_interval_hours: int = 24


@dataclass
class ConsolidatedKnowledge:
    pattern: str
    tool_name: str
    occurrence_count: int
    id: str = field(default_factory=lambda: str(uuid4()))
    resource_name: str | None = None
    resource_kind: str | None = None
    namespace: str | None = None
    first_seen: str = ""
    last_seen: str = ""
    source_incident_ids: list[str] = field(default_factory=list)
    embedding: list[float] = field(default_factory=list)
    weight: float = 1.0
    confidence: float = 0.5
