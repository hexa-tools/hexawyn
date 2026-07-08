from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.version_regression.version_regression_command import (
    VersionRegressionCommand,
)
from hexawyn.application.ports.driving.version_regression.version_regression_response import (
    VersionRegressionResponse,
)


class VersionRegressionServicePort(ABC):
    @abstractmethod
    def detect(self, command: VersionRegressionCommand) -> VersionRegressionResponse: ...
