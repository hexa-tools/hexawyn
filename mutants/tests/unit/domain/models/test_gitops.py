from __future__ import annotations

import pytest
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsEngine,
    GitOpsSource,
    HealthStatus,
    SyncStatus,
)


class TestGitOpsEngine:
    def test_three_values(self) -> None:
        assert GitOpsEngine.FLUX.value == "flux"
        assert GitOpsEngine.ARGOCD.value == "argocd"
        assert GitOpsEngine.NONE.value == "none"

    def test_is_str_enum(self) -> None:
        assert isinstance(GitOpsEngine.FLUX, GitOpsEngine)


class TestSyncStatus:
    def test_four_values(self) -> None:
        assert SyncStatus.SYNCED.value == "synced"
        assert SyncStatus.OUT_OF_SYNC.value == "out_of_sync"
        assert SyncStatus.UNKNOWN.value == "unknown"
        assert SyncStatus.FAILED.value == "failed"


class TestHealthStatus:
    def test_five_values(self) -> None:
        assert HealthStatus.HEALTHY.value == "healthy"
        assert HealthStatus.DEGRADED.value == "degraded"
        assert HealthStatus.PROGRESSING.value == "progressing"
        assert HealthStatus.SUSPENDED.value == "suspended"
        assert HealthStatus.MISSING.value == "missing"


class TestGitOpsApp:
    def test_is_frozen(self) -> None:
        app = GitOpsApp(
            name="payments-api",
            namespace="flux-system",
            engine=GitOpsEngine.FLUX,
            kind="HelmRelease",
            sync_status=SyncStatus.SYNCED,
            health_status=HealthStatus.HEALTHY,
        )
        with pytest.raises(AttributeError):
            app.name = "changed"  # type: ignore[misc]

    def test_required_and_optional_fields(self) -> None:
        app = GitOpsApp(
            name="payments-api",
            namespace="flux-system",
            engine=GitOpsEngine.FLUX,
            kind="HelmRelease",
            sync_status=SyncStatus.OUT_OF_SYNC,
            health_status=HealthStatus.DEGRADED,
            last_synced_at="2026-06-30T10:00:00Z",
            last_commit="abc1234",
            source_url="https://github.com/org/repo",
            revision="main@sha256:abc",
            message="HelmRelease reconciliation failed: values mismatch",
        )
        assert app.name == "payments-api"
        assert app.sync_status == SyncStatus.OUT_OF_SYNC
        assert app.message == "HelmRelease reconciliation failed: values mismatch"
        assert app.source_url == "https://github.com/org/repo"

    def test_optional_fields_default_to_none(self) -> None:
        app = GitOpsApp(
            name="app",
            namespace="ns",
            engine=GitOpsEngine.NONE,
            kind="Application",
            sync_status=SyncStatus.UNKNOWN,
            health_status=HealthStatus.MISSING,
        )
        assert app.last_synced_at is None
        assert app.last_commit is None


class TestGitOpsSource:
    def test_is_frozen(self) -> None:
        source = GitOpsSource(
            name="prod-repo",
            namespace="flux-system",
            kind="GitRepository",
            url="https://github.com/org/prod-manifests",
            ready=True,
        )
        with pytest.raises(AttributeError):
            source.name = "changed"  # type: ignore[misc]

    def test_optional_fields(self) -> None:
        source = GitOpsSource(
            name="prod-repo",
            namespace="flux-system",
            kind="GitRepository",
            url="https://github.com/org/repo",
            ready=False,
            last_updated_at="2026-06-30T09:00:00Z",
            message="authentication failed",
        )
        assert source.ready is False
        assert source.message == "authentication failed"


class TestGitOpsDetectionResult:
    def test_flux_detected(self) -> None:
        result = GitOpsDetectionResult(
            engine=GitOpsEngine.FLUX,
            version="v2.4.0",
            namespace="flux-system",
            apps_count=12,
            out_of_sync_count=2,
            failed_count=1,
        )
        assert result.engine == GitOpsEngine.FLUX
        assert result.version == "v2.4.0"
        assert result.apps_count == 12  # noqa: PLR2004
        assert result.out_of_sync_count == 2  # noqa: PLR2004
        assert result.failed_count == 1

    def test_none_detected(self) -> None:
        result = GitOpsDetectionResult(
            engine=GitOpsEngine.NONE,
            version=None,
            namespace=None,
            apps_count=0,
            out_of_sync_count=0,
            failed_count=0,
        )
        assert result.engine == GitOpsEngine.NONE
        assert result.version is None


class TestGitOpsEngineNotFoundError:
    def test_inherits_from_hexawyn_error(self) -> None:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError, HexawynError

        error = GitOpsEngineNotFoundError()
        assert isinstance(error, HexawynError)

    def test_message_includes_install_hint(self) -> None:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        error = GitOpsEngineNotFoundError()
        message = str(error)
        assert "GitOps" in message
        assert "fluxcd.io" in message or "argo-cd" in message
