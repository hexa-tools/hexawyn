"""Tests for DetectOverProvisionedNamespacesService — full coverage in test_detect_over_provisioned_namespaces_use_case.py."""

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_service_port import (
    DetectOverProvisionedNamespacesServicePort,
)
from hexawyn.application.service.detect_over_provisioned_namespaces_service import (
    DetectOverProvisionedNamespacesService,
)


class TestDetectOverProvisionedNamespacesService:
    def test_implements_service_port(self) -> None:
        service = DetectOverProvisionedNamespacesService(
            waste_port=MagicMock(spec=NamespaceWasteAnalysisPort)
        )
        assert isinstance(service, DetectOverProvisionedNamespacesServicePort)

    def test_returns_response_with_report(self) -> None:
        waste_port = MagicMock(spec=NamespaceWasteAnalysisPort)
        waste_port.get_all_namespace_waste_data.return_value = []
        service = DetectOverProvisionedNamespacesService(waste_port=waste_port)

        response = service.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        assert response.report is not None
        assert response.report.analysis_window_days == 7
