from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.ports.driving.check_resource_constraints.check_resource_constraints_response import (
    CheckResourceConstraintsResponse,
)


class CheckResourceConstraintsServicePort(ABC):
    @abstractmethod
    def check_resource_constraints(
        self, command: CheckResourceConstraintsCommand
    ) -> CheckResourceConstraintsResponse: ...
