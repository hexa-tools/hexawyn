import json
from unittest.mock import MagicMock, patch

import httpx
from hexawyn.adapters.secondary.runtime_client import RuntimeClient


def _mock_response_raw(status_code: int) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.headers = {}
    return resp


def _mock_response(status_code: int, json_data: dict[str, object]) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.json.return_value = json_data
    resp.raise_for_status = MagicMock()
    if status_code >= 400:
        resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            "error", request=MagicMock(), response=resp
        )
    return resp


class TestRuntimeClient:
    def test_post_investigation_returns_job_id(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.post.return_value = _mock_response(200, {"job_id": "job-abc-123"})

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            job_id = client.post_investigation(
                query="why is payments-api crashing?",
                cluster_name="prod-eu",
                provider="vanilla",
            )

        assert job_id == "job-abc-123"
        mock_client.post.assert_called_once()
        request_body = mock_client.post.call_args[1]["json"]
        assert request_body["query"] == "why is payments-api crashing?"
        assert request_body["cluster_name"] == "prod-eu"
        assert request_body["provider"] == "vanilla"

    def test_get_investigation_returns_raw_response(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            200,
            {
                "job_id": "job-abc-123",
                "status": "completed",
                "result": {"answer": "OOMKilled", "status": "complete"},
            },
        )

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            data = client.get_investigation("job-abc-123")

        assert data["status"] == "completed"
        assert data["result"] is not None

    def test_poll_investigation_waits_for_completed(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        call_count = [0]

        def mock_get(*args: object, **kwargs: object) -> MagicMock:
            call_count[0] += 1
            if call_count[0] < 3:
                return _mock_response(
                    200,
                    {"job_id": "job-1", "status": "running", "result": None},
                )
            return _mock_response(
                200,
                {
                    "job_id": "job-1",
                    "status": "completed",
                    "result": {"answer": "done", "status": "complete"},
                },
            )

        mock_client.get.side_effect = mock_get

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            result = client.poll_investigation("job-1", timeout=10.0, interval=0.01)

        assert result["status"] == "completed"
        assert call_count[0] == 3

    def test_poll_investigation_returns_failed_status(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            200,
            {
                "job_id": "job-1",
                "status": "failed",
                "result": {"error": "cluster unreachable"},
            },
        )

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            result = client.poll_investigation("job-1", timeout=5.0, interval=0.01)

        assert result["status"] == "failed"

    def test_poll_investigation_timeout_returns_last_status(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            200,
            {"job_id": "job-1", "status": "running", "result": None},
        )

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            result = client.poll_investigation("job-1", timeout=0.05, interval=0.01)

        assert result["status"] == "running"

    def test_client_closes_httpx_on_context_exit(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.close()

        mock_client.close.assert_called_once()

    def test_post_investigation_http_error_propagates(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.post.side_effect = httpx.ConnectError("connection refused")

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.post_investigation("test", "cluster", "vanilla")
            except httpx.ConnectError as exc:
                assert "connection refused" in str(exc)
            else:
                assert False, "Expected ConnectError"

    def test_check_quota_returns_data(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            200, {"allowed": True, "used": 5, "limit": 50}
        )

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            result = client.check_quota()

        assert result["allowed"] is True

    def test_increment_quota_calls_post(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.post.return_value = _mock_response(200, {"status": "ok"})

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.increment_quota()

        mock_client.post.assert_called_once()

    def test_stream_investigation_yields_events(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = [
            'data: {"node":"plan","output":{"intent":"diagnose"}}',
            'data: {"node":"execute","output":{"result":"ok"}}',
            'data: {"done":true}',
        ]
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            events = list(client.stream_investigation(query="test query"))

        assert len(events) == 2
        assert events[0] == ("plan", {"intent": "diagnose"})

    def test_stream_investigation_handles_error_event(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = [
            'data: {"error":"connection lost"}',
        ]
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            events = list(client.stream_investigation(query="test query"))

        assert len(events) == 1
        assert events[0][0] == "error"

    def test_stream_investigation_skips_invalid_json(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = [
            "data: not-json!!!",
            'data: {"node":"plan","output":{"intent":"diagnose"}}',
        ]
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            events = list(client.stream_investigation(query="test query"))

        assert len(events) == 1

    def test_stream_investigation_skips_non_data_lines(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = [
            "event: ping",
            'data: {"node":"plan","output":{"intent":"diagnose"}}',
        ]
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            events = list(client.stream_investigation(query="test query"))

        assert len(events) == 1

    def test_close_calls_httpx_close(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.close()
        mock_client.close.assert_called_once()

    def test_post_investigation_http_401_raises_http_status_error(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.post.return_value = _mock_response(401, {"detail": "Invalid API key"})

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.post_investigation("test", "cluster", "vanilla")
            except httpx.HTTPStatusError as exc:
                assert exc.response.status_code == 401
            else:
                raise AssertionError("Expected HTTPStatusError")

    def test_post_investigation_http_500_raises_http_status_error(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.post.return_value = _mock_response(500, {"detail": "Internal server error"})

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.post_investigation("test", "cluster", "vanilla")
            except httpx.HTTPStatusError as exc:
                assert exc.response.status_code == 500
            else:
                raise AssertionError("Expected HTTPStatusError")

    def test_get_investigation_http_503_raises_http_status_error(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(503, {"detail": "Service unavailable"})

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.get_investigation("job-1")
            except httpx.HTTPStatusError as exc:
                assert exc.response.status_code == 503
            else:
                raise AssertionError("Expected HTTPStatusError")

    def test_post_investigation_read_timeout_propagates(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.post.side_effect = httpx.ReadTimeout("read timed out")

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.post_investigation("test", "cluster", "vanilla")
            except httpx.ReadTimeout as exc:
                assert "read timed out" in str(exc)
            else:
                raise AssertionError("Expected ReadTimeout")

    def test_check_quota_http_429_raises_http_status_error(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(429, {"detail": "Rate limit exceeded"})

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.check_quota()
            except httpx.HTTPStatusError as exc:
                assert exc.response.status_code == 429
            else:
                raise AssertionError("Expected HTTPStatusError")

    def test_post_investigation_invalid_json_raises_error(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.status_code = 200
        mock_resp.raise_for_status = MagicMock()
        mock_resp.json.side_effect = json.JSONDecodeError("Expecting value", "not json", 0)
        mock_client.post.return_value = mock_resp

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                client.post_investigation("test", "cluster", "vanilla")
            except json.JSONDecodeError:
                pass
            else:
                raise AssertionError("Expected JSONDecodeError")

    def test_stream_investigation_http_500_before_stream_raises(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Internal Server Error",
            request=MagicMock(),
            response=_mock_response_raw(500),
        )
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")

            try:
                list(client.stream_investigation(query="test query"))
            except httpx.HTTPStatusError as exc:
                assert exc.response.status_code == 500
            else:
                raise AssertionError("Expected HTTPStatusError")

    def test_stream_with_pods_and_history(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = [
            'data: {"node":"plan","output":{}}',
            'data: {"done":true}',
        ]
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            events = list(
                client.stream_investigation(
                    query="test",
                    pods=[{"name": "pod1"}],
                    conversation_history=[{"role": "user", "content": "hi"}],
                )
            )
        assert len(events) == 1
