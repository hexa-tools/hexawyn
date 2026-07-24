from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
from hexawyn.application.use_case.configuration_drift_detection.command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.use_case.configuration_drift_detection.response import (
    ConfigurationDriftDetectionResponse,
)
from hexawyn.domain.models.configuration_drift import ManagedBy, ResourceManifest
from hexawyn.domain.services.configuration_drift.drift_report_builder import build_drift_report
from hexawyn.domain.services.configuration_drift.manifest_diff import compare_resource


class ConfigurationDriftDetectionUseCase:
    def __init__(
        self,
        live_resource_port: LiveResourcePort,
        helm_drift_port: DriftDetectionPort,
        kustomize_drift_port: DriftDetectionPort,
    ) -> None:
        self._live_port = live_resource_port
        self._helm_port = helm_drift_port
        self._kustomize_port = kustomize_drift_port

    def execute(
        self, command: ConfigurationDriftDetectionCommand
    ) -> ConfigurationDriftDetectionResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        live_manifests = {
            f"{r['kind']}/{r['name']}": ResourceManifest(
                kind=r["kind"], name=r["name"], namespace=r["namespace"], data=r["data"]
            )
            for r in live_raw
        }

        helm_releases: set[str] = set()
        for r in live_raw:
            release_name = r.get("labels", {}).get("app.kubernetes.io/managed-by", "")
            if not release_name:
                release_name = r.get("annotations", {}).get("meta.helm.sh/release-name", "")
            if release_name and release_name != "kustomize":
                helm_releases.add(release_name)

        desired_manifests: dict[str, ResourceManifest] = {}
        managed_by_map: dict[str, tuple[ManagedBy, str]] = {}
        for release in helm_releases:
            if self._helm_port.source_exists(release, namespace):
                rendered = self._helm_port.render_desired_manifests(release, namespace)
                for rm in rendered:
                    key = f"{rm['kind']}/{rm['name']}"
                    desired_manifests[key] = ResourceManifest(
                        kind=rm["kind"], name=rm["name"], namespace=rm["namespace"], data=rm["data"]
                    )
                    managed_by_map[key] = ("helm", release)

        for kustomize_path in kustomize_paths:
            if self._kustomize_port.source_exists(kustomize_path, namespace):
                rendered = self._kustomize_port.render_desired_manifests(kustomize_path, namespace)
                for rm in rendered:
                    key = f"{rm['kind']}/{rm['name']}"
                    desired_manifests[key] = ResourceManifest(
                        kind=rm["kind"], name=rm["name"], namespace=rm["namespace"], data=rm["data"]
                    )
                    managed_by_map[key] = ("kustomize", kustomize_path)

        results = []
        excluded: list[str] = []
        for key, live in live_manifests.items():
            if key not in managed_by_map:
                excluded.append(f"{live.kind}/{live.name}")
                continue
            managed_by, source = managed_by_map[key]
            desired = desired_manifests.get(key)
            result = compare_resource(desired, live, managed_by, source)
            results.append(result)

        report = build_drift_report(results, excluded)

        drifted_resources: list[dict[str, object]] = []
        for dr in report.drifted_resources:
            drifted_resources.append(
                {
                    "kind": dr.kind,
                    "name": dr.name,
                    "namespace": dr.namespace,
                    "managed_by": dr.managed_by,
                    "release_or_source": dr.release_or_source,
                    "drifted_fields": [
                        {
                            "field_path": f.field_path,
                            "desired_value": f.desired_value,
                            "live_value": f.live_value,
                            "severity": f.severity,
                        }
                        for f in dr.drifted_fields
                    ],
                    "has_critical_drift": dr.has_critical_drift,
                    "is_orphaned": dr.is_orphaned,
                }
            )

        drifted_by_ns: dict[str, int] = {}
        for ns, drs in report.drifted_by_namespace.items():
            drifted_by_ns[ns] = len(drs)

        return ConfigurationDriftDetectionResponse(
            drifted_resources=drifted_resources,
            drifted_by_namespace=drifted_by_ns,
            in_sync_count=report.in_sync_count,
            excluded_resources=len(report.excluded_resources),
            total_checked=report.total_checked,
            summary=report.summary,
        )
