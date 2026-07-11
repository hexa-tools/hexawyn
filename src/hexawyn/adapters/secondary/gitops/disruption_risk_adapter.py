from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.disruption_risk_port import (
    DisruptionRiskPort,
    RiskEventRaw,
)


class DisruptionRiskSource(Protocol):
    def fetch_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]: ...


class DisruptionRiskAdapter(DisruptionRiskPort):
    def __init__(self, source: DisruptionRiskSource) -> None:
        self._source = source

    def get_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]:
        return self._source.fetch_disruption_risks(warning_days)
