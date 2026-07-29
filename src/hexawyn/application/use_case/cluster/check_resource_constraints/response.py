from dataclasses import dataclass

from hexawyn.domain.models.resource_constraint import ResourceConstraintReport


@dataclass
class CheckResourceConstraintsResponse:
    report: ResourceConstraintReport | None = None
