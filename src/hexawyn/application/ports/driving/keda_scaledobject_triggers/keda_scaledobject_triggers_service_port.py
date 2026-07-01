from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_command import (
    KedaScaledObjectTriggersCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_triggers.keda_scaledobject_triggers_response import (
    KedaScaledObjectTriggersResponse,
)


class KedaScaledObjectTriggersServicePort(ABC):
    @abstractmethod
    def get_triggers(
        self, command: KedaScaledObjectTriggersCommand
    ) -> KedaScaledObjectTriggersResponse: ...
