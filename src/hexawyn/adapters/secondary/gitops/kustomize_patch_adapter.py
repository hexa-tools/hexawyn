from __future__ import annotations

import subprocess

from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    BaseFieldRawData,
    KustomizePatchAnalysisPort,
    PatchFieldRawData,
)


class KustomizeCLIPatchAdapter(KustomizePatchAnalysisPort):
    def extract_patch_fields(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = result.stdout.split("\n")
            patches: list[PatchFieldRawData] = []
            current_resource = ""
            for line in lines:
                line = line.strip()
                if line.startswith("apiVersion:"):
                    current_resource = line
                elif (
                    ":" in line and not line.startswith("kind:") and not line.startswith("metadata")
                ):  # noqa: E501
                    key_val = line.split(":", 1)
                    if len(key_val) == 2:  # noqa: PLR2004
                        patches.append(
                            PatchFieldRawData(  # type: ignore
                                resource=current_resource,
                                field=key_val[0].strip(),
                                value=key_val[1].strip(),
                            )
                        )
            return patches
        except Exception:
            return []

    def extract_base_fields(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = result.stdout.split("\n")
            bases: list[BaseFieldRawData] = []
            for i, line in enumerate(lines):
                if line.startswith("  name:"):
                    name = line.split(":", 1)[1].strip()
                    kind_line = lines[i - 1] if i > 0 else ""
                    kind = kind_line.split(":", 1)[1].strip() if ":" in kind_line else "unknown"
                    bases.append(
                        BaseFieldRawData(  # type: ignore
                            kind=kind,
                            name=name,
                            field_count=1,
                        )
                    )
            return bases
        except Exception:
            return []
