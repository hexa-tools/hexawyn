from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class IncidentMemoryRecord:
    """A completed investigation to persist in the incident-memory store.

    Pure domain value object — no infrastructure concerns. The embedding is a
    dense vector (768 dims, nomic-embed-text) produced by the runtime backend;
    an empty list means no embedding is available and the record must not be
    persisted for similarity search.
    """

    cluster_name: str
    tool_name: str
    cause: str = ""
    solution: str = ""
    severity: str = "low"
    namespace: str | None = None
    resource_name: str | None = None
    resource_kind: str | None = None
    symptoms: list[str] = field(default_factory=list)
    embedding: list[float] = field(default_factory=list)
    sanitized: bool = False

    @property
    def is_storable(self) -> bool:
        """True when the record carries the data required for VSS retrieval."""
        return bool(self.cluster_name) and bool(self.tool_name) and len(self.embedding) > 0
