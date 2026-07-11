from abc import ABC


class TestReportPlatformReliabilityServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (  # noqa: E501
            ReportPlatformReliabilityServicePort,
        )

        assert issubclass(ReportPlatformReliabilityServicePort, ABC)

    def test_declares_report_method(self) -> None:
        from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (  # noqa: E501
            ReportPlatformReliabilityServicePort,
        )

        assert "report" in ReportPlatformReliabilityServicePort.__abstractmethods__
