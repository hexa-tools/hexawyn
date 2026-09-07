from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort, LiveResourceRaw
from hexawyn.application.use_case.security.configuration_drift_detection.command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.use_case.security.configuration_drift_detection.mapper import (
    find_matching,
    to_live_manifest,
    to_manifest,
    to_response,
)
from hexawyn.application.use_case.security.configuration_drift_detection.response import (
    ConfigurationDriftDetectionResponse,
)
from hexawyn.domain.models.configuration_drift import (
    DriftResult,
)
from hexawyn.domain.models.constants import ConfigurationDriftConstants
from hexawyn.domain.services.configuration_drift.drift_report_builder import build_drift_report
from hexawyn.domain.services.configuration_drift.manifest_diff import compare_resource

_cfg = ConfigurationDriftConstants()

_ResourceKey = tuple[str, str, str]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut: MutantDict = {}  # type: ignore


class ConfigurationDriftDetectionUseCase:
    @_mutmut_mutated(mutants_xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut)
    def __init__(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter
    def xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_orig(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter
    def xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_1(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
    ) -> None:
        self._live_resource_port = None
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter
    def xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_2(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = None
        self._kustomize_adapter = kustomize_adapter
    def xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_3(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = None

    @_mutmut_mutated(mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut)
    def detect_drift(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_orig(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_1(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = None
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_2(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(None)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_3(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = None

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_4(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(None, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_5(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, None)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_6(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_7(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, )

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_8(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = None
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_9(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = None
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_10(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = None
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_11(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = None

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_12(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = None
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_13(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["XXkindXX"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_14(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["KIND"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_15(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["XXnameXX"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_16(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["NAME"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_17(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["XXnamespaceXX"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_18(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["NAMESPACE"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_19(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key not in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_20(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = None
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_21(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    None
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_22(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        None, to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_23(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), None, "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_24(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), None, source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_25(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", None
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_26(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_27(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_28(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_29(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_30(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(None), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_31(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(None), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_32(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "XXkustomizeXX", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_33(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "KUSTOMIZE", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_34(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                break

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_35(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = None
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_36(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(None)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_37(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["XXannotationsXX"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_38(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["ANNOTATIONS"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_39(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_40(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    None
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_41(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['XXkindXX']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_42(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['KIND']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_43(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['XXnameXX']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_44(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['NAME']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_45(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['XXnamespaceXX']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_46(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['NAMESPACE']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_47(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "XXnot managed by Helm or KustomizeXX"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_48(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by helm or kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_49(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "NOT MANAGED BY HELM OR KUSTOMIZE"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_50(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                break

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_51(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                None
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_52(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(None, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_53(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, None, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_54(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, None, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_55(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, None)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_56(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_57(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_58(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_exists_cache)
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_59(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, )
            )

        return to_response(build_drift_report(results, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_60(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(None)

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_61(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(None, excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_62(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, None))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_63(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(excluded))

    def xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_64(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)

        results: list[DriftResult] = []
        excluded: list[str] = []
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for live in live_resources:
            key: _ResourceKey = (live["kind"], live["name"], live["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                results.append(
                    compare_resource(
                        to_manifest(desired_raw), to_live_manifest(live), "kustomize", source
                    )
                )
                continue

            release = live["annotations"].get(_cfg.helm_release_annotation_key)
            if not release:
                excluded.append(
                    f"{live['kind']}/{live['name']} in {live['namespace']} — "
                    "not managed by Helm or Kustomize"
                )
                continue

            results.append(
                self._compare_helm_resource(live, release, helm_manifest_cache, helm_exists_cache)
            )

        return to_response(build_drift_report(results, ))

    @_mutmut_mutated(mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut)
    def _compare_helm_resource(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_orig(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_1(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_2(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = None
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_3(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                None, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_4(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, None
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_5(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_6(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_7(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["XXnamespaceXX"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_8(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["NAMESPACE"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_9(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_10(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, None, "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_11(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), None, release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_12(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", None)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_13(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_14(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_15(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_16(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", )

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_17(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(None), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_18(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "XXhelmXX", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_19(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "HELM", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_20(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_21(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = None
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_22(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                None, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_23(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, None
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_24(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_25(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_26(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["XXnamespaceXX"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_27(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["NAMESPACE"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_28(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = None
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_29(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            None,
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_30(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            None,
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_31(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            None,
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_32(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_33(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_34(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_35(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["XXkindXX"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_36(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["KIND"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_37(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["XXnameXX"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_38(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["NAME"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_39(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_40(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(None) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_41(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is None else None
        return compare_resource(desired, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_42(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(None, to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_43(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, None, "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_44(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), None, release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_45(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", None)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_46(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(to_live_manifest(live), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_47(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_48(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_49(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "helm", )

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_50(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(None), "helm", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_51(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "XXhelmXX", release)

    def xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_52(
        self,
        live: LiveResourceRaw,
        release: str,
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]],
        helm_exists_cache: dict[str, bool],
    ) -> DriftResult:
        if release not in helm_exists_cache:
            helm_exists_cache[release] = self._helm_adapter.source_exists(
                release, live["namespace"]
            )
        if not helm_exists_cache[release]:
            return compare_resource(None, to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = find_matching(
            helm_manifest_cache[release],
            live["kind"],
            live["name"],
        )
        desired = to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, to_live_manifest(live), "HELM", release)

    @_mutmut_mutated(mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut)
    def _render_kustomize_paths(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_orig(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_1(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = None
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_2(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(None, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_3(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, None):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_4(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_5(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, ):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_6(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = None
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_7(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] and namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_8(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["XXnamespaceXX"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_9(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["NAMESPACE"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_10(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = None
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_11(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["XXkindXX"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_12(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["KIND"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_13(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["XXnameXX"], resolved_namespace)] = (raw, path)
        return desired

    def xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_14(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["NAME"], resolved_namespace)] = (raw, path)
        return desired

mutants_xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut['_mutmut_orig'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut['xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_1'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut['xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_2'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut['xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_3'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['_mutmut_orig'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_1'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_2'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_3'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_4'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_5'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_6'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_7'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_8'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_9'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_10'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_11'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_12'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_13'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_14'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_15'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_16'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_17'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_18'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_18 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_19'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_19 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_20'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_20 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_21'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_21 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_22'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_22 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_23'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_23 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_24'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_24 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_25'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_25 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_26'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_26 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_27'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_27 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_28'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_28 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_29'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_29 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_30'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_30 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_31'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_31 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_32'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_32 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_33'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_33 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_34'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_34 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_35'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_35 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_36'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_36 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_37'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_37 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_38'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_38 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_39'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_39 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_40'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_40 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_41'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_41 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_42'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_42 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_43'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_43 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_44'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_44 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_45'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_45 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_46'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_46 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_47'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_47 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_48'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_48 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_49'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_49 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_50'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_50 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_51'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_51 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_52'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_52 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_53'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_53 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_54'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_54 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_55'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_55 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_56'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_56 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_57'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_57 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_58'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_58 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_59'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_59 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_60'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_60 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_61'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_61 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_62'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_62 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_63'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_63 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut['xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_64'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁdetect_drift__mutmut_64 # type: ignore # mutmut generated

mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['_mutmut_orig'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_1'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_2'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_3'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_4'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_5'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_6'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_7'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_8'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_9'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_10'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_11'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_12'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_13'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_14'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_15'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_16'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_17'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_18'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_18 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_19'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_19 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_20'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_20 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_21'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_21 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_22'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_22 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_23'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_23 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_24'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_24 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_25'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_25 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_26'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_26 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_27'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_27 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_28'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_28 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_29'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_29 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_30'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_30 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_31'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_31 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_32'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_32 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_33'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_33 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_34'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_34 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_35'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_35 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_36'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_36 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_37'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_37 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_38'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_38 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_39'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_39 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_40'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_40 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_41'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_41 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_42'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_42 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_43'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_43 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_44'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_44 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_45'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_45 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_46'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_46 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_47'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_47 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_48'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_48 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_49'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_49 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_50'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_50 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_51'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_51 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_52'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_compare_helm_resource__mutmut_52 # type: ignore # mutmut generated

mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['_mutmut_orig'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_1'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_2'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_3'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_4'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_5'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_6'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_7'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_8'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_9'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_10'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_11'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_12'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_13'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut['xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_14'] = ConfigurationDriftDetectionUseCase.xǁConfigurationDriftDetectionUseCaseǁ_render_kustomize_paths__mutmut_14 # type: ignore # mutmut generated
