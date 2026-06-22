from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.main import app


class TestClusterSwitchClearsCache:
    def test_cluster_switch_clears_l1_cache(self):
        with patch("hexawyn.cli.commands.cluster_command.clear_l1") as mock_clear:
            runner = CliRunner()
            runner.invoke(app, ["cluster", "use", "prod-us"])
            mock_clear.assert_called_once()
