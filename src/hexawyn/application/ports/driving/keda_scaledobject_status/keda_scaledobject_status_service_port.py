from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledobject_status.command import (  # type: ignore
    KedaScaledObjectStatusCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_status.response import (  # type: ignore
    KedaScaledObjectStatusResponse,
)


class KedaScaledObjectStatusServicePort(ABC):
    @abstractmethod
    def get_status(
        self, command: KedaScaledObjectStatusCommand
    ) -> KedaScaledObjectStatusResponse: ...
