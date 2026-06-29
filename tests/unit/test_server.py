import asyncio
from unittest.mock import MagicMock, patch

from hexawyn.domain.errors import ClusterUnreachableError


class TestMCPHealthTool:
    def test_health_returns_status_ok_when_duckdb_connected(self):
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (1,)

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=mock_conn),
            patch("hexawyn.mcp.server.get_api_key", return_value="sk-ant-fake"),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "connected", "context": "prod-eu"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["status"] == "ok"
            assert result["duckdb"] == "connected"
            assert result["api_key"] == "configured"
            assert result["version"] == "0.1.0b0"
            assert result["cluster"] == "connected"
            assert result["context"] == "prod-eu"

    def test_health_returns_degraded_when_duckdb_fails(self):
        with (
            patch(
                "hexawyn.mcp.server.get_connection",
                side_effect=Exception("DB down"),
            ),
            patch("hexawyn.mcp.server.get_api_key", return_value="sk-ant-fake"),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "connected", "context": "prod-eu"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["status"] == "degraded"
            assert result["duckdb"] == "unavailable"
            assert result["cluster"] == "connected"

    def test_health_returns_missing_when_no_api_key(self):
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (1,)

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=mock_conn),
            patch("hexawyn.mcp.server.get_api_key", return_value=None),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "no_kubeconfig", "error": "no config found"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["api_key"] == "missing"
            assert result["cluster"] == "no_kubeconfig"
            assert result["context"] == "none"

    def test_health_returns_degraded_when_both_fail(self):
        with (
            patch(
                "hexawyn.mcp.server.get_connection",
                side_effect=Exception("DB down"),
            ),
            patch("hexawyn.mcp.server.get_api_key", return_value=None),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "no_kubeconfig"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["status"] == "degraded"
            assert result["duckdb"] == "unavailable"
            assert result["api_key"] == "missing"
            assert result["cluster"] == "no_kubeconfig"


class TestMCPServerStartupValidation:
    def test_cluster_status_no_kubeconfig_when_config_missing(self):
        import sys

        sys.modules.pop("hexawyn.mcp.server", None)
        sys.modules.pop("hexawyn.mcp", None)

        with patch(
            "hexawyn.infrastructure.config.kubeconfig_reader.load_kubeconfig",
            side_effect=ClusterUnreachableError("no kubeconfig"),
        ):
            import hexawyn.mcp.server as server_mod

            assert server_mod._cluster_status["status"] == "no_kubeconfig"

    def test_cluster_status_connected_when_config_found(self):
        import sys

        sys.modules.pop("hexawyn.mcp.server", None)
        sys.modules.pop("hexawyn.mcp", None)

        mock_api = MagicMock()
        with (
            patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.load_kubeconfig",
                return_value=mock_api,
            ),
            patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.get_active_context",
                return_value={"name": "prod-eu", "context": {"cluster": "cluster-eu"}},
            ),
            patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.validate_connection",
                return_value={"status": "connected", "context": "prod-eu"},
            ),
        ):
            import hexawyn.mcp.server as server_mod

            assert server_mod._cluster_status["status"] == "connected"
            assert server_mod._cluster_status["context"] == "prod-eu"


class TestMCPServerInit:
    def test_mcp_server_has_correct_name_and_version(self):
        from hexawyn.mcp.server import mcp

        assert "hexawyn" in mcp.name.lower()
        assert mcp.version is not None

    def test_health_tool_is_registered(self):
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "health" in tool_names

    def test_list_namespaces_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_namespaces" in tool_names


class TestMCPListNamespacesTool:
    def test_list_namespaces_returns_dict_with_namespaces_key(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_namespaces import list_namespaces

            result = list_namespaces()
            assert isinstance(result, dict)
            assert "namespaces" in result
            assert isinstance(result["namespaces"], list)

    def test_list_namespaces_items_have_expected_fields(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_namespaces import list_namespaces

            result = list_namespaces()
            for ns in result["namespaces"]:
                assert "name" in ns
                assert "status" in ns
                assert "age" in ns

    def test_list_namespaces_handles_no_cluster(self) -> None:
        from hexawyn.domain.errors import ClusterUnreachableError

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=ClusterUnreachableError("no kubeconfig"),
        ):
            from hexawyn.mcp.tools.list_namespaces import list_namespaces

            result = list_namespaces()
            assert result["error"] is not None
            assert result["namespaces"] == []

    def test_list_pods_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_pods" in tool_names


class TestMCPListPodsTool:
    def test_list_pods_returns_pods_for_namespace(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_pods import list_pods

            result = list_pods(namespace="production")
            assert isinstance(result, dict)
            assert "pods" in result
            assert isinstance(result["pods"], list)
            assert len(result["pods"]) > 0

    def test_list_pods_empty_namespace(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_pods import list_pods

            result = list_pods(namespace="nonexistent")
            assert result["pods"] == []

    def test_list_pods_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=Exception("k8s down"),
        ):
            from hexawyn.mcp.tools.list_pods import list_pods

            result = list_pods(namespace="default")
            assert result["error"] == "k8s down"
            assert result["pods"] == []
