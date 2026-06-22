import asyncio
from unittest.mock import MagicMock, patch


class TestMCPHealthTool:
    def test_health_returns_status_ok_when_duckdb_connected(self):
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (1,)

        with patch(
            "hexawyn.mcp.server.get_connection", return_value=mock_conn
        ), patch(
            "hexawyn.mcp.server.get_api_key", return_value="sk-ant-fake"
        ):
            from hexawyn.mcp.server import health

            result = health.fn()
            assert result["status"] == "ok"
            assert result["duckdb"] == "connected"
            assert result["api_key"] == "configured"
            assert result["version"] == "0.1.0b0"

    def test_health_returns_degraded_when_duckdb_fails(self):
        with patch(
            "hexawyn.mcp.server.get_connection",
            side_effect=Exception("DB down"),
        ), patch(
            "hexawyn.mcp.server.get_api_key", return_value="sk-ant-fake"
        ):
            from hexawyn.mcp.server import health

            result = health.fn()
            assert result["status"] == "degraded"
            assert result["duckdb"] == "unavailable"

    def test_health_returns_missing_when_no_api_key(self):
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (1,)

        with patch(
            "hexawyn.mcp.server.get_connection", return_value=mock_conn
        ), patch(
            "hexawyn.mcp.server.get_api_key", return_value=None
        ):
            from hexawyn.mcp.server import health

            result = health.fn()
            assert result["api_key"] == "missing"

    def test_health_returns_degraded_when_both_fail(self):
        with patch(
            "hexawyn.mcp.server.get_connection",
            side_effect=Exception("DB down"),
        ), patch(
            "hexawyn.mcp.server.get_api_key", return_value=None
        ):
            from hexawyn.mcp.server import health

            result = health.fn()
            assert result["status"] == "degraded"
            assert result["duckdb"] == "unavailable"
            assert result["api_key"] == "missing"


class TestMCPServerInit:
    def test_mcp_server_has_correct_name_and_version(self):
        from hexawyn.mcp.server import mcp

        assert "hexawyn" in mcp.name.lower()
        assert mcp.version is not None

    def test_health_tool_is_registered(self):
        import asyncio

        from hexawyn.mcp.server import mcp

        tool_names = asyncio.run(mcp.get_tools())
        assert "health" in tool_names
