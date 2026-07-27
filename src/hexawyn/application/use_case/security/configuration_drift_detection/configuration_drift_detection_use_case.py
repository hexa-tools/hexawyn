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


class ConfigurationDriftDetectionUseCase:
    def __init__(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter

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

    def _render_kustomize_paths(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired
