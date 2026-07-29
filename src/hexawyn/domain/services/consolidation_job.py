"""Memory consolidation domain service."""

import logging
import uuid
from datetime import UTC, datetime

from hexawyn.application.ports.driven.consolidation_port import (
    ConsolidationConfig,
    ConsolidationPort,
)
from hexawyn.domain.models.consolidation import (
    ConsolidatedKnowledge,
)
from hexawyn.domain.models.consolidation import (
    ConsolidationConfig as DomainConfig,
)

logger = logging.getLogger(__name__)


class ConsolidationJob:
    def __init__(
        self,
        port: ConsolidationPort,
        config: DomainConfig | None = None,
    ) -> None:
        self._port = port
        self._config = config or DomainConfig()

    def run(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def _consolidate_group(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    @staticmethod
    def _build_pattern(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "unknown resource"
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )
