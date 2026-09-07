from __future__ import annotations

from hexawyn.application.ports.driven.helm_release_version_port import (
    HelmReleaseVersionPort,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.command import (
    DetectOutdatedHelmReleasesCommand,
)
from hexawyn.application.use_case.gitops.detect_outdated_helm_releases.response import (
    DetectOutdatedHelmReleasesResponse,
)
from hexawyn.domain.services.outdated_helm.outdated_helm_engine import (
    HelmOutdatedReleaseEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut: MutantDict = {}  # type: ignore


class DetectOutdatedHelmReleasesUseCase:
    @_mutmut_mutated(mutants_xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut)
    def __init__(self, helm_port: HelmReleaseVersionPort) -> None:
        self._port = helm_port
        self._engine = HelmOutdatedReleaseEngine()
    def xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_orig(self, helm_port: HelmReleaseVersionPort) -> None:
        self._port = helm_port
        self._engine = HelmOutdatedReleaseEngine()
    def xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_1(self, helm_port: HelmReleaseVersionPort) -> None:
        self._port = None
        self._engine = HelmOutdatedReleaseEngine()
    def xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_2(self, helm_port: HelmReleaseVersionPort) -> None:
        self._port = helm_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut)
    def detect_outdated(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_orig(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_1(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = None
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_2(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(None)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_3(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = None

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_4(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(None) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_5(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = None
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_6(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = None
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_7(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(None)
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_8(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get(None, ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_9(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", None))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_10(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get(""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_11(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_12(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("XXchart_nameXX", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_13(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("CHART_NAME", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_14(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", "XXXX"))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_15(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart or chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_16(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_17(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = None
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_18(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(None)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_19(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = None

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_20(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(None)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_21(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = None
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_22(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(None, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_23(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, None)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_24(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(latest_map)
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_25(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, )
        return DetectOutdatedHelmReleasesResponse(result=result)  # type: ignore

    def xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_26(
        self, command: DetectOutdatedHelmReleasesCommand
    ) -> DetectOutdatedHelmReleasesResponse:
        releases_raw = self._port.list_releases(command.namespace)
        releases: list[dict[str, object]] = [dict(r) for r in releases_raw]

        latest_map: dict[str, dict[str, object]] = {}
        for rel in releases:
            chart = str(rel.get("chart_name", ""))
            if chart and chart not in latest_map:
                latest_raw = self._port.fetch_latest_version(chart)
                latest_map[chart] = dict(latest_raw)

        result = self._engine.compute(releases, latest_map)
        return DetectOutdatedHelmReleasesResponse(result=None)  # type: ignore

mutants_xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_1'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_2'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['_mutmut_orig'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_1'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_2'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_3'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_4'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_5'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_6'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_7'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_8'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_9'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_10'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_11'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_12'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_13'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_14'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_15'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_16'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_17'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_18'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_19'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_20'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_21'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_22'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_23'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_24'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_25'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut['xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_26'] = DetectOutdatedHelmReleasesUseCase.xǁDetectOutdatedHelmReleasesUseCaseǁdetect_outdated__mutmut_26 # type: ignore # mutmut generated
