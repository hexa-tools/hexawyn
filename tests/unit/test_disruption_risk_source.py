from hexawyn.adapters.secondary.gitops.disruption_risk_source import EmptyDisruptionRiskSource


class TestEmptyDisruptionRiskSource:
    def test_returns_empty(self) -> None:
        assert EmptyDisruptionRiskSource().fetch_disruption_risks(7) == []
