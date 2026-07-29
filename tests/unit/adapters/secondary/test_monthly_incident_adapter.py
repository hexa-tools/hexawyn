from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
    MonthlyIncidentAdapter,
)
from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort

_CFG = "kubernetes.config.load_kube_config"
_API = "kubernetes.client.CoreV1Api"


class TestMonthlyIncidentAdapter:
    def test_implements_port(self) -> None:
        adapter = MonthlyIncidentAdapter()
        assert isinstance(adapter, MonthlyIncidentPort)

    def test_fetch_incidents_returns_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            adapter = MonthlyIncidentAdapter()
            result = adapter.fetch_incidents("2026-07")
            assert isinstance(result, list)

    def test_fetch_incidents_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            adapter = MonthlyIncidentAdapter()
            result = adapter.fetch_incidents("2026-07")
            assert result == []
