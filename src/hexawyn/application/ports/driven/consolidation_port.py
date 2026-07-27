"""Consolidation port — memory consolidation driven port."""

from abc import ABC, abstractmethod
from typing import TypedDict


class ConsolidationConfig(TypedDict):
    min_occurrences: int
    similarity_threshold: float
    max_age_days: int


class ConsolidationPort(ABC):
    @abstractmethod
    def find_incident_groups(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        """Group incidents by namespace+resource+tool, return tuples."""

    @abstractmethod
    def get_incidents_for_group(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        """Return incident IDs for a given group."""

    @abstractmethod
    def store_knowledge(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        """Persist consolidated knowledge."""

    @abstractmethod
    def mark_consolidated(self, incident_ids: list[str], knowledge_id: str) -> None:
        """Mark source incidents as consolidated."""

    @abstractmethod
    def search_consolidated(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        """VSS search in consolidated knowledge."""
