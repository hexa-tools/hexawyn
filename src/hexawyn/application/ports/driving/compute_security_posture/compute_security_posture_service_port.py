from abc import ABC, abstractmethod

from hexawyn.application.use_case.compute_security_posture.command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.compute_security_posture.response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)


class ComputeSecurityPostureServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse: ...
