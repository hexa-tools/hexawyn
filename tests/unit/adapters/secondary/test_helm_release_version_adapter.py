from __future__ import annotations

from unittest.mock import MagicMock, patch

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

    def test_list_releases_with_data(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(
                returncode=0,
                stdout='[{"name":"nginx","namespace":"default","chart":"nginx-1.0","app_version":"1.25","status":"deployed","revision":1}]',
            )
            adapter = HelmReleaseVersionAdapter()
            result = adapter.list_releases(None)

            assert len(result) == 1
            assert result[0]["name"] == "nginx"
            assert result[0]["status"] == "deployed"

    def test_list_releases_empty_on_subprocess_error(self) -> None:
        with patch("subprocess.run", side_effect=Exception("helm not found")):
            adapter = HelmReleaseVersionAdapter()
            result = adapter.list_releases(None)
            assert result == []

    def test_list_releases_empty_on_non_zero_exit(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=1, stdout="")
            adapter = HelmReleaseVersionAdapter()
            result = adapter.list_releases("default")
            assert result == []

    def test_fetch_latest_version_with_data(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(
                returncode=0, stdout='[{"name":"nginx-ingress","version":"4.9.0"}]'
            )
            adapter = HelmReleaseVersionAdapter()
            result = adapter.fetch_latest_version("nginx-ingress")

            assert result["chart_name"] == "nginx-ingress"
            assert result["latest_version"] == "4.9.0"

    def test_fetch_latest_version_empty_on_error(self) -> None:
        with patch("subprocess.run", side_effect=Exception("helm not found")):
            adapter = HelmReleaseVersionAdapter()
            result = adapter.fetch_latest_version("nginx-ingress")

            assert result["chart_name"] == "nginx-ingress"
            assert result["latest_version"] == ""

    def test_fetch_latest_version_empty_on_no_results(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="[]")
            adapter = HelmReleaseVersionAdapter()
            result = adapter.fetch_latest_version("unknown-chart")

            assert result["chart_name"] == "unknown-chart"
            assert result["latest_version"] == ""
