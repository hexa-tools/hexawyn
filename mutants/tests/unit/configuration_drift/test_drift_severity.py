"""Unit tests for classify_severity — deterministic field/kind severity matrix."""

from __future__ import annotations

from hexawyn.domain.services.configuration_drift.drift_severity import classify_severity


class TestFieldBasedSeverity:
    def test_image_is_critical(self) -> None:
        assert classify_severity("image", "Deployment") == "critical"

    def test_replicas_is_warning(self) -> None:
        assert classify_severity("replicas", "Deployment") == "warning"

    def test_resource_limits_is_warning(self) -> None:
        assert classify_severity("resource_limits", "Deployment") == "warning"

    def test_env_vars_is_warning(self) -> None:
        assert classify_severity("env_vars", "Deployment") == "warning"

    def test_configmap_data_is_warning(self) -> None:
        assert classify_severity("configmap_data", "ConfigMap") == "warning"

    def test_labels_is_info(self) -> None:
        assert classify_severity("labels", "Deployment") == "info"

    def test_unknown_field_defaults_to_warning(self) -> None:
        assert classify_severity("some_new_field", "Deployment") == "warning"


class TestKindBasedOverride:
    def test_role_is_always_critical(self) -> None:
        assert classify_severity("labels", "Role") == "critical"

    def test_cluster_role_is_always_critical(self) -> None:
        assert classify_severity("replicas", "ClusterRole") == "critical"

    def test_role_binding_is_always_critical(self) -> None:
        assert classify_severity("labels", "RoleBinding") == "critical"

    def test_cluster_role_binding_is_always_critical(self) -> None:
        assert classify_severity("labels", "ClusterRoleBinding") == "critical"

    def test_secret_is_always_critical(self) -> None:
        assert classify_severity("labels", "Secret") == "critical"

    def test_deployment_is_not_forced_critical(self) -> None:
        assert classify_severity("labels", "Deployment") == "info"
