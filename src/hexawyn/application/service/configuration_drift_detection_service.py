from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort, LiveResourceRaw
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_response import (
    ConfigurationDriftDetectionResponse,
    DriftedFieldDict,
    DriftResultDict,
)
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_service_port import (
    ConfigurationDriftDetectionServicePort,
)
from hexawyn.domain.models.configuration_drift import (
    ConfigurationDriftReport,
    DriftedField,
    DriftResult,
    ManagedBy,
    ResourceManifest,
)
from hexawyn.domain.models.constants import ConfigurationDriftConstants
from hexawyn.domain.services.configuration_drift.drift_report_builder import build_drift_report
from hexawyn.domain.services.configuration_drift.manifest_diff import compare_resource

_cfg = ConfigurationDriftConstants()

_ResourceKey = tuple[str, str, str]


class ConfigurationDriftDetectionService(ConfigurationDriftDetectionServicePort):
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
                        _to_manifest(desired_raw), _to_live_manifest(live), "kustomize", source
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

        return _to_response(build_drift_report(results, excluded))

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
            return compare_resource(None, _to_live_manifest(live), "helm", release)

        if release not in helm_manifest_cache:
            helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                release, live["namespace"]
            )
        desired_raw = _find_matching(helm_manifest_cache[release], live["kind"], live["name"])
        desired = _to_manifest(desired_raw) if desired_raw is not None else None
        return compare_resource(desired, _to_live_manifest(live), "helm", release)

    def _render_kustomize_paths(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired


def _find_matching(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def _to_manifest(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"], name=raw["name"], namespace=raw["namespace"], data=raw["data"]
    )


def _to_live_manifest(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"], name=live["name"], namespace=live["namespace"], data=live["data"]
    )


def _to_response(report: ConfigurationDriftReport) -> ConfigurationDriftDetectionResponse:
    return ConfigurationDriftDetectionResponse(
        drifted_resources=[_to_result_dict(result) for result in report.drifted_resources],
        drifted_by_namespace={
            namespace: [_to_result_dict(result) for result in results]
            for namespace, results in report.drifted_by_namespace.items()
        },
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,
        total_checked=report.total_checked,
        summary=report.summary,
    )


def _to_result_dict(result: DriftResult) -> DriftResultDict:
    managed_by: ManagedBy = result.managed_by
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(field) for field in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def _to_field_dict(drifted_field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=drifted_field.field_path,
        desired_value=drifted_field.desired_value,
        live_value=drifted_field.live_value,
        severity=drifted_field.severity,
    )
