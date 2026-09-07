"""Unit tests for compare_resource — pure per-resource drift orchestration."""

from __future__ import annotations

from hexawyn.domain.models.configuration_drift import ResourceManifest
from hexawyn.domain.services.configuration_drift.manifest_diff import compare_resource


def _deployment(image: str, replicas: int, name: str = "payment-service") -> ResourceManifest:
    return ResourceManifest(
        kind="Deployment",
        name=name,
        namespace="production",
        data={
            "spec": {
                "replicas": replicas,
                "template": {"spec": {"containers": [{"image": image}]}},
            }
        },
    )


def _configmap(data: dict[str, str], name: str = "app-config") -> ResourceManifest:
    return ResourceManifest(
        kind="ConfigMap", name=name, namespace="production", data={"data": data}
    )


class TestImageDrift:
    def test_tc1_image_tag_change_is_critical(self) -> None:
        """TC1: image tag changed from v1.2 (Helm) to v1.3-hotfix (live) → critical."""
        desired = _deployment(image="payment:v1.2", replicas=3)
        live = _deployment(image="payment:v1.3-hotfix", replicas=3)

        result = compare_resource(desired, live, "helm", "payment-chart")

        assert result.has_critical_drift is True
        image_field = next(f for f in result.drifted_fields if f.field_path == "image")
        assert image_field.desired_value == "payment:v1.2"
        assert image_field.live_value == "payment:v1.3-hotfix"
        assert image_field.severity == "critical"


class TestReplicasDrift:
    def test_tc2_replicas_change_is_warning(self) -> None:
        """TC2: replicas changed from 3 (Helm) to 1 (live) → warning."""
        desired = _deployment(image="payment:v1.2", replicas=3)
        live = _deployment(image="payment:v1.2", replicas=1)

        result = compare_resource(desired, live, "helm", "payment-chart")

        assert result.has_critical_drift is False
        replicas_field = next(f for f in result.drifted_fields if f.field_path == "replicas")
        assert replicas_field.desired_value == "3"
        assert replicas_field.live_value == "1"
        assert replicas_field.severity == "warning"


class TestConfigMapDataDrift:
    def test_tc4_data_key_changed_is_flagged(self) -> None:
        """TC4: ConfigMap data key changed manually → data drift flagged."""
        desired = _configmap({"log_level": "info"})
        live = _configmap({"log_level": "debug"})

        result = compare_resource(desired, live, "helm", "app-chart")

        data_field = next(
            f for f in result.drifted_fields if f.field_path == "configmap_data.log_level"
        )
        assert data_field.desired_value == "info"
        assert data_field.live_value == "debug"
        assert data_field.severity == "warning"

    def test_configmap_data_not_compared_for_deployment(self) -> None:
        desired = _deployment(image="payment:v1.2", replicas=3)
        live = _deployment(image="payment:v1.2", replicas=3)

        result = compare_resource(desired, live, "helm", "payment-chart")

        assert not any(f.field_path.startswith("configmap_data") for f in result.drifted_fields)


class TestNoDrift:
    def test_identical_manifests_produce_no_drifted_fields(self) -> None:
        desired = _deployment(image="payment:v1.2", replicas=3)
        live = _deployment(image="payment:v1.2", replicas=3)

        result = compare_resource(desired, live, "helm", "payment-chart")

        assert result.drifted_fields == []
        assert result.has_critical_drift is False
        assert result.is_orphaned is False


class TestOrphanedResource:
    def test_no_desired_manifest_is_orphaned(self) -> None:
        """Edge case: Helm release deleted but resources still live → orphaned."""
        live = _deployment(image="payment:v1.2", replicas=3)

        result = compare_resource(None, live, "helm", "deleted-release")

        assert result.is_orphaned is True
        assert result.drifted_fields == []
        assert result.has_critical_drift is False
        assert result.name == "payment-service"
