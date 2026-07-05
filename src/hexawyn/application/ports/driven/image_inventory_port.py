from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class RunningImageRaw(TypedDict):
    image: str
    namespace: str
    pod_name: str


class ImageInventoryPort(ABC):
    """Port for enumerating every unique container image currently running
    in the cluster, covering init, regular, and ephemeral containers."""

    @abstractmethod
    def list_running_images(self) -> list[RunningImageRaw]:
        """List every container's image reference across all namespaces,
        joined to its owning Pod."""
