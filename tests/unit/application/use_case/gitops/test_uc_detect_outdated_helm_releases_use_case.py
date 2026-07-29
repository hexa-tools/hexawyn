from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.detect_outdated_helm_releases_use_case import (  # noqa: E501
    DetectOutdatedHelmReleasesUseCase,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.response import (  # noqa: E501
    DetectOutdatedHelmReleasesResponse,
)


class TestDetectOutdatedHelmReleasesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_releases.return_value = []
        port.fetch_latest_version.return_value = {}

        use_case = DetectOutdatedHelmReleasesUseCase(helm_port=port)
        use_case._engine.compute = MagicMock(
            return_value={
                "outdated_count": 0,
                "total_releases": 0,
            }
        )

        result = use_case.detect_outdated(DetectOutdatedHelmReleasesCommand(namespace="default"))

        assert isinstance(result, DetectOutdatedHelmReleasesResponse)

    def test_execute_all_up_to_date(self) -> None:
        port = MagicMock()
        port.list_releases.return_value = []
        port.fetch_latest_version.return_value = {}

        use_case = DetectOutdatedHelmReleasesUseCase(helm_port=port)
        use_case._engine.compute = MagicMock(
            return_value={
                "outdated_count": 0,
            }
        )

        result = use_case.detect_outdated(DetectOutdatedHelmReleasesCommand(namespace="default"))

        assert result.result["outdated_count"] == 0

    def test_execute_fetches_latest_version_for_charts(self) -> None:
        port = MagicMock()
        port.list_releases.return_value = [
            {"chart_name": "nginx", "name": "my-nginx", "namespace": "default", "version": "1.0.0"},
            {
                "chart_name": "nginx",
                "name": "my-nginx-2",
                "namespace": "default",
                "version": "1.0.0",
            },
        ]
        port.fetch_latest_version.return_value = {"version": "2.0.0"}

        use_case = DetectOutdatedHelmReleasesUseCase(helm_port=port)
        use_case._engine.compute = MagicMock(
            return_value={"outdated_count": 0, "total_releases": 0}
        )

        result = use_case.detect_outdated(DetectOutdatedHelmReleasesCommand())

        port.fetch_latest_version.assert_called_once_with("nginx")
        assert isinstance(result, DetectOutdatedHelmReleasesResponse)

    def test_execute_skips_empty_chart_name(self) -> None:
        port = MagicMock()
        port.list_releases.return_value = [
            {"chart_name": "", "name": "unknown", "namespace": "default", "version": "1.0.0"},
        ]
        port.fetch_latest_version.return_value = {}

        use_case = DetectOutdatedHelmReleasesUseCase(helm_port=port)
        use_case._engine.compute = MagicMock(
            return_value={"outdated_count": 0, "total_releases": 0}
        )

        result = use_case.detect_outdated(DetectOutdatedHelmReleasesCommand())

        port.fetch_latest_version.assert_not_called()
        assert isinstance(result, DetectOutdatedHelmReleasesResponse)
