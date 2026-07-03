from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.label_search import ResourceType

_ALL_RESOURCE_TYPES: list[ResourceType] = ["pods", "deployments", "services", "configmaps"]


@dataclass(frozen=True)
class SearchResourcesByLabelsCommand:
    label_selector: str
    resource_types: list[ResourceType] = field(default_factory=lambda: list(_ALL_RESOURCE_TYPES))
    namespace: str | None = None
