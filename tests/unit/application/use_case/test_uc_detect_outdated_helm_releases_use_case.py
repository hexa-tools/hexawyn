"""Unit tests for DetectOutdatedHelmReleasesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_outdated_helm_releases.detect_outdated_helm_releases_service_port import (
    DetectOutdatedHelmReleasesServicePort,
)
from hexawyn.application.use_case.detect_outdated_helm_releases.detect_outdated_helm_releases_use_case import (
    DetectOutdatedHelmReleasesUseCase,
)


class TestDetectOutdatedHelmReleasesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectOutdatedHelmReleasesServicePort)
        use_case = DetectOutdatedHelmReleasesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_outdated.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectOutdatedHelmReleasesServicePort)
        mock_service.detect_outdated.side_effect = RuntimeError("test error")
        use_case = DetectOutdatedHelmReleasesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
