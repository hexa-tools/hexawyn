from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.gitops.gitops_detector import GitOpsDetector
from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsEngine,
    GitOpsSource,
    HealthStatus,
    SyncStatus,
)


class TestGitOpsDetector:
    def test_implements_gitops_port(self) -> None:
        detector = GitOpsDetector()
        assert isinstance(detector, GitOpsPort)

    def test_detect_engine_returns_none_when_no_crds(self) -> None:
        detector = GitOpsDetector()
        result = detector.detect_engine()
        assert result.engine == GitOpsEngine.NONE
        assert result.apps_count == 0

    def test_detect_engine_with_flux_delegate(self) -> None:
        mock_flux = MagicMock(spec=GitOpsPort)
        mock_flux.detect_engine.return_value = GitOpsDetectionResult(
            engine=GitOpsEngine.FLUX,
            version="v2.4.0",
            namespace="flux-system",
            apps_count=12,
            out_of_sync_count=2,
            failed_count=1,
        )
        detector = GitOpsDetector()
        detector._delegate = mock_flux
        result = detector.detect_engine()
        assert result.engine == GitOpsEngine.FLUX
        assert result.apps_count == 12

    def test_list_apps_delegates(self) -> None:
        mock_flux = MagicMock(spec=GitOpsPort)
        mock_flux.list_apps.return_value = [
            GitOpsApp(
                name="app",
                namespace="ns",
                engine=GitOpsEngine.FLUX,
                kind="HelmRelease",
                sync_status=SyncStatus.SYNCED,
                health_status=HealthStatus.HEALTHY,
            ),
        ]
        detector = GitOpsDetector()
        detector._delegate = mock_flux
        result = detector.list_apps(namespace="flux-system")
        assert len(result) == 1
        mock_flux.list_apps.assert_called_once_with(namespace="flux-system")

    def test_get_app_delegates(self) -> None:
        mock = MagicMock(spec=GitOpsPort)
        mock.get_app.return_value = GitOpsApp(
            name="payments",
            namespace="flux-system",
            engine=GitOpsEngine.FLUX,
            kind="HelmRelease",
            sync_status=SyncStatus.OUT_OF_SYNC,
            health_status=HealthStatus.DEGRADED,
        )
        detector = GitOpsDetector()
        detector._delegate = mock
        result = detector.get_app(name="payments", namespace="flux-system")
        assert result.name == "payments"
        mock.get_app.assert_called_once_with(name="payments", namespace="flux-system")

    def test_list_sources_delegates(self) -> None:
        mock = MagicMock(spec=GitOpsPort)
        mock.list_sources.return_value = [
            GitOpsSource(
                name="repo",
                namespace="ns",
                kind="GitRepository",
                url="https://github.com/org/repo",
                ready=True,
            ),
        ]
        detector = GitOpsDetector()
        detector._delegate = mock
        result = detector.list_sources(namespace="flux-system")
        assert len(result) == 1
        mock.list_sources.assert_called_once_with(namespace="flux-system")

    def test_get_source_delegates(self) -> None:
        mock = MagicMock(spec=GitOpsPort)
        mock.get_source.return_value = GitOpsSource(
            name="repo",
            namespace="ns",
            kind="GitRepository",
            url="https://github.com/org/repo",
            ready=True,
        )
        detector = GitOpsDetector()
        detector._delegate = mock
        result = detector.get_source(name="repo", namespace="flux-system")
        assert result.name == "repo"
        mock.get_source.assert_called_once_with(name="repo", namespace="flux-system")

    def test_ensure_detected_raises_when_no_delegate(self) -> None:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        detector = GitOpsDetector()
        with pytest.raises(GitOpsEngineNotFoundError):
            detector._ensure_detected()
