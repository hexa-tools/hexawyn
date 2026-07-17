"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.helm_release_version_port import (
    ChartLatestRawData,
    HelmReleaseRawData,
    HelmReleaseVersionPort,
)
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_response import (
    DetectOutdatedHelmReleasesResponse,
)
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_service_port import (
    DetectOutdatedHelmReleasesServicePort,
)
from hexawyn.application.service.detect_outdated_helm_releases_service import (
    DetectOutdatedHelmReleasesService,
)
from hexawyn.application.use_case.detect_outdated_helm_releases.detect_outdated_helm_releases_use_case import (
    DetectOutdatedHelmReleasesUseCase,
)
from hexawyn.domain.models.outdated_helm import OutdatedHelmReport


class TestHelmReleaseVersionPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(HelmReleaseVersionPort)

    def test_concrete_impl_must_implement_methods(self) -> None:
        class Bad(HelmReleaseVersionPort):
            pass

        with pytest.raises(TypeError):
            Bad()  # type: ignore[abstract]


class TestDetectOutdatedHelmReleasesCommand:
    def test_default_namespace_is_none(self) -> None:
        cmd = DetectOutdatedHelmReleasesCommand()
        assert cmd.namespace is None

    def test_custom_namespace(self) -> None:
        cmd = DetectOutdatedHelmReleasesCommand(namespace="production")
        assert cmd.namespace == "production"

    def test_is_frozen(self) -> None:
        cmd = DetectOutdatedHelmReleasesCommand()
        with pytest.raises(Exception):
            cmd.namespace = "staging"  # type: ignore[misc]


class TestDetectOutdatedHelmReleasesResponse:
    def test_holds_result(self) -> None:
        inner = OutdatedHelmReport(total_releases=5, outdated_count=3)
        resp = DetectOutdatedHelmReleasesResponse(result=inner)
        assert resp.result is inner


class TestDetectOutdatedHelmReleasesService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=HelmReleaseVersionPort)
        port.list_releases.return_value = []
        port.fetch_latest_version.return_value = ChartLatestRawData(
            chart_name="",
            latest_version="",
            breaking_changes="",
            repo_error="",
        )
        return port

    def test_calls_list_releases(self) -> None:
        port = self._mock_port()
        service = DetectOutdatedHelmReleasesService(helm_port=port)

        service.detect_outdated(DetectOutdatedHelmReleasesCommand(namespace="production"))

        port.list_releases.assert_called_once_with("production")

    def test_detects_minor_outdated_release(self) -> None:
        port = MagicMock(spec=HelmReleaseVersionPort)
        port.list_releases.return_value = [
            HelmReleaseRawData(
                release_name="nginx-ingress",
                namespace="default",
                chart_name="nginx-ingress",
                chart_version="4.7.1",
                is_pinned=False,
            ),
        ]
        port.fetch_latest_version.return_value = ChartLatestRawData(
            chart_name="nginx-ingress",
            latest_version="4.10.3",
            breaking_changes="",
            repo_error="",
        )
        service = DetectOutdatedHelmReleasesService(helm_port=port)

        response = service.detect_outdated(DetectOutdatedHelmReleasesCommand())

        assert response.result.outdated_count == 1
        assert response.result.releases[0].delta_type == "minor"
        assert response.result.releases[0].current_version == "4.7.1"

    def test_returns_response_with_result(self) -> None:
        port = self._mock_port()
        service = DetectOutdatedHelmReleasesService(helm_port=port)

        response = service.detect_outdated(DetectOutdatedHelmReleasesCommand())

        assert isinstance(response, DetectOutdatedHelmReleasesResponse)
        assert isinstance(response.result, OutdatedHelmReport)

    def test_fetches_latest_once_per_chart(self) -> None:
        port = MagicMock(spec=HelmReleaseVersionPort)
        port.list_releases.return_value = [
            HelmReleaseRawData(
                release_name="nginx-prod",
                namespace="production",
                chart_name="nginx-ingress",
                chart_version="4.7.1",
                is_pinned=False,
            ),
            HelmReleaseRawData(
                release_name="nginx-staging",
                namespace="staging",
                chart_name="nginx-ingress",
                chart_version="4.7.1",
                is_pinned=False,
            ),
        ]
        port.fetch_latest_version.return_value = ChartLatestRawData(
            chart_name="nginx-ingress",
            latest_version="4.10.3",
            breaking_changes="",
            repo_error="",
        )
        service = DetectOutdatedHelmReleasesService(helm_port=port)

        service.detect_outdated(DetectOutdatedHelmReleasesCommand())

        assert port.fetch_latest_version.call_count == 1


class TestDetectOutdatedHelmReleasesUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectOutdatedHelmReleasesServicePort)
        inner = OutdatedHelmReport(total_releases=5)
        service.detect_outdated.return_value = DetectOutdatedHelmReleasesResponse(result=inner)
        use_case = DetectOutdatedHelmReleasesUseCase(service=service)

        result = use_case.execute(DetectOutdatedHelmReleasesCommand())

        service.detect_outdated.assert_called_once()
        assert result.result is inner
