from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.db_command import _format_size, db


class TestFormatSize:
    def test_formats_bytes(self) -> None:
        assert _format_size(512) == "512 B"

    def test_formats_kilobytes(self) -> None:
        assert _format_size(2048) == "2.0 KB"

    def test_formats_megabytes(self) -> None:
        assert _format_size(5_242_880) == "5.0 MB"

    def test_formats_gigabytes(self) -> None:
        assert _format_size(2_147_483_648) == "2.00 GB"

    def test_boundary_exactly_1kb(self) -> None:
        assert "KB" in _format_size(1024)


class TestSizeCommand:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_shows_db_path_and_size(self) -> None:
        with (
            patch("hexawyn.cli.commands.db_command.get_db_size_bytes", return_value=1024),
            patch("hexawyn.cli.commands.db_command.DB_PATH", "/tmp/test.duckdb"),
        ):
            result = self.runner.invoke(db, ["size"])
        assert result.exit_code == 0
        assert "/tmp/test.duckdb" in result.output
        assert "1.0 KB" in result.output

    def test_shows_warning_when_above_threshold(self) -> None:
        with (
            patch("hexawyn.cli.commands.db_command.get_db_size_bytes", return_value=600_000_000),
            patch("hexawyn.cli.commands.db_command._DB_SIZE_WARNING_THRESHOLD", 500_000_000),
        ):
            result = self.runner.invoke(db, ["size"])
        assert result.exit_code == 0
        assert "exceeds" in result.output

    def test_shows_threshold_when_below(self) -> None:
        with (
            patch("hexawyn.cli.commands.db_command.get_db_size_bytes", return_value=1024),
            patch("hexawyn.cli.commands.db_command._DB_SIZE_WARNING_THRESHOLD", 500_000_000),
        ):
            result = self.runner.invoke(db, ["size"])
        assert result.exit_code == 0
        assert "Warning threshold" in result.output

    def test_empty_db_shows_no_threshold(self) -> None:
        with (
            patch("hexawyn.cli.commands.db_command.get_db_size_bytes", return_value=0),
        ):
            result = self.runner.invoke(db, ["size"])
        assert result.exit_code == 0
        assert "Warning threshold" not in result.output


class TestPurgeCommand:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def _mock_conn(self, count: int = 0, remaining: int = 0) -> MagicMock:
        conn = MagicMock()
        conn.execute.return_value.fetchone.side_effect = [count, remaining]
        return conn

    def test_purge_expired_deletes_and_reports(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (3,)
        with (
            patch("hexawyn.cli.commands.db_command.get_connection", return_value=mock_conn),
            patch("hexawyn.cli.commands.db_command.purge_expired_incidents", return_value=5),
        ):
            result = self.runner.invoke(db, ["purge"])
        assert result.exit_code == 0
        assert "5 expired incident(s)" in result.output

    def test_purge_older_than_deletes_and_reports(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (2,)
        with (
            patch("hexawyn.cli.commands.db_command.get_connection", return_value=mock_conn),
            patch("hexawyn.cli.commands.db_command.purge_older_than", return_value=3),
        ):
            result = self.runner.invoke(db, ["purge", "--older-than", "30"])
        assert result.exit_code == 0
        assert "3 incident(s) older than 30 days" in result.output

    def test_purge_dry_run_expired_shows_count(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.side_effect = [(4,), (10,)]
        with patch("hexawyn.cli.commands.db_command.get_connection", return_value=mock_conn):
            result = self.runner.invoke(db, ["purge", "--dry-run"])
        assert result.exit_code == 0
        assert "Would delete 4 expired" in result.output
        assert "dry run" in result.output

    def test_purge_dry_run_older_than_shows_count(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.side_effect = [(7,), (5,)]
        with patch("hexawyn.cli.commands.db_command.get_connection", return_value=mock_conn):
            result = self.runner.invoke(db, ["purge", "--older-than", "7", "--dry-run"])
        assert result.exit_code == 0
        assert "Would delete 7" in result.output

    def test_purge_shows_error_when_db_unavailable(self) -> None:
        with patch(
            "hexawyn.cli.commands.db_command.get_connection",
            side_effect=Exception("file not found"),
        ):
            result = self.runner.invoke(db, ["purge"])
        assert result.exit_code == 0
        assert "Cannot connect" in result.output
