from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_command import (
    KedaTriggerAuthListCommand,
)
from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_response import (
    KedaTriggerAuthListResponse,
)


class KedaTriggerAuthListServicePort(ABC):
    @abstractmethod
    def list_auths(self, command: KedaTriggerAuthListCommand) -> KedaTriggerAuthListResponse: ...
