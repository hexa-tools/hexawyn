from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort, RiskEventRaw


class _FakeSource:
    def fetch_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]:
        return [
            RiskEventRaw(
                business_service_name="moteur de recommandation",
                risk_type="memory_saturation",
                predicted_date="2026-09-20",
                days_from_now=3,
                detail="Saturation memoire",
            )
        ]


class TestPortImplementation:
    def test_is_disruption_risk_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.disruption_risk_adapter import DisruptionRiskAdapter

        assert isinstance(DisruptionRiskAdapter(source=_FakeSource()), DisruptionRiskPort)

    def test_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.disruption_risk_adapter import DisruptionRiskAdapter

        adapter = DisruptionRiskAdapter(source=_FakeSource())
        result = adapter.get_disruption_risks(7)

        assert result[0]["business_service_name"] == "moteur de recommandation"
