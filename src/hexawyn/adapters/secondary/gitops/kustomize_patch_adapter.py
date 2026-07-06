from __future__ import annotations

from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    BaseFieldRawData,
    KustomizePatchAnalysisPort,
    PatchFieldRawData,
)


class KustomizeCLIPatchAdapter(KustomizePatchAnalysisPort):
    def extract_patch_fields(self, overlay_path: str) -> list[PatchFieldRawData]:
        return []

    def extract_base_fields(self, overlay_path: str) -> list[BaseFieldRawData]:
        return []
