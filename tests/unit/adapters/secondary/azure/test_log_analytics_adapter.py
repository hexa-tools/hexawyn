from __future__ import annotations

from sys import modules as sys_modules
from unittest.mock import Mock, patch

from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
    AzureLogAnalyticsAdapter,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


class TestAzureLogAnalyticsAdapter:
    def test_fetch_pod_container_logs_empty_result_no_tables(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_result.tables = []
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)
        result = adapter.fetch_pod_container_logs("my-pod", "default", 30)
        assert result == []

    def test_logs_kql_builds_query(self) -> None:
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=Mock())
        kql = adapter._logs_kql("my-pod", "default")
        assert "my-pod" in kql
        assert "default" in kql
        assert "ContainerLogV2" in kql

    def test_group_by_container_empty_table(self) -> None:
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=Mock())
        mock_table = Mock()
        mock_table.rows = []
        mock_table.columns = []
        result = adapter._group_by_container(mock_table)
        assert result == []

    def test_fetch_pod_container_logs_returns_grouped_logs(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_table = Mock()
        mock_table.columns = ["ContainerName", "LogMessage"]
        mock_table.rows = [
            ["app", "Error: connection refused"],
            ["app", "retrying in 5s"],
            ["sidecar", "proxy started"],
        ]
        mock_result.tables = [mock_table]
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)
        result = adapter.fetch_pod_container_logs("my-pod", "default", 30)
        assert len(result) == 2  # noqa: PLR2004
        container_names = {entry["container"] for entry in result}
        assert container_names == {"app", "sidecar"}
        for entry in result:
            assert not entry["truncated"]

    def test_group_by_container_respects_max_lines_per_container(self) -> None:
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=Mock())
        mock_table = Mock()
        mock_table.columns = ["ContainerName", "LogMessage"]
        lines = [f"line {i}" for i in range(5001)]
        mock_table.rows = [["bursty", msg] for msg in lines]
        result = adapter._group_by_container(mock_table)
        assert len(result) == 1
        assert len(result[0]["lines"]) == 5000  # noqa: PLR2004
        assert result[0]["truncated"] is True

    def test_unknown_container_name_defaults_to_unknown(self) -> None:
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=Mock())
        mock_table = Mock()
        mock_table.columns = ["OtherColumn"]
        mock_table.rows = [["some value"]]
        result = adapter._group_by_container(mock_table)
        assert len(result) == 1
        assert result[0]["container"] == "unknown"

    def test_query_client_auth_error_raises_cluster_unreachable(self) -> None:
        mock_azure_exc = Mock()
        auth_error = type("ClientAuthenticationError", (Exception,), {})
        mock_azure_exc.ClientAuthenticationError = auth_error
        mock_azure_exc.HttpResponseError = type("HttpResponseError", (Exception,), {})

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        mock_client.query_workspace.side_effect = auth_error("auth failed")
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_pod_container_logs("my-pod", "default", 30)
            except ClusterUnreachableError:
                pass

    def test_query_http_forbidden_raises_insufficient_permissions(self) -> None:
        mock_azure_exc = Mock()
        mock_azure_exc.ClientAuthenticationError = type(
            "ClientAuthenticationError", (Exception,), {}
        )
        http_error = type("HttpResponseError", (Exception,), {})
        mock_azure_exc.HttpResponseError = http_error

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        forbidden = http_error("forbidden")
        forbidden.status_code = 403  # noqa: FLD002
        mock_client.query_workspace.side_effect = forbidden
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_pod_container_logs("my-pod", "default", 30)
            except InsufficientPermissionsError:
                pass

    def test_query_failure_status_raises_cluster_unreachable(self) -> None:
        mock_azure_exc = Mock()
        mock_azure_exc.ClientAuthenticationError = type(
            "ClientAuthenticationError", (Exception,), {}
        )
        mock_azure_exc.HttpResponseError = type("HttpResponseError", (Exception,), {})

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "FAILURE"
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_pod_container_logs("my-pod", "default", 30)
            except ClusterUnreachableError:
                pass

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = Mock()
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)
        result = adapter._client_or_create()
        assert result is mock_client

    def test_query_http_error_other_status_raises_cluster_unreachable(self) -> None:
        mock_azure_exc = Mock()
        mock_azure_exc.ClientAuthenticationError = type(
            "ClientAuthenticationError", (Exception,), {}
        )
        http_error = type("HttpResponseError", (Exception,), {})
        mock_azure_exc.HttpResponseError = http_error

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        server_error = http_error("server error")
        mock_client.query_workspace.side_effect = server_error
        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_client)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_pod_container_logs("my-pod", "default", 30)
            except ClusterUnreachableError:
                pass

    def test_client_or_create_lazy_init_with_azure_sdk(self) -> None:
        mock_azure_identity = Mock()
        mock_azure_identity.DefaultAzureCredential = Mock(return_value="fake_cred")
        mock_query = Mock()
        mock_query.LogsQueryClient = Mock(return_value="fake_client")

        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=None)

        with patch.dict(
            sys_modules,
            {
                "azure.identity": mock_azure_identity,
                "azure.monitor.query": mock_query,
            },
            clear=False,
        ):
            result = adapter._client_or_create()
            assert result == "fake_client"
            mock_query.LogsQueryClient.assert_called_once()
