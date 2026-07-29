from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledobjects_list.command import (  # type: ignore
    KedaScaledObjectsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobjects_list.response import (  # type: ignore
    KedaScaledObjectsListResponse,
)


class KedaScaledObjectsListServicePort(ABC):
    @abstractmethod
    def list_objects(
        self, command: KedaScaledObjectsListCommand
    ) -> KedaScaledObjectsListResponse: ...
