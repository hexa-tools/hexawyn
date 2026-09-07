from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.compute_security_posture.command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.security.compute_security_posture.response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComputeSecurityPostureServicePort(ABC):
    @abstractmethod
    def compute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse: ...
