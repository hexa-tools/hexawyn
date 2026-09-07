"""RED → GREEN — Kustomize Patch Conflict domain logic."""

from hexawyn.domain.models.kustomize_patch_conflict import (
    KustomizePatchConflictReport,
    PatchConflict,
    PatchRedundancy,
    PatchValue,
)
from hexawyn.domain.services.kustomize_patch_conflict.kustomize_patch_conflict_engine import (
    KustomizePatchConflictEngine,
    _as_int_for_sort,
    _field_key,
)


def _patch_field(  # noqa: PLR0913
    field_path: str = "spec.replicas",
    resource: str = "Deployment/payment-service",
    value: str = "2",
    source_file: str = "patches/scale-up.yaml",
    patch_type: str = "strategic_merge",
    order: int = 0,
) -> dict[str, object]:
    return {
        "field_path": field_path,
        "resource": resource,
        "value": value,
        "source_file": source_file,
        "patch_type": patch_type,
        "order": order,
    }


def _base_field(
    field_path: str = "spec.replicas",
    resource: str = "Deployment/payment-service",
    value: str = "1",
) -> dict[str, object]:
    return {
        "field_path": field_path,
        "resource": resource,
        "value": value,
    }


class TestConflictDetection:
    def test_two_patches_same_field_different_values_conflict(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/scale-up.yaml", order=0),
            _patch_field(value="5", source_file="patches/production-replicas.yaml", order=1),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_conflicts == 1
        assert result.patch_conflicts[0].field_path == "spec.replicas"
        assert result.patch_conflicts[0].effective_value == "5"
        assert len(result.patch_conflicts[0].conflicting_values) == 2  # noqa: PLR2004
        assert (
            result.patch_conflicts[0].conflicting_values[0].source_file == "patches/scale-up.yaml"
        )

    def test_same_field_same_value_no_conflict(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/a.yaml", order=0),
            _patch_field(value="2", source_file="patches/b.yaml", order=1),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_conflicts == 0

    def test_multiple_conflicts_across_patches(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(
                field_path="spec.replicas",
                value="2",
                source_file="patches/a.yaml",
                order=0,
            ),
            _patch_field(
                field_path="spec.replicas",
                value="5",
                source_file="patches/b.yaml",
                order=1,
            ),
            _patch_field(
                field_path="spec.template.spec.containers[0].image",
                resource="Deployment/payment-service",
                value="app:v1",
                source_file="patches/a.yaml",
                order=0,
            ),
            _patch_field(
                field_path="spec.template.spec.containers[0].image",
                resource="Deployment/payment-service",
                value="app:v2",
                source_file="patches/c.yaml",
                order=2,
            ),
        ]
        base = [
            _base_field(value="1"),
            _base_field(
                field_path="spec.template.spec.containers[0].image",
                value="app:v0",
            ),
        ]

        result = engine.compute(patches, base)

        assert result.total_conflicts == 2  # noqa: PLR2004

    def test_last_patch_wins(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", order=0),
            _patch_field(value="3", order=1),
            _patch_field(value="5", order=2),
        ]
        base = []

        result = engine.compute(patches, base)

        assert result.patch_conflicts[0].effective_value == "5"

    def test_no_patches_no_conflicts(self) -> None:
        engine = KustomizePatchConflictEngine()

        result = engine.compute([], [])

        assert result.total_conflicts == 0
        assert result.total_redundancies == 0


class TestRedundancyDetection:
    def test_patch_same_value_as_base_redundant(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [_patch_field(value="1", source_file="patches/redundant.yaml")]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_redundancies == 1
        assert result.patch_redundancies[0].field_path == "spec.replicas"
        assert result.patch_redundancies[0].source_file == "patches/redundant.yaml"

    def test_patch_different_from_base_not_redundant(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [_patch_field(value="2")]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_redundancies == 0

    def test_multiple_redundancies(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(
                field_path="spec.replicas",
                value="3",
                source_file="patches/a.yaml",
            ),
            _patch_field(
                field_path="spec.template.spec.containers[0].image",
                resource="Deployment/auth-service",
                value="auth:v1",
                source_file="patches/b.yaml",
            ),
        ]
        base = [
            _base_field(value="3"),
            _base_field(
                field_path="spec.template.spec.containers[0].image",
                resource="Deployment/auth-service",
                value="auth:v1",
            ),
        ]

        result = engine.compute(patches, base)

        assert result.total_redundancies == 2  # noqa: PLR2004

    def test_patch_redundant_from_earlier_patch_not_base(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/a.yaml", order=0),
            _patch_field(value="2", source_file="patches/b.yaml", order=1),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_redundancies == 1
        assert result.patch_redundancies[0].source_file == "patches/b.yaml"


class TestEdgeCases:
    def test_json6902_vs_strategic_merge_distinguished(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(
                value="2", source_file="patches/strategic.yaml", patch_type="strategic_merge"
            ),
            _patch_field(value="5", source_file="patches/json.yaml", patch_type="json6902"),
        ]
        base = []

        result = engine.compute(patches, base)

        assert result.total_conflicts == 1
        types = {v.patch_type for v in result.patch_conflicts[0].conflicting_values}
        assert "strategic_merge" in types
        assert "json6902" in types

    def test_orphan_patch_detected(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(
                resource="Deployment/nonexistent-svc",
                source_file="patches/orphan.yaml",
            ),
        ]
        base = [_base_field(resource="Deployment/payment-service")]

        result = engine.compute(patches, base)

        assert len(result.orphan_patches) == 1
        assert result.orphan_patches[0] == "patches/orphan.yaml"

    def test_deeply_nested_field_path_preserved(self) -> None:
        engine = KustomizePatchConflictEngine()
        deep_path = "spec.template.spec.containers[0].env[name=DB_HOST].value"
        patches = [
            _patch_field(field_path=deep_path, value="db-prod", source_file="a.yaml"),
            _patch_field(field_path=deep_path, value="db-staging", source_file="b.yaml"),
        ]
        base = []

        result = engine.compute(patches, base)

        assert result.patch_conflicts[0].field_path == deep_path

    def test_different_resources_same_field_no_conflict(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(resource="Deployment/payment-service", value="2"),
            _patch_field(resource="Deployment/auth-service", value="5"),
        ]
        base = []

        result = engine.compute(patches, base)

        assert result.total_conflicts == 0

    def test_invalid_order_field_handled(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches: list[dict[str, object]] = [
            {
                "field_path": "spec.replicas",
                "resource": "Deployment/svc",
                "value": "2",
                "source_file": "a.yaml",
                "patch_type": "strategic_merge",
                "order": "bad_value",
            },
            {
                "field_path": "spec.replicas",
                "resource": "Deployment/svc",
                "value": "5",
                "source_file": "b.yaml",
                "patch_type": "strategic_merge",
                "order": "also_bad",
            },
            {
                "field_path": "spec.replicas",
                "resource": "Deployment/svc",
                "value": "6",
                "source_file": "c.yaml",
                "patch_type": "strategic_merge",
                "order": None,
            },
        ]
        base: list[dict[str, object]] = []

        result = engine.compute(patches, base)

        assert result.total_conflicts == 1
        assert result.patch_conflicts[0].effective_value == "6"


class TestFieldKey:
    def test_joins_resource_and_field_path(self) -> None:
        patch = {"resource": "Deployment/payment-service", "field_path": "spec.replicas"}

        assert _field_key(patch) == "Deployment/payment-service:spec.replicas"

    def test_missing_resource_defaults_to_empty_prefix(self) -> None:
        patch = {"field_path": "spec.replicas"}

        assert _field_key(patch) == ":spec.replicas"

    def test_missing_field_path_defaults_to_empty_suffix(self) -> None:
        patch = {"resource": "Deployment/payment-service"}

        assert _field_key(patch) == "Deployment/payment-service:"

    def test_both_missing_defaults_to_single_colon(self) -> None:
        assert _field_key({}) == ":"

    def test_non_string_values_are_stringified(self) -> None:
        patch = {"resource": "Deployment/api", "field_path": "spec.replicas", "extra": 3}

        assert _field_key(patch) == "Deployment/api:spec.replicas"


class TestAsIntForSort:
    def test_none_returns_zero(self) -> None:
        assert _as_int_for_sort(None) == 0

    def test_numeric_string_parsed(self) -> None:
        assert _as_int_for_sort("5") == 5  # noqa: PLR2004

    def test_float_string_truncated(self) -> None:
        assert _as_int_for_sort("5.9") == 5  # noqa: PLR2004

    def test_float_truncated(self) -> None:
        assert _as_int_for_sort(5.9) == 5  # noqa: PLR2004

    def test_int_passthrough(self) -> None:
        assert _as_int_for_sort(7) == 7  # noqa: PLR2004

    def test_negative_string_parsed(self) -> None:
        assert _as_int_for_sort("-3") == -3  # noqa: PLR2004

    def test_non_numeric_string_returns_zero(self) -> None:
        assert _as_int_for_sort("not-a-number") == 0

    def test_bool_returns_int(self) -> None:
        assert _as_int_for_sort(True) == 1


class TestConflictExactFields:
    def test_conflict_all_fields_reported_exactly(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/scale-up.yaml", order=1),
            _patch_field(
                value="5",
                source_file="patches/production-replicas.yaml",
                order=2,
                patch_type="json6902",
            ),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.patch_conflicts == [
            PatchConflict(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                conflicting_values=[
                    PatchValue(
                        source_file="patches/scale-up.yaml",
                        value="2",
                        patch_type="strategic_merge",
                    ),
                    PatchValue(
                        source_file="patches/production-replicas.yaml",
                        value="5",
                        patch_type="json6902",
                    ),
                ],
                effective_value="5",
                severity="warning",
            )
        ]

    def test_conflict_defaults_patch_type_to_strategic_merge(self) -> None:
        engine = KustomizePatchConflictEngine()
        patch_a: dict[str, object] = {
            "resource": "Deployment/payment-service",
            "field_path": "spec.replicas",
            "value": "2",
            "source_file": "patches/a.yaml",
            "order": 0,
        }
        patch_b: dict[str, object] = {
            "resource": "Deployment/payment-service",
            "field_path": "spec.replicas",
            "value": "4",
            "source_file": "patches/b.yaml",
            "order": 1,
        }

        result = engine.compute([patch_a, patch_b], [])

        assert result.patch_conflicts[0].conflicting_values[0].patch_type == "strategic_merge"
        assert result.patch_conflicts[0].conflicting_values[1].patch_type == "strategic_merge"

    def test_conflict_defaults_when_core_keys_missing(self) -> None:
        engine = KustomizePatchConflictEngine()
        minimal_a: dict[str, object] = {"value": "1"}
        minimal_b: dict[str, object] = {"value": "2"}

        result = engine.compute([minimal_a, minimal_b], [])

        assert result.patch_conflicts == [
            PatchConflict(
                field_path="",
                resource="",
                conflicting_values=[
                    PatchValue(source_file="", value="1", patch_type="strategic_merge"),
                    PatchValue(source_file="", value="2", patch_type="strategic_merge"),
                ],
                effective_value="2",
                severity="warning",
            )
        ]

    def test_conflict_value_is_stringified_when_non_string(self) -> None:
        engine = KustomizePatchConflictEngine()
        patch_a: dict[str, object] = {
            "resource": "Deployment/api",
            "field_path": "spec.replicas",
            "value": 2,
            "source_file": "patches/a.yaml",
            "order": 0,
        }
        patch_b: dict[str, object] = {
            "resource": "Deployment/api",
            "field_path": "spec.replicas",
            "value": 3,
            "source_file": "patches/b.yaml",
            "order": 1,
        }

        result = engine.compute([patch_a, patch_b], [])

        assert result.patch_conflicts[0].conflicting_values[0].value == "2"
        assert result.patch_conflicts[0].effective_value == "3"

    def test_same_value_patches_do_not_conflict_even_with_base_present(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/a.yaml", order=0),
            _patch_field(value="2", source_file="patches/b.yaml", order=1),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_conflicts == 0

    def test_empty_effective_value_when_last_patch_lacks_value(self) -> None:
        engine = KustomizePatchConflictEngine()
        patch_a = _patch_field(value="2", source_file="patches/a.yaml", order=0)
        patch_b: dict[str, object] = {
            "resource": "Deployment/payment-service",
            "field_path": "spec.replicas",
            "source_file": "patches/no-value.yaml",
            "order": 1,
        }

        result = engine.compute([patch_a, patch_b], [])

        assert result.patch_conflicts == [
            PatchConflict(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                conflicting_values=[
                    PatchValue(
                        source_file="patches/a.yaml",
                        value="2",
                        patch_type="strategic_merge",
                    ),
                    PatchValue(
                        source_file="patches/no-value.yaml",
                        value="",
                        patch_type="strategic_merge",
                    ),
                ],
                effective_value="",
                severity="warning",
            )
        ]


class TestRedundancyExactFields:
    def test_base_redundancy_all_fields_reported_exactly(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [_patch_field(value="1", source_file="patches/redundant.yaml", order=3)]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.patch_redundancies == [
            PatchRedundancy(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                base_value="1",
                patch_value="1",
                source_file="patches/redundant.yaml",
                severity="informational",
            )
        ]

    def test_earlier_patch_redundancy_all_fields_reported_exactly(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/a.yaml", order=0),
            _patch_field(value="2", source_file="patches/b.yaml", order=1),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.patch_redundancies == [
            PatchRedundancy(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                base_value="",
                patch_value="2",
                source_file="patches/b.yaml",
                severity="informational",
            )
        ]

    def test_earlier_patch_redundancy_defaults_when_core_keys_missing(self) -> None:
        engine = KustomizePatchConflictEngine()
        minimal_a: dict[str, object] = {"value": "1"}
        minimal_b: dict[str, object] = {"value": "1"}

        result = engine.compute([minimal_a, minimal_b], [])

        assert result.patch_redundancies == [
            PatchRedundancy(
                field_path="",
                resource="",
                base_value="",
                patch_value="1",
                source_file="",
                severity="informational",
            )
        ]

    def test_base_redundancy_when_core_keys_missing(self) -> None:
        engine = KustomizePatchConflictEngine()
        base: list[dict[str, object]] = [{"value": "1"}]
        patches: list[dict[str, object]] = [{"value": "1"}]

        result = engine.compute(patches, base)

        assert result.patch_redundancies == [
            PatchRedundancy(
                field_path="",
                resource="",
                base_value="1",
                patch_value="1",
                source_file="",
                severity="informational",
            )
        ]

    def test_base_redundancy_when_base_and_patch_values_default_empty(self) -> None:
        engine = KustomizePatchConflictEngine()
        base: list[dict[str, object]] = [{}]
        patches: list[dict[str, object]] = [{}]

        result = engine.compute(patches, base)

        assert result.patch_redundancies == [
            PatchRedundancy(
                field_path="",
                resource="",
                base_value="",
                patch_value="",
                source_file="",
                severity="informational",
            )
        ]

    def test_earlier_patch_redundancy_when_earlier_lacks_value(self) -> None:
        engine = KustomizePatchConflictEngine()
        patch_a: dict[str, object] = {
            "resource": "Deployment/payment-service",
            "field_path": "spec.replicas",
            "source_file": "patches/a.yaml",
            "order": 0,
        }
        patch_b: dict[str, object] = {
            "resource": "Deployment/payment-service",
            "field_path": "spec.replicas",
            "value": "",
            "source_file": "patches/b.yaml",
            "order": 1,
        }

        result = engine.compute([patch_a, patch_b], [])

        assert result.patch_redundancies == [
            PatchRedundancy(
                field_path="spec.replicas",
                resource="Deployment/payment-service",
                base_value="",
                patch_value="",
                source_file="patches/b.yaml",
                severity="informational",
            )
        ]

    def test_three_identical_patches_flag_each_later_duplicate(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/a.yaml", order=0),
            _patch_field(value="2", source_file="patches/b.yaml", order=1),
            _patch_field(value="2", source_file="patches/c.yaml", order=2),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_redundancies == 2  # noqa: PLR2004
        assert [r.source_file for r in result.patch_redundancies] == [
            "patches/b.yaml",
            "patches/c.yaml",
        ]


class TestOrphanBoundaries:
    def test_patch_on_resource_present_in_base_is_not_orphan(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(resource="Deployment/payment-service", source_file="patches/kept.yaml")
        ]
        base = [_base_field()]

        result = engine.compute(patches, base)

        assert result.orphan_patches == []

    def test_duplicate_orphan_source_deduplicated(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(resource="Deployment/missing-a", source_file="patches/orphan.yaml"),
            _patch_field(resource="Deployment/missing-b", source_file="patches/orphan.yaml"),
        ]
        base = [_base_field()]

        result = engine.compute(patches, base)

        assert result.orphan_patches == ["patches/orphan.yaml"]

    def test_empty_resource_is_not_orphan(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [_patch_field(resource="", source_file="patches/blank.yaml")]
        base = []

        result = engine.compute(patches, base)

        assert result.orphan_patches == []

    def test_missing_source_file_defaults_to_empty_string(self) -> None:
        engine = KustomizePatchConflictEngine()
        patch: dict[str, object] = {
            "resource": "Deployment/missing-c",
            "field_path": "spec.replicas",
            "value": "2",
        }

        result = engine.compute([patch], [])

        assert result.orphan_patches == [""]

    def test_patch_without_resource_key_is_not_orphan(self) -> None:
        engine = KustomizePatchConflictEngine()
        patch: dict[str, object] = {
            "field_path": "spec.replicas",
            "value": "2",
            "source_file": "patches/no-resource.yaml",
        }

        result = engine.compute([patch], [])

        assert result.orphan_patches == []


class TestSortingBoundaries:
    def test_effective_value_uses_numeric_order_across_types(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="a", order="10"),
            _patch_field(value="b", order="2.9"),
            _patch_field(value="c", order=None),
        ]
        base = []

        result = engine.compute(patches, base)

        assert result.patch_conflicts[0].effective_value == "a"

    def test_effective_value_uses_negative_order_first(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="early", order=-5),
            _patch_field(value="late", order=0),
        ]
        base = []

        result = engine.compute(patches, base)

        assert result.patch_conflicts[0].effective_value == "late"


class TestFullReportAggregation:
    def test_mixed_scenario_aggregates_all_counts(self) -> None:
        engine = KustomizePatchConflictEngine()
        patches = [
            _patch_field(value="2", source_file="patches/scale.yaml", order=0),
            _patch_field(value="5", source_file="patches/prod.yaml", order=1),
            _patch_field(value="1", source_file="patches/redundant-with-base.yaml", order=2),
        ]
        base = [_base_field(value="1")]

        result = engine.compute(patches, base)

        assert result.total_conflicts == 1
        assert result.total_redundancies == 1
        assert isinstance(result, KustomizePatchConflictReport)
        assert result.orphan_patches == []

    def test_empty_patches_reuse_default_report(self) -> None:
        engine = KustomizePatchConflictEngine()

        result = engine.compute([], [_base_field()])

        assert result == KustomizePatchConflictReport()
