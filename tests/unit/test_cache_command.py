from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.cache_command import cache


class TestCacheStats:
    def test_stats_displays_total_entries(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.stats.return_value = {"total": 42, "valid": 30, "expired": 12}

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            result = runner.invoke(cache, ["stats"])

        assert result.exit_code == 0
        assert "42" in result.output
        assert "valid" in result.output.lower()

    def test_stats_closes_adapter(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.stats.return_value = {"total": 1, "valid": 1, "expired": 0}

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            runner.invoke(cache, ["stats"])

        mock_adapter.close.assert_called_once()

    def test_stats_propagates_adapter_error(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.stats.side_effect = RuntimeError("db error")

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            result = runner.invoke(cache, ["stats"])

        assert result.exit_code != 0


class TestCacheClear:
    def test_clear_displays_entries_removed(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.stats.return_value = {"total": 15, "valid": 10, "expired": 5}

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            result = runner.invoke(cache, ["clear"])

        assert result.exit_code == 0
        assert "15" in result.output

    def test_clear_calls_adapter_clear(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.stats.return_value = {"total": 0, "valid": 0, "expired": 0}

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            runner.invoke(cache, ["clear"])

        mock_adapter.clear.assert_called_once()

    def test_clear_closes_adapter(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.stats.return_value = {"total": 3, "valid": 3, "expired": 0}

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            runner.invoke(cache, ["clear"])

        mock_adapter.close.assert_called_once()


class TestCacheInvalidate:
    def test_invalidate_displays_entry_count(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.invalidate_by_resource.return_value = 7

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            result = runner.invoke(
                cache,
                [
                    "invalidate",
                    "--cluster",
                    "prod-eu",
                    "--namespace",
                    "default",
                    "--resource",
                    "payments-api",
                ],
            )

        assert result.exit_code == 0
        assert "7" in result.output
        assert "prod-eu/default/payments-api" in result.output

    def test_invalidate_passes_correct_args(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.invalidate_by_resource.return_value = 2

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            runner.invoke(
                cache,
                [
                    "invalidate",
                    "--cluster",
                    "staging",
                    "--namespace",
                    "kube-system",
                    "--resource",
                    "coredns",
                ],
            )

        mock_adapter.invalidate_by_resource.assert_called_once_with(
            "staging", "kube-system", "coredns"
        )

    def test_invalidate_requires_all_options(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            result = runner.invoke(cache, ["invalidate"])

        assert result.exit_code != 0

    def test_invalidate_closes_adapter(self) -> None:
        runner = CliRunner()
        mock_adapter = MagicMock()
        mock_adapter.invalidate_by_resource.return_value = 0

        with patch("hexawyn.cli.commands.cache_command._get_adapter", return_value=mock_adapter):
            runner.invoke(
                cache,
                ["invalidate", "--cluster", "x", "--namespace", "y", "--resource", "z"],
            )

        mock_adapter.close.assert_called_once()
