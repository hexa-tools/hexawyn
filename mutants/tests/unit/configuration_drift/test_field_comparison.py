"""Unit tests for the field extractors and comparison helpers — pure,
path-specific accessors mirroring resource_yaml.py's ResourceYAMLResult style."""

from __future__ import annotations

from hexawyn.domain.services.configuration_drift.field_comparison import (
    compare_dict_field,
    compare_scalar_field,
    get_configmap_data,
    get_env_vars,
    get_image,
    get_labels,
    get_replicas,
    get_resource_limits,
)


def _deployment_manifest(
    image: str = "payment:v1.2",
    replicas: int = 3,
    env: list[dict[str, object]] | None = None,
    limits: dict[str, str] | None = None,
    labels: dict[str, str] | None = None,
) -> dict[str, object]:
    container: dict[str, object] = {"image": image}
    if env is not None:
        container["env"] = env
    if limits is not None:
        container["resources"] = {"limits": limits}
    manifest: dict[str, object] = {
        "spec": {
            "replicas": replicas,
            "template": {"spec": {"containers": [container]}},
        }
    }
    if labels is not None:
        manifest["metadata"] = {"labels": labels}
    return manifest


class TestGetImage:
    def test_extracts_first_container_image(self) -> None:
        assert get_image(_deployment_manifest(image="payment:v1.3-hotfix")) == "payment:v1.3-hotfix"

    def test_missing_spec_returns_none(self) -> None:
        assert get_image({}) is None

    def test_non_dict_spec_returns_none(self) -> None:
        assert get_image({"spec": "not-a-dict"}) is None

    def test_no_containers_returns_none(self) -> None:
        assert get_image({"spec": {"template": {"spec": {"containers": []}}}}) is None

    def test_missing_template_returns_none(self) -> None:
        assert get_image({"spec": {}}) is None

    def test_non_dict_template_returns_none(self) -> None:
        assert get_image({"spec": {"template": "not-a-dict"}}) is None

    def test_missing_pod_spec_returns_none(self) -> None:
        assert get_image({"spec": {"template": {}}}) is None

    def test_non_dict_pod_spec_returns_none(self) -> None:
        assert get_image({"spec": {"template": {"spec": "not-a-dict"}}}) is None

    def test_non_list_containers_returns_none(self) -> None:
        assert get_image({"spec": {"template": {"spec": {"containers": "not-a-list"}}}}) is None


class TestGetReplicas:
    def test_extracts_replicas(self) -> None:
        assert get_replicas(_deployment_manifest(replicas=1)) == 1

    def test_missing_replicas_returns_none(self) -> None:
        assert get_replicas({"spec": {}}) is None

    def test_missing_spec_returns_none(self) -> None:
        assert get_replicas({}) is None

    def test_non_int_replicas_returns_none(self) -> None:
        assert get_replicas({"spec": {"replicas": "three"}}) is None


class TestGetEnvVars:
    def test_extracts_name_value_pairs(self) -> None:
        env = [{"name": "LOG_LEVEL", "value": "debug"}, {"name": "PORT", "value": "8080"}]
        assert get_env_vars(_deployment_manifest(env=env)) == {"LOG_LEVEL": "debug", "PORT": "8080"}

    def test_no_env_returns_empty(self) -> None:
        assert get_env_vars(_deployment_manifest()) == {}

    def test_no_containers_returns_empty(self) -> None:
        assert get_env_vars({}) == {}


class TestGetResourceLimits:
    def test_extracts_limits(self) -> None:
        limits = {"cpu": "500m", "memory": "512Mi"}
        assert get_resource_limits(_deployment_manifest(limits=limits)) == limits

    def test_no_limits_returns_empty(self) -> None:
        assert get_resource_limits(_deployment_manifest()) == {}

    def test_no_containers_returns_empty(self) -> None:
        assert get_resource_limits({}) == {}

    def test_non_dict_limits_returns_empty(self) -> None:
        manifest = _deployment_manifest()
        containers = manifest["spec"]["template"]["spec"]["containers"]
        containers[0]["resources"] = {"limits": "not-a-dict"}
        assert get_resource_limits(manifest) == {}


class TestGetLabels:
    def test_extracts_labels(self) -> None:
        labels = {"app": "payment", "tier": "backend"}
        assert get_labels(_deployment_manifest(labels=labels)) == labels

    def test_no_labels_returns_empty(self) -> None:
        assert get_labels({}) == {}

    def test_non_dict_labels_returns_empty(self) -> None:
        assert get_labels({"metadata": {"labels": "not-a-dict"}}) == {}


class TestGetConfigmapData:
    def test_extracts_data(self) -> None:
        data = {"config.yaml": "key: value"}
        assert get_configmap_data({"data": data}) == data

    def test_no_data_returns_empty(self) -> None:
        assert get_configmap_data({}) == {}


class TestCompareScalarField:
    def test_same_values_produce_no_drift(self) -> None:
        assert compare_scalar_field("replicas", 3, 3, "Deployment") == []

    def test_different_values_produce_one_drifted_field(self) -> None:
        result = compare_scalar_field("image", "payment:v1.2", "payment:v1.3-hotfix", "Deployment")

        assert len(result) == 1
        assert result[0].field_path == "image"
        assert result[0].desired_value == "payment:v1.2"
        assert result[0].live_value == "payment:v1.3-hotfix"
        assert result[0].severity == "critical"


class TestCompareDictField:
    def test_identical_dicts_produce_no_drift(self) -> None:
        assert (
            compare_dict_field("labels", {"app": "payment"}, {"app": "payment"}, "Deployment") == []
        )

    def test_changed_key_produces_drifted_field(self) -> None:
        result = compare_dict_field(
            "configmap_data", {"config.yaml": "a"}, {"config.yaml": "b"}, "ConfigMap"
        )

        assert len(result) == 1
        assert result[0].field_path == "configmap_data.config.yaml"
        assert result[0].desired_value == "a"
        assert result[0].live_value == "b"

    def test_key_absent_on_one_side(self) -> None:
        result = compare_dict_field("env_vars", {"PORT": "8080"}, {}, "Deployment")

        assert len(result) == 1
        assert result[0].desired_value == "8080"
        assert result[0].live_value == "<absent>"
