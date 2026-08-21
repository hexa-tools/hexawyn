"""E2E tests: list_ingresses — real cluster ingress inventory.

Requires a Kubernetes cluster (k3d, kind, or KUBECONFIG).

Usage:
    make cluster-up
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter import VanillaK8sAdapter

_NAMESPACE = "hexawyn-test"

_INGRESS_FIXTURE = """
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hexawyn-e2e-ingress
spec:
  rules:
  - host: hexawyn-e2e.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: hexawyn-e2e-svc
            port:
              number: 80
"""


@pytest.mark.e2e
class TestListIngressesE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = VanillaK8sAdapter(
            api=None, metrics_api=None, cluster_name="k3d-hexawyn-e2e"
        )

    def test_lists_ingresses_in_test_namespace(self, k8s_apply) -> None:
        k8s_apply(_INGRESS_FIXTURE)

        ingresses = self._adapter.list_ingresses(namespace=_NAMESPACE)

        assert isinstance(ingresses, list)
        names = {item["name"] for item in ingresses}
        assert "hexawyn-e2e-ingress" in names

    def test_each_ingress_has_required_fields(self, k8s_apply) -> None:
        k8s_apply(_INGRESS_FIXTURE)

        ingresses = self._adapter.list_ingresses(namespace=_NAMESPACE)

        for item in ingresses:
            assert "name" in item, f"Ingress missing 'name': {item}"
            assert "namespace" in item, f"Ingress missing 'namespace': {item}"
            assert "host" in item, f"Ingress missing 'host': {item}"
            assert "target_service" in item, f"Ingress missing 'target_service': {item}"
            assert "tls_enabled" in item, f"Ingress missing 'tls_enabled': {item}"
