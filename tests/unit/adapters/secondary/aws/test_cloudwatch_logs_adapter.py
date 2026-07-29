from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError
from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import (
    CloudWatchLogsAdapter,
    _error_code,
    _parse_message,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


class TestCloudWatchLogsAdapter:
    def _make_logs_client(self) -> MagicMock:
        mock = MagicMock()
        mock.filter_log_events.return_value = {"events": []}
        return mock

    def test_log_group_correct_format(self) -> None:
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1")

        result = adapter._log_group()

        assert result == "/aws/containerinsights/my-cluster/application"

    def test_filter_pattern_correct_format(self) -> None:
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1")

        result = adapter._filter_pattern("my-pod", "default")

        assert "my-pod" in result
        assert "default" in result
        assert "pod_name" in result
        assert "namespace_name" in result

    def test_filter_events_success(self) -> None:
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.return_value = {
            "events": [
                {"message": '{"log":"error line 1","kubernetes":{"container_name":"app"}}'},
                {"message": '{"log":"error line 2","kubernetes":{"container_name":"app"}}'},
            ],
        }
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        result = adapter._filter_events("my-pod", "default", 1000, 2000)

        assert len(result) == 2  # noqa: PLR2004

    def test_filter_events_paginates(self) -> None:
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.side_effect = [
            {
                "events": [
                    {"message": '{"log":"line 1","kubernetes":{"container_name":"app"}}'},
                ],
                "nextToken": "page-2",
            },
            {
                "events": [
                    {"message": '{"log":"line 2","kubernetes":{"container_name":"app"}}'},
                ],
            },
        ]
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        result = adapter._filter_events("my-pod", "default", 1000, 2000)

        assert len(result) == 2  # noqa: PLR2004

    def test_filter_events_skips_empty_messages(self) -> None:
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.return_value = {
            "events": [
                {"message": ""},
                {"message": '{"log":"valid","kubernetes":{"container_name":"app"}}'},
            ],
        }
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        result = adapter._filter_events("my-pod", "default", 1000, 2000)

        assert len(result) == 1

    def test_filter_events_no_credentials_raises(self) -> None:
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.side_effect = NoCredentialsError()
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        with pytest.raises(ClusterUnreachableError, match="credentials"):
            adapter._filter_events("my-pod", "default", 1000, 2000)

    def test_filter_events_access_denied_returns_empty(self) -> None:
        error_response = {"Error": {"Code": "AccessDeniedException", "Message": "Access denied"}}
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.side_effect = ClientError(error_response, "FilterLogEvents")
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        with pytest.raises(InsufficientPermissionsError, match="Access denied"):
            adapter._filter_events("my-pod", "default", 1000, 2000)

    def test_filter_events_resource_not_found_returns_empty(self) -> None:
        error_response = {"Error": {"Code": "ResourceNotFoundException", "Message": "Not found"}}
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.side_effect = ClientError(error_response, "FilterLogEvents")
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        result = adapter._filter_events("my-pod", "default", 1000, 2000)

        assert result == []

    def test_filter_events_botocore_error_raises(self) -> None:
        mock_client = self._make_logs_client()
        mock_client.filter_log_events.side_effect = BotoCoreError()
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        with pytest.raises(ClusterUnreachableError, match="CloudWatch"):
            adapter._filter_events("my-pod", "default", 1000, 2000)

    def test_group_by_container_groups_correctly(self) -> None:
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=MagicMock())
        messages = [
            '{"log":"app line 1","kubernetes":{"container_name":"app"}}',
            '{"log":"app line 2","kubernetes":{"container_name":"app"}}',
            '{"log":"sidecar line 1","kubernetes":{"container_name":"sidecar"}}',
        ]

        result = adapter._group_by_container(messages)

        assert len(result) == 2  # noqa: PLR2004
        names = {r["container"] for r in result}
        assert names == {"app", "sidecar"}

    def test_group_by_container_truncates_when_limit_exceeded(self) -> None:
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=MagicMock())
        messages = [
            f'{{"log":"line {i}","kubernetes":{{"container_name":"app"}}}}' for i in range(6000)
        ]

        result = adapter._group_by_container(messages)

        assert len(result) == 1
        log = result[0]
        assert len(log["lines"]) == 5000  # noqa: PLR2004
        assert log["truncated"] is True

    def test_fetch_pod_container_logs_calls_filter_and_groups(self) -> None:
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=MagicMock())

        with patch.object(adapter, "_filter_events", return_value=[]) as mock_filter:
            with patch.object(adapter, "_group_by_container", return_value=[]) as mock_group:
                result = adapter.fetch_pod_container_logs("my-pod", "default", 15)

                assert isinstance(result, list)
                mock_filter.assert_called_once()
                mock_group.assert_called_once()

    def test_client_or_create_injects_client(self) -> None:
        mock_client = MagicMock()
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        result = adapter._client_or_create()

        assert result is mock_client

    def test_client_or_create_lazy_init_boto3(self) -> None:
        import sys

        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=None)
        mock_boto3 = MagicMock()
        mock_logs_client = MagicMock()
        mock_boto3.client.return_value = mock_logs_client

        with patch.dict(sys.modules, {"boto3": mock_boto3}):
            result = adapter._client_or_create()

            assert result is mock_logs_client
            mock_boto3.client.assert_called_once_with("logs", region_name="us-east-1")

    def test_filter_page_includes_next_token(self) -> None:
        mock_client = self._make_logs_client()
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        adapter._filter_page(mock_client, "my-pod", "default", 1000, 2000, "page-2")

        call_kwargs = mock_client.filter_log_events.call_args[1]
        assert call_kwargs["nextToken"] == "page-2"

    def test_filter_page_without_token(self) -> None:
        mock_client = self._make_logs_client()
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=mock_client)

        adapter._filter_page(mock_client, "my-pod", "default", 1000, 2000, None)

        call_kwargs = mock_client.filter_log_events.call_args[1]
        assert "nextToken" not in call_kwargs

    def test_handle_client_error_other_error_raises(self) -> None:
        adapter = CloudWatchLogsAdapter("my-cluster", "us-east-1", logs_client=MagicMock())
        error_response = {"Error": {"Code": "InternalError", "Message": "Internal failure"}}
        exc = ClientError(error_response, "FilterLogEvents")

        with pytest.raises(ClusterUnreachableError, match="CloudWatch"):
            adapter._handle_client_error(exc)


class TestErrorCode:
    def test_extracts_error_code_from_response(self) -> None:
        error_response = {"Error": {"Code": "AccessDeniedException", "Message": "boom"}}

        class TestExc(Exception):  # noqa: N818
            response = error_response

        assert _error_code(TestExc()) == "AccessDeniedException"

    def test_returns_empty_for_no_response(self) -> None:
        assert _error_code(Exception()) == ""

    def test_returns_empty_for_non_dict_error(self) -> None:
        class TestExc(Exception):  # noqa: N818
            response = {"Error": "not-a-dict"}

        assert _error_code(TestExc()) == ""


class TestParseMessage:
    def test_parses_valid_json(self) -> None:
        container, line = _parse_message(
            '{"log":"error message","kubernetes":{"container_name":"app"}}'
        )
        assert container == "app"
        assert line == "error message"

    def test_returns_unknown_for_invalid_json(self) -> None:
        container, line = _parse_message("plain text not json")
        assert container == "unknown"
        assert line == "plain text not json"

    def test_returns_unknown_for_non_dict_parsed(self) -> None:
        container, line = _parse_message('["list", "not", "dict"]')
        assert container == "unknown"
        assert line == '["list", "not", "dict"]'

    def test_returns_unknown_when_no_container_name(self) -> None:
        container, line = _parse_message('{"log":"some log","kubernetes":{"other":"data"}}')
        assert container == "unknown"
        assert line == "some log"

    def test_handles_non_dict_kubernetes(self) -> None:
        container, line = _parse_message('{"log":"some log","kubernetes":"not-dict"}')
        assert container == "unknown"
        assert line == "some log"
