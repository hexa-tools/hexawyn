from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw


class EmptyDisruptionRiskSource:
    def fetch_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]:
        return []
