from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.gitops.gitops_adapter import GitOpsAdapter
from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsEngine,
    HealthStatus,
    SyncStatus,
)


def _make_crd_mock() -> MagicMock:
    return MagicMock()


def _make_vanilla_mock(crd_mock: MagicMock) -> MagicMock:
    vanilla = MagicMock()
    vanilla._crd_api_client.return_value = crd_mock
    return vanilla


def _make_app_raw(
    name: str,
    namespace: str = "argocd",
    synced: bool = True,
    healthy: bool = True,
) -> dict:
    sync_status = "Synced" if synced else "OutOfSync"
    health_status = "Healthy" if healthy else "Degraded"

    return {
        "metadata": {"name": name, "namespace": namespace},
        "spec": {
            "source": {
                "repoURL": f"https://github.com/org/{name}",
                "targetRevision": "main",
            }
        },
        "status": {
            "sync": {"status": sync_status, "revision": "abc123"},
            "health": {"status": health_status},
            "reconciledAt": "2024-01-01T00:00:00Z",
        },
    }


class TestGitOpsAdapter:
    def test_implements_gitops_port(self) -> None:
        adapter = GitOpsAdapter(MagicMock())
        assert isinstance(adapter, GitOpsPort)

    def test_detect_engine_returns_none_when_no_apps(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {"items": []}
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.detect_engine()

        assert result.engine == GitOpsEngine.NONE
        assert result.apps_count == 0  # noqa: PLR2004

    def test_detect_engine_returns_none_on_exception(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = RuntimeError("boom")
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.detect_engine()

        assert result.engine == GitOpsEngine.NONE

    def test_detect_engine_argocd_with_apps(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [_make_app_raw("app1"), _make_app_raw("app2")]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.detect_engine()

        assert result.engine == GitOpsEngine.ARGOCD
        assert result.apps_count == 2  # noqa: PLR2004

    def test_detect_engine_counts_out_of_sync(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [
                _make_app_raw("app1", synced=False),
                _make_app_raw("app2", synced=True),
            ]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.detect_engine()

        assert result.out_of_sync_count == 1  # noqa: PLR2004

    def test_detect_engine_counts_failed(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [
                _make_app_raw("app1", healthy=False),
                _make_app_raw("app2", healthy=True),
            ]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.detect_engine()

        assert result.failed_count == 1  # noqa: PLR2004

    def test_list_apps_all_namespaces(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {"items": [_make_app_raw("app1")]}
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.list_apps()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0].name == "app1"
        assert result[0].engine == GitOpsEngine.ARGOCD

    def test_list_apps_specific_namespace(self) -> None:
        crd = _make_crd_mock()
        crd.list_namespaced_custom_object.return_value = {"items": [_make_app_raw("app1")]}
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.list_apps(namespace="argocd")

        assert len(result) == 1  # noqa: PLR2004
        crd.list_namespaced_custom_object.assert_called_once()

    def test_list_apps_returns_empty_on_exception(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = RuntimeError("boom")
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.list_apps()

        assert result == []

    def test_get_app(self) -> None:
        crd = _make_crd_mock()
        crd.get_namespaced_custom_object.return_value = _make_app_raw("app1")
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.get_app(name="app1", namespace="argocd")

        assert result.name == "app1"
        assert result.namespace == "argocd"

    def test_list_sources_deduplicates_urls(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [
                _make_app_raw("app1"),
                _make_app_raw("app2"),
            ]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.list_sources()

        assert len(result) == 2  # noqa: PLR2004

    def test_list_sources_deduplicates_same_repo_url(self) -> None:
        crd = _make_crd_mock()
        raw1 = _make_app_raw("app1")
        raw2 = _make_app_raw("app2")
        raw2["spec"]["source"]["repoURL"] = "https://github.com/org/app1"
        crd.list_cluster_custom_object.return_value = {"items": [raw1, raw2]}
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.list_sources()

        assert len(result) == 1  # noqa: PLR2004

    def test_get_source_found(self) -> None:
        crd = _make_crd_mock()
        crd.list_namespaced_custom_object.return_value = {
            "items": [_make_app_raw("my-app", namespace="argocd")]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        result = adapter.get_source(name="my-app", namespace="argocd")

        assert result.name == "my-app"
        assert result.kind == "GitRepository"

    def test_get_source_not_found_raises(self) -> None:
        crd = _make_crd_mock()
        crd.list_namespaced_custom_object.return_value = {"items": []}
        vanilla = _make_vanilla_mock(crd)
        adapter = GitOpsAdapter(vanilla)

        with pytest.raises(ValueError, match="not found"):
            adapter.get_source(name="missing", namespace="argocd")


class TestParseApp:
    def test_parse_synced_healthy_app(self) -> None:
        raw = _make_app_raw("app1", synced=True, healthy=True)

        result = GitOpsAdapter._parse_app(raw)

        assert result.name == "app1"
        assert result.sync_status == SyncStatus.SYNCED
        assert result.health_status == HealthStatus.HEALTHY
        assert result.source_url == "https://github.com/org/app1"

    def test_parse_out_of_sync_degraded_app(self) -> None:
        raw = _make_app_raw("app1", synced=False, healthy=False)

        result = GitOpsAdapter._parse_app(raw)

        assert result.sync_status == SyncStatus.OUT_OF_SYNC
        assert result.health_status == HealthStatus.DEGRADED

    def test_parse_progressing_app(self) -> None:
        raw = _make_app_raw("app1")
        raw["status"] = {"health": {"status": "Progressing"}}

        result = GitOpsAdapter._parse_app(raw)

        assert result.health_status == HealthStatus.PROGRESSING

    def test_parse_suspended_app(self) -> None:
        raw = _make_app_raw("app1")
        raw["status"] = {"health": {"status": "Suspended"}}

        result = GitOpsAdapter._parse_app(raw)

        assert result.health_status == HealthStatus.SUSPENDED

    def test_parse_missing_app(self) -> None:
        raw = _make_app_raw("app1")
        raw["status"] = {"health": {"status": "Missing"}}

        result = GitOpsAdapter._parse_app(raw)

        assert result.health_status == HealthStatus.MISSING

    def test_parse_unknown_when_empty(self) -> None:
        raw = {"metadata": {"name": "app1"}, "spec": {}, "status": {}}

        result = GitOpsAdapter._parse_app(raw)

        assert result.sync_status == SyncStatus.UNKNOWN
        assert result.health_status == HealthStatus.HEALTHY

    def test_parse_app_extracts_last_synced_at(self) -> None:
        raw = _make_app_raw("app1")
        raw["status"]["reconciledAt"] = "2024-06-15T12:00:00Z"

        result = GitOpsAdapter._parse_app(raw)

        assert result.last_synced_at == "2024-06-15T12:00:00Z"

    def test_parse_app_extracts_revision(self) -> None:
        raw = _make_app_raw("app1")
        raw["status"]["sync"]["revision"] = "abc123def"

        result = GitOpsAdapter._parse_app(raw)

        assert result.last_commit == "abc123def"
        assert result.revision == "main"

    def test_parse_app_without_optional_fields(self) -> None:
        raw = {
            "metadata": {"name": "minimal"},
            "spec": {},
            "status": {},
        }

        result = GitOpsAdapter._parse_app(raw)

        assert result.name == "minimal"
        assert result.source_url is None
        assert result.revision is None
        assert result.last_synced_at is None
        assert result.namespace == "argocd"
