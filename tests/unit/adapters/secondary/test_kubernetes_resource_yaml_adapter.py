from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
    KubernetesResourceYAMLAdapter,
)
from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest


class TestKubernetesResourceYAMLAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesResourceYAMLAdapter(), ResourceYAMLPort)

    def test_fetch_returns_empty(self) -> None:
        r = KubernetesResourceYAMLAdapter().fetch_resource(
            ResourceYAMLRequest(resource_name="x", namespace="ns", kind="Deployment")
        )
        assert r == {}

    def test_exists_returns_false(self) -> None:
        r = KubernetesResourceYAMLAdapter().resource_exists(
            ResourceYAMLRequest(resource_name="x", namespace="ns", kind="Deployment")
        )
        assert r is False
