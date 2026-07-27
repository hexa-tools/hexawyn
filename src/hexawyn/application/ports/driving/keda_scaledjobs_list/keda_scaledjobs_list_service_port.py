from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledjobs_list.command import (  # type: ignore
    KedaScaledJobsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjobs_list.response import (  # type: ignore
    KedaScaledJobsListResponse,
)


class KedaScaledJobsListServicePort(ABC):
    @abstractmethod
    def list_jobs(self, command: KedaScaledJobsListCommand) -> KedaScaledJobsListResponse: ...
