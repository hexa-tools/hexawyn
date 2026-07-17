"""Tests for ConsolidationJob domain service."""

from unittest.mock import MagicMock

from hexawyn.domain.models.consolidation import ConsolidationConfig
from hexawyn.domain.services.consolidation_job import ConsolidationJob


class TestConsolidationJob:
    def _make_port(self, groups=None, incident_ids=None):
        port = MagicMock()
        port.find_incident_groups.return_value = groups or []
        port.get_incidents_for_group.return_value = incident_ids or []
        port.store_knowledge.return_value = None
        port.mark_consolidated.return_value = None
        return port

    def test_run_returns_empty_when_no_groups(self) -> None:
        port = self._make_port(groups=[])
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert results == []

    def test_run_skips_groups_below_min_occurrences(self) -> None:
        port = self._make_port(
            groups=[("payments", "api", "crashloop", 1)],
        )
        config = ConsolidationConfig(min_occurrences=2)
        job = ConsolidationJob(port=port, config=config)
        results = job.run(cluster_name="test")
        assert results == []

    def test_run_consolidates_valid_group(self) -> None:
        port = self._make_port(
            groups=[("payments", "payments-api", "crashloop_detector", 3)],
            incident_ids=["i1", "i2", "i3"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="prod-eu")

        assert len(results) == 1
        assert results[0].occurrence_count == 3
        assert results[0].tool_name == "crashloop_detector"
        port.store_knowledge.assert_called_once()
        port.mark_consolidated.assert_called_once()

    def test_run_handles_multiple_groups(self) -> None:
        port = self._make_port(
            groups=[
                ("payments", "api", "crashloop", 3),
                ("monitoring", "grafana", "oomkilled", 2),
            ],
            incident_ids=["i1", "i2"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="prod-eu")

        assert len(results) == 2
        assert port.store_knowledge.call_count == 2

    def test_weight_caps_at_5(self) -> None:
        port = self._make_port(
            groups=[("ns", "res", "tool", 20)],
            incident_ids=["i1"] * 20,
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert results[0].weight == 5.0

    def test_confidence_caps_at_1(self) -> None:
        port = self._make_port(
            groups=[("ns", "res", "tool", 10)],
            incident_ids=["i1"] * 10,
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert results[0].confidence <= 1.0

    def test_build_pattern_includes_namespace(self) -> None:
        pattern = ConsolidationJob._build_pattern(
            namespace="payments",
            resource_name="api",
            tool_name="crashloop",
            occurrence_count=3,
        )
        assert "payments" in pattern
        assert "api" in pattern
        assert "3 times" in pattern

    def test_build_pattern_without_namespace(self) -> None:
        pattern = ConsolidationJob._build_pattern(
            namespace="",
            resource_name="db",
            tool_name="oomkilled",
            occurrence_count=2,
        )
        assert "db" in pattern
        assert "2 times" in pattern

    def test_run_skips_when_incident_ids_below_threshold(self) -> None:
        port = self._make_port(
            groups=[("ns", "res", "tool", 3)],
            incident_ids=["i1"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert results == []
        port.store_knowledge.assert_not_called()

    def test_run_handles_mixed_valid_and_invalid_groups(self) -> None:
        port = self._make_port(
            groups=[
                ("ns1", "res1", "tool1", 3),
                ("ns2", "res2", "tool2", 1),
            ],
            incident_ids=["i1", "i2", "i3"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert len(results) == 1

    def test_run_with_empty_namespace_and_resource(self) -> None:
        port = self._make_port(
            groups=[("", "", "crashloop_detector", 2)],
            incident_ids=["i1", "i2"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="prod-eu")
        assert len(results) == 1
        call_kwargs = port.store_knowledge.call_args[1]
        assert call_kwargs["namespace"] is None
        assert call_kwargs["resource_name"] is None

    def test_weight_formula(self) -> None:
        port = self._make_port(
            groups=[("ns", "res", "tool", 4)],
            incident_ids=["i1", "i2", "i3", "i4"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert results[0].weight == 1.0 + (4 - 1) * 0.5

    def test_confidence_formula(self) -> None:
        port = self._make_port(
            groups=[("ns", "res", "tool", 3)],
            incident_ids=["i1", "i2", "i3"],
        )
        job = ConsolidationJob(port=port)
        results = job.run(cluster_name="test")
        assert results[0].confidence == 0.5 + 3 * 0.1
