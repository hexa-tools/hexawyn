"""E2E / integration test fixtures — Kubernetes cluster management.

Supports:
- k3d (lightweight K8s in Docker)
- kind (Kubernetes in Docker)
- Existing KUBECONFIG (any cluster)

Usage:
    @pytest.mark.e2e
    def test_something(test_namespace, k8s_client):
        ...
"""

from __future__ import annotations

import os
import subprocess
import time
import uuid
from pathlib import Path

import pytest

_K3D_CLUSTER_NAME = "hexawyn-e2e"
_KUBECONFIG = os.environ.get("KUBECONFIG", str(Path.home() / ".kube" / "config"))


def _kubectl(args: str, namespace: str | None = None) -> str:
    cmd = ["kubectl"]
    if namespace:
        cmd.extend(["-n", namespace])
    cmd.extend(args.split())
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0 and "NotFound" not in result.stderr:
        # Don't fail on cleanup "NotFound" errors
        if "error" in result.stderr.lower() and "not found" not in result.stderr.lower():
            raise RuntimeError(f"kubectl failed: {result.stderr.strip()}")
    return result.stdout + result.stderr


@pytest.fixture(scope="session", autouse=True)
def k8s_cluster_ready() -> bool:
    """Ensure a K8s cluster is available and kubeconfig is loaded."""
    try:
        from kubernetes import config

        config.load_kube_config()
        return True
    except Exception:
        pass

    try:
        subprocess.run(
            [
                "k3d",
                "cluster",
                "create",
                _K3D_CLUSTER_NAME,
                "--wait",
                "--timeout",
                "120s",
                "--k3s-arg",
                "--disable=traefik@server:0",
                "--k3s-arg",
                "--disable=servicelb@server:0",
            ],
            capture_output=True,
            check=True,
            timeout=180,
        )
        time.sleep(5)
        from kubernetes import config

        config.load_kube_config()
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    pytest.skip("No Kubernetes cluster available (k3d, kind, or KUBECONFIG)")
    return False


@pytest.fixture
def test_namespace(k8s_cluster_ready: bool) -> str:
    """Create a unique test namespace, clean up after test."""
    ns = f"hexawyn-e2e-{uuid.uuid4().hex[:8]}"
    _kubectl(f"create namespace {ns}")
    yield ns
    _kubectl(f"delete namespace {ns} --wait=false", namespace=None)


@pytest.fixture
def k8s_apply(test_namespace: str):
    """Fixture that applies YAML to the test namespace and returns resource names."""

    def _apply(yaml_content: str) -> dict[str, list[str]]:
        import tempfile

        created: dict[str, list[str]] = {}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            f.write(yaml_content)
            f.flush()
            try:
                output = _kubectl(f"apply -f {f.name}", namespace=test_namespace)
                for line in output.splitlines():
                    line = line.strip()
                    if "created" in line:
                        kind = (
                            line.split()[0].split("/")[0]
                            if "/" in line.split()[0]
                            else line.split()[0]
                        )
                        name = line.split()[1] if len(line.split()) > 1 else ""
                        created.setdefault(kind, []).append(name)
            finally:
                Path(f.name).unlink()
        return created

    return _apply


@pytest.fixture
def k8s_client():
    """Return a pre-configured kubernetes client for the test cluster."""
    from kubernetes import client, config

    try:
        config.load_kube_config()
    except Exception:
        config.load_incluster_config()

    return client


@pytest.fixture
def generate_tls_cert():
    """Generate a TLS certificate pair for testing. Returns (cert_pem, key_pem, cert_b64)."""
    import base64
    import datetime

    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    def _generate(
        subject_cn: str,
        not_before: datetime.datetime | None = None,
        not_after: datetime.datetime | None = None,
    ) -> tuple[str, str, str]:
        now = datetime.datetime.now(datetime.UTC)
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, subject_cn)])
        cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(private_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(not_before or now - datetime.timedelta(days=30))
            .not_valid_after(not_after or now + datetime.timedelta(days=365))
            .sign(private_key, hashes.SHA256())
        )
        cert_pem = cert.public_bytes(serialization.Encoding.PEM).decode()
        key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ).decode()
        cert_b64 = base64.b64encode(cert.public_bytes(serialization.Encoding.PEM)).decode()
        return cert_pem, key_pem, cert_b64

    return _generate
