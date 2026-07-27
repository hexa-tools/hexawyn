from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
    RecurringIncidentAdapter,
)
from hexawyn.application.ports.driven.recurring_incident_port import (
    RecurringIncidentPort,
)

_CFG = "kubernetes.config.load_kube_config"
_API = "kubernetes.client.CoreV1Api"


class TestRecurringIncidentAdapter:
    def test_implements_port(self) -> None:
        adapter = RecurringIncidentAdapter()
        assert isinstance(adapter, RecurringIncidentPort)

    def test_fetch_incidents_returns_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            adapter = RecurringIncidentAdapter()
            result = adapter.fetch_incidents(30)
            assert isinstance(result, list)

    def test_fetch_incidents_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            adapter = RecurringIncidentAdapter()
            result = adapter.fetch_incidents(30)
            assert result == []
