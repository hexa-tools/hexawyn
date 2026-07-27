from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterInventoryData,
    ResourceInventoryRaw,
)
from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
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
