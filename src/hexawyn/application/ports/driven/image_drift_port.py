from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class ResolvedContainerImageRaw(TypedDict):
    deployment: str
    namespace: str
    container: str
    image_id: str


class ImageDriftPort(ABC):
    """Port for resolving each running container's actually-pulled image
    digest (kubelet-populated pod status), used to detect mutable-tag drift
    without ever calling a container registry."""

    @abstractmethod
    def list_resolved_container_images(self, namespace: str) -> list[ResolvedContainerImageRaw]:
        """List every container's resolved imageID, joined to its owning
        Deployment via label-selector match."""
