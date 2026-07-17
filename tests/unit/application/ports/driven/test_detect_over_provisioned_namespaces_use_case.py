"""Unit tests for DetectOverProvisionedNamespacesUseCase and application service."""

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.namespace_waste_port import (
    NamespaceRawData,
    NamespaceWasteAnalysisPort,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_response import (
    DetectOverProvisionedNamespacesResponse,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_service_port import (
    DetectOverProvisionedNamespacesServicePort,
)
from hexawyn.application.service.detect_over_provisioned_namespaces_service import (
    DetectOverProvisionedNamespacesService,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_use_case import (
    DetectOverProvisionedNamespacesUseCase,
)
from hexawyn.domain.errors import PrometheusUnavailableError


def _raw(
    namespace: str,
    cpu_req: float | None = 4.0,
    mem_req: float | None = 8.0,
    cpu_actual: float | None = 2.0,
    mem_actual: float | None = 4.0,
    age_hours: float = 48.0,
    has_requests: bool = True,
) -> NamespaceRawData:
    return {
        "namespace": namespace,
        "cpu_requested_cores": cpu_req,
        "memory_requested_gb": mem_req,
        "cpu_actual_avg_cores": cpu_actual,
        "memory_actual_avg_gb": mem_actual,
        "age_hours": age_hours,
        "has_resource_requests": has_requests,
    }


class TestDetectOverProvisionedNamespacesCommand:
    def test_is_frozen(self) -> None:
        cmd = DetectOverProvisionedNamespacesCommand()
        with pytest.raises(AttributeError):
            cmd.analysis_window_days = 14  # type: ignore[misc]

    def test_default_window_is_7_days(self) -> None:
        cmd = DetectOverProvisionedNamespacesCommand()
        assert cmd.analysis_window_days == 7

    def test_default_top_n_is_5(self) -> None:
        cmd = DetectOverProvisionedNamespacesCommand()
        assert cmd.top_n == 5

    def test_custom_values(self) -> None:
        cmd = DetectOverProvisionedNamespacesCommand(analysis_window_days=14, top_n=10)
        assert cmd.analysis_window_days == 14
        assert cmd.top_n == 10


class TestDetectOverProvisionedNamespacesResponse:
    def test_has_report_field(self) -> None:
        from hexawyn.domain.models.namespace_waste import OverProvisioningReport

        report = OverProvisioningReport(
            namespaces=[],
            excluded=[],
            total_wasted_cpu_cores=0.0,
            total_wasted_memory_gb=0.0,
            analysis_window_days=7,
        )
        response = DetectOverProvisionedNamespacesResponse(report=report, prometheus_available=True)
        assert response.report is report

    def test_has_prometheus_available_flag(self) -> None:
        from hexawyn.domain.models.namespace_waste import OverProvisioningReport

        report = OverProvisioningReport(
            namespaces=[],
            excluded=[],
            total_wasted_cpu_cores=0.0,
            total_wasted_memory_gb=0.0,
            analysis_window_days=7,
        )
        response = DetectOverProvisionedNamespacesResponse(
            report=report, prometheus_available=False
        )
        assert response.prometheus_available is False


class TestDetectOverProvisionedNamespacesServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(DetectOverProvisionedNamespacesServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            DetectOverProvisionedNamespacesServicePort()  # type: ignore[abstract]


class TestDetectOverProvisionedNamespacesUseCase:
    def test_delegates_to_service_port(self) -> None:
        from hexawyn.domain.models.namespace_waste import OverProvisioningReport

        fake_service = MagicMock(spec=DetectOverProvisionedNamespacesServicePort)
        report = OverProvisioningReport(
            namespaces=[],
            excluded=[],
            total_wasted_cpu_cores=0.0,
            total_wasted_memory_gb=0.0,
            analysis_window_days=7,
        )
        expected = DetectOverProvisionedNamespacesResponse(report=report, prometheus_available=True)
        fake_service.detect_over_provisioned_namespaces.return_value = expected

        result = DetectOverProvisionedNamespacesUseCase(service=fake_service).execute(
            DetectOverProvisionedNamespacesCommand()
        )

        assert result.report is report

    def test_passes_command_to_service(self) -> None:
        from hexawyn.domain.models.namespace_waste import OverProvisioningReport

        fake_service = MagicMock(spec=DetectOverProvisionedNamespacesServicePort)
        report = OverProvisioningReport(
            namespaces=[],
            excluded=[],
            total_wasted_cpu_cores=0.0,
            total_wasted_memory_gb=0.0,
            analysis_window_days=7,
        )
        fake_service.detect_over_provisioned_namespaces.return_value = (
            DetectOverProvisionedNamespacesResponse(report=report, prometheus_available=True)
        )
        cmd = DetectOverProvisionedNamespacesCommand(analysis_window_days=14, top_n=3)
        DetectOverProvisionedNamespacesUseCase(service=fake_service).execute(cmd)

        fake_service.detect_over_provisioned_namespaces.assert_called_once_with(cmd)


class TestDetectOverProvisionedNamespacesService:
    def test_implements_service_port(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)
        assert isinstance(service, DetectOverProvisionedNamespacesServicePort)

    def test_tc1_dev_flagged_production_healthy(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = [
            _raw("dev", cpu_req=8.0, cpu_actual=0.45, mem_req=16.0, mem_actual=1.2),
            _raw("production", cpu_req=4.0, cpu_actual=3.5, mem_req=8.0, mem_actual=7.5),
        ]
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        namespaces_map = {ns.namespace: ns for ns in response.report.namespaces}
        assert namespaces_map["dev"].is_over_provisioned is True
        assert namespaces_map["production"].is_over_provisioned is False

    def test_tc1_dev_ranked_first(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = [
            _raw("production", cpu_req=4.0, cpu_actual=3.5),
            _raw("dev", cpu_req=8.0, cpu_actual=0.45),
        ]
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        assert response.report.namespaces[0].namespace == "dev"

    def test_tc2_excluded_namespace_not_in_results(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = [
            _raw("dev", cpu_req=8.0, cpu_actual=0.45),
            _raw("new-ns", age_hours=6.0),
        ]
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        names = [ns.namespace for ns in response.report.namespaces]
        assert "new-ns" not in names
        excluded_names = [e.namespace for e in response.report.excluded]
        assert "new-ns" in excluded_names

    def test_prometheus_available_true_when_data_present(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = [
            _raw("dev", cpu_actual=0.45),
        ]
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        assert response.prometheus_available is True

    def test_prometheus_available_false_when_no_actual_data(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = [
            _raw("dev", cpu_actual=None, mem_actual=None),
        ]
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        assert response.prometheus_available is False

    def test_window_days_passed_to_port(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = []
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand(analysis_window_days=14)
        )

        waste_port.get_all_namespace_waste_data.assert_called_once_with(window_days=14)

    def test_prometheus_unavailable_error_propagates(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.side_effect = PrometheusUnavailableError(
            "http://prometheus:9090"
        )
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        with pytest.raises(PrometheusUnavailableError):
            service.detect_over_provisioned_namespaces(DetectOverProvisionedNamespacesCommand())

    def test_total_wasted_cores_in_report(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = [
            _raw("dev", cpu_req=8.0, cpu_actual=0.45),
        ]
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        assert round(response.report.total_wasted_cpu_cores, 2) == pytest.approx(7.55, abs=0.01)
