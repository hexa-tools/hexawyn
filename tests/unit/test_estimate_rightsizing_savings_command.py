"""RED tests — driving ports: command / response / service_port"""

from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_command import (
    EstimateRightsizingSavingsCommand,
)


class TestEstimateRightsizingSavingsCommand:
    def test_defaults(self) -> None:
        cmd = EstimateRightsizingSavingsCommand()
        assert cmd.top_n == 5

    def test_custom_top_n(self) -> None:
        cmd = EstimateRightsizingSavingsCommand(top_n=10)
        assert cmd.top_n == 10

    def test_is_frozen(self) -> None:
        import pytest

        cmd = EstimateRightsizingSavingsCommand()
        with pytest.raises((AttributeError, TypeError)):
            cmd.top_n = 99  # type: ignore[misc]
