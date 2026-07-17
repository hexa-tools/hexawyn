"""RED → GREEN — KustomizeCLIPatchAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.kustomize_patch_adapter import (
    KustomizeCLIPatchAdapter,
)
from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
)


class TestKustomizeCLIPatchAdapter:
    def test_implements_port(self) -> None:
        adapter = KustomizeCLIPatchAdapter()
        assert isinstance(adapter, KustomizePatchAnalysisPort)

    def test_extract_patch_fields_returns_empty(self) -> None:
        adapter = KustomizeCLIPatchAdapter()
        result = adapter.extract_patch_fields("overlays/test")
        assert result == []

    def test_extract_base_fields_returns_empty(self) -> None:
        adapter = KustomizeCLIPatchAdapter()
        result = adapter.extract_base_fields("overlays/test")
        assert result == []
