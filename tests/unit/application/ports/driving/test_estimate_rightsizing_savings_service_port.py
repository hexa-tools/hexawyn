"""RED tests — EstimateRightsizingSavingsServicePort ABC"""

from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_service_port import (
    EstimateRightsizingSavingsServicePort,
)


class TestEstimateRightsizingSavingsServicePort:
    def test_cannot_instantiate_directly(self) -> None:
        import pytest

        with pytest.raises(TypeError):
            EstimateRightsizingSavingsServicePort()  # type: ignore[abstract]

    def test_has_estimate_method(self) -> None:
        assert hasattr(EstimateRightsizingSavingsServicePort, "estimate_rightsizing_savings")
