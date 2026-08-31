from __future__ import annotations

from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.gitops.helm_drift_adapter import (
    HelmDriftAdapter,
    _parse_multi_doc_yaml,
)
from hexawyn.domain.errors import ComponentNotInstalledError


class TestHelmDriftAdapter:
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

            adapter = HelmDriftAdapter()
            result = adapter.render_desired_manifests("my-release", "default")

        assert len(result) == 1
        assert result[0]["kind"] == "Service"
        assert result[0]["name"] == "test-svc"
        assert result[0]["namespace"] == "default"

    def test_render_desired_manifests_helm_not_found(self) -> None:
        with patch("subprocess.run", side_effect=FileNotFoundError):
            adapter = HelmDriftAdapter()
            with pytest.raises(ComponentNotInstalledError):
                adapter.render_desired_manifests("my-release", "default")

    def test_source_exists_returns_true(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = "{}"

            adapter = HelmDriftAdapter()
            assert adapter.source_exists("my-release", "default") is True

    def test_source_exists_not_found_returns_false(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 1
            mock_run.return_value.stderr = "Error: release: not found"

            adapter = HelmDriftAdapter()
            result = adapter.source_exists("my-release", "default")
            assert result is False


class TestParseMultiDocYaml:
    def test_single_doc(self) -> None:
        stdout = """---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: default
spec:
  containers: []
"""
        result = _parse_multi_doc_yaml(stdout)
        assert len(result) == 1
        assert result[0]["kind"] == "Pod"
        assert result[0]["name"] == "my-pod"

    def test_multiple_docs(self) -> None:
        stdout = """---
apiVersion: v1
kind: Service
metadata:
  name: svc-a
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dep-a
"""
        result = _parse_multi_doc_yaml(stdout)
        assert len(result) == 2  # noqa: PLR2004

    def test_skips_non_dict_docs(self) -> None:
        stdout = "just a string\n---\napiVersion: v1\nkind: Service\nmetadata:\n  name: svc-a\n"
        result = _parse_multi_doc_yaml(stdout)
        assert len(result) == 1

    def test_skips_docs_without_name(self) -> None:
        stdout = """---
apiVersion: v1
kind: Service
metadata: {}
"""
        result = _parse_multi_doc_yaml(stdout)
        assert len(result) == 0

    def test_empty_output(self) -> None:
        assert _parse_multi_doc_yaml("") == []
