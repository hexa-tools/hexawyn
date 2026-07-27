from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
from hexawyn.application.ports.driven.image_drift_port import (
    ImageDriftPort,
    ResolvedContainerImageRaw,
)
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (
    ContainerImageDriftDict,
    DetectContainerImageDriftResponse,
)
from hexawyn.domain.models.image_drift import ContainerImageDrift
from hexawyn.domain.services.image_drift.drift_classifier import classify_drift
from hexawyn.domain.services.image_drift.image_drift_report_builder import build_report
from hexawyn.domain.services.image_drift.image_reference import parse_image_reference


class DetectContainerImageDriftUseCase:
    def __init__(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_port = live_resource_port
        self._helm_port = helm_adapter
        self._kustomize_port = kustomize_adapter
        self._image_port = image_drift_port

    def execute(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = {}
        for ri in resolved_images:
            key = f"{ri['deployment']}/{ri['container']}"
            running_by_pod[key] = ri

        helm_releases: set[str] = set()
        for dep in deployments:
            ann = dep.get("annotations", {})
            release = ann.get("meta.helm.sh/release-name", "")
            if release:
                helm_releases.add(release)

        desired_by_deployment: dict[str, dict[str, str]] = {}
        for release in helm_releases:
            if self._helm_port.source_exists(release, namespace):
                desired = self._helm_port.render_desired_manifests(release, namespace)
                for rm in desired:
                    if rm["kind"] == "Deployment":
                        images = _extract_container_images(rm["data"])
                        if images:
                            desired_by_deployment[rm["name"]] = images

        for kp in kustomize_paths:
            if self._kustomize_port.source_exists(kp, namespace):
                desired = self._kustomize_port.render_desired_manifests(kp, namespace)
                for rm in desired:
                    if rm["kind"] == "Deployment":
                        images = _extract_container_images(rm["data"])
                        if images:
                            desired_by_deployment[rm["name"]] = images

        drifts: list[ContainerImageDrift] = []
        in_sync = 0
        excluded_count = 0

        for dep in deployments:
            dep_name = dep["name"]
            declared = desired_by_deployment.get(dep_name, {})
            for container_name, running_raw in running_by_pod.items():
                ctn_name = "/".join(container_name.split("/")[1:])
                dep_ctx_name = container_name.split("/")[0]
                if dep_ctx_name != dep_name:
                    continue

                declared_img = declared.get(ctn_name, "")
                if not declared_img:
                    excluded_count += 1
                    continue

                running_ref = parse_image_reference(running_raw["image_id"])
                declared_ref = parse_image_reference(declared_img)

                drift_type = classify_drift(running_ref, declared_ref, running_raw.get("image_id"))
                if drift_type is None:
                    in_sync += 1
                else:
                    drifts.append(
                        ContainerImageDrift(
                            deployment=dep_name,
                            namespace=namespace,
                            container=ctn_name,
                            running_image=running_raw["image_id"],
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(  # type: ignore
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
                source_of_truth=d.source_of_truth,
                drift_type=d.drift_type,
                severity=d.severity,
            )
            for d in report.out_of_sync
        ]

        return DetectContainerImageDriftResponse(
            out_of_sync=out_of_sync,
            in_sync_count=report.in_sync_count,
            excluded_count=report.excluded_count,
            total_checked=report.total_checked,
            summary=report.summary,
        )


def _extract_container_images(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get("containers", [])
    if not isinstance(containers, list):
        return {}
    result: dict[str, str] = {}
    for c in containers:
        if not isinstance(c, dict):
            continue
        name = c.get("name")
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result
