from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_response import (
    DiffHelmValuesResponse,
)


class DiffHelmValuesServicePort(ABC):
    @abstractmethod
    def diff(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse: ...
