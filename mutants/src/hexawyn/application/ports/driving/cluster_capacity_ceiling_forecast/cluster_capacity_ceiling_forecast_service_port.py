from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.response import (
    ClusterCapacityCeilingForecastResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ClusterCapacityCeilingForecastServicePort(ABC):
    @abstractmethod
    def forecast(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse: ...
