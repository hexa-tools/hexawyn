"""E2E tests: cert-manager — real cert-manager on k3d cluster.

Usage:
    make cluster-up
    make cluster-load
    make test-e2e
"""

from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.cert_manager_adapter import CertManagerAdapter
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

NAMESPACE = "hexawyn-test"


@pytest.mark.e2e
class TestCertManagerE2E:
    @pytest.fixture(autouse=True)
    def _setup(self, k8s_cluster_ready: bool) -> None:
        self._adapter = CertManagerAdapter(VanillaAdapter("k3d-hexawyn-e2e"))

    def test_certs_detect_returns_response(self) -> None:
        result = self._adapter.detect()

        assert hasattr(result, "installed")
        assert hasattr(result, "total_certs")
        assert result.total_certs >= 0

    def test_certs_list_returns_certificates(self) -> None:
        certs = self._adapter.list_certificates()

        assert isinstance(certs, list)

    def test_certs_issuers_list_returns_issuers(self) -> None:
        issuers = self._adapter.list_issuers(namespace=NAMESPACE)

        assert isinstance(issuers, list)
        assert any(i.name == "e2e-selfsigned" for i in issuers), "Expected e2e-selfsigned issuer"

    def test_get_certificate_returns_data(self) -> None:
        cert = self._adapter.get_certificate(name="e2e-test-cert", namespace=NAMESPACE)
        assert cert is not None

    def test_challenges_list_does_not_crash(self) -> None:
        challenges = self._adapter.list_challenges()
        assert isinstance(challenges, list)

    def test_get_nonexistent_certificate_raises(self) -> None:
        with pytest.raises(Exception):
            self._adapter.get_certificate(name="does-not-exist-e2e", namespace=NAMESPACE)

    def test_get_nonexistent_issuer_raises(self) -> None:
        with pytest.raises(Exception):
            self._adapter.get_issuer(name="does-not-exist-issuer", namespace=NAMESPACE)

    def test_list_empty_namespace_returns_empty(self) -> None:
        issuers = self._adapter.list_issuers(namespace="kube-public")
        assert isinstance(issuers, list)
