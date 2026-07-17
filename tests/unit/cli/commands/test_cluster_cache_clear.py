from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.main import app


class TestClusterSwitchClearsCache:
    def test_cluster_switch_clears_l1_cache(self):
        with patch("hexawyn.cli.commands.cluster_command.clear_l1") as mock_clear:
            runner = CliRunner()
            runner.invoke(app, ["cluster", "use", "prod-us"])
            mock_clear.assert_called_once()

    def test_cluster_use_without_name_shows_error(self) -> None:
        runner = CliRunner()
        result = runner.invoke(app, ["cluster", "use"])
        assert result.exit_code != 0

    def test_cluster_use_clears_cache(self) -> None:
        with patch("hexawyn.cli.commands.cluster_command.clear_l1") as mock_clear:
            runner = CliRunner()
            result = runner.invoke(app, ["cluster", "use", "staging"])
            assert result.exit_code == 0
            mock_clear.assert_called_once()
