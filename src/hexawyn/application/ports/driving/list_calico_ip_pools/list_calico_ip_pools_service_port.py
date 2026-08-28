from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.response import (
    ListCalicoIpPoolsResponse,
)


class ListCalicoIpPoolsServicePort(ABC):
    """Inbound port for listing Calico IPPools."""

    @abstractmethod
    def list_pools(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse: ...
