from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest
from hexawyn.adapters.secondary.kubearchive_http_adapter import (
    KubeArchiveHTTPAdapter,
)
from hexawyn.application.ports.driven.kubearchive_port import (
    KubeArchivePort,
    KubeArchiveQuery,
)
from hexawyn.domain.errors import KubeArchiveUnavailableError


class TestKubeArchiveHTTPAdapter:
    def test_implements_kubearchive_port(self) -> None:
        adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
        assert isinstance(adapter, KubeArchivePort)

    def test_query_historical_state_happy_path(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "namespace": "payment",
            "resource_type": "pods",
            "queried_timestamp": "2026-06-09T10:00:00Z",
            "total_resources": 8,
            "items": [
                {
                    "name": "payment-pod-abc",
                    "namespace": "payment",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "2026-06-09T10:00:00Z",
                    "currently_exists": True,
                    "status_changed_since": False,
                },
                {
                    "name": "payment-pod-def",
                    "namespace": "payment",
                    "phase": "Running",
                    "restart_count": 8,
                    "queried_timestamp": "2026-06-09T10:00:00Z",
                    "currently_exists": True,
                    "status_changed_since": False,
                },
            ],
        }

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            query: KubeArchiveQuery = {
                "namespace": "payment",
                "resource_type": "pods",
                "timestamp": "2026-06-09T10:00:00Z",
            }
            result = adapter.query_historical_state(query)

        assert result["total_resources"] == 8
        assert len(result["pods"]) == 2
        assert result["kubearchive_available"] is True
        assert result["error"] is None

    def test_query_empty_namespace(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "namespace": "empty-ns",
            "resource_type": "pods",
            "queried_timestamp": "2026-06-09T10:00:00Z",
            "total_resources": 0,
            "items": [],
        }

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            query: KubeArchiveQuery = {
                "namespace": "empty-ns",
                "resource_type": "pods",
                "timestamp": "2026-06-09T10:00:00Z",
            }
            result = adapter.query_historical_state(query)

        assert result["total_resources"] == 0
        assert result["pods"] == []

    def test_kubearchive_unreachable(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.side_effect = httpx.ConnectError("Connection refused")
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            query: KubeArchiveQuery = {
                "namespace": "payment",
                "resource_type": "pods",
                "timestamp": "t",
            }

            with pytest.raises(KubeArchiveUnavailableError):
                adapter.query_historical_state(query)

    def test_http_error_translated(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Not found", request=MagicMock(), response=MagicMock(status_code=404)
        )

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            query: KubeArchiveQuery = {
                "namespace": "payment",
                "resource_type": "pods",
                "timestamp": "t",
            }

            with pytest.raises(KubeArchiveUnavailableError):
                adapter.query_historical_state(query)

    def test_null_timestamp_data(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "namespace": "payment",
            "resource_type": "pods",
            "queried_timestamp": "2020-01-01T00:00:00Z",
            "total_resources": 0,
            "items": None,
        }

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            query: KubeArchiveQuery = {
                "namespace": "payment",
                "resource_type": "pods",
                "timestamp": "2020-01-01T00:00:00Z",
            }
            result = adapter.query_historical_state(query)

        assert result["total_resources"] == 0
        assert result["pods"] == []

    def test_close_calls_client_close(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            adapter.close()

        mock_client.close.assert_called_once()

    def test_skips_non_dict_items(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "namespace": "ns",
            "resource_type": "pods",
            "queried_timestamp": "t",
            "total_resources": 3,
            "items": [
                {
                    "name": "pod-a",
                    "namespace": "ns",
                    "phase": "Running",
                    "restart_count": 0,
                    "queried_timestamp": "t",
                },
                "not_a_dict",
                {
                    "name": "pod-b",
                    "namespace": "ns",
                    "phase": "Running",
                    "restart_count": 1,
                    "queried_timestamp": "t",
                },
            ],
        }

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = KubeArchiveHTTPAdapter(endpoint="http://localhost:8081")
            query: KubeArchiveQuery = {
                "namespace": "ns",
                "resource_type": "pods",
                "timestamp": "t",
            }
            result = adapter.query_historical_state(query)

        assert len(result["pods"]) == 2
