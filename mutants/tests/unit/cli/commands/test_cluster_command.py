from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.commands.cluster_command import cluster


class TestClusterGroup:
    def test_cluster_group_exists(self) -> None:
        runner = CliRunner()
        with patch("hexawyn.cli.commands.cluster_command.clear_l1"):
            result = runner.invoke(cluster, ["--help"])
        assert result.exit_code == 0
        assert "Manage Kubernetes cluster contexts" in result.output


class TestClusterUse:
    def test_use_switches_context(self) -> None:
        runner = CliRunner()
        with patch("hexawyn.cli.commands.cluster_command.clear_l1"):
            result = runner.invoke(cluster, ["use", "prod-eu"])

        assert result.exit_code == 0
        assert "prod-eu" in result.output
        assert "Switched" in result.output
        assert "Cache cleared" in result.output

    def test_use_calls_clear_l1(self) -> None:
        runner = CliRunner()
        mock_clear = patch("hexawyn.cli.commands.cluster_command.clear_l1").start()

        result = runner.invoke(cluster, ["use", "staging"])
        mock_clear.assert_called_once()
        assert result.exit_code == 0

        patch.stopall()

    def test_use_requires_context_name(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cluster, ["use"])
        assert result.exit_code != 0
