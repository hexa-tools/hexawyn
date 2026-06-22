from unittest.mock import patch

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


class TestCLIHelp:
    def test_help_shows_commands(self, runner):
        from hexawyn.cli.main import app

        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "start" in result.output
        assert "setup" in result.output
        assert "hexawyn" in result.output.lower()


class TestStartCommand:
    def test_start_without_api_key_shows_warning(self, runner):
        with patch("hexawyn.cli.main.get_api_key", return_value=None):
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["start"])
            assert "No Anthropic API key found" in result.output

    def test_start_with_demo_flag_sets_env_vars(self, runner):
        with (
            patch("hexawyn.cli.main.get_api_key", return_value="sk-ant-xxx"),
            patch("hexawyn.cli.app.HexawynApp", create=True) as mock_app,
        ):
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["start", "--demo", "--scenario", "gcp_gke"])
            assert result.exit_code == 0
            mock_app.assert_called_once_with(expert_mode=False)
            mock_app.return_value.run.assert_called_once()

    def test_start_with_expert_flag(self, runner):
        with (
            patch("hexawyn.cli.main.get_api_key", return_value="sk-ant-xxx"),
            patch("hexawyn.cli.app.HexawynApp", create=True) as mock_app,
        ):
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["start", "--expert"])
            assert result.exit_code == 0
            mock_app.assert_called_once_with(expert_mode=True)

    def test_start_accepts_all_scenarios(self, runner):
        scenarios = ["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]
        for scenario in scenarios:
            with (
                patch("hexawyn.cli.main.get_api_key", return_value="sk-ant-xxx"),
                patch("hexawyn.cli.app.HexawynApp", create=True),
            ):
                from hexawyn.cli.main import app

                result = runner.invoke(app, ["start", "--demo", "--scenario", scenario])
                assert result.exit_code == 0

    def test_start_rejects_invalid_scenario(self, runner):
        from hexawyn.cli.main import app

        result = runner.invoke(app, ["start", "--demo", "--scenario", "invalid"])
        assert result.exit_code != 0


class TestSetupCommand:
    def test_setup_creates_app_with_force_setup(self, runner):
        with patch("hexawyn.cli.app.HexawynApp", create=True) as mock_app:
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["setup"])
            assert result.exit_code == 0
            mock_app.assert_called_once_with(force_setup=True)
            mock_app.return_value.run.assert_called_once()
