from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.cluster_diff_adapter import ClusterDiffAdapter
from hexawyn.adapters.secondary.gitops.critical_cve_adapter import CriticalCveAdapter
from hexawyn.adapters.secondary.gitops.cross_cluster_incident_adapter import (
    CrossClusterIncidentAdapter,
)
from hexawyn.adapters.secondary.gitops.disruption_risk_adapter import DisruptionRiskAdapter
from hexawyn.adapters.secondary.gitops.incident_cost_adapter import IncidentCostAdapter


class TestDisruptionRiskAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_disruption_risks.return_value = []
        adapter = DisruptionRiskAdapter(source=source)
        assert adapter.get_disruption_risks(7) == []
        source.fetch_disruption_risks.assert_called_once_with(7)


class TestCrossClusterIncidentAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_all_cluster_failures.return_value = []
        adapter = CrossClusterIncidentAdapter(source=source)
        assert adapter.list_all_cluster_failures() == []
        source.fetch_all_cluster_failures.assert_called_once()


class TestClusterDiffAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_resource_inventory.return_value = {"resources": [], "cluster_name": "test"}
        adapter = ClusterDiffAdapter(source=source)
        assert adapter.get_resource_inventory("ctx") == {"resources": [], "cluster_name": "test"}
        source.fetch_resource_inventory.assert_called_once_with("ctx")


class TestCriticalCveAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_critical_cves.return_value = []
        adapter = CriticalCveAdapter(source=source)
        assert adapter.get_critical_cves() == []
        source.fetch_critical_cves.assert_called_once()


class TestIncidentCostAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_incident_cost_data.return_value = {"downtime_minutes": 30}
        adapter = IncidentCostAdapter(source=source)
        assert adapter.get_incident_cost_data("yesterday") == {"downtime_minutes": 30}
        source.fetch_incident_cost_data.assert_called_once_with("yesterday")
