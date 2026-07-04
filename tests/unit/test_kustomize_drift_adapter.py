from __future__ import annotations

import subprocess
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
from hexawyn.domain.errors import KustomizeNotFoundError, ManifestRenderError

_MULTI_DOC_MANIFEST = """\
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reporting-service
  namespace: production
spec:
  replicas: 2
"""


def _completed(returncode: int = 0, stdout: str = "", stderr: str = "") -> MagicMock:
    result = MagicMock()
    result.returncode = returncode
    result.stdout = stdout
    result.stderr = stderr
    return result


class TestKustomizeDriftAdapterIsPort:
    def test_is_drift_detection_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        assert isinstance(KustomizeDriftAdapter(), DriftDetectionPort)


class TestRenderDesiredManifests:
    def test_parses_yaml_output(self) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        with patch("subprocess.run", return_value=_completed(stdout=_MULTI_DOC_MANIFEST)):
            adapter = KustomizeDriftAdapter()
            manifests = adapter.render_desired_manifests("overlays/production", "production")

        assert len(manifests) == 1
        assert manifests[0]["kind"] == "Deployment"
        assert manifests[0]["name"] == "reporting-service"

    def test_malformed_documents_are_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

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
            adapter = KustomizeDriftAdapter()
            manifests = adapter.render_desired_manifests("overlays/production", "production")

        assert len(manifests) == 1
        assert manifests[0]["name"] == "valid-service"

    def test_binary_not_found_raises_kustomize_not_found_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        with patch("subprocess.run", side_effect=FileNotFoundError()):
            adapter = KustomizeDriftAdapter()
            with pytest.raises(KustomizeNotFoundError):
                adapter.render_desired_manifests("overlays/production", "production")

    def test_timeout_raises_manifest_render_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        with patch(
            "subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="kustomize", timeout=15)
        ):
            adapter = KustomizeDriftAdapter()
            with pytest.raises(ManifestRenderError):
                adapter.render_desired_manifests("overlays/production", "production")

    def test_non_zero_exit_raises_manifest_render_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        with patch(
            "subprocess.run",
            return_value=_completed(returncode=1, stderr="Error: no such file or directory"),
        ):
            adapter = KustomizeDriftAdapter()
            with pytest.raises(ManifestRenderError):
                adapter.render_desired_manifests("overlays/missing", "production")


class TestSourceExists:
    def test_existing_path_returns_true(self, tmp_path) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        adapter = KustomizeDriftAdapter()
        assert adapter.source_exists(str(tmp_path), "production") is True

    def test_missing_path_returns_false(self, tmp_path) -> None:
        from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
            KustomizeDriftAdapter,
        )

        adapter = KustomizeDriftAdapter()
        assert adapter.source_exists(str(tmp_path / "does-not-exist"), "production") is False
