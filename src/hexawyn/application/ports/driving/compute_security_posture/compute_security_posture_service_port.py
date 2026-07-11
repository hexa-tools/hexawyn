from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)


class ComputeSecurityPostureServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse: ...
