"""RED → GREEN — MCP tools: custom_tools_list, custom_tool_describe, custom_tool_run."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCustomToolsList:
    def test_returns_tools_list_when_runtime_available(self) -> None:
        mock_client = MagicMock()
        mock_client.list_custom_tools.return_value = [
            {"name": "custom/pci-check", "description": "PCI", "transport": "http"},
        ]

        with (
            patch(
                "hexawyn.adapters.secondary.runtime_client.RuntimeClient",
                return_value=mock_client,
            ),
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
                return_value="https://api.test",
            ),
        ):
            from hexawyn.mcp.tools.custom_tools_list import custom_tools_list

            result = custom_tools_list()

        assert result["error"] is None
        assert result["count"] == 1
        assert len(result["tools"]) == 1
        mock_client.close.assert_called_once()

    def test_returns_error_when_no_endpoint(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
            return_value=None,
        ):
            from hexawyn.mcp.tools.custom_tools_list import custom_tools_list

            result = custom_tools_list()

        assert result["count"] == 0
        assert result["error"] is not None

    def test_handles_exception_gracefully(self) -> None:
        with (
            patch(
                "hexawyn.adapters.secondary.runtime_client.RuntimeClient",
                side_effect=RuntimeError("timeout"),
            ),
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
                return_value="https://api.test",
            ),
        ):
            from hexawyn.mcp.tools.custom_tools_list import custom_tools_list

            result = custom_tools_list()

        assert result["error"] == "timeout"


class TestCustomToolDescribe:
    def test_returns_tool_contract(self) -> None:
        mock_client = MagicMock()
        mock_client.describe_custom_tool.return_value = {
            "name": "custom/pci-check",
            "description": "PCI compliance",
            "transport": "grpc",
            "input_schema": {"fields": ["namespace"]},
            "error": None,
        }

        with (
            patch(
                "hexawyn.adapters.secondary.runtime_client.RuntimeClient",
                return_value=mock_client,
            ),
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
                return_value="https://api.test",
            ),
        ):
            from hexawyn.mcp.tools.custom_tool_describe import custom_tool_describe

            result = custom_tool_describe("custom/pci-check")

        assert result["error"] is None
        assert result["name"] == "custom/pci-check"
        assert result["transport"] == "grpc"

    def test_handles_no_endpoint(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
            return_value=None,
        ):
            from hexawyn.mcp.tools.custom_tool_describe import custom_tool_describe

            result = custom_tool_describe("custom/x")
        assert result["error"] is not None


class TestCustomToolRun:
    def test_runs_tool_and_returns_result(self) -> None:
        mock_client = MagicMock()
        mock_client.run_custom_tool.return_value = {
            "tool_name": "custom/pci-check",
            "success": True,
            "findings": ["No violations"],
            "provenance": "external",
            "error": None,
        }

        with (
            patch(
                "hexawyn.adapters.secondary.runtime_client.RuntimeClient",
                return_value=mock_client,
            ),
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
                return_value="https://api.test",
            ),
        ):
            from hexawyn.mcp.tools.custom_tool_run import custom_tool_run

            result = custom_tool_run("custom/pci-check", '{"namespace": "default"}')

        assert result["error"] is None
        assert result["success"] is True
        assert result["tool_name"] == "custom/pci-check"

    def test_handles_invalid_json_params(self) -> None:
        from hexawyn.mcp.tools.custom_tool_run import custom_tool_run

        result = custom_tool_run("custom/t", "not valid json")
        assert result["error"] is not None

    def test_handles_exception(self) -> None:
        with (
            patch(
                "hexawyn.adapters.secondary.runtime_client.RuntimeClient",
                side_effect=RuntimeError("offline"),
            ),
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
                return_value="https://api.test",
            ),
        ):
            from hexawyn.mcp.tools.custom_tool_run import custom_tool_run

            result = custom_tool_run("custom/t", "{}")
        assert result["error"] == "offline"


class TestCustomToolRegister:
    def test_register_is_callable(self) -> None:
        from hexawyn.mcp.tools.custom_tool_describe import register as reg_desc
        from hexawyn.mcp.tools.custom_tool_run import register as reg_run
        from hexawyn.mcp.tools.custom_tools_list import register as reg_list

        assert callable(reg_list)
        assert callable(reg_desc)
        assert callable(reg_run)
