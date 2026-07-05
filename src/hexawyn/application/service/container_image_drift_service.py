from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.application.ports.driven.image_drift_port import (
    ImageDriftPort,
    ResolvedContainerImageRaw,
)
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_response import (
    ContainerImageDriftDict,
    ContainerImageDriftResponse,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (
    ContainerImageDriftServicePort,
)
from hexawyn.domain.models.constants import ConfigurationDriftConstants
from hexawyn.domain.models.image_drift import ContainerImageDrift, ContainerImageDriftReport
from hexawyn.domain.services.image_drift.container_image_extractor import get_container_images
from hexawyn.domain.services.image_drift.drift_classifier import classify_drift
from hexawyn.domain.services.image_drift.drift_severity import classify_severity
from hexawyn.domain.services.image_drift.image_drift_report_builder import build_report
from hexawyn.domain.services.image_drift.image_reference import (
    is_mutable_tag,
    parse_image_reference,
)

_cfg = ConfigurationDriftConstants()

_ResourceKey = tuple[str, str, str]


class ContainerImageDriftService(ContainerImageDriftServicePort):
    def __init__(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter
        self._image_drift_port = image_drift_port

    def detect_image_drift(
        self, command: ContainerImageDriftCommand
    ) -> ContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = []
        in_sync_count = 0
        excluded_count = 0
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = {}
        helm_exists_cache: dict[str, bool] = {}

        for deployment in deployments:
            key: _ResourceKey = (deployment["kind"], deployment["name"], deployment["namespace"])
            if key in kustomize_desired:
                desired_raw, source = kustomize_desired[key]
                source_of_truth = f"kustomize:{source}"
            else:
                release = deployment["annotations"].get(_cfg.helm_release_annotation_key)
                if not release:
                    continue
                if release not in helm_exists_cache:
                    helm_exists_cache[release] = self._helm_adapter.source_exists(
                        release, deployment["namespace"]
                    )
                if not helm_exists_cache[release]:
                    continue
                if release not in helm_manifest_cache:
                    helm_manifest_cache[release] = self._helm_adapter.render_desired_manifests(
                        release, deployment["namespace"]
                    )
                found = _find_matching(
                    helm_manifest_cache[release], deployment["kind"], deployment["name"]
                )
                if found is None:
                    continue
                desired_raw = found
                source_of_truth = f"helm-release:{release}"

            running_images = get_container_images(deployment["data"])
            declared_images = get_container_images(desired_raw["data"])

            for container_name, running_image in running_images.items():
                declared_image = declared_images.get(container_name)
                if declared_image is None:
                    continue
                running_ref = parse_image_reference(running_image)
                if is_mutable_tag(running_ref.tag):
                    excluded_count += 1
                    continue
                declared_ref = parse_image_reference(declared_image)
                image_id = image_id_by_key.get((deployment["name"], container_name))
                drift_type = classify_drift(running_ref, declared_ref, image_id)
                if drift_type is None:
                    in_sync_count += 1
                    continue
                drifts.append(
                    ContainerImageDrift(
                        deployment=deployment["name"],
                        namespace=deployment["namespace"],
                        container=container_name,
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def _render_kustomize_paths(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired


def _index_resolved_images(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["image_id"] for item in resolved}


def _find_matching(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def _to_response(report: ContainerImageDriftReport) -> ContainerImageDriftResponse:
    return ContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def _to_drift_dict(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )
