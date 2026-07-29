from dataclasses import dataclass

from hexawyn.domain.models.consolidation import ConsolidatedKnowledge


@dataclass
class RunConsolidationResponse:
    consolidated: list[ConsolidatedKnowledge]
    groups_found: int = 0
