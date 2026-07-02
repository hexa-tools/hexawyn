from __future__ import annotations

from hexawyn.domain.models.resource_yaml import (
    ResourceYAMLRequest,
    ResourceYAMLResult,
)


class TestResourceYAMLResult:
    def test_deployment_with_limits(self) -> None:
        result = ResourceYAMLResult.compute(
            request=ResourceYAMLRequest(
                resource_name="order-api",
                namespace="production",
                kind="Deployment",
            ),
            yaml_data={
                "kind": "Deployment",
                "spec": {
                    "replicas": 3,
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "name": "app",
                                    "image": "registry/order-api:v2.3.1",
                                    "resources": {"limits": {"cpu": "500m", "memory": "512Mi"}},
                                }
                            ]
                        }
                    },
                },
            },
            resource_found=True,
        )
        assert result.resource_found is True
        assert result.image_tags == ["registry/order-api:v2.3.1"]
        assert result.resource_limits == {"cpu": "500m", "memory": "512Mi"}

    def test_resource_not_found(self) -> None:
        result = ResourceYAMLResult.compute(
            request=ResourceYAMLRequest(
                resource_name="ghost", namespace="production", kind="Deployment"
            ),
            yaml_data={},
            resource_found=False,
        )
        assert result.resource_found is False
        assert result.yaml_data == {}

    def test_secret_redacted(self) -> None:
        result = ResourceYAMLResult.compute(
            request=ResourceYAMLRequest(
                resource_name="db-creds", namespace="production", kind="Secret"
            ),
            yaml_data={
                "kind": "Secret",
                "data": {"DB_PASSWORD": "REDACTED", "API_KEY": "REDACTED"},
            },
            resource_found=True,
        )
        assert result.resource_found is True
        assert result.yaml_data.get("data", {}).get("DB_PASSWORD") == "***REDACTED***"

    def test_with_init_containers(self) -> None:
        result = ResourceYAMLResult.compute(
            request=ResourceYAMLRequest(resource_name="app", namespace="ns", kind="Deployment"),
            yaml_data={
                "kind": "Deployment",
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [{"image": "app:v1"}],
                            "initContainers": [{"image": "init:v2"}],
                        }
                    }
                },
            },
            resource_found=True,
        )
        assert result.image_tags == ["app:v1", "init:v2"]

    def test_with_requests(self) -> None:
        result = ResourceYAMLResult.compute(
            request=ResourceYAMLRequest(resource_name="app", namespace="ns", kind="Deployment"),
            yaml_data={
                "kind": "Deployment",
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "image": "app:v1",
                                    "resources": {
                                        "limits": {"cpu": "500m"},
                                        "requests": {"cpu": "250m"},
                                    },
                                }
                            ]
                        }
                    }
                },
            },
            resource_found=True,
        )
        assert result.resource_requests == {"cpu": "250m"}

    def test_malformed_data_handled(self) -> None:
        result = ResourceYAMLResult.compute(
            request=ResourceYAMLRequest(resource_name="bad", namespace="ns", kind="Deployment"),
            yaml_data={"kind": "Deployment"},
            resource_found=True,
        )
        assert result.image_tags == []
        assert result.resource_limits == {}
        assert result.resource_requests == {}
