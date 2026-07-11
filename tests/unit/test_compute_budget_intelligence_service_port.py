from abc import ABC


class TestComputeBudgetIntelligenceServicePort:
    def test_is_abc(self) -> None:
        from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (  # noqa: E501
            ComputeBudgetIntelligenceServicePort,
        )

        assert issubclass(ComputeBudgetIntelligenceServicePort, ABC)

    def test_declares_compute(self) -> None:
        from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (  # noqa: E501
            ComputeBudgetIntelligenceServicePort,
        )

        assert "compute" in ComputeBudgetIntelligenceServicePort.__abstractmethods__
