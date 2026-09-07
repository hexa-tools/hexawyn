"""E2E tests: certificate_health_check — end-to-end TLS certificate analysis.

Requires a real Kubernetes cluster (k3d, kind, or KUBECONFIG).
Marked with @pytest.mark.e2e — run manually, never in CI.

Usage:
    poetry run pytest tests/e2e/test_certificate_health_check_e2e.py -v -m e2e
"""

from __future__ import annotations

import base64
import datetime

import pytest


@pytest.mark.e2e
class TestCertificateHealthCheckE2E:
    def test_expired_certificate_detected(
        self,
        test_namespace: str,
        k8s_apply,
        generate_tls_cert,
    ) -> None:
        """E2E: Create an expired TLS secret, verify hexawyn detects it."""
        now = datetime.datetime.now(datetime.UTC)
        cert_pem, key_pem, cert_b64 = generate_tls_cert(
            "expired.example.com",
            not_before=now - datetime.timedelta(days=400),
            not_after=now - datetime.timedelta(days=10),
        )

        yaml = f"""apiVersion: v1
kind: Secret
metadata:
  name: expired-cert
  namespace: {test_namespace}
type: kubernetes.io/tls
data:
  tls.crt: {cert_b64}
  tls.key: {base64.b64encode(key_pem.encode()).decode()}
"""
        k8s_apply(yaml)

        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        result = check_cluster_certificate_health()

        assert result["error"] is None
        expired = result.get("expired", [])
        expired_names = [e["secret_name"] for e in expired]
        assert "expired-cert" in expired_names

    def test_healthy_certificate_detected(
        self,
        test_namespace: str,
        k8s_apply,
        generate_tls_cert,
    ) -> None:
        """E2E: Create a valid TLS secret, verify hexawyn marks it healthy."""
        cert_pem, key_pem, cert_b64 = generate_tls_cert("healthy.example.com")

        yaml = f"""apiVersion: v1
kind: Secret
metadata:
  name: healthy-cert
  namespace: {test_namespace}
type: kubernetes.io/tls
data:
  tls.crt: {cert_b64}
  tls.key: {base64.b64encode(key_pem.encode()).decode()}
"""
        k8s_apply(yaml)

        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        result = check_cluster_certificate_health()

        assert result["error"] is None
        healthy = result.get("healthy", [])
        healthy_names = [e["secret_name"] for e in healthy]
        assert "healthy-cert" in healthy_names

    def test_orphaned_certificate_detected(
        self,
        test_namespace: str,
        k8s_apply,
        generate_tls_cert,
    ) -> None:
        """E2E: Create a TLS secret without ingress → orphaned."""
        cert_pem, key_pem, cert_b64 = generate_tls_cert("orphan.example.com")

        yaml = f"""apiVersion: v1
kind: Secret
metadata:
  name: orphan-cert
  namespace: {test_namespace}
type: kubernetes.io/tls
data:
  tls.crt: {cert_b64}
  tls.key: {base64.b64encode(key_pem.encode()).decode()}
"""
        k8s_apply(yaml)

        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        result = check_cluster_certificate_health()

        assert result["error"] is None
        all_entries = (
            result.get("healthy", []) + result.get("warning", []) + result.get("critical", [])
        )
        orphan_entry = next((e for e in all_entries if e["secret_name"] == "orphan-cert"), None)
        assert orphan_entry is not None
        assert orphan_entry["is_orphan"] is True
