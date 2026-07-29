"""E2E tests: RBAC + Secret Rotation + Helm — real cluster."""

from __future__ import annotations

import pytest


@pytest.mark.e2e
class TestRBACE2E:
    def test_rbac_audit_does_not_crash(self, k8s_cluster_ready: bool) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        adapter = KubernetesRBACAdapter()
        result = adapter.list_role_bindings()
        assert isinstance(result, list)


@pytest.mark.e2e
class TestSecretRotationE2E:
    def test_secret_audit_does_not_crash(self, k8s_cluster_ready: bool) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        adapter = KubernetesSecretAuditAdapter()
        result = adapter.list_secrets()
        assert isinstance(result, list)


@pytest.mark.e2e
class TestHelmE2E:
    def test_helm_list_releases(self, k8s_cluster_ready: bool) -> None:
        from hexawyn.adapters.secondary.gitops.helm_release_version_adapter import (
            HelmReleaseVersionAdapter,
        )

        adapter = HelmReleaseVersionAdapter()
        result = adapter.list_releases(None)
        assert isinstance(result, list)
