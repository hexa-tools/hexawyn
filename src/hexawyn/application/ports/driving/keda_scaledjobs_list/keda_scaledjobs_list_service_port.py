from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_command import (
    KedaScaledJobsListCommand,
)
from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_response import (
    KedaScaledJobsListResponse,
)


class KedaScaledJobsListServicePort(ABC):
    @abstractmethod
    def list_jobs(self, command: KedaScaledJobsListCommand) -> KedaScaledJobsListResponse: ...
