"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.probe_audit_port import (
    ProbeAuditPort,
    ProbeContainerRawData,
    ProbeDeploymentRawData,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_response import (
    DetectMissingProbesResponse,
)
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_service_port import (
    DetectMissingProbesServicePort,
)
from hexawyn.application.service.detect_missing_probes_service import (
    DetectMissingProbesService,
)
from hexawyn.application.use_case.detect_missing_probes.detect_missing_probes_use_case import (
    DetectMissingProbesUseCase,
)
from hexawyn.domain.models.probe_audit import ProbeAuditResult


class TestProbeAuditPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(ProbeAuditPort)

    def test_concrete_impl_must_implement_get_probe_audit_data(self) -> None:
        class BadAdapter(ProbeAuditPort):
            pass

        with pytest.raises(TypeError):
            BadAdapter()  # type: ignore[abstract]

    def test_concrete_impl_accepted(self) -> None:
        class GoodAdapter(ProbeAuditPort):
            def get_probe_audit_data(
                self, namespace: str | None = None
            ) -> list[ProbeDeploymentRawData]:
                return []

        adapter = GoodAdapter()
        assert adapter.get_probe_audit_data() == []


class TestDetectMissingProbesCommand:
    def test_default_namespace_is_none(self) -> None:
        cmd = DetectMissingProbesCommand()
        assert cmd.namespace is None

    def test_custom_namespace(self) -> None:
        cmd = DetectMissingProbesCommand(namespace="production")
        assert cmd.namespace == "production"

    def test_is_frozen(self) -> None:
        cmd = DetectMissingProbesCommand()
        with pytest.raises(Exception):
            cmd.namespace = "staging"  # type: ignore[misc]


class TestDetectMissingProbesResponse:
    def test_holds_result(self) -> None:
        result = ProbeAuditResult(
            total_without_probes=0,
            critical=0,
            warning=0,
            informational=0,
        )
        response = DetectMissingProbesResponse(result=result)
        assert response.result is result


class TestDetectMissingProbesService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=ProbeAuditPort)
        port.get_probe_audit_data.return_value = []
        return port

    def test_calls_port_with_no_namespace(self) -> None:
        port = self._mock_port()
        service = DetectMissingProbesService(probe_audit_port=port)

        service.detect_missing_probes(DetectMissingProbesCommand())

        port.get_probe_audit_data.assert_called_once_with(None)

    def test_calls_port_with_namespace_filter(self) -> None:
        port = self._mock_port()
        service = DetectMissingProbesService(probe_audit_port=port)

        service.detect_missing_probes(DetectMissingProbesCommand(namespace="production"))

        port.get_probe_audit_data.assert_called_once_with("production")

    def test_returns_detect_missing_probes_response(self) -> None:
        port = self._mock_port()
        service = DetectMissingProbesService(probe_audit_port=port)

        result = service.detect_missing_probes(DetectMissingProbesCommand())

        assert isinstance(result, DetectMissingProbesResponse)
        assert isinstance(result.result, ProbeAuditResult)

    def test_detects_missing_both_probes_as_critical(self) -> None:
        port = MagicMock(spec=ProbeAuditPort)
        port.get_probe_audit_data.return_value = [
            ProbeDeploymentRawData(
                deployment_name="payment-service",
                namespace="production",
                workload_type="Deployment",
                containers=[
                    ProbeContainerRawData(
                        container_name="main",
                        is_init_container=False,
                        exposed_ports=[8080],
                        has_liveness_probe=False,
                        has_readiness_probe=False,
                        liveness_probe_type="",
                        readiness_probe_type="",
                        liveness_http_path="",
                        readiness_http_path="",
                        liveness_port=0,
                        readiness_port=0,
                    ),
                ],
                has_service=True,
                is_exposed_externally=True,
            ),
        ]
        service = DetectMissingProbesService(probe_audit_port=port)

        result = service.detect_missing_probes(DetectMissingProbesCommand())

        assert result.result.total_without_probes == 1
        assert result.result.critical == 1
        assert result.result.missing_probes[0].deployment_name == "payment-service"


class TestDetectMissingProbesUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectMissingProbesServicePort)
        inner = ProbeAuditResult()
        service.detect_missing_probes.return_value = DetectMissingProbesResponse(result=inner)
        use_case = DetectMissingProbesUseCase(service=service)

        result = use_case.execute(DetectMissingProbesCommand())

        service.detect_missing_probes.assert_called_once()
        assert result.result is inner

    def test_passes_command_through(self) -> None:
        service = MagicMock(spec=DetectMissingProbesServicePort)
        service.detect_missing_probes.return_value = DetectMissingProbesResponse(
            result=ProbeAuditResult(),
        )
        use_case = DetectMissingProbesUseCase(service=service)
        cmd = DetectMissingProbesCommand(namespace="staging")

        use_case.execute(cmd)

        service.detect_missing_probes.assert_called_once_with(cmd)
