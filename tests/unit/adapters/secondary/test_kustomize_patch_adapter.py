from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.kustomize_patch_adapter import (
    KustomizeCLIPatchAdapter,
)
from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
)


class TestKustomizeCLIPatchAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KustomizeCLIPatchAdapter(), KustomizePatchAnalysisPort)

    def test_extract_patch_fields_with_data(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(
                returncode=0,
                stdout="apiVersion: apps/v1\n  replicas: 3\n  image: nginx:1.25\n",
            )
            adapter = KustomizeCLIPatchAdapter()
            result = adapter.extract_patch_fields("/path/to/overlay")

            assert len(result) >= 1
            assert any(p["field"] == "replicas" for p in result)

    def test_extract_patch_fields_empty_on_error(self) -> None:
        with patch("subprocess.run", side_effect=Exception("kustomize not found")):
            adapter = KustomizeCLIPatchAdapter()
            result = adapter.extract_patch_fields("/path/to/overlay")
            assert result == []

    def test_extract_patch_fields_empty_on_non_zero(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=1, stdout="")
            adapter = KustomizeCLIPatchAdapter()
            result = adapter.extract_patch_fields("/invalid/path")
            assert result == []

    def test_extract_base_fields_with_data(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(
                returncode=0,
                stdout="kind: Deployment\n  name: my-app\n",
            )
            adapter = KustomizeCLIPatchAdapter()
            result = adapter.extract_base_fields("/path/to/overlay")

            assert isinstance(result, list)
            assert any(b.get("kind") == "Deployment" or b.get("name") == "my-app" for b in result)

    def test_extract_base_fields_empty_on_error(self) -> None:
        with patch("subprocess.run", side_effect=Exception("kustomize not found")):
            adapter = KustomizeCLIPatchAdapter()
            result = adapter.extract_base_fields("/path/to/overlay")
            assert result == []

    def test_extract_patch_fields_empty_path(self) -> None:
        with patch("subprocess.run", side_effect=Exception("bad path")):
            adapter = KustomizeCLIPatchAdapter()
            result = adapter.extract_patch_fields("")
            assert result == []
