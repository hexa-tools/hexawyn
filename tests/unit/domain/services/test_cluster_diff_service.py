from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterInventoryData,
    ResourceInventoryRaw,
)
from hexawyn.domain.models.cluster_diff import ResourceDiff
from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
    _is_secret,
    _missing,
    compute_diff,
)


def _make_resource(  # noqa: PLR0913
    kind: str = "Deployment",
    name: str = "api-gateway",
    namespace: str = "prod",
    image_tag: str = "v1.2.3",
    replicas: int = 3,
    is_secret: bool = False,
) -> ResourceInventoryRaw:
    return {
        "kind": kind,
        "name": name,
        "namespace": namespace,
        "image_tag": image_tag,
        "replicas": replicas,
        "is_secret": is_secret,
    }


def _make_inventory(
    cluster_name: str = "staging",
    resources: list[ResourceInventoryRaw] | None = None,
) -> ClusterInventoryData:
    return {
        "cluster_name": cluster_name,
        "resources": resources or [],
    }


class TestComputeDiff:
    def test_happy_path_in_sync(self) -> None:
        staging = _make_inventory(
            cluster_name="staging-us",
            resources=[
                _make_resource(name="api-gateway", namespace="ns1", image_tag="v1.0", replicas=3),
            ],
        )
        prod = _make_inventory(
            cluster_name="prod-us",
            resources=[
                _make_resource(name="api-gateway", namespace="ns1", image_tag="v1.0", replicas=3),
            ],
        )

        result = compute_diff(staging, prod)

        assert result.source_cluster == "staging-us"
        assert result.target_cluster == "prod-us"
        assert result.sync_status == "in_sync"
        assert result.total_differences == 0
        assert result.has_data is True
        assert len(result.in_staging_not_prod) == 0
        assert len(result.version_mismatches) == 0
        assert len(result.prod_only) == 0

    def test_missing_resource_in_prod(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="new-service", namespace="ns1")],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.sync_status == "out_of_sync"
        assert len(result.in_staging_not_prod) == 1
        assert result.in_staging_not_prod[0].reason == "never_promoted"
        assert result.in_staging_not_prod[0].priority == "blocking"

    def test_missing_secret_in_prod_marks_manual(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(kind="Secret", name="db-pass", namespace="ns1", is_secret=True),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod[0].reason == "secret_manual"

    def test_version_mismatch_image_tag(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v2.0")],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0")],
        )

        result = compute_diff(staging, prod)

        assert len(result.version_mismatches) == 1
        assert result.version_mismatches[0].reason == "version_mismatch"
        assert result.version_mismatches[0].priority == "blocking"
        assert result.version_mismatches[0].staging_value == "v2.0"
        assert result.version_mismatches[0].prod_value == "v1.0"

    def test_version_mismatch_replicas(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(name="api", namespace="ns1", image_tag="v1.0", replicas=5),
            ],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[
                _make_resource(name="api", namespace="ns1", image_tag="v1.0", replicas=3),
            ],
        )

        result = compute_diff(staging, prod)

        assert len(result.version_mismatches) == 1
        assert result.version_mismatches[0].reason == "version_mismatch"
        assert result.version_mismatches[0].priority == "informational"

    def test_prod_only_resource(self) -> None:
        staging = _make_inventory(cluster_name="staging")
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="extra-service", namespace="ns1")],
        )

        result = compute_diff(staging, prod)

        assert len(result.prod_only) == 1
        assert result.prod_only[0].priority == "informational"

    def test_promotion_checklist_ready(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(name="svc-a", namespace="ns1"),
                _make_resource(name="svc-b", namespace="ns1"),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert len(result.promotion_checklist.ready_to_promote) == 2  # noqa: PLR2004
        assert len(result.promotion_checklist.requires_review) == 0

    def test_secrets_not_in_ready_to_promote(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(kind="Secret", name="db-pass", namespace="ns1", is_secret=True),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert len(result.promotion_checklist.ready_to_promote) == 0
        assert len(result.in_staging_not_prod) == 1

    def test_version_mismatches_in_review(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v2.0")],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0")],
        )

        result = compute_diff(staging, prod)

        assert len(result.promotion_checklist.requires_review) == 1

    def test_empty_inventories(self) -> None:
        staging = _make_inventory(cluster_name="staging")
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.sync_status == "in_sync"
        assert result.total_differences == 0

    def test_multiple_kinds_same_name(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(kind="Deployment", name="api", namespace="ns1", image_tag="v1.0"),
                _make_resource(kind="Service", name="api", namespace="ns1"),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert len(result.in_staging_not_prod) == 2  # noqa: PLR2004
        assert result.total_differences == 2  # noqa: PLR2004


class TestMissingExact:
    def test_never_promoted_full_equality(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(kind="Deployment", name="api", namespace="ns1", image_tag="v2.0"),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod == [
            ResourceDiff(
                resource="Deployment/api",
                namespace="ns1",
                reason="never_promoted",
                priority="blocking",
                staging_value="v2.0",
                prod_value="",
                detail="Resource present in staging, absent in production",
            )
        ]

    def test_secret_manual_full_equality(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(kind="Secret", name="db-pass", namespace="ns1", is_secret=True),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod == [
            ResourceDiff(
                resource="Secret/db-pass",
                namespace="ns1",
                reason="secret_manual",
                priority="blocking",
                staging_value="v1.2.3",
                prod_value="",
                detail="Secret requires manual promotion",
            )
        ]

    def test_missing_image_tag_defaults_to_empty(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[{"kind": "Deployment", "name": "svc", "namespace": "ns1"}],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod[0].staging_value == ""
        assert result.in_staging_not_prod[0].resource == "Deployment/svc"

    def test_missing_is_secret_defaults_to_not_secret(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[{"kind": "ConfigMap", "name": "cfg", "namespace": "ns1"}],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod[0].reason == "never_promoted"
        assert result.in_staging_not_prod[0].detail == (
            "Resource present in staging, absent in production"
        )

    def test_missing_default_priority_when_arg_omitted(self) -> None:
        resources = [
            {"kind": "Deployment", "name": "svc", "namespace": "ns1", "image_tag": "v1"},
        ]

        diffs = _missing(resources, {})

        assert diffs == [
            ResourceDiff(
                resource="Deployment/svc",
                namespace="ns1",
                reason="never_promoted",
                priority="blocking",
                staging_value="v1",
                prod_value="",
                detail="Resource present in staging, absent in production",
            )
        ]


class TestVersionMismatchExact:
    def test_image_mismatch_full_equality(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v2.0")],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0")],
        )

        result = compute_diff(staging, prod)

        assert result.version_mismatches == [
            ResourceDiff(
                resource="Deployment/api",
                namespace="ns1",
                reason="version_mismatch",
                priority="blocking",
                staging_value="v2.0",
                prod_value="v1.0",
                detail="Image version differs: staging=v2.0, prod=v1.0",
            )
        ]

    def test_replicas_mismatch_full_equality(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0", replicas=5)],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0", replicas=3)],
        )

        result = compute_diff(staging, prod)

        assert result.version_mismatches == [
            ResourceDiff(
                resource="Deployment/api",
                namespace="ns1",
                reason="version_mismatch",
                priority="informational",
                staging_value="5",
                prod_value="3",
                detail="Replica count differs: staging=5, prod=3",
            )
        ]

    def test_image_tag_missing_on_staging_defaults_empty(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[{"kind": "Deployment", "name": "api", "namespace": "ns1"}],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0")],
        )

        result = compute_diff(staging, prod)

        assert result.version_mismatches == [
            ResourceDiff(
                resource="Deployment/api",
                namespace="ns1",
                reason="version_mismatch",
                priority="blocking",
                staging_value="",
                prod_value="v1.0",
                detail="Image version differs: staging=, prod=v1.0",
            )
        ]

    def test_image_tag_missing_on_prod_defaults_empty(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0")],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[{"kind": "Deployment", "name": "api", "namespace": "ns1"}],
        )

        result = compute_diff(staging, prod)

        assert result.version_mismatches[0].staging_value == "v1.0"
        assert result.version_mismatches[0].prod_value == ""
        assert result.version_mismatches[0].detail == "Image version differs: staging=v1.0, prod="

    def test_replicas_missing_on_staging_defaults_zero(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                {"kind": "Deployment", "name": "api", "namespace": "ns1", "image_tag": "v1.0"}
            ],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0", replicas=5)],
        )

        result = compute_diff(staging, prod)

        assert result.version_mismatches[0].priority == "informational"
        assert result.version_mismatches[0].staging_value == "0"
        assert result.version_mismatches[0].prod_value == "5"

    def test_replicas_missing_on_prod_defaults_zero(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0", replicas=5)],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[
                {"kind": "Deployment", "name": "api", "namespace": "ns1", "image_tag": "v1.0"}
            ],
        )

        result = compute_diff(staging, prod)

        assert result.version_mismatches[0].staging_value == "5"
        assert result.version_mismatches[0].prod_value == "0"

    def test_staging_only_resource_does_not_break_later_mismatch(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(name="only-in-staging", namespace="ns1", image_tag="v1.0"),
                _make_resource(name="api", namespace="ns1", image_tag="v2.0"),
            ],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="api", namespace="ns1", image_tag="v1.0")],
        )

        result = compute_diff(staging, prod)

        assert len(result.version_mismatches) == 1
        assert result.version_mismatches[0].resource == "Deployment/api"


class TestSecretWithoutFlag:
    """Category: absence/vide × invariant — a Secret resource whose ``is_secret``
    flag is absent must never be auto-promotable."""

    def test_secret_kind_without_flag_marked_manual(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[{"kind": "Secret", "name": "db-pass", "namespace": "ns1"}],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod[0].reason == "secret_manual"
        assert result.in_staging_not_prod[0].detail == "Secret requires manual promotion"

    def test_secret_kind_without_flag_not_ready_to_promote(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[{"kind": "Secret", "name": "db-pass", "namespace": "ns1"}],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.promotion_checklist.ready_to_promote == []
        assert result.in_staging_not_prod[0].reason == "secret_manual"

    def test_secret_kind_with_false_flag_still_manual(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(kind="Secret", name="db-pass", namespace="ns1", is_secret=False),
            ],
        )
        prod = _make_inventory(cluster_name="prod")

        result = compute_diff(staging, prod)

        assert result.in_staging_not_prod[0].reason == "secret_manual"


class TestIsSecretHelper:
    def test_flag_true_wins_for_any_kind(self) -> None:
        resource = {"kind": "Deployment", "name": "api", "namespace": "ns1", "is_secret": True}
        assert _is_secret(resource)

    def test_secret_kind_without_flag_is_secret(self) -> None:
        assert _is_secret({"kind": "Secret", "name": "db-pass", "namespace": "ns1"})

    def test_secret_kind_with_false_flag_is_secret(self) -> None:
        resource = _make_resource(kind="Secret", name="db-pass", namespace="ns1", is_secret=False)
        assert _is_secret(resource)

    def test_regular_kind_without_flag_is_not_secret(self) -> None:
        assert not _is_secret({"kind": "ConfigMap", "name": "cfg", "namespace": "ns1"})

    def test_regular_kind_with_false_flag_is_not_secret(self) -> None:
        resource = _make_resource(kind="Deployment", name="api", namespace="ns1", is_secret=False)
        assert not _is_secret(resource)


class TestReportAggregation:
    def test_total_differences_combines_both_sides(self) -> None:
        staging = _make_inventory(
            cluster_name="staging",
            resources=[
                _make_resource(name="svc-a", namespace="ns1"),
                _make_resource(name="svc-b", namespace="ns1"),
            ],
        )
        prod = _make_inventory(
            cluster_name="prod",
            resources=[_make_resource(name="extra-service", namespace="ns1")],
        )

        result = compute_diff(staging, prod)

        assert result.sync_status == "out_of_sync"
        assert result.total_differences == 3  # noqa: PLR2004
        assert len(result.in_staging_not_prod) == 2  # noqa: PLR2004
        assert len(result.prod_only) == 1
