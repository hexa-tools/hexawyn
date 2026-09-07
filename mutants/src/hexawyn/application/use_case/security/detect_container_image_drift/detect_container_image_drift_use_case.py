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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectContainerImageDriftUseCase:
    @_mutmut_mutated(mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut)
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
    def xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_orig(
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
    def xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_1(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_port = None
        self._helm_port = helm_adapter
        self._kustomize_port = kustomize_adapter
        self._image_port = image_drift_port
    def xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_2(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_port = live_resource_port
        self._helm_port = None
        self._kustomize_port = kustomize_adapter
        self._image_port = image_drift_port
    def xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_3(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_port = live_resource_port
        self._helm_port = helm_adapter
        self._kustomize_port = None
        self._image_port = image_drift_port
    def xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_4(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_port = live_resource_port
        self._helm_port = helm_adapter
        self._kustomize_port = kustomize_adapter
        self._image_port = None

    @_mutmut_mutated(mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_orig(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_1(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_2(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_3(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_4(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_5(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_6(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["XXkindXX"] == "Deployment"]

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_7(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["KIND"] == "Deployment"]

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_8(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] != "Deployment"]

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_9(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "XXDeploymentXX"]

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_10(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "deployment"]

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_11(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "DEPLOYMENT"]

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_12(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_13(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_14(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_15(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = {}
        for ri in resolved_images:
            key = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_16(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = {}
        for ri in resolved_images:
            key = f"{ri['XXdeploymentXX']}/{ri['container']}"
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_17(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = {}
        for ri in resolved_images:
            key = f"{ri['DEPLOYMENT']}/{ri['container']}"
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_18(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = {}
        for ri in resolved_images:
            key = f"{ri['deployment']}/{ri['XXcontainerXX']}"
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_19(  # noqa: C901, PLR0912
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        namespace = command.namespace
        kustomize_paths = command.kustomize_paths if command.kustomize_paths else []

        live_raw = self._live_port.list_live_resources(namespace)
        deployments = [r for r in live_raw if r["kind"] == "Deployment"]

        resolved_images = self._image_port.list_resolved_container_images(namespace)
        running_by_pod: dict[str, ResolvedContainerImageRaw] = {}
        for ri in resolved_images:
            key = f"{ri['deployment']}/{ri['CONTAINER']}"
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_20(  # noqa: C901, PLR0912
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
            running_by_pod[key] = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_21(  # noqa: C901, PLR0912
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

        helm_releases: set[str] = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_22(  # noqa: C901, PLR0912
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
            ann = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_23(  # noqa: C901, PLR0912
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
            ann = dep.get(None, {})
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_24(  # noqa: C901, PLR0912
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
            ann = dep.get("annotations", None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_25(  # noqa: C901, PLR0912
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
            ann = dep.get({})
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_26(  # noqa: C901, PLR0912
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
            ann = dep.get("annotations", )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_27(  # noqa: C901, PLR0912
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
            ann = dep.get("XXannotationsXX", {})
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_28(  # noqa: C901, PLR0912
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
            ann = dep.get("ANNOTATIONS", {})
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_29(  # noqa: C901, PLR0912
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
            release = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_30(  # noqa: C901, PLR0912
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
            release = ann.get(None, "")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_31(  # noqa: C901, PLR0912
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
            release = ann.get("meta.helm.sh/release-name", None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_32(  # noqa: C901, PLR0912
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
            release = ann.get("")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_33(  # noqa: C901, PLR0912
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
            release = ann.get("meta.helm.sh/release-name", )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_34(  # noqa: C901, PLR0912
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
            release = ann.get("XXmeta.helm.sh/release-nameXX", "")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_35(  # noqa: C901, PLR0912
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
            release = ann.get("META.HELM.SH/RELEASE-NAME", "")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_36(  # noqa: C901, PLR0912
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
            release = ann.get("meta.helm.sh/release-name", "XXXX")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_37(  # noqa: C901, PLR0912
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
                helm_releases.add(None)

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_38(  # noqa: C901, PLR0912
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

        desired_by_deployment: dict[str, dict[str, str]] = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_39(  # noqa: C901, PLR0912
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
            if self._helm_port.source_exists(None, namespace):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_40(  # noqa: C901, PLR0912
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
            if self._helm_port.source_exists(release, None):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_41(  # noqa: C901, PLR0912
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
            if self._helm_port.source_exists(namespace):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_42(  # noqa: C901, PLR0912
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
            if self._helm_port.source_exists(release, ):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_43(  # noqa: C901, PLR0912
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
                desired = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_44(  # noqa: C901, PLR0912
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
                desired = self._helm_port.render_desired_manifests(None, namespace)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_45(  # noqa: C901, PLR0912
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
                desired = self._helm_port.render_desired_manifests(release, None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_46(  # noqa: C901, PLR0912
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
                desired = self._helm_port.render_desired_manifests(namespace)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_47(  # noqa: C901, PLR0912
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
                desired = self._helm_port.render_desired_manifests(release, )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_48(  # noqa: C901, PLR0912
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
                    if rm["XXkindXX"] == "Deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_49(  # noqa: C901, PLR0912
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
                    if rm["KIND"] == "Deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_50(  # noqa: C901, PLR0912
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
                    if rm["kind"] != "Deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_51(  # noqa: C901, PLR0912
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
                    if rm["kind"] == "XXDeploymentXX":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_52(  # noqa: C901, PLR0912
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
                    if rm["kind"] == "deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_53(  # noqa: C901, PLR0912
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
                    if rm["kind"] == "DEPLOYMENT":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_54(  # noqa: C901, PLR0912
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
                        images = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_55(  # noqa: C901, PLR0912
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
                        images = _extract_container_images(None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_56(  # noqa: C901, PLR0912
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
                        images = _extract_container_images(rm["XXdataXX"])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_57(  # noqa: C901, PLR0912
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
                        images = _extract_container_images(rm["DATA"])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_58(  # noqa: C901, PLR0912
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
                            desired_by_deployment[rm["name"]] = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_59(  # noqa: C901, PLR0912
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
                            desired_by_deployment[rm["XXnameXX"]] = images

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_60(  # noqa: C901, PLR0912
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
                            desired_by_deployment[rm["NAME"]] = images

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_61(  # noqa: C901, PLR0912
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
            if self._kustomize_port.source_exists(None, namespace):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_62(  # noqa: C901, PLR0912
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
            if self._kustomize_port.source_exists(kp, None):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_63(  # noqa: C901, PLR0912
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
            if self._kustomize_port.source_exists(namespace):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_64(  # noqa: C901, PLR0912
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
            if self._kustomize_port.source_exists(kp, ):
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_65(  # noqa: C901, PLR0912
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
                desired = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_66(  # noqa: C901, PLR0912
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
                desired = self._kustomize_port.render_desired_manifests(None, namespace)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_67(  # noqa: C901, PLR0912
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
                desired = self._kustomize_port.render_desired_manifests(kp, None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_68(  # noqa: C901, PLR0912
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
                desired = self._kustomize_port.render_desired_manifests(namespace)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_69(  # noqa: C901, PLR0912
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
                desired = self._kustomize_port.render_desired_manifests(kp, )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_70(  # noqa: C901, PLR0912
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
                    if rm["XXkindXX"] == "Deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_71(  # noqa: C901, PLR0912
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
                    if rm["KIND"] == "Deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_72(  # noqa: C901, PLR0912
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
                    if rm["kind"] != "Deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_73(  # noqa: C901, PLR0912
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
                    if rm["kind"] == "XXDeploymentXX":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_74(  # noqa: C901, PLR0912
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
                    if rm["kind"] == "deployment":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_75(  # noqa: C901, PLR0912
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
                    if rm["kind"] == "DEPLOYMENT":
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_76(  # noqa: C901, PLR0912
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
                        images = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_77(  # noqa: C901, PLR0912
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
                        images = _extract_container_images(None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_78(  # noqa: C901, PLR0912
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
                        images = _extract_container_images(rm["XXdataXX"])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_79(  # noqa: C901, PLR0912
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
                        images = _extract_container_images(rm["DATA"])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_80(  # noqa: C901, PLR0912
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
                            desired_by_deployment[rm["name"]] = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_81(  # noqa: C901, PLR0912
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
                            desired_by_deployment[rm["XXnameXX"]] = images

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_82(  # noqa: C901, PLR0912
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
                            desired_by_deployment[rm["NAME"]] = images

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_83(  # noqa: C901, PLR0912
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

        drifts: list[ContainerImageDrift] = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_84(  # noqa: C901, PLR0912
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
        in_sync = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_85(  # noqa: C901, PLR0912
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
        in_sync = 1
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_86(  # noqa: C901, PLR0912
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
        excluded_count = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_87(  # noqa: C901, PLR0912
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
        excluded_count = 1

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_88(  # noqa: C901, PLR0912
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
            dep_name = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_89(  # noqa: C901, PLR0912
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
            dep_name = dep["XXnameXX"]
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_90(  # noqa: C901, PLR0912
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
            dep_name = dep["NAME"]
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_91(  # noqa: C901, PLR0912
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
            declared = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_92(  # noqa: C901, PLR0912
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
            declared = desired_by_deployment.get(None, {})
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_93(  # noqa: C901, PLR0912
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
            declared = desired_by_deployment.get(dep_name, None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_94(  # noqa: C901, PLR0912
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
            declared = desired_by_deployment.get({})
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_95(  # noqa: C901, PLR0912
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
            declared = desired_by_deployment.get(dep_name, )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_96(  # noqa: C901, PLR0912
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
                ctn_name = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_97(  # noqa: C901, PLR0912
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
                ctn_name = "/".join(None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_98(  # noqa: C901, PLR0912
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
                ctn_name = "XX/XX".join(container_name.split("/")[1:])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_99(  # noqa: C901, PLR0912
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
                ctn_name = "/".join(container_name.split(None)[1:])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_100(  # noqa: C901, PLR0912
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
                ctn_name = "/".join(container_name.split("XX/XX")[1:])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_101(  # noqa: C901, PLR0912
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
                ctn_name = "/".join(container_name.split("/")[2:])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_102(  # noqa: C901, PLR0912
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
                dep_ctx_name = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_103(  # noqa: C901, PLR0912
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
                dep_ctx_name = container_name.split(None)[0]
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_104(  # noqa: C901, PLR0912
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
                dep_ctx_name = container_name.split("XX/XX")[0]
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_105(  # noqa: C901, PLR0912
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
                dep_ctx_name = container_name.split("/")[1]
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_106(  # noqa: C901, PLR0912
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
                if dep_ctx_name == dep_name:
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_107(  # noqa: C901, PLR0912
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
                    break

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_108(  # noqa: C901, PLR0912
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

                declared_img = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_109(  # noqa: C901, PLR0912
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

                declared_img = declared.get(None, "")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_110(  # noqa: C901, PLR0912
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

                declared_img = declared.get(ctn_name, None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_111(  # noqa: C901, PLR0912
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

                declared_img = declared.get("")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_112(  # noqa: C901, PLR0912
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

                declared_img = declared.get(ctn_name, )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_113(  # noqa: C901, PLR0912
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

                declared_img = declared.get(ctn_name, "XXXX")
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_114(  # noqa: C901, PLR0912
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
                if declared_img:
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_115(  # noqa: C901, PLR0912
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
                    excluded_count = 1
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_116(  # noqa: C901, PLR0912
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
                    excluded_count -= 1
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_117(  # noqa: C901, PLR0912
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
                    excluded_count += 2
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_118(  # noqa: C901, PLR0912
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
                    break

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_119(  # noqa: C901, PLR0912
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

                running_ref = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_120(  # noqa: C901, PLR0912
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

                running_ref = parse_image_reference(None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_121(  # noqa: C901, PLR0912
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

                running_ref = parse_image_reference(running_raw["XXimage_idXX"])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_122(  # noqa: C901, PLR0912
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

                running_ref = parse_image_reference(running_raw["IMAGE_ID"])
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_123(  # noqa: C901, PLR0912
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
                declared_ref = None

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_124(  # noqa: C901, PLR0912
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
                declared_ref = parse_image_reference(None)

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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_125(  # noqa: C901, PLR0912
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

                drift_type = None
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_126(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(None, declared_ref, running_raw.get("image_id"))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_127(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, None, running_raw.get("image_id"))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_128(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, declared_ref, None)
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_129(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(declared_ref, running_raw.get("image_id"))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_130(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, running_raw.get("image_id"))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_131(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, declared_ref, )
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_132(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, declared_ref, running_raw.get(None))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_133(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, declared_ref, running_raw.get("XXimage_idXX"))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_134(  # noqa: C901, PLR0912
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

                drift_type = classify_drift(running_ref, declared_ref, running_raw.get("IMAGE_ID"))
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_135(  # noqa: C901, PLR0912
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
                if drift_type is not None:
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_136(  # noqa: C901, PLR0912
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
                    in_sync = 1
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_137(  # noqa: C901, PLR0912
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
                    in_sync -= 1
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_138(  # noqa: C901, PLR0912
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
                    in_sync += 2
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_139(  # noqa: C901, PLR0912
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
                        None
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_140(  # noqa: C901, PLR0912
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
                            deployment=None,
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_141(  # noqa: C901, PLR0912
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
                            namespace=None,
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_142(  # noqa: C901, PLR0912
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
                            container=None,
                            running_image=running_raw["image_id"],
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_143(  # noqa: C901, PLR0912
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
                            running_image=None,
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_144(  # noqa: C901, PLR0912
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
                            declared_image=None,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_145(  # noqa: C901, PLR0912
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
                            source_of_truth=None,
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_146(  # noqa: C901, PLR0912
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
                            drift_type=None,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_147(  # noqa: C901, PLR0912
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
                            severity=None,
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_148(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_149(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_150(  # noqa: C901, PLR0912
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
                            running_image=running_raw["image_id"],
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_151(  # noqa: C901, PLR0912
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
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_152(  # noqa: C901, PLR0912
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
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_153(  # noqa: C901, PLR0912
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
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_154(  # noqa: C901, PLR0912
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
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_155(  # noqa: C901, PLR0912
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
                            )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_156(  # noqa: C901, PLR0912
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
                            running_image=running_raw["XXimage_idXX"],
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_157(  # noqa: C901, PLR0912
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
                            running_image=running_raw["IMAGE_ID"],
                            declared_image=declared_img,
                            source_of_truth="helm",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_158(  # noqa: C901, PLR0912
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
                            source_of_truth="XXhelmXX",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_159(  # noqa: C901, PLR0912
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
                            source_of_truth="HELM",
                            drift_type=drift_type,
                            severity="critical",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_160(  # noqa: C901, PLR0912
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
                            severity="XXcriticalXX",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_161(  # noqa: C901, PLR0912
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
                            severity="CRITICAL",
                        )
                    )

        report = build_report(drifts, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_162(  # noqa: C901, PLR0912
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

        report = None

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_163(  # noqa: C901, PLR0912
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

        report = build_report(None, in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_164(  # noqa: C901, PLR0912
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

        report = build_report(drifts, None, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_165(  # noqa: C901, PLR0912
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

        report = build_report(drifts, in_sync, None)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_166(  # noqa: C901, PLR0912
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

        report = build_report(in_sync, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_167(  # noqa: C901, PLR0912
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

        report = build_report(drifts, excluded_count)

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_168(  # noqa: C901, PLR0912
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

        report = build_report(drifts, in_sync, )

        out_of_sync: list[ContainerImageDriftDict] = [
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_169(  # noqa: C901, PLR0912
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

        out_of_sync: list[ContainerImageDriftDict] = None

        return DetectContainerImageDriftResponse(
            out_of_sync=out_of_sync,
            in_sync_count=report.in_sync_count,
            excluded_count=report.excluded_count,
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_170(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_171(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_172(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_173(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_174(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_175(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
                source_of_truth=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_176(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
                source_of_truth=d.source_of_truth,
                drift_type=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_177(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
                source_of_truth=d.source_of_truth,
                drift_type=d.drift_type,
                severity=None,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_178(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_179(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_180(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_181(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_182(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_183(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_184(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
                source_of_truth=d.source_of_truth,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_185(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
                deployment=d.deployment,
                namespace=d.namespace,
                container=d.container,
                running_image=d.running_image,
                declared_image=d.declared_image,
                source_of_truth=d.source_of_truth,
                drift_type=d.drift_type,
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

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_186(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            out_of_sync=None,
            in_sync_count=report.in_sync_count,
            excluded_count=report.excluded_count,
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_187(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            in_sync_count=None,
            excluded_count=report.excluded_count,
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_188(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            excluded_count=None,
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_189(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            total_checked=None,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_190(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            summary=None,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_191(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            in_sync_count=report.in_sync_count,
            excluded_count=report.excluded_count,
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_192(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            excluded_count=report.excluded_count,
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_193(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            total_checked=report.total_checked,
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_194(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            summary=report.summary,
        )

    def xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_195(  # noqa: C901, PLR0912
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
            ContainerImageDriftDict(
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
            )

mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut['xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_1'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut['xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_2'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut['xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_3'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁ__init____mutmut['xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_4'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_1'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_2'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_3'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_4'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_5'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_6'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_7'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_8'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_9'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_10'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_11'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_12'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_13'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_14'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_15'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_16'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_17'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_18'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_19'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_20'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_21'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_22'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_23'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_24'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_25'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_26'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_27'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_28'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_29'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_30'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_31'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_32'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_33'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_34'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_35'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_36'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_37'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_38'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_39'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_40'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_41'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_42'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_43'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_44'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_45'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_46'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_47'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_48'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_49'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_50'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_51'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_52'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_53'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_54'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_55'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_56'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_57'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_58'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_59'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_60'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_61'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_62'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_63'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_64'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_65'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_66'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_67'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_68'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_69'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_70'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_71'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_72'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_73'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_74'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_75'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_76'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_77'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_78'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_79'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_80'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_81'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_82'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_83'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_84'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_85'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_86'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_87'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_88'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_89'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_90'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_91'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_92'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_93'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_94'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_95'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_96'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_97'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_98'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_99'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_99 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_100'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_100 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_101'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_101 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_102'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_102 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_103'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_103 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_104'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_104 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_105'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_105 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_106'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_106 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_107'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_107 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_108'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_108 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_109'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_109 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_110'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_110 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_111'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_111 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_112'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_112 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_113'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_113 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_114'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_114 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_115'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_115 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_116'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_116 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_117'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_117 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_118'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_118 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_119'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_119 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_120'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_120 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_121'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_121 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_122'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_122 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_123'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_123 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_124'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_124 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_125'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_125 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_126'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_126 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_127'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_127 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_128'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_128 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_129'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_129 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_130'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_130 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_131'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_131 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_132'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_132 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_133'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_133 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_134'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_134 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_135'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_135 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_136'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_136 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_137'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_137 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_138'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_138 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_139'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_139 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_140'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_140 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_141'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_141 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_142'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_142 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_143'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_143 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_144'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_144 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_145'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_145 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_146'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_146 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_147'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_147 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_148'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_148 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_149'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_149 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_150'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_150 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_151'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_151 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_152'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_152 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_153'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_153 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_154'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_154 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_155'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_155 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_156'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_156 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_157'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_157 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_158'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_158 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_159'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_159 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_160'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_160 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_161'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_161 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_162'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_162 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_163'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_163 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_164'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_164 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_165'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_165 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_166'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_166 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_167'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_167 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_168'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_168 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_169'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_169 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_170'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_170 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_171'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_171 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_172'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_172 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_173'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_173 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_174'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_174 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_175'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_175 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_176'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_176 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_177'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_177 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_178'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_178 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_179'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_179 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_180'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_180 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_181'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_181 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_182'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_182 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_183'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_183 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_184'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_184 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_185'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_185 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_186'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_186 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_187'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_187 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_188'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_188 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_189'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_189 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_190'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_190 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_191'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_191 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_192'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_192 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_193'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_193 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_194'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_194 # type: ignore # mutmut generated
mutants_xǁDetectContainerImageDriftUseCaseǁexecute__mutmut['xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_195'] = DetectContainerImageDriftUseCase.xǁDetectContainerImageDriftUseCaseǁexecute__mutmut_195 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_container_images__mutmut)
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


def x__extract_container_images__mutmut_orig(data: dict[str, object]) -> dict[str, str]:
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


def x__extract_container_images__mutmut_1(data: dict[str, object]) -> dict[str, str]:
    spec = None
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


def x__extract_container_images__mutmut_2(data: dict[str, object]) -> dict[str, str]:
    spec = data.get(None, {})
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


def x__extract_container_images__mutmut_3(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", None)
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


def x__extract_container_images__mutmut_4(data: dict[str, object]) -> dict[str, str]:
    spec = data.get({})
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


def x__extract_container_images__mutmut_5(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", )
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


def x__extract_container_images__mutmut_6(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("XXspecXX", {})
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


def x__extract_container_images__mutmut_7(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("SPEC", {})
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


def x__extract_container_images__mutmut_8(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if isinstance(spec, dict):
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


def x__extract_container_images__mutmut_9(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = None
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


def x__extract_container_images__mutmut_10(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get(None, {})
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


def x__extract_container_images__mutmut_11(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", None)
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


def x__extract_container_images__mutmut_12(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get({})
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


def x__extract_container_images__mutmut_13(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", )
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


def x__extract_container_images__mutmut_14(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("XXtemplateXX", {})
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


def x__extract_container_images__mutmut_15(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("TEMPLATE", {})
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


def x__extract_container_images__mutmut_16(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if isinstance(template, dict):
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


def x__extract_container_images__mutmut_17(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = None
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


def x__extract_container_images__mutmut_18(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get(None, {})
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


def x__extract_container_images__mutmut_19(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", None)
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


def x__extract_container_images__mutmut_20(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get({})
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


def x__extract_container_images__mutmut_21(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", )
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


def x__extract_container_images__mutmut_22(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("XXspecXX", {})
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


def x__extract_container_images__mutmut_23(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("SPEC", {})
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


def x__extract_container_images__mutmut_24(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if isinstance(pod_spec, dict):
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


def x__extract_container_images__mutmut_25(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = None
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


def x__extract_container_images__mutmut_26(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get(None, [])
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


def x__extract_container_images__mutmut_27(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get("containers", None)
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


def x__extract_container_images__mutmut_28(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get([])
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


def x__extract_container_images__mutmut_29(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get("containers", )
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


def x__extract_container_images__mutmut_30(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get("XXcontainersXX", [])
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


def x__extract_container_images__mutmut_31(data: dict[str, object]) -> dict[str, str]:
    spec = data.get("spec", {})
    if not isinstance(spec, dict):
        return {}
    template = spec.get("template", {})
    if not isinstance(template, dict):
        return {}
    pod_spec = template.get("spec", {})
    if not isinstance(pod_spec, dict):
        return {}
    containers = pod_spec.get("CONTAINERS", [])
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


def x__extract_container_images__mutmut_32(data: dict[str, object]) -> dict[str, str]:
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
    if isinstance(containers, list):
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


def x__extract_container_images__mutmut_33(data: dict[str, object]) -> dict[str, str]:
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
    result: dict[str, str] = None
    for c in containers:
        if not isinstance(c, dict):
            continue
        name = c.get("name")
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_34(data: dict[str, object]) -> dict[str, str]:
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
        if isinstance(c, dict):
            continue
        name = c.get("name")
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_35(data: dict[str, object]) -> dict[str, str]:
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
            break
        name = c.get("name")
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_36(data: dict[str, object]) -> dict[str, str]:
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
        name = None
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_37(data: dict[str, object]) -> dict[str, str]:
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
        name = c.get(None)
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_38(data: dict[str, object]) -> dict[str, str]:
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
        name = c.get("XXnameXX")
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_39(data: dict[str, object]) -> dict[str, str]:
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
        name = c.get("NAME")
        image = c.get("image")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_40(data: dict[str, object]) -> dict[str, str]:
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
        image = None
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_41(data: dict[str, object]) -> dict[str, str]:
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
        image = c.get(None)
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_42(data: dict[str, object]) -> dict[str, str]:
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
        image = c.get("XXimageXX")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_43(data: dict[str, object]) -> dict[str, str]:
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
        image = c.get("IMAGE")
        if name and image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_44(data: dict[str, object]) -> dict[str, str]:
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
        if name and image and isinstance(name, str) or isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_45(data: dict[str, object]) -> dict[str, str]:
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
        if name and image or isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_46(data: dict[str, object]) -> dict[str, str]:
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
        if name or image and isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x__extract_container_images__mutmut_47(data: dict[str, object]) -> dict[str, str]:
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
            result[name] = None
    return result

mutants_x__extract_container_images__mutmut['_mutmut_orig'] = x__extract_container_images__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_1'] = x__extract_container_images__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_2'] = x__extract_container_images__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_3'] = x__extract_container_images__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_4'] = x__extract_container_images__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_5'] = x__extract_container_images__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_6'] = x__extract_container_images__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_7'] = x__extract_container_images__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_8'] = x__extract_container_images__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_9'] = x__extract_container_images__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_10'] = x__extract_container_images__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_11'] = x__extract_container_images__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_12'] = x__extract_container_images__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_13'] = x__extract_container_images__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_14'] = x__extract_container_images__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_15'] = x__extract_container_images__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_16'] = x__extract_container_images__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_17'] = x__extract_container_images__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_18'] = x__extract_container_images__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_19'] = x__extract_container_images__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_20'] = x__extract_container_images__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_21'] = x__extract_container_images__mutmut_21 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_22'] = x__extract_container_images__mutmut_22 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_23'] = x__extract_container_images__mutmut_23 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_24'] = x__extract_container_images__mutmut_24 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_25'] = x__extract_container_images__mutmut_25 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_26'] = x__extract_container_images__mutmut_26 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_27'] = x__extract_container_images__mutmut_27 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_28'] = x__extract_container_images__mutmut_28 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_29'] = x__extract_container_images__mutmut_29 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_30'] = x__extract_container_images__mutmut_30 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_31'] = x__extract_container_images__mutmut_31 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_32'] = x__extract_container_images__mutmut_32 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_33'] = x__extract_container_images__mutmut_33 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_34'] = x__extract_container_images__mutmut_34 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_35'] = x__extract_container_images__mutmut_35 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_36'] = x__extract_container_images__mutmut_36 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_37'] = x__extract_container_images__mutmut_37 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_38'] = x__extract_container_images__mutmut_38 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_39'] = x__extract_container_images__mutmut_39 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_40'] = x__extract_container_images__mutmut_40 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_41'] = x__extract_container_images__mutmut_41 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_42'] = x__extract_container_images__mutmut_42 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_43'] = x__extract_container_images__mutmut_43 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_44'] = x__extract_container_images__mutmut_44 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_45'] = x__extract_container_images__mutmut_45 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_46'] = x__extract_container_images__mutmut_46 # type: ignore # mutmut generated
mutants_x__extract_container_images__mutmut['x__extract_container_images__mutmut_47'] = x__extract_container_images__mutmut_47 # type: ignore # mutmut generated
