# mypy: ignore-errors
from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledobject_triggers.command import (  # noqa: E501  # type: ignore
    KedaScaledObjectTriggersCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.response import (  # noqa: E501  # type: ignore
    KedaScaledObjectTriggersResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KedaScaledObjectTriggersServicePort(ABC):
    @abstractmethod
    def get_triggers(
        self, command: KedaScaledObjectTriggersCommand
    ) -> KedaScaledObjectTriggersResponse: ...
