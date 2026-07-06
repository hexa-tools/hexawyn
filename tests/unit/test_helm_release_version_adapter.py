"""RED → GREEN — HelmReleaseVersionAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.helm_release_version_adapter import (
    HelmReleaseVersionAdapter,
)
from hexawyn.application.ports.driven.helm_release_version_port import (
    HelmReleaseVersionPort,
)


class TestHelmReleaseVersionAdapter:
    def test_implements_port(self) -> None:
        adapter = HelmReleaseVersionAdapter()
        assert isinstance(adapter, HelmReleaseVersionPort)

    def test_list_releases_returns_empty_list(self) -> None:
        adapter = HelmReleaseVersionAdapter()
        result = adapter.list_releases(None)
        assert result == []

    def test_list_releases_with_namespace_returns_empty(self) -> None:
        adapter = HelmReleaseVersionAdapter()
        result = adapter.list_releases("production")
        assert result == []

    def test_fetch_latest_version_returns_chart_name(self) -> None:
        adapter = HelmReleaseVersionAdapter()
        result = adapter.fetch_latest_version("nginx-ingress")

        assert result["chart_name"] == "nginx-ingress"
        assert result["latest_version"] == ""
        assert result["repo_error"] == ""
