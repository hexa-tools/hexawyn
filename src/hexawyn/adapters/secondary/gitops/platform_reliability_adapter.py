from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
    ReliabilityData,
)


class ReliabilityDataSource(Protocol):
    """Assembles reliability inputs from the incident/MTTR sources and pricing
    config into the uniform ReliabilityData contract."""

    def fetch_reliability_data(self, period: str) -> ReliabilityData: ...


class PlatformReliabilityAdapter(PlatformReliabilityPort):
    """Facade over the incident / MTTR / pricing sources for the CTO report.

    Delegates to an injected source that normalizes those sources into
    ReliabilityData, keeping the domain free of any knowledge of them.
    """

    def __init__(self, source: ReliabilityDataSource) -> None:
        self._source = source

    def get_reliability_data(self, period: str) -> ReliabilityData:
        return self._source.fetch_reliability_data(period)
