"""Unit tests for `hexa config provider` — CLI-set cloud credentials."""

from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner
from hexawyn.cli.commands.config_command import config


class TestConfigProviderCommand:
    def test_set_provider_credentials(self) -> None:
        with (
            patch("hexawyn.cli.commands.config_command.set_provider_credentials") as set_creds,
            patch("hexawyn.cli.commands.config_command.apply_provider_env") as apply_env,
        ):
            result = CliRunner().invoke(
                config,
                ["provider", "set", "aws", "access_key=AKIA", "secret_key=s3cr3t", "region=eu"],
            )

        assert result.exit_code == 0
        set_creds.assert_called_once_with(
            "aws", {"access_key": "AKIA", "secret_key": "s3cr3t", "region": "eu"}
        )
        apply_env.assert_called_once_with("aws")

    def test_set_rejects_missing_equals(self) -> None:
        with patch("hexawyn.cli.commands.config_command.set_provider_credentials") as set_creds:
            result = CliRunner().invoke(config, ["provider", "set", "aws", "access_key"])

        assert result.exit_code != 0
        set_creds.assert_not_called()

    def test_provider_list(self) -> None:
        with patch(
            "hexawyn.cli.commands.config_command.list_provider_credentials",
            return_value={"aws": {"access_key": "AKIA"}},
        ):
            result = CliRunner().invoke(config, ["provider", "list"])

        assert result.exit_code == 0
        assert "aws" in result.output

    def test_provider_clear(self) -> None:
        with patch("hexawyn.cli.commands.config_command.clear_provider_credentials") as clear:
            result = CliRunner().invoke(config, ["provider", "clear", "aws"])

        assert result.exit_code == 0
        clear.assert_called_once_with("aws")

    def test_providers_listing(self) -> None:
        with (
            patch(
                "hexawyn.cli.commands.config_command.detect_installed_providers",
                return_value={"aws": True, "vanilla": True},
            ),
            patch(
                "hexawyn.cli.commands.config_command.list_provider_credentials",
                return_value={},
            ),
        ):
            result = CliRunner().invoke(config, ["providers"])

        assert result.exit_code == 0
        assert "aws" in result.output
