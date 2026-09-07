"""RED → GREEN — ConsolidationJob domain service."""

from datetime import datetime
from unittest.mock import MagicMock
from uuid import UUID

from hexawyn.domain.models.consolidation import ConsolidatedKnowledge, ConsolidationConfig
from hexawyn.domain.services.consolidation_job import ConsolidationJob

_PATTERN = (
    "payments-api in payments has been investigated 3 times via crashloop_detector — "
    "review past causes and solutions before investigating again."
)


def _port(
    groups: list[tuple[str, str, str, int]],
    incidents: list[str] | None = None,
) -> MagicMock:
    port = MagicMock()
    port.find_incident_groups.return_value = groups
    port.get_incidents_for_group.return_value = incidents or []
    return port


class TestNoGroups:
    def test_run_returns_empty_when_no_groups(self) -> None:
        port = _port([])
        job = ConsolidationJob(port=port)

        results = job.run(cluster_name="test")

        assert results == []
        port.find_incident_groups.assert_called_once_with(
            config={
                "min_occurrences": 2,
                "similarity_threshold": 0.85,
                "max_age_days": 90,
            },
            cluster_name="test",
        )


class TestRunFiltering:
    def test_skips_group_below_min_occurrences(self) -> None:
        port = _port([("payments", "api", "crashloop", 1)], incidents=["i1"])
        job = ConsolidationJob(port=port, config=ConsolidationConfig(min_occurrences=2))

        results = job.run(cluster_name="test")

        assert results == []
        port.store_knowledge.assert_not_called()

    def test_skips_group_when_fewer_incidents_than_min(self) -> None:
        port = _port([("payments", "api", "crashloop", 3)], incidents=["i1"])
        job = ConsolidationJob(port=port, config=ConsolidationConfig(min_occurrences=2))

        results = job.run(cluster_name="test")

        assert results == []
        port.store_knowledge.assert_not_called()
        port.mark_consolidated.assert_not_called()

    def test_keeps_valid_group_after_below_min_group(self) -> None:
        port = _port(
            [
                ("monitoring", "grafana", "oomkilled", 1),
                ("payments", "api", "crashloop", 3),
            ],
            incidents=["i1", "i2", "i3"],
        )
        job = ConsolidationJob(port=port)

        results = job.run(cluster_name="test")

        assert len(results) == 1
        assert results[0].tool_name == "crashloop"
        assert port.store_knowledge.call_count == 1


class TestConsolidatedValidGroup:
    def test_store_and_return_knowledge_with_exact_values(self) -> None:
        port = _port(
            [("payments", "payments-api", "crashloop_detector", 3)],
            incidents=["i1", "i2", "i3"],
        )
        job = ConsolidationJob(port=port)

        results = job.run(cluster_name="prod-eu")

        assert len(results) == 1
        port.get_incidents_for_group.assert_called_once_with(
            namespace="payments",
            resource_name="payments-api",
            tool_name="crashloop_detector",
            cluster_name="prod-eu",
            max_age_days=90,
        )
        store_kwargs = port.store_knowledge.call_args.kwargs
        assert UUID(store_kwargs["id"]) is not None
        assert store_kwargs["pattern"] == _PATTERN
        assert store_kwargs["resource_name"] == "payments-api"
        assert store_kwargs["namespace"] == "payments"
        assert store_kwargs["tool_name"] == "crashloop_detector"
        assert store_kwargs["cluster_name"] == "prod-eu"
        assert store_kwargs["occurrence_count"] == 3  # noqa: PLR2004
        assert store_kwargs["first_seen"] == store_kwargs["last_seen"]
        parsed = datetime.fromisoformat(store_kwargs["first_seen"])
        assert parsed.tzinfo is not None
        assert store_kwargs["source_incident_ids"] == ["i1", "i2", "i3"]
        assert store_kwargs["weight"] == 2.0  # noqa: PLR2004
        assert store_kwargs["confidence"] == 0.8  # noqa: PLR2004

        knowledge: ConsolidatedKnowledge = results[0]
        assert knowledge.id == store_kwargs["id"]
        assert knowledge.pattern == _PATTERN
        assert knowledge.resource_name == "payments-api"
        assert knowledge.namespace == "payments"
        assert knowledge.tool_name == "crashloop_detector"
        assert knowledge.occurrence_count == 3  # noqa: PLR2004
        assert knowledge.source_incident_ids == ["i1", "i2", "i3"]
        assert knowledge.weight == 2.0  # noqa: PLR2004
        assert knowledge.confidence == 0.8  # noqa: PLR2004

        port.mark_consolidated.assert_called_once_with(
            incident_ids=["i1", "i2", "i3"],
            knowledge_id=store_kwargs["id"],
        )


class TestNamespaceHandling:
    def test_empty_namespace_and_resource_use_sentinels_and_none_fields(self) -> None:
        port = _port([("", "", "crashloop_detector", 2)], incidents=["i1", "i2"])
        job = ConsolidationJob(port=port)

        results = job.run(cluster_name="prod-eu")

        assert len(results) == 1
        port.get_incidents_for_group.assert_called_once_with(
            namespace="_null_",
            resource_name="_null_",
            tool_name="crashloop_detector",
            cluster_name="prod-eu",
            max_age_days=90,
        )
        store_kwargs = port.store_knowledge.call_args.kwargs
        assert store_kwargs["namespace"] is None
        assert store_kwargs["resource_name"] is None
        assert results[0].namespace is None
        assert results[0].resource_name is None


class TestCustomConfiguration:
    def test_configuration_values_forwarded_to_port(self) -> None:
        port = _port([("payments", "api", "crashloop", 3)], incidents=["i1", "i2", "i3"])
        job = ConsolidationJob(
            port=port,
            config=ConsolidationConfig(
                min_occurrences=3, similarity_threshold=0.9, max_age_days=30
            ),
        )

        job.run(cluster_name="prod-eu")

        port.find_incident_groups.assert_called_once_with(
            config={
                "min_occurrences": 3,
                "similarity_threshold": 0.9,
                "max_age_days": 30,
            },
            cluster_name="prod-eu",
        )
        port.get_incidents_for_group.assert_called_once_with(
            namespace="payments",
            resource_name="api",
            tool_name="crashloop",
            cluster_name="prod-eu",
            max_age_days=30,
        )


class TestWeightAndConfidence:
    def test_weight_formula_below_cap(self) -> None:
        port = _port([("ns", "res", "tool", 4)], incidents=["i1", "i2", "i3", "i4"])
        job = ConsolidationJob(port=port)

        knowledge = job.run(cluster_name="test")[0]

        assert knowledge.weight == 2.5  # noqa: PLR2004
        assert port.store_knowledge.call_args.kwargs["weight"] == 2.5  # noqa: PLR2004

    def test_weight_caps_at_five(self) -> None:
        incidents = [f"i{n}" for n in range(10)]
        port = _port([("ns", "res", "tool", 10)], incidents=incidents)
        job = ConsolidationJob(port=port)

        knowledge = job.run(cluster_name="test")[0]

        assert knowledge.weight == 5.0  # noqa: PLR2004
        assert port.store_knowledge.call_args.kwargs["weight"] == 5.0  # noqa: PLR2004

    def test_confidence_formula_below_cap(self) -> None:
        port = _port([("ns", "res", "tool", 4)], incidents=["i1", "i2", "i3", "i4"])
        job = ConsolidationJob(port=port)

        knowledge = job.run(cluster_name="test")[0]

        assert knowledge.confidence == 0.9  # noqa: PLR2004
        assert port.store_knowledge.call_args.kwargs["confidence"] == 0.9  # noqa: PLR2004

    def test_confidence_caps_at_one(self) -> None:
        incidents = [f"i{n}" for n in range(6)]
        port = _port([("ns", "res", "tool", 6)], incidents=incidents)
        job = ConsolidationJob(port=port)

        knowledge = job.run(cluster_name="test")[0]

        assert knowledge.confidence == 1.0  # noqa: PLR2004
        assert port.store_knowledge.call_args.kwargs["confidence"] == 1.0  # noqa: PLR2004


class TestPatternText:
    def test_pattern_includes_namespace_and_tool(self) -> None:
        pattern = ConsolidationJob._build_pattern(
            namespace="payments",
            resource_name="payments-api",
            tool_name="crashloop_detector",
            occurrence_count=3,
        )

        assert pattern == _PATTERN

    def test_pattern_without_namespace(self) -> None:
        pattern = ConsolidationJob._build_pattern(
            namespace="",
            resource_name="db",
            tool_name="oomkilled",
            occurrence_count=2,
        )

        assert pattern == (
            "db has been investigated 2 times via oomkilled — "
            "review past causes and solutions before investigating again."
        )

    def test_pattern_with_unknown_resource(self) -> None:
        pattern = ConsolidationJob._build_pattern(
            namespace="payments",
            resource_name="",
            tool_name="crashloop",
            occurrence_count=2,
        )

        assert pattern == (
            "unknown resource in payments has been investigated 2 times via crashloop — "
            "review past causes and solutions before investigating again."
        )
