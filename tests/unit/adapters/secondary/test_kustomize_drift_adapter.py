from __future__ import annotations

import tempfile
from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
    KustomizeDriftAdapter,
)
from hexawyn.domain.errors import ComponentNotInstalledError


class TestKustomizeDriftAdapter:
    def test_render_desired_manifests(self) -> None:
        mock_stdout = """---
apiVersion: v1
kind: Service
metadata:
  name: test-svc
  namespace: default
spec:
  ports:
  - port: 80
"""
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = mock_stdout

            adapter = KustomizeDriftAdapter()
            result = adapter.render_desired_manifests("overlays/production", "default")

        assert len(result) == 1
        assert result[0]["kind"] == "Service"
        assert result[0]["name"] == "test-svc"

    def test_render_desired_manifests_kustomize_not_found(self) -> None:
        with patch("subprocess.run", side_effect=FileNotFoundError):
            adapter = KustomizeDriftAdapter()
            with pytest.raises(ComponentNotInstalledError):
                adapter.render_desired_manifests("overlays/production", "default")

    def test_source_exists_when_directory_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            adapter = KustomizeDriftAdapter()
            assert adapter.source_exists(tmpdir, "") is True

    def test_source_exists_when_missing(self) -> None:
        adapter = KustomizeDriftAdapter()
        assert adapter.source_exists("/nonexistent/path/12345", "") is False
