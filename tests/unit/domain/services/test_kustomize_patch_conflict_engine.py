"""RED → GREEN — Kustomize Patch Conflict domain logic."""

from hexawyn.domain.services.kustomize_patch_conflict.kustomize_patch_conflict_engine import (
    KustomizePatchConflictEngine,
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
