from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalPodInfo,
    KubeArchiveResponse,
)
from hexawyn.mcp.tools.query_kubearchive import query_kubearchive


class TestQueryKubeArchiveTool:
    def test_returns_pods_for_namespace(self) -> None:
        mock_kubearchive = MagicMock()
        mock_kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=8,
            pods=[
                HistoricalPodInfo(
                    name="payment-pod-abc",
                    namespace="payment",
                    phase="Running",
                    restart_count=0,
                    queried_timestamp="2026-06-09T10:00:00Z",
                ),
            ],
            kubearchive_available=True,
            error=None,
        )

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter") as mock_k8s,
            patch(
                "hexawyn.adapters.secondary.kubearchive_http_adapter.KubeArchiveHTTPAdapter"
            ) as mock_ka_class,
        ):
            mock_k8s.return_value = MagicMock()
            mock_ka_class.return_value = mock_kubearchive

            result = query_kubearchive(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )

        assert result["error"] is None
        assert isinstance(result["pods"], list)
        assert len(result["pods"]) == 1
        assert result["total_resources"] == 8

    def test_handles_error_gracefully(self) -> None:
        mock_kubearchive = MagicMock()
        mock_kubearchive.query_historical_state.side_effect = RuntimeError("Connection refused")

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter") as mock_k8s,
            patch(
                "hexawyn.adapters.secondary.kubearchive_http_adapter.KubeArchiveHTTPAdapter"
            ) as mock_ka_class,
        ):
            mock_k8s.return_value = MagicMock()
            mock_ka_class.return_value = mock_kubearchive

            result = query_kubearchive(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )

        assert result["error"] is not None
        assert "Connection refused" in str(result["error"])

    def test_with_comparison_mode(self) -> None:
        mock_kubearchive = MagicMock()
        mock_kubearchive.query_historical_state.return_value = KubeArchiveResponse(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=8,
            pods=[
                HistoricalPodInfo(
                    name="payment-pod-abc",
                    namespace="payment",
                    phase="Running",
                    restart_count=0,
                    queried_timestamp="2026-06-09T10:00:00Z",
                ),
            ],
            kubearchive_available=True,
            error=None,
        )

        mock_k8s_adapter = MagicMock()
        mock_k8s_adapter.list_pods.return_value = [
            PodInfo(
                name="payment-pod-abc",
                namespace="payment",
                status="Running",
                restarts=0,
                age="1d",
                node="n1",
            ),
        ]

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter") as mock_k8s_builder,
            patch(
                "hexawyn.adapters.secondary.kubearchive_http_adapter.KubeArchiveHTTPAdapter"
            ) as mock_ka_class,
        ):
            mock_k8s_builder.return_value = mock_k8s_adapter
            mock_ka_class.return_value = mock_kubearchive

            result = query_kubearchive(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
                compare_with_current=True,
            )

        assert result["error"] is None
        assert result["comparison"] is not None

    def test_build_k8s_adapter_failure(self) -> None:
        with (
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                side_effect=RuntimeError("k8s unreachable"),
            ),
            patch(
                "hexawyn.adapters.secondary.kubearchive_http_adapter.KubeArchiveHTTPAdapter"
            ) as mock_ka_class,
        ):
            mock_ka_class.return_value = MagicMock()

            result = query_kubearchive(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )

        assert result["error"] is not None
        assert "k8s unreachable" in str(result["error"])
        assert result["pods"] == []
