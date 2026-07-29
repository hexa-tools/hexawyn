from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.version_regression.command import (
    VersionRegressionCommand,
)
from hexawyn.application.use_case.pipelines.version_regression.response import (
    VersionRegressionResponse,
)


class VersionRegressionServicePort(ABC):
    @abstractmethod
    def detect(self, command: VersionRegressionCommand) -> VersionRegressionResponse: ...
