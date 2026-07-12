from unittest.mock import patch

import click.testing
from hexawyn.cli.main import app


class TestScheduleCommands:
    def test_schedule_list_output(self) -> None:
        runner = click.testing.CliRunner()
        with patch(
            "hexawyn.infrastructure.config.schedule_source.load_config",
            return_value={
                "schedule": {"certs": {"schedule": "0 */6 * * *", "use_case": "certs_list"}}
            },
        ):
            result = runner.invoke(app, ["schedule", "list"])

        assert result.exit_code == 0
        assert "certs" in result.output
        assert "certs_list" in result.output

    def test_schedule_create_and_delete(self) -> None:
        runner = click.testing.CliRunner()
        with (
            patch(
                "hexawyn.infrastructure.config.schedule_source.load_config",
                return_value={},
            ),
            patch(
                "hexawyn.infrastructure.config.schedule_source.save_config",
            ) as _,
        ):
            result = runner.invoke(
                app,
                [
                    "schedule",
                    "create",
                    "--name",
                    "test-check",
                    "--use-case",
                    "certs_list",
                    "--every",
                    "6h",
                ],
            )

        assert result.exit_code == 0
        assert "Created" in result.output or "test-check" in result.output

    def test_schedule_create_invalid_schedule(self) -> None:
        runner = click.testing.CliRunner()
        result = runner.invoke(
            app,
            [
                "schedule",
                "create",
                "--name",
                "bad",
                "--use-case",
                "test",
                "--every",
                "5x",
            ],
        )

        assert result.exit_code == 0
        assert "Invalid" in result.output

    def test_schedule_status(self) -> None:
        runner = click.testing.CliRunner()
        with patch(
            "hexawyn.infrastructure.config.schedule_source.load_config",
            return_value={"schedule": {}},
        ):
            result = runner.invoke(app, ["schedule", "status"])

        assert result.exit_code == 0
        assert "Total" in result.output
