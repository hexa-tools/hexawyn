"""Unit tests for the global_health_check MCP tool (pagination + unlimited)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

_UNLIMITED = 0
_PAGE = 2
_PAGE_SIZE = 5
_MAX_WORKERS = 3
_TOTAL = 100
_PAGE_SIZE_BATCH = 10


class TestGlobalHealthCheckTool:
    def _mock_success(self) -> tuple[MagicMock, MagicMock]:
        mock_cluster_report = MagicMock()
        mock_cluster_report.context_name = "test-ctx"
        mock_cluster_report.reachable = True
        mock_cluster_report.unreachable_reason = None
        mock_cluster_report.health_score = 85.0
        mock_cluster_report.health_status = "healthy"
        mock_cluster_report.categories = {}
        mock_cluster_report.checked_at = MagicMock()
        mock_cluster_report.checked_at.isoformat.return_value = "2024-01-01T00:00:00"

        mock_report = MagicMock()
        mock_report.cluster_reports = [mock_cluster_report]
        mock_report.fleet_score = 85.0
        mock_report.fleet_status = "healthy"
        mock_report.reachable_count = 1
        mock_report.unreachable_count = 0
        mock_report.checked_at = MagicMock()
        mock_report.checked_at.isoformat.return_value = "2024-01-01T00:00:00"

        mock_response = MagicMock()
        mock_response.report = mock_report
        mock_response.fleet_score_trend = "stable"
        mock_response.total_contexts = _TOTAL
        mock_response.page = 1
        mock_response.page_size = _PAGE_SIZE_BATCH
        mock_response.has_more = True

        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        return mock_uc, mock_report

    def test_returns_dict_with_pagination_meta(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        mock_uc, _ = self._mock_success()
        with (
            patch("hexawyn.mcp.server.build_fleet_health_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.global_health_check.GlobalHealthCheckUseCase",
                return_value=mock_uc,
            ),
        ):
            result = global_health_check(
                max_clusters=_UNLIMITED, page=1, page_size=_PAGE_SIZE_BATCH
            )

        assert result["fleet_status"] == "healthy"
        assert result["total_contexts"] == _TOTAL
        assert result["page_size"] == _PAGE_SIZE_BATCH
        assert result["has_more"] is True

    def test_forwards_pagination_and_unlimited_to_command(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        captured: dict[str, object] = {}

        def _capture(command: object) -> MagicMock:
            captured["command"] = command
            return self._mock_success()[0].execute.return_value

        with (
            patch("hexawyn.mcp.server.build_fleet_health_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.global_health_check.GlobalHealthCheckUseCase",
                return_value=MagicMock(),
            ) as mock_uc_cls,
        ):
            mock_uc = MagicMock()
            mock_uc.execute.side_effect = _capture
            mock_uc_cls.return_value = mock_uc

            global_health_check(
                max_clusters=_UNLIMITED, page=_PAGE, page_size=_PAGE_SIZE, max_workers=_MAX_WORKERS
            )

        command = captured["command"]
        assert command.max_clusters == _UNLIMITED
        assert command.page == _PAGE
        assert command.page_size == _PAGE_SIZE
        assert command.max_workers == _MAX_WORKERS

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = global_health_check()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
