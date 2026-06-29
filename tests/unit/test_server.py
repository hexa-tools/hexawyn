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

    def test_list_task_runs_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_task_runs" in tool_names

    def test_build_tekton_adapter_returns_vanilla_adapter(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
        from hexawyn.mcp.server import build_tekton_adapter

        result = build_tekton_adapter()
        assert isinstance(result, VanillaAdapter)


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


class TestMCPListTaskRunsTool:
    def test_list_task_runs_returns_task_runs_list(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driven.tekton_port import TaskRunInfo, TektonPort

        fake_run: TaskRunInfo = {
            "name": "build-deploy-clone-repo-abc",
            "task_ref": "clone-repo",
            "status": "Succeeded",
            "start_time": "2024-01-01T10:00:00Z",
            "duration": "12s",
            "failing_step": None,
            "failing_step_error": None,
        }
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_task_runs.return_value = [fake_run]

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            return_value=mock_adapter,
        ):
            from hexawyn.mcp.tools.list_task_runs import list_task_runs

            result = list_task_runs(pipeline_name="build-deploy", namespace="ci")
            assert isinstance(result["task_runs"], list)
            assert len(result["task_runs"]) == 1
            assert result["error"] is None

    def test_list_task_runs_returns_error_when_pipeline_not_found(self) -> None:
        from hexawyn.domain.errors import PipelineNotFoundError

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=PipelineNotFoundError(pipeline_name="ghost"),
        ):
            from hexawyn.mcp.tools.list_task_runs import list_task_runs

            result = list_task_runs(pipeline_name="ghost", namespace="ci")
            assert result["task_runs"] == []
            assert result["error"] is not None
            assert "ghost" in str(result["error"])

    def test_list_task_runs_returns_error_on_cluster_failure(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=Exception("tekton API down"),
        ):
            from hexawyn.mcp.tools.list_task_runs import list_task_runs

            result = list_task_runs(pipeline_name="build-deploy", namespace="ci")
            assert result["task_runs"] == []
            assert result["error"] == "tekton API down"


class TestMCPListPipelineRunsTool:
    def test_list_pipeline_runs_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_pipeline_runs" in tool_names

    def test_list_pipeline_runs_returns_runs_and_stats(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo, TektonPort

        fake_run: PipelineRunInfo = {
            "name": "payment-service-run-abc",
            "status": "Succeeded",
            "start_time": "2024-01-15T10:00:00Z",
            "duration": "4m30s",
            "duration_seconds": 270,
            "triggered_by": "github-push",
        }
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs.return_value = [fake_run]

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="payment-service", namespace="ci")
            assert isinstance(result["runs"], list)
            assert len(result["runs"]) == 1
            assert isinstance(result["stats"], dict)
            assert result["error"] is None

    def test_list_pipeline_runs_returns_error_when_service_not_found(self) -> None:
        from hexawyn.domain.errors import ServiceNotFoundError

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=ServiceNotFoundError(service_name="ghost"),
        ):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="ghost", namespace="ci")
            assert result["runs"] == []
            assert result["error"] is not None
            assert "ghost" in str(result["error"])

    def test_list_pipeline_runs_returns_error_on_cluster_failure(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=Exception("tekton API down"),
        ):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="payment-service", namespace="ci")
            assert result["runs"] == []
            assert result["error"] == "tekton API down"

    def test_list_pipeline_runs_includes_outliers_and_note(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo, TektonPort

        normal = [
            {
                "name": f"run-{i}",
                "status": "Succeeded",
                "start_time": f"2024-01-{15 - i:02d}T10:00:00Z",
                "duration": "5m",
                "duration_seconds": 300,
                "triggered_by": None,
            }
            for i in range(2)
        ]
        outlier: PipelineRunInfo = {
            "name": "run-outlier",
            "status": "Succeeded",
            "start_time": "2024-01-10T10:00:00Z",
            "duration": "22m",
            "duration_seconds": 1320,
            "triggered_by": None,
        }
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs.return_value = normal + [outlier]

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="payment-service", namespace="ci", limit=10)
            assert "run-outlier" in result["outliers"]
            assert result["note"] is not None
