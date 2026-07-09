import json
from unittest.mock import MagicMock, patch

import pytest

boto3 = pytest.importorskip("boto3")
from botocore.exceptions import (  # noqa: E402
    ClientError,
    EndpointConnectionError,
    NoCredentialsError,
)
from hexawyn.application.ports.driven.log_search_port import LogSearchPort  # noqa: E402
from hexawyn.domain.errors import (  # noqa: E402
    ClusterUnreachableError,
    InsufficientPermissionsError,
)


def _event(message: str) -> dict:
    return {"message": message}


def _ci_event(container: str, line: str, pod: str = "payments-api", ns: str = "prod") -> dict:
    return _event(
        json.dumps(
            {
                "log": line,
                "kubernetes": {
                    "container_name": container,
                    "pod_name": pod,
                    "namespace_name": ns,
                },
            }
        )
    )


def _client_error(code: str) -> ClientError:
    return ClientError({"Error": {"Code": code, "Message": "x"}}, "FilterLogEvents")


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import (
        CloudWatchLogsAdapter,
    )

    return CloudWatchLogsAdapter(cluster_name="prod", region="eu-west-1", logs_client=client)


class TestContract:
    def test_is_a_log_search_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), LogSearchPort)


class TestFetchPodContainerLogs:
    def test_groups_lines_by_container(self) -> None:
        client = MagicMock()
        client.filter_log_events.return_value = {
            "events": [
                _ci_event("app", "boot ok"),
                _ci_event("app", "serving"),
                _ci_event("sidecar", "proxy up"),
            ]
        }
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        by_name = {c["container"]: c for c in result}
        assert by_name["app"]["lines"] == ["boot ok", "serving"]
        assert by_name["sidecar"]["lines"] == ["proxy up"]
        assert by_name["app"]["truncated"] is False

    def test_uses_container_insights_log_group_and_pod_filter(self) -> None:
        client = MagicMock()
        client.filter_log_events.return_value = {"events": []}
        adapter = _adapter(client)

        adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        kwargs = client.filter_log_events.call_args.kwargs
        assert kwargs["logGroupName"] == "/aws/containerinsights/prod/application"
        assert "payments-api" in kwargs["filterPattern"]

    def test_non_json_message_falls_back_to_unknown_container(self) -> None:
        client = MagicMock()
        client.filter_log_events.return_value = {"events": [_event("plain text line")]}
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert result[0]["container"] == "unknown"
        assert result[0]["lines"] == ["plain text line"]

    def test_json_non_object_message_falls_back_to_unknown_container(self) -> None:
        client = MagicMock()
        client.filter_log_events.return_value = {"events": [_event(json.dumps([1, 2, 3]))]}
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert result[0]["container"] == "unknown"
        assert result[0]["lines"] == ["[1, 2, 3]"]

    def test_paginates_with_next_token(self) -> None:
        client = MagicMock()
        client.filter_log_events.side_effect = [
            {"events": [_ci_event("app", "one")], "nextToken": "n"},
            {"events": [_ci_event("app", "two")]},
        ]
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert client.filter_log_events.call_count == 2
        assert result[0]["lines"] == ["one", "two"]

    def test_missing_log_group_returns_empty(self) -> None:
        client = MagicMock()
        client.filter_log_events.side_effect = _client_error("ResourceNotFoundException")
        adapter = _adapter(client)

        assert adapter.fetch_pod_container_logs("payments-api", "prod", 15) == []


class TestErrorTranslation:
    def test_access_denied_raises_insufficient_permissions(self) -> None:
        client = MagicMock()
        client.filter_log_events.side_effect = _client_error("AccessDeniedException")
        adapter = _adapter(client)

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_missing_credentials_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.filter_log_events.side_effect = NoCredentialsError()
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_endpoint_connection_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.filter_log_events.side_effect = EndpointConnectionError(
            endpoint_url="https://logs.eu-west-1.amazonaws.com"
        )
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_other_client_error_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.filter_log_events.side_effect = _client_error("ThrottlingException")
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)


class TestTruncation:
    def test_truncates_at_max_lines(self) -> None:
        from hexawyn.adapters.secondary.aws import cloudwatch_logs_adapter as module

        max_lines = module._MAX_LINES_PER_CONTAINER
        client = MagicMock()
        client.filter_log_events.return_value = {
            "events": [_ci_event("app", f"line-{i}") for i in range(max_lines + 10)]
        }
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == max_lines
        assert result[0]["truncated"] is True


class TestErrorCodeHelper:
    def test_returns_empty_when_exception_has_no_response(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import _error_code

        assert _error_code(ValueError("boom")) == ""


class TestLazyClientCreation:
    def test_lazily_creates_boto3_client(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )

        created = MagicMock()
        created.filter_log_events.return_value = {"events": []}
        adapter = CloudWatchLogsAdapter(cluster_name="prod", region="eu-west-1")

        with patch.object(boto3, "client", return_value=created) as mock_client:
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        mock_client.assert_called_once_with("logs", region_name="eu-west-1")
