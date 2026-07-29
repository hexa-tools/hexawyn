from unittest.mock import MagicMock, patch

import httpx
from hexawyn.adapters.secondary.runtime_client import RuntimeClient


class TestRuntimeClientContract:
    def test_post_investigation_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"job_id": "job-42"}
        mock_client.post.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.post_investigation(
                query="why is payments-api crashing?",
                cluster_name="prod-eu",
                provider="vanilla",
            )

        mock_client.post.assert_called_once()
        url = mock_client.post.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/investigations"

    def test_post_investigation_payload_shape(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"job_id": "job-42"}
        mock_client.post.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.post_investigation(
                query="why?",
                cluster_name="prod-eu",
                provider="gcp_gke",
                pods=[{"name": "api-pod", "namespace": "default"}],
            )

        payload = mock_client.post.call_args[1]["json"]
        assert set(payload.keys()) == {"query", "cluster_name", "provider", "pods"}
        assert isinstance(payload["query"], str)
        assert isinstance(payload["cluster_name"], str)
        assert isinstance(payload["provider"], str)
        assert isinstance(payload["pods"], list)
        assert payload["pods"][0]["name"] == "api-pod"

    def test_get_investigation_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"job_id": "job-42", "status": "completed"}
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.get_investigation("job-abc-123")

        mock_client.get.assert_called_once()
        url = mock_client.get.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/investigations/job-abc-123"

    def test_stream_investigation_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = ['data: {"done":true}']
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            list(client.stream_investigation(query="test", cluster_name="prod-eu"))

        mock_client.stream.assert_called_once()
        args = mock_client.stream.call_args
        assert args[0][0] == "POST"
        assert args[0][1] == "http://localhost:8000/api/v1/investigations/stream"

    def test_stream_investigation_payload_shape(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value = mock_stream
        mock_stream.__exit__.return_value = None
        mock_stream.raise_for_status = MagicMock()
        mock_stream.iter_lines.return_value = ['data: {"done":true}']
        mock_client.stream.return_value = mock_stream

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            list(
                client.stream_investigation(
                    query="why?",
                    cluster_name="prod-eu",
                    provider="aws",
                    pods=[{"name": "pod1"}],
                    conversation_history=[{"role": "user", "content": "hi"}],
                )
            )

        payload = mock_client.stream.call_args[1]["json"]
        assert set(payload.keys()) == {
            "query",
            "cluster_name",
            "provider",
            "pods",
            "conversation_history",
        }

    def test_check_quota_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"allowed": True, "used": 0, "limit": 50}
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.check_quota()

        mock_client.get.assert_called_once()
        url = mock_client.get.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/quota"

    def test_increment_quota_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_client.post.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.increment_quota()

        mock_client.post.assert_called_once()
        url = mock_client.post.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/quota/increment"

    def test_startup_scan_url_and_payload_shape(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"health_score": 85}
        mock_client.post.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.startup_scan(
                cluster_name="prod-eu",
                pods=[{"name": "api-pod", "namespace": "default"}],
            )

        mock_client.post.assert_called_once()
        url = mock_client.post.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/startup-scan"
        payload = mock_client.post.call_args[1]["json"]
        assert set(payload.keys()) == {"cluster_name", "pods"}

    def test_list_custom_tools_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = []
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.list_custom_tools()

        mock_client.get.assert_called_once()
        url = mock_client.get.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/custom-tools"

    def test_run_custom_tool_url_and_method(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"result": "ok"}
        mock_client.post.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000")
            client.run_custom_tool("detect_crashloop", {"namespace": "default"})

        mock_client.post.assert_called_once()
        url = mock_client.post.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/custom-tools/detect_crashloop/run"

    def test_headers_include_api_key_when_provided(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"allowed": True}
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000", api_key="sk-test-key")
            client.check_quota()

        headers = mock_client.get.call_args[1]["headers"]
        assert headers["X-API-Key"] == "sk-test-key"

    def test_endpoint_trailing_slash_is_stripped(self) -> None:
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {"job_id": "job-1"}
        mock_client.post.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            client = RuntimeClient(endpoint="http://localhost:8000/")
            client.post_investigation(query="test", cluster_name="c", provider="v")

        url = mock_client.post.call_args[0][0]
        assert url == "http://localhost:8000/api/v1/investigations"
        assert "http://localhost:8000//" not in url
