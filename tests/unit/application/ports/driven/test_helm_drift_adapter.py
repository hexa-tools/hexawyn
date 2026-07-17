from __future__ import annotations

import subprocess
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
from hexawyn.domain.errors import HelmNotFoundError, ManifestRenderError

_MULTI_DOC_MANIFEST = """\
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
  namespace: production
spec:
  replicas: 3
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: payment-config
  namespace: production
data:
  log_level: info
"""


def _completed(returncode: int = 0, stdout: str = "", stderr: str = "") -> MagicMock:
    result = MagicMock()
    result.returncode = returncode
    result.stdout = stdout
    result.stderr = stderr
    return result


class TestHelmDriftAdapterIsPort:
    def test_is_drift_detection_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        assert isinstance(HelmDriftAdapter(), DriftDetectionPort)


class TestRenderDesiredManifests:
    def test_parses_multi_document_yaml(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch("subprocess.run", return_value=_completed(stdout=_MULTI_DOC_MANIFEST)):
            adapter = HelmDriftAdapter()
            manifests = adapter.render_desired_manifests("payment-chart", "production")

        assert len(manifests) == 2
        by_kind = {m["kind"]: m for m in manifests}
        assert by_kind["Deployment"]["name"] == "payment-service"
        assert by_kind["Deployment"]["namespace"] == "production"
        assert by_kind["ConfigMap"]["data"]["data"]["log_level"] == "info"

    def test_malformed_documents_are_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        malformed = """\
---
just a string, not a mapping
---
kind: Deployment
---
kind: Deployment
metadata:
  name: 123
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: valid-service
  namespace: production
spec:
  replicas: 1
"""
        with patch("subprocess.run", return_value=_completed(stdout=malformed)):
            adapter = HelmDriftAdapter()
            manifests = adapter.render_desired_manifests("payment-chart", "production")

        assert len(manifests) == 1
        assert manifests[0]["name"] == "valid-service"

    def test_binary_not_found_raises_helm_not_found_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch("subprocess.run", side_effect=FileNotFoundError()):
            adapter = HelmDriftAdapter()
            with pytest.raises(HelmNotFoundError):
                adapter.render_desired_manifests("payment-chart", "production")

    def test_timeout_raises_manifest_render_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="helm", timeout=30)):
            adapter = HelmDriftAdapter()
            with pytest.raises(ManifestRenderError):
                adapter.render_desired_manifests("payment-chart", "production")

    def test_non_zero_exit_raises_manifest_render_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch(
            "subprocess.run", return_value=_completed(returncode=1, stderr="Error: something broke")
        ):
            adapter = HelmDriftAdapter()
            with pytest.raises(ManifestRenderError):
                adapter.render_desired_manifests("payment-chart", "production")


class TestSourceExists:
    def test_existing_release_returns_true(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch("subprocess.run", return_value=_completed(stdout='{"name": "payment-chart"}')):
            adapter = HelmDriftAdapter()
            assert adapter.source_exists("payment-chart", "production") is True

    def test_release_not_found_returns_false(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch(
            "subprocess.run",
            return_value=_completed(returncode=1, stderr="Error: release: not found"),
        ):
            adapter = HelmDriftAdapter()
            assert adapter.source_exists("deleted-release", "production") is False

    def test_other_failure_reraises(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

        with patch(
            "subprocess.run",
            return_value=_completed(returncode=1, stderr="Error: Kubernetes cluster unreachable"),
        ):
            adapter = HelmDriftAdapter()
            with pytest.raises(ManifestRenderError):
                adapter.source_exists("payment-chart", "production")
