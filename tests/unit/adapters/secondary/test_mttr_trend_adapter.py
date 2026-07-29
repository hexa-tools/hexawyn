from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import MTTRTrendAdapter
from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort

_CFG = "kubernetes.config.load_kube_config"
_API = "kubernetes.client.CoreV1Api"


class TestMTTRTrendAdapter:
    def test_implements_port(self) -> None:
        adapter = MTTRTrendAdapter()
        assert isinstance(adapter, MTTRTrendPort)

    def test_fetch_incidents_by_month_returns_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            adapter = MTTRTrendAdapter()
            result = adapter.fetch_incidents_by_month("2026-07")
            assert isinstance(result, list)

    def test_fetch_incidents_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            adapter = MTTRTrendAdapter()
            result = adapter.fetch_incidents_by_month("2026-07")
            assert result == []
