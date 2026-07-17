from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterInventoryData,
    ResourceInventoryRaw,
)


def _res(
    kind: str = "Deployment",
    name: str = "svc",
    namespace: str = "production",
    image: str = "v1.0",
    replicas: int = 1,
    is_secret: bool = False,
) -> ResourceInventoryRaw:
    return ResourceInventoryRaw(
        kind=kind,
        name=name,
        namespace=namespace,
        image_tag=image,
        replicas=replicas,
        is_secret=is_secret,
    )


def _inventory(name: str, resources: list[ResourceInventoryRaw]) -> ClusterInventoryData:
    return ClusterInventoryData(cluster_name=name, resources=resources)


class TestMissingResources:
    def test_notification_missing_in_prod(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory("staging", [_res(name="notification-service")])
        prod = _inventory("prod", [])

        report = compute_diff(staging, prod)

        assert report.sync_status == "out_of_sync"
        assert report.total_differences == 1
        assert report.in_staging_not_prod[0].resource == "Deployment/notification-service"

    def test_all_resources_in_sync(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        inv = _inventory("staging", [_res(name="payment-service")])
        report = compute_diff(inv, inv)

        assert report.sync_status == "in_sync"
        assert report.total_differences == 0


class TestVersionMismatches:
    def test_staging_v1_3_prod_v1_2(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory("staging", [_res(name="payment-service", image="v1.3")])
        prod = _inventory("prod", [_res(name="payment-service", image="v1.2")])

        report = compute_diff(staging, prod)

        assert report.version_mismatches[0].staging_value == "v1.3"
        assert report.version_mismatches[0].prod_value == "v1.2"

    def test_replicas_diff_detected(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory("staging", [_res(name="payment-service", replicas=3)])
        prod = _inventory("prod", [_res(name="payment-service", replicas=1)])

        report = compute_diff(staging, prod)

        assert report.version_mismatches[0].staging_value == "3"
        assert report.version_mismatches[0].prod_value == "1"


class TestPromotionChecklist:
    def test_ready_to_promote_and_requires_review(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory(
            "staging",
            [
                _res(name="notification-service"),
                _res(name="payment-service", image="v1.3"),
                _res(name="feature-flags-v2", kind="ConfigMap"),
            ],
        )
        prod = _inventory("prod", [_res(name="payment-service", image="v1.2")])

        report = compute_diff(staging, prod)

        assert "Deployment/notification-service" in report.promotion_checklist.ready_to_promote
        assert "ConfigMap/feature-flags-v2" in report.promotion_checklist.ready_to_promote
        assert "Deployment/payment-service" in report.promotion_checklist.requires_review


class TestSecrets:
    def test_secret_manual_promotion_warning(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory("staging", [_res(name="db-password", is_secret=True)])
        prod = _inventory("prod", [])

        report = compute_diff(staging, prod)

        assert report.in_staging_not_prod[0].reason == "secret_manual"
        assert "manual" in report.in_staging_not_prod[0].detail.lower()


class TestProdOnlyResources:
    def test_prod_only_listed_separately(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory("staging", [])
        prod = _inventory("prod", [_res(name="legacy-cron")])

        report = compute_diff(staging, prod)

        assert report.prod_only[0].resource == "Deployment/legacy-cron"
        assert report.prod_only[0].priority == "informational"


class TestTicketScenario:
    def test_full_scenario(self) -> None:
        from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
            compute_diff,
        )

        staging = _inventory(
            "staging",
            [
                _res(name="notification-service"),
                _res(name="payment-service", image="v1.3"),
                _res(name="feature-flags-v2", kind="ConfigMap"),
            ],
        )
        prod = _inventory(
            "prod",
            [
                _res(name="payment-service", image="v1.2"),
            ],
        )

        report = compute_diff(staging, prod)

        assert len(report.in_staging_not_prod) == 2
        assert len(report.version_mismatches) == 1
        assert "Deployment/notification-service" in report.promotion_checklist.ready_to_promote
        assert "Deployment/payment-service" in report.promotion_checklist.requires_review
