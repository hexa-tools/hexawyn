from __future__ import annotations

from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.response import (
    DetectKustomizePatchConflictsResponse,
)
from hexawyn.domain.services.kustomize_patch_conflict.kustomize_patch_conflict_engine import (
    KustomizePatchConflictEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut: MutantDict = {}  # type: ignore


class DetectKustomizePatchConflictsUseCase:
    @_mutmut_mutated(mutants_xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut)
    def __init__(self, analysis_port: KustomizePatchAnalysisPort) -> None:
        self._port = analysis_port
        self._engine = KustomizePatchConflictEngine()
    def xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_orig(self, analysis_port: KustomizePatchAnalysisPort) -> None:
        self._port = analysis_port
        self._engine = KustomizePatchConflictEngine()
    def xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_1(self, analysis_port: KustomizePatchAnalysisPort) -> None:
        self._port = None
        self._engine = KustomizePatchConflictEngine()
    def xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_2(self, analysis_port: KustomizePatchAnalysisPort) -> None:
        self._port = analysis_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut)
    def detect_conflicts(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_orig(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_1(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = None
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_2(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(None)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_3(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = None

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_4(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(None)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_5(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = None
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_6(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(None) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_7(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = None

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_8(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(None) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_9(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = None
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_10(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(None, base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_11(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, None)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_12(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(base)
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_13(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, )
        return DetectKustomizePatchConflictsResponse(result=result)  # type: ignore

    def xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_14(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=None)  # type: ignore

mutants_xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut['xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_1'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut['xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_2'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['_mutmut_orig'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_1'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_2'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_3'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_4'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_5'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_6'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_7'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_8'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_9'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_10'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_11'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_12'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_13'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut['xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_14'] = DetectKustomizePatchConflictsUseCase.xǁDetectKustomizePatchConflictsUseCaseǁdetect_conflicts__mutmut_14 # type: ignore # mutmut generated
