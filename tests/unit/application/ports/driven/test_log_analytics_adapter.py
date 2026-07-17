from datetime import timedelta
from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("azure.monitor.query")
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError  # noqa: E402
from azure.monitor.query import LogsQueryStatus  # noqa: E402
from hexawyn.application.ports.driven.log_search_port import LogSearchPort  # noqa: E402
from hexawyn.domain.errors import (  # noqa: E402
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_WORKSPACE = "ws-123"


def _table(columns: list[str], rows: list[list[object]]) -> MagicMock:
    table = MagicMock()
    table.columns = columns
    table.rows = rows
    return table


def _result(tables: list[MagicMock], status: object = LogsQueryStatus.SUCCESS) -> MagicMock:
    result = MagicMock()
    result.status = status
    result.tables = tables
    return result


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
        AzureLogAnalyticsAdapter,
    )

    return AzureLogAnalyticsAdapter(workspace_id=_WORKSPACE, logs_client=client)


class TestContract:
    def test_is_a_log_search_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), LogSearchPort)


class TestFetchPodContainerLogs:
    def test_groups_lines_by_container(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result(
            [
                _table(
                    ["ContainerName", "LogMessage"],
                    [
                        ["app", "boot ok"],
                        ["app", "serving"],
                        ["sidecar", "proxy up"],
                    ],
                )
            ]
        )
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        by_name = {c["container"]: c for c in result}
        assert by_name["app"]["lines"] == ["boot ok", "serving"]
        assert by_name["sidecar"]["lines"] == ["proxy up"]

    def test_query_uses_pod_namespace_and_timespan(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([])
        adapter = _adapter(client)

        adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        call = client.query_workspace.call_args
        assert call.args[0] == _WORKSPACE
        kql = call.args[1]
        assert "payments-api" in kql
        assert "prod" in kql
        assert call.kwargs["timespan"] == timedelta(minutes=15)

    def test_empty_result_returns_empty(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([])
        adapter = _adapter(client)

        assert adapter.fetch_pod_container_logs("payments-api", "prod", 15) == []

    def test_truncates_at_max_lines(self) -> None:
        from hexawyn.adapters.secondary.azure import log_analytics_adapter as module

        max_lines = module._MAX_LINES_PER_CONTAINER
        client = MagicMock()
        rows = [["app", f"line-{i}"] for i in range(max_lines + 10)]
        client.query_workspace.return_value = _result(
            [_table(["ContainerName", "LogMessage"], rows)]
        )
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == max_lines
        assert result[0]["truncated"] is True


class TestErrorTranslation:
    def test_forbidden_raises_insufficient_permissions(self) -> None:
        client = MagicMock()
        error = HttpResponseError("denied")
        error.status_code = 403
        client.query_workspace.side_effect = error
        adapter = _adapter(client)

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_missing_credentials_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.query_workspace.side_effect = ClientAuthenticationError("no creds")
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError) as exc_info:
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert "az login" in str(exc_info.value).lower()

    def test_other_http_error_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        error = HttpResponseError("boom")
        error.status_code = 500
        client.query_workspace.side_effect = error
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_query_failure_status_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([], status=LogsQueryStatus.FAILURE)
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)


class TestLazyClientCreation:
    def test_lazily_creates_client(self) -> None:
        created = MagicMock()
        created.query_workspace.return_value = _result([])
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        adapter = AzureLogAnalyticsAdapter(workspace_id=_WORKSPACE)

        with (
            patch("azure.identity.DefaultAzureCredential", return_value=MagicMock()),
            patch("azure.monitor.query.LogsQueryClient", return_value=created) as client_cls,
        ):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        client_cls.assert_called_once()
