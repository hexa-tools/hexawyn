from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledobject_get.command import (  # type: ignore
    KedaScaledObjectGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_get.response import (  # type: ignore
    KedaScaledObjectGetResponse,
)


class KedaScaledObjectGetServicePort(ABC):
    @abstractmethod
    def get_object(self, command: KedaScaledObjectGetCommand) -> KedaScaledObjectGetResponse: ...
