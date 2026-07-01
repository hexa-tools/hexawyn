from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_command import (
    KedaTriggerAuthGetCommand,
)
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_response import (
    KedaTriggerAuthGetResponse,
)


class KedaTriggerAuthGetServicePort(ABC):
    @abstractmethod
    def get_auth(self, command: KedaTriggerAuthGetCommand) -> KedaTriggerAuthGetResponse: ...
