from __future__ import annotations

import subprocess

from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    BaseFieldRawData,
    KustomizePatchAnalysisPort,
    PatchFieldRawData,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut: MutantDict = {}  # type: ignore


class KustomizeCLIPatchAdapter(KustomizePatchAnalysisPort):
    @_mutmut_mutated(mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_orig(self, overlay_path: str) -> list[PatchFieldRawData]:
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_1(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_2(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                None,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_3(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=None,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_4(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=None,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_5(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=None,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_6(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_7(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_8(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_9(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_10(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["XXkustomizeXX", "build", overlay_path],
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_11(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["KUSTOMIZE", "build", overlay_path],
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_12(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "XXbuildXX", overlay_path],
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_13(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "BUILD", overlay_path],
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_14(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=False,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_15(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=False,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_16(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=16,
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_17(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode == 0:
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_18(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 1:
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_19(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_20(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = result.stdout.split(None)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_21(self, overlay_path: str) -> list[PatchFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = result.stdout.split("XX\nXX")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_22(self, overlay_path: str) -> list[PatchFieldRawData]:
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
            patches: list[PatchFieldRawData] = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_23(self, overlay_path: str) -> list[PatchFieldRawData]:
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
            current_resource = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_24(self, overlay_path: str) -> list[PatchFieldRawData]:
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
            current_resource = "XXXX"
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_25(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                line = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_26(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                if line.startswith(None):
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_27(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                if line.startswith("XXapiVersion:XX"):
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_28(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                if line.startswith("apiversion:"):
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_29(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                if line.startswith("APIVERSION:"):
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_30(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    current_resource = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_31(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("kind:") or not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_32(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line or not line.startswith("kind:") and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_33(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    "XX:XX" in line and not line.startswith("kind:") and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_34(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" not in line and not line.startswith("kind:") and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_35(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and line.startswith("kind:") and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_36(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith(None) and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_37(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("XXkind:XX") and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_38(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("KIND:") and not line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_39(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("kind:") and line.startswith("metadata")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_40(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("kind:") and not line.startswith(None)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_41(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("kind:") and not line.startswith("XXmetadataXX")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_42(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    ":" in line and not line.startswith("kind:") and not line.startswith("METADATA")
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_43(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = None
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_44(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.split(None, 1)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_45(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.split(":", None)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_46(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.split(1)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_47(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.split(":", )
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_48(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.rsplit(":", 1)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_49(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.split("XX:XX", 1)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_50(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    key_val = line.split(":", 2)
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_51(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    if len(key_val) != 2:  # noqa: PLR2004
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_52(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                    if len(key_val) == 3:  # noqa: PLR2004
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
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_53(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                            None
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_54(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                resource=None,
                                field=key_val[0].strip(),
                                value=key_val[1].strip(),
                            )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_55(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                field=None,
                                value=key_val[1].strip(),
                            )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_56(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                value=None,
                            )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_57(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                field=key_val[0].strip(),
                                value=key_val[1].strip(),
                            )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_58(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                value=key_val[1].strip(),
                            )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_59(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_60(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                field=key_val[1].strip(),
                                value=key_val[1].strip(),
                            )
                        )
            return patches
        except Exception:
            return []
    def xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_61(self, overlay_path: str) -> list[PatchFieldRawData]:
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
                                value=key_val[2].strip(),
                            )
                        )
            return patches
        except Exception:
            return []

    @_mutmut_mutated(mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut)
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_orig(self, overlay_path: str) -> list[BaseFieldRawData]:
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_1(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = None
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_2(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                None,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_3(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=None,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_4(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=None,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_5(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=None,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_6(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_7(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_8(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_9(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_10(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["XXkustomizeXX", "build", overlay_path],
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_11(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["KUSTOMIZE", "build", overlay_path],
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_12(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "XXbuildXX", overlay_path],
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_13(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "BUILD", overlay_path],
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_14(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=False,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_15(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=False,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_16(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=16,
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_17(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode == 0:
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_18(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 1:
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_19(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = None
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_20(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = result.stdout.split(None)
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_21(self, overlay_path: str) -> list[BaseFieldRawData]:
        try:
            result = subprocess.run(
                ["kustomize", "build", overlay_path],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if result.returncode != 0:
                return []
            lines = result.stdout.split("XX\nXX")
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_22(self, overlay_path: str) -> list[BaseFieldRawData]:
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
            bases: list[BaseFieldRawData] = None
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_23(self, overlay_path: str) -> list[BaseFieldRawData]:
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
            for i, line in enumerate(None):
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_24(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                if line.startswith(None):
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_25(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                if line.startswith("XX  name:XX"):
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_26(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                if line.startswith("  NAME:"):
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_27(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = None
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_28(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split(None, 1)[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_29(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split(":", None)[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_30(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split(1)[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_31(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split(":", )[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_32(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.rsplit(":", 1)[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_33(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split("XX:XX", 1)[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_34(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split(":", 2)[1].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_35(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    name = line.split(":", 1)[2].strip()
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_36(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind_line = None
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_37(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind_line = lines[i + 1] if i > 0 else ""
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_38(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind_line = lines[i - 2] if i > 0 else ""
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_39(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind_line = lines[i - 1] if i >= 0 else ""
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_40(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind_line = lines[i - 1] if i > 1 else ""
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_41(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind_line = lines[i - 1] if i > 0 else "XXXX"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_42(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = None
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_43(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(None, 1)[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_44(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", None)[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_45(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(1)[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_46(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", )[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_47(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.rsplit(":", 1)[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_48(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split("XX:XX", 1)[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_49(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", 2)[1].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_50(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", 1)[2].strip() if ":" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_51(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", 1)[1].strip() if "XX:XX" in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_52(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", 1)[1].strip() if ":" not in kind_line else "unknown"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_53(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", 1)[1].strip() if ":" in kind_line else "XXunknownXX"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_54(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                    kind = kind_line.split(":", 1)[1].strip() if ":" in kind_line else "UNKNOWN"
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

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_55(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                        None
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_56(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            kind=None,
                            name=name,
                            field_count=1,
                        )
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_57(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            name=None,
                            field_count=1,
                        )
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_58(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            field_count=None,
                        )
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_59(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            name=name,
                            field_count=1,
                        )
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_60(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            field_count=1,
                        )
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_61(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            )
                    )
            return bases
        except Exception:
            return []

    def xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_62(self, overlay_path: str) -> list[BaseFieldRawData]:
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
                            field_count=2,
                        )
                    )
            return bases
        except Exception:
            return []

mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['_mutmut_orig'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_1'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_2'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_3'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_4'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_5'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_6'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_7'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_8'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_9'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_10'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_11'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_12'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_13'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_14'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_15'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_16'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_17'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_18'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_19'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_20'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_21'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_22'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_23'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_24'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_25'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_26'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_27'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_28'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_29'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_30'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_31'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_32'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_33'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_34'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_35'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_36'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_37'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_38'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_39'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_40'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_41'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_42'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_43'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_44'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_45'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_46'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_47'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_48'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_49'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_50'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_51'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_52'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_53'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_54'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_55'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_56'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_57'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_58'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_59'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_59 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_60'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_60 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_61'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_patch_fields__mutmut_61 # type: ignore # mutmut generated

mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['_mutmut_orig'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_1'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_2'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_3'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_4'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_5'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_6'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_7'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_8'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_9'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_10'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_11'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_12'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_13'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_14'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_15'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_16'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_17'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_18'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_19'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_20'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_21'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_22'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_23'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_24'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_25'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_26'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_27'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_28'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_29'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_30'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_31'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_32'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_33'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_34'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_35'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_36'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_37'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_38'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_39'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_40'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_41'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_42'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_43'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_44'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_45'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_46'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_47'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_48'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_49'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_50'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_51'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_52'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_53'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_54'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_55'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_56'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_57'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_58'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_59'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_59 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_60'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_60 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_61'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_61 # type: ignore # mutmut generated
mutants_xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut['xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_62'] = KustomizeCLIPatchAdapter.xǁKustomizeCLIPatchAdapterǁextract_base_fields__mutmut_62 # type: ignore # mutmut generated
