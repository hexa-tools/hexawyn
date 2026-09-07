from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.response import (
    ListCalicoIpPoolsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListCalicoIpPoolsServicePort(ABC):
    """Inbound port for listing Calico IPPools."""

    @abstractmethod
    def list_pools(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse: ...
