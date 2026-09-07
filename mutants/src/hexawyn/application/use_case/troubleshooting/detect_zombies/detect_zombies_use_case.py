from __future__ import annotations

from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort
from hexawyn.application.use_case.troubleshooting.detect_zombies.command import (
    DetectZombiesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_zombies.response import (
    DetectZombiesResponse,
)
from hexawyn.domain.services.zombie_detection.zombie_detection_engine import (
    ZombieDetectionEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectZombiesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectZombiesUseCase:
    @_mutmut_mutated(mutants_xǁDetectZombiesUseCaseǁ__init____mutmut)
    def __init__(
        self,
        zombie_detection_port: ZombieDetectionPort,
    ) -> None:
        self._port = zombie_detection_port
        self._engine = ZombieDetectionEngine()
    def xǁDetectZombiesUseCaseǁ__init____mutmut_orig(
        self,
        zombie_detection_port: ZombieDetectionPort,
    ) -> None:
        self._port = zombie_detection_port
        self._engine = ZombieDetectionEngine()
    def xǁDetectZombiesUseCaseǁ__init____mutmut_1(
        self,
        zombie_detection_port: ZombieDetectionPort,
    ) -> None:
        self._port = None
        self._engine = ZombieDetectionEngine()
    def xǁDetectZombiesUseCaseǁ__init____mutmut_2(
        self,
        zombie_detection_port: ZombieDetectionPort,
    ) -> None:
        self._port = zombie_detection_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁDetectZombiesUseCaseǁexecute__mutmut)
    def execute(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_orig(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_1(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = None
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_2(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(None)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_3(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = None
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_4(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(None) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_5(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = None
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_6(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(None, command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_7(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, None)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_8(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(command.analysis_window_hours)
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_9(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, )
        return DetectZombiesResponse(result=result)

    def xǁDetectZombiesUseCaseǁexecute__mutmut_10(self, command: DetectZombiesCommand) -> DetectZombiesResponse:
        pods_raw = self._port.get_zombie_workloads(command.analysis_window_hours)
        pods: list[dict[str, object]] = [dict(p) for p in pods_raw]
        result = self._engine.detect(pods, command.analysis_window_hours)
        return DetectZombiesResponse(result=None)

mutants_xǁDetectZombiesUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁ__init____mutmut['xǁDetectZombiesUseCaseǁ__init____mutmut_1'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁ__init____mutmut['xǁDetectZombiesUseCaseǁ__init____mutmut_2'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_1'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_2'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_3'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_4'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_5'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_6'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_7'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_8'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_9'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectZombiesUseCaseǁexecute__mutmut['xǁDetectZombiesUseCaseǁexecute__mutmut_10'] = DetectZombiesUseCase.xǁDetectZombiesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
