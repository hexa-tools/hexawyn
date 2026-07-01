from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_command import (
    KedaScaledObjectsListCommand,
)
from hexawyn.application.ports.driving.keda_scaledobjects_list.keda_scaledobjects_list_response import (
    KedaScaledObjectsListResponse,
)


class KedaScaledObjectsListServicePort(ABC):
    @abstractmethod
    def list_objects(
        self, command: KedaScaledObjectsListCommand
    ) -> KedaScaledObjectsListResponse: ...
