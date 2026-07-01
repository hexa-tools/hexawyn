from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsEngine,
    GitOpsSource,
    HealthStatus,
    SyncStatus,
)


class TestGitOpsAppsList:
    def test_service_implements_port(self) -> None:
        from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_service_port import (
            GitOpsAppsListServicePort,
        )
        from hexawyn.application.service.gitops_apps_list_service import (
            GitOpsAppsListService,
        )

        svc = GitOpsAppsListService(gitops_port=MagicMock(spec=GitOpsPort))
        assert isinstance(svc, GitOpsAppsListServicePort)

    def test_service_delegates_to_port(self) -> None:
        from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_command import (
            GitOpsAppsListCommand,
        )
        from hexawyn.application.service.gitops_apps_list_service import (
            GitOpsAppsListService,
        )

        gitops = MagicMock(spec=GitOpsPort)
        gitops.list_apps.return_value = [
            GitOpsApp(
                name="payments",
                namespace="flux-system",
                engine=GitOpsEngine.FLUX,
                kind="HelmRelease",
                sync_status=SyncStatus.SYNCED,
                health_status=HealthStatus.HEALTHY,
            ),
        ]
        svc = GitOpsAppsListService(gitops_port=gitops)
        result = svc.list_apps(GitOpsAppsListCommand(namespace="flux-system"))
        assert len(result.apps) == 1
        assert result.error is None

    def test_tool_returns_apps(self) -> None:
        from hexawyn.mcp.tools.gitops_apps_list import gitops_apps_list

        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            adapter = MagicMock(spec=GitOpsPort)
            adapter.list_apps.return_value = [
                GitOpsApp(
                    name="app1",
                    namespace="ns",
                    engine=GitOpsEngine.ARGOCD,
                    kind="Application",
                    sync_status=SyncStatus.OUT_OF_SYNC,
                    health_status=HealthStatus.DEGRADED,
                    message="out of sync with Git",
                ),
            ]
            mock_build.return_value = adapter
            result = gitops_apps_list(namespace="argocd")

        assert result["error"] is None
        assert len(result["apps"]) == 1


class TestGitOpsAppGet:
    def test_service_delegates_to_port(self) -> None:
        from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_command import (
            GitOpsAppGetCommand,
        )
        from hexawyn.application.service.gitops_app_get_service import GitOpsAppGetService

        gitops = MagicMock(spec=GitOpsPort)
        gitops.get_app.return_value = GitOpsApp(
            name="payments",
            namespace="flux-system",
            engine=GitOpsEngine.FLUX,
            kind="HelmRelease",
            sync_status=SyncStatus.OUT_OF_SYNC,
            health_status=HealthStatus.DEGRADED,
            message="HelmRelease reconciliation failed: values mismatch",
            last_synced_at="2026-06-30T10:00:00Z",
            last_commit="abc1234",
            source_url="https://github.com/org/repo",
            revision="main@sha256:abc",
        )
        svc = GitOpsAppGetService(gitops_port=gitops)
        result = svc.get_app(GitOpsAppGetCommand(name="payments", namespace="flux-system"))
        assert result.name == "payments"
        assert result.sync_status == "out_of_sync"
        assert result.error is None

    def test_tool_returns_app_detail(self) -> None:
        from hexawyn.mcp.tools.gitops_app_get import gitops_app_get

        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            adapter = MagicMock(spec=GitOpsPort)
            adapter.get_app.return_value = GitOpsApp(
                name="payments",
                namespace="ns",
                engine=GitOpsEngine.FLUX,
                kind="HelmRelease",
                sync_status=SyncStatus.SYNCED,
                health_status=HealthStatus.HEALTHY,
            )
            mock_build.return_value = adapter
            result = gitops_app_get(name="payments", namespace="flux-system")

        assert result["error"] is None
        assert result["name"] == "payments"


class TestGitOpsAppStatus:
    def test_tool_returns_status(self) -> None:
        from hexawyn.mcp.tools.gitops_app_status import gitops_app_status

        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            adapter = MagicMock(spec=GitOpsPort)
            adapter.get_app.return_value = GitOpsApp(
                name="app",
                namespace="ns",
                engine=GitOpsEngine.FLUX,
                kind="Kustomization",
                sync_status=SyncStatus.SYNCED,
                health_status=HealthStatus.HEALTHY,
                last_synced_at="2026-06-30T09:00:00Z",
                last_commit="def5678",
            )
            mock_build.return_value = adapter
            result = gitops_app_status(name="app", namespace="flux-system")

        assert result["error"] is None
        assert result["sync_status"] == "synced"
        assert result["last_synced_at"] == "2026-06-30T09:00:00Z"


class TestGitOpsAppSync:
    def test_tool_returns_sync_status_read_only(self) -> None:
        from hexawyn.mcp.tools.gitops_app_sync import gitops_app_sync

        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            adapter = MagicMock(spec=GitOpsPort)
            adapter.get_app.return_value = GitOpsApp(
                name="app",
                namespace="ns",
                engine=GitOpsEngine.FLUX,
                kind="HelmRelease",
                sync_status=SyncStatus.SYNCED,
                health_status=HealthStatus.HEALTHY,
                last_synced_at="2026-06-30T08:00:00Z",
                revision="main@sha:xyz",
            )
            mock_build.return_value = adapter
            result = gitops_app_sync(name="app", namespace="flux-system")

        assert result["error"] is None
        assert result["sync_status"] == "synced"
        assert result["revision"] == "main@sha:xyz"


class TestGitOpsSourcesList:
    def test_service_delegates_to_port(self) -> None:
        from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_command import (
            GitOpsSourcesListCommand,
        )
        from hexawyn.application.service.gitops_sources_list_service import (
            GitOpsSourcesListService,
        )

        gitops = MagicMock(spec=GitOpsPort)
        gitops.list_sources.return_value = [
            GitOpsSource(
                name="prod-repo",
                namespace="flux-system",
                kind="GitRepository",
                url="https://github.com/org/repo",
                ready=True,
                last_updated_at="2026-06-30T09:00:00Z",
            ),
        ]
        svc = GitOpsSourcesListService(gitops_port=gitops)
        result = svc.list_sources(GitOpsSourcesListCommand(namespace="flux-system"))
        assert len(result.sources) == 1
        assert result.error is None

    def test_tool_returns_sources(self) -> None:
        from hexawyn.mcp.tools.gitops_sources_list import gitops_sources_list

        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            adapter = MagicMock(spec=GitOpsPort)
            adapter.list_sources.return_value = [
                GitOpsSource(
                    name="prod-repo",
                    namespace="ns",
                    kind="GitRepository",
                    url="https://github.com/org/repo",
                    ready=False,
                    message="auth failed",
                ),
            ]
            mock_build.return_value = adapter
            result = gitops_sources_list(namespace="flux-system")

        assert result["error"] is None
        assert len(result["sources"]) == 1
        assert result["sources"][0]["ready"] is False


class TestGitOpsSourceGet:
    def test_tool_returns_source_detail(self) -> None:
        from hexawyn.mcp.tools.gitops_source_get import gitops_source_get

        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            adapter = MagicMock(spec=GitOpsPort)
            adapter.get_source.return_value = GitOpsSource(
                name="prod-repo",
                namespace="ns",
                kind="GitRepository",
                url="https://github.com/org/repo",
                ready=True,
                last_updated_at="2026-06-30T09:00:00Z",
            )
            mock_build.return_value = adapter
            result = gitops_source_get(name="prod-repo", namespace="flux-system")

        assert result["error"] is None
        assert result["name"] == "prod-repo"


class TestBuildGitOpsAdapter:
    def test_returns_gitops_port(self) -> None:
        from hexawyn.application.ports.driven.gitops_port import GitOpsPort
        from hexawyn.mcp.server import build_gitops_adapter

        adapter = build_gitops_adapter()
        assert isinstance(adapter, GitOpsPort)


class TestGitOpsToolsErrorHandling:
    def test_apps_list_handles_adapter_error(self) -> None:
        from hexawyn.mcp.tools.gitops_apps_list import gitops_apps_list

        with patch("hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("boom")):
            result = gitops_apps_list()
        assert result["error"] == "boom"

    def test_app_get_handles_adapter_error(self) -> None:
        from hexawyn.mcp.tools.gitops_app_get import gitops_app_get

        with patch("hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("boom")):
            result = gitops_app_get(name="x", namespace="ns")
        assert result["error"] == "boom"

    def test_app_status_handles_adapter_error(self) -> None:
        from hexawyn.mcp.tools.gitops_app_status import gitops_app_status

        with patch("hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("boom")):
            result = gitops_app_status(name="x", namespace="ns")
        assert result["error"] == "boom"

    def test_app_sync_handles_adapter_error(self) -> None:
        from hexawyn.mcp.tools.gitops_app_sync import gitops_app_sync

        with patch("hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("boom")):
            result = gitops_app_sync(name="x", namespace="ns")
        assert result["error"] == "boom"

    def test_sources_list_handles_adapter_error(self) -> None:
        from hexawyn.mcp.tools.gitops_sources_list import gitops_sources_list

        with patch("hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("boom")):
            result = gitops_sources_list()
        assert result["error"] == "boom"

    def test_source_get_handles_adapter_error(self) -> None:
        from hexawyn.mcp.tools.gitops_source_get import gitops_source_get

        with patch("hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("boom")):
            result = gitops_source_get(name="x", namespace="ns")
        assert result["error"] == "boom"


class TestRegisterFunctions:
    def test_all_gitops_tools_have_register(self) -> None:
        import importlib

        tools = [
            "gitops_detect",
            "gitops_apps_list",
            "gitops_app_get",
            "gitops_app_status",
            "gitops_app_sync",
            "gitops_sources_list",
            "gitops_source_get",
        ]
        from fastmcp import FastMCP

        test_mcp = FastMCP("test-gitops")
        for tool_name in tools:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{tool_name}")
            register_fn = getattr(mod, "register", None)
            assert callable(register_fn)
            register_fn(test_mcp)
