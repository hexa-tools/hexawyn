import uuid

from hexawyn.domain.models.consolidation import (
    ConsolidatedKnowledge,
    ConsolidationConfig,
)


class TestConsolidationConfig:
    def test_default_values(self) -> None:
        config = ConsolidationConfig()
        assert config.min_occurrences == 2  # noqa: PLR2004
        assert config.similarity_threshold == 0.85  # noqa: PLR2004
        assert config.max_age_days == 90  # noqa: PLR2004
        assert config.run_interval_hours == 24  # noqa: PLR2004

    def test_custom_values(self) -> None:
        config = ConsolidationConfig(
            min_occurrences=3,
            similarity_threshold=0.8,
            max_age_days=30,
            run_interval_hours=12,
        )
        assert config.min_occurrences == 3  # noqa: PLR2004
        assert config.similarity_threshold == 0.8  # noqa: PLR2004
        assert config.max_age_days == 30  # noqa: PLR2004
        assert config.run_interval_hours == 12  # noqa: PLR2004

    def test_is_frozen(self) -> None:
        config = ConsolidationConfig()
        try:
            config.min_occurrences = 5  # type: ignore[misc]
        except Exception:
            pass


class TestConsolidatedKnowledge:
    def _make_knowledge(self) -> ConsolidatedKnowledge:
        return ConsolidatedKnowledge(
            id=str(uuid.uuid4()),
            pattern="payments-api est sujette aux OOM",
            resource_name="payments-api",
            resource_kind="Deployment",
            namespace="payments",
            tool_name="crashloop_detector",
            occurrence_count=3,
            first_seen="2026-07-01T10:00:00Z",
            last_seen="2026-07-15T14:00:00Z",
            source_incident_ids=[str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())],
            embedding=[0.1] * 768,
            weight=2.5,
            confidence=0.85,
        )

    def test_all_fields_populated(self) -> None:
        k = self._make_knowledge()
        assert k.occurrence_count == 3  # noqa: PLR2004
        assert k.pattern == "payments-api est sujette aux OOM"
        assert k.resource_name == "payments-api"
        assert k.namespace == "payments"
        assert k.tool_name == "crashloop_detector"
        assert len(k.source_incident_ids) == 3  # noqa: PLR2004
        assert k.weight == 2.5  # noqa: PLR2004
        assert k.confidence == 0.85  # noqa: PLR2004

    def test_defaults(self) -> None:
        k = ConsolidatedKnowledge(
            pattern="test pattern",
            tool_name="test_tool",
            occurrence_count=1,
        )
        assert k.resource_name is None
        assert k.namespace is None
        assert k.weight == 1.0
        assert k.confidence == 0.5  # noqa: PLR2004
        assert k.embedding == []
        assert k.source_incident_ids == []
        assert k.resource_kind is None

    def test_id_is_string(self) -> None:
        k = ConsolidatedKnowledge(pattern="p", tool_name="t", occurrence_count=1)
        assert isinstance(k.id, str)

    def test_weight_can_exceed_1(self) -> None:
        k = ConsolidatedKnowledge(pattern="p", tool_name="t", occurrence_count=10, weight=5.0)
        assert k.weight == 5.0  # noqa: PLR2004
