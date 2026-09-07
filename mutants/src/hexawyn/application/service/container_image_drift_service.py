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
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (  # noqa: E501
    ContainerImageDriftServicePort,
)
from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (
    ContainerImageDriftDict,
    DetectContainerImageDriftResponse,
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁContainerImageDriftServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut: MutantDict = {}  # type: ignore


class ContainerImageDriftService(ContainerImageDriftServicePort):
    @_mutmut_mutated(mutants_xǁContainerImageDriftServiceǁ__init____mutmut)
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
    def xǁContainerImageDriftServiceǁ__init____mutmut_orig(
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
    def xǁContainerImageDriftServiceǁ__init____mutmut_1(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_resource_port = None
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter
        self._image_drift_port = image_drift_port
    def xǁContainerImageDriftServiceǁ__init____mutmut_2(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = None
        self._kustomize_adapter = kustomize_adapter
        self._image_drift_port = image_drift_port
    def xǁContainerImageDriftServiceǁ__init____mutmut_3(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = None
        self._image_drift_port = image_drift_port
    def xǁContainerImageDriftServiceǁ__init____mutmut_4(
        self,
        live_resource_port: LiveResourcePort,
        helm_adapter: DriftDetectionPort,
        kustomize_adapter: DriftDetectionPort,
        image_drift_port: ImageDriftPort,
    ) -> None:
        self._live_resource_port = live_resource_port
        self._helm_adapter = helm_adapter
        self._kustomize_adapter = kustomize_adapter
        self._image_drift_port = None

    @_mutmut_mutated(mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut)
    def detect_image_drift(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_orig(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_1(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_2(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_3(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_4(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["XXkindXX"] == "Deployment"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_5(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["KIND"] == "Deployment"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_6(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] != "Deployment"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_7(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "XXDeploymentXX"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_8(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "deployment"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_9(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "DEPLOYMENT"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_10(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_11(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(None, command.namespace)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_12(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_13(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.namespace)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_14(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, )
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_15(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = None

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_16(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_17(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_18(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_19(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = []
        in_sync_count = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_20(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = []
        in_sync_count = 1
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_21(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = []
        in_sync_count = 0
        excluded_count = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_22(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = []
        in_sync_count = 0
        excluded_count = 1
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_23(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
        live_resources = self._live_resource_port.list_live_resources(command.namespace)
        deployments = [resource for resource in live_resources if resource["kind"] == "Deployment"]
        kustomize_desired = self._render_kustomize_paths(command.kustomize_paths, command.namespace)
        image_id_by_key = _index_resolved_images(
            self._image_drift_port.list_resolved_container_images(command.namespace)
        )

        drifts: list[ContainerImageDrift] = []
        in_sync_count = 0
        excluded_count = 0
        helm_manifest_cache: dict[str, list[ResourceManifestRaw]] = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_24(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
        helm_exists_cache: dict[str, bool] = None

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_25(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_26(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = (deployment["XXkindXX"], deployment["name"], deployment["namespace"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_27(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = (deployment["KIND"], deployment["name"], deployment["namespace"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_28(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = (deployment["kind"], deployment["XXnameXX"], deployment["namespace"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_29(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = (deployment["kind"], deployment["NAME"], deployment["namespace"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_30(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = (deployment["kind"], deployment["name"], deployment["XXnamespaceXX"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_31(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            key: _ResourceKey = (deployment["kind"], deployment["name"], deployment["NAMESPACE"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_32(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            if key not in kustomize_desired:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_33(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                desired_raw, source = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_34(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                source_of_truth = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_35(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                release = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_36(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                release = deployment["annotations"].get(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_37(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                release = deployment["XXannotationsXX"].get(_cfg.helm_release_annotation_key)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_38(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                release = deployment["ANNOTATIONS"].get(_cfg.helm_release_annotation_key)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_39(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if release:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_40(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    break
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_41(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if release in helm_exists_cache:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_42(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_exists_cache[release] = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_43(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        None, deployment["namespace"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_44(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_45(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        deployment["namespace"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_46(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, )
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_47(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, deployment["XXnamespaceXX"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_48(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, deployment["NAMESPACE"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_49(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if helm_exists_cache[release]:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_50(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    break
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_51(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if release in helm_manifest_cache:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_52(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release] = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_53(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        None, deployment["namespace"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_54(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_55(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        deployment["namespace"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_56(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, )
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_57(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, deployment["XXnamespaceXX"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_58(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        release, deployment["NAMESPACE"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_59(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                found = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_60(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    None, deployment["kind"], deployment["name"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_61(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], None, deployment["name"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_62(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["kind"], None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_63(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    deployment["kind"], deployment["name"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_64(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["name"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_65(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["kind"], )
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_66(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["XXkindXX"], deployment["name"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_67(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["KIND"], deployment["name"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_68(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["kind"], deployment["XXnameXX"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_69(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    helm_manifest_cache[release], deployment["kind"], deployment["NAME"]
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_70(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if found is not None:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_71(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    break
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_72(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                desired_raw = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_73(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                source_of_truth = None

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_74(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

            running_images = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_75(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

            running_images = get_container_images(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_76(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

            running_images = get_container_images(deployment["XXdataXX"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_77(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

            running_images = get_container_images(deployment["DATA"])
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_78(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            declared_images = None

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_79(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            declared_images = get_container_images(None)

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_80(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            declared_images = get_container_images(desired_raw["XXdataXX"])

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_81(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
            declared_images = get_container_images(desired_raw["DATA"])

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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_82(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                declared_image = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_83(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                declared_image = declared_images.get(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_84(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if declared_image is not None:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_85(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    break
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_86(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                running_ref = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_87(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                running_ref = parse_image_reference(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_88(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if is_mutable_tag(None):
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_89(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    excluded_count = 1
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_90(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    excluded_count -= 1
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_91(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    excluded_count += 2
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_92(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    break
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_93(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                declared_ref = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_94(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                declared_ref = parse_image_reference(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_95(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                image_id = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_96(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                image_id = image_id_by_key.get(None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_97(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                image_id = image_id_by_key.get((deployment["XXnameXX"], container_name))
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_98(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                image_id = image_id_by_key.get((deployment["NAME"], container_name))
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_99(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = None
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_100(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = classify_drift(None, declared_ref, image_id)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_101(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = classify_drift(running_ref, None, image_id)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_102(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = classify_drift(running_ref, declared_ref, None)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_103(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = classify_drift(declared_ref, image_id)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_104(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = classify_drift(running_ref, image_id)
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_105(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                drift_type = classify_drift(running_ref, declared_ref, )
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_106(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                if drift_type is not None:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_107(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    in_sync_count = 1
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_108(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    in_sync_count -= 1
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_109(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    in_sync_count += 2
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_110(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    break
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_111(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                    None
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_112(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        deployment=None,
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_113(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        namespace=None,
                        container=container_name,
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_114(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        container=None,
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_115(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        running_image=None,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_116(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        declared_image=None,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_117(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        source_of_truth=None,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_118(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        drift_type=None,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_119(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        severity=None,
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_120(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_121(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        container=container_name,
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_122(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_123(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_124(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_125(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_126(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_127(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_128(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        deployment=deployment["XXnameXX"],
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_129(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        deployment=deployment["NAME"],
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

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_130(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        namespace=deployment["XXnamespaceXX"],
                        container=container_name,
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_131(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        namespace=deployment["NAMESPACE"],
                        container=container_name,
                        running_image=running_image,
                        declared_image=declared_image,
                        source_of_truth=source_of_truth,
                        drift_type=drift_type,
                        severity=classify_severity(drift_type),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_132(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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
                        severity=classify_severity(None),
                    )
                )

        return _to_response(build_report(drifts, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_133(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(None)

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_134(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(build_report(None, in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_135(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(build_report(drifts, None, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_136(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(build_report(drifts, in_sync_count, None))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_137(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(build_report(in_sync_count, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_138(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(build_report(drifts, excluded_count))

    def xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_139(  # noqa: C901
        self, command: DetectContainerImageDriftCommand
    ) -> DetectContainerImageDriftResponse:
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

        return _to_response(build_report(drifts, in_sync_count, ))

    @_mutmut_mutated(mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut)
    def _render_kustomize_paths(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_orig(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_1(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = None
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_2(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(None, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_3(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, None):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_4(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_5(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, ):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_6(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = None
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_7(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] and namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_8(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["XXnamespaceXX"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_9(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["NAMESPACE"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_10(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["name"], resolved_namespace)] = None
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_11(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["XXkindXX"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_12(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["KIND"], raw["name"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_13(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["XXnameXX"], resolved_namespace)] = (raw, path)
        return desired

    def xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_14(
        self, paths: list[str], namespace: str
    ) -> dict[_ResourceKey, tuple[ResourceManifestRaw, str]]:
        desired: dict[_ResourceKey, tuple[ResourceManifestRaw, str]] = {}
        for path in paths:
            for raw in self._kustomize_adapter.render_desired_manifests(path, namespace):
                resolved_namespace = raw["namespace"] or namespace
                desired[(raw["kind"], raw["NAME"], resolved_namespace)] = (raw, path)
        return desired

mutants_xǁContainerImageDriftServiceǁ__init____mutmut['_mutmut_orig'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ__init____mutmut['xǁContainerImageDriftServiceǁ__init____mutmut_1'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ__init____mutmut['xǁContainerImageDriftServiceǁ__init____mutmut_2'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ__init____mutmut['xǁContainerImageDriftServiceǁ__init____mutmut_3'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ__init____mutmut['xǁContainerImageDriftServiceǁ__init____mutmut_4'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['_mutmut_orig'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_1'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_2'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_3'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_4'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_5'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_6'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_7'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_8'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_9'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_9 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_10'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_10 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_11'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_11 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_12'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_12 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_13'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_13 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_14'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_14 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_15'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_15 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_16'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_16 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_17'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_17 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_18'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_18 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_19'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_19 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_20'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_20 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_21'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_21 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_22'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_22 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_23'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_23 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_24'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_24 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_25'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_25 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_26'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_26 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_27'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_27 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_28'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_28 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_29'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_29 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_30'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_30 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_31'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_31 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_32'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_32 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_33'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_33 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_34'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_34 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_35'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_35 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_36'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_36 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_37'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_37 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_38'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_38 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_39'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_39 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_40'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_40 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_41'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_41 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_42'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_42 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_43'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_43 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_44'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_44 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_45'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_45 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_46'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_46 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_47'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_47 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_48'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_48 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_49'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_49 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_50'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_50 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_51'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_51 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_52'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_52 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_53'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_53 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_54'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_54 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_55'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_55 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_56'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_56 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_57'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_57 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_58'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_58 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_59'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_59 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_60'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_60 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_61'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_61 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_62'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_62 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_63'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_63 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_64'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_64 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_65'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_65 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_66'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_66 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_67'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_67 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_68'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_68 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_69'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_69 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_70'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_70 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_71'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_71 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_72'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_72 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_73'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_73 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_74'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_74 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_75'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_75 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_76'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_76 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_77'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_77 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_78'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_78 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_79'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_79 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_80'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_80 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_81'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_81 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_82'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_82 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_83'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_83 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_84'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_84 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_85'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_85 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_86'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_86 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_87'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_87 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_88'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_88 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_89'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_89 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_90'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_90 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_91'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_91 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_92'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_92 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_93'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_93 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_94'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_94 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_95'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_95 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_96'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_96 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_97'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_97 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_98'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_98 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_99'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_99 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_100'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_100 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_101'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_101 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_102'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_102 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_103'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_103 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_104'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_104 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_105'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_105 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_106'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_106 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_107'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_107 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_108'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_108 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_109'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_109 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_110'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_110 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_111'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_111 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_112'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_112 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_113'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_113 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_114'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_114 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_115'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_115 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_116'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_116 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_117'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_117 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_118'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_118 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_119'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_119 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_120'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_120 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_121'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_121 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_122'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_122 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_123'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_123 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_124'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_124 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_125'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_125 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_126'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_126 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_127'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_127 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_128'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_128 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_129'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_129 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_130'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_130 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_131'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_131 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_132'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_132 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_133'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_133 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_134'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_134 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_135'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_135 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_136'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_136 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_137'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_137 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_138'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_138 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁdetect_image_drift__mutmut['xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_139'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁdetect_image_drift__mutmut_139 # type: ignore # mutmut generated

mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['_mutmut_orig'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_1'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_2'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_3'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_4'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_5'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_6'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_7'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_8'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_9'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_9 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_10'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_10 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_11'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_11 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_12'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_12 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_13'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_13 # type: ignore # mutmut generated
mutants_xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut['xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_14'] = ContainerImageDriftService.xǁContainerImageDriftServiceǁ_render_kustomize_paths__mutmut_14 # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__index_resolved_images__mutmut)
def _index_resolved_images(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["image_id"] for item in resolved}


def x__index_resolved_images__mutmut_orig(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["image_id"] for item in resolved}


def x__index_resolved_images__mutmut_1(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["XXdeploymentXX"], item["container"]): item["image_id"] for item in resolved}


def x__index_resolved_images__mutmut_2(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["DEPLOYMENT"], item["container"]): item["image_id"] for item in resolved}


def x__index_resolved_images__mutmut_3(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["XXcontainerXX"]): item["image_id"] for item in resolved}


def x__index_resolved_images__mutmut_4(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["CONTAINER"]): item["image_id"] for item in resolved}


def x__index_resolved_images__mutmut_5(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["XXimage_idXX"] for item in resolved}


def x__index_resolved_images__mutmut_6(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["IMAGE_ID"] for item in resolved}

mutants_x__index_resolved_images__mutmut['_mutmut_orig'] = x__index_resolved_images__mutmut_orig # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut['x__index_resolved_images__mutmut_1'] = x__index_resolved_images__mutmut_1 # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut['x__index_resolved_images__mutmut_2'] = x__index_resolved_images__mutmut_2 # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut['x__index_resolved_images__mutmut_3'] = x__index_resolved_images__mutmut_3 # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut['x__index_resolved_images__mutmut_4'] = x__index_resolved_images__mutmut_4 # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut['x__index_resolved_images__mutmut_5'] = x__index_resolved_images__mutmut_5 # type: ignore # mutmut generated
mutants_x__index_resolved_images__mutmut['x__index_resolved_images__mutmut_6'] = x__index_resolved_images__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_matching__mutmut)
def _find_matching(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def x__find_matching__mutmut_orig(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def x__find_matching__mutmut_1(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind or raw["name"] == name:
            return raw
    return None


def x__find_matching__mutmut_2(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["XXkindXX"] == kind and raw["name"] == name:
            return raw
    return None


def x__find_matching__mutmut_3(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["KIND"] == kind and raw["name"] == name:
            return raw
    return None


def x__find_matching__mutmut_4(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] != kind and raw["name"] == name:
            return raw
    return None


def x__find_matching__mutmut_5(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["XXnameXX"] == name:
            return raw
    return None


def x__find_matching__mutmut_6(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["NAME"] == name:
            return raw
    return None


def x__find_matching__mutmut_7(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] != name:
            return raw
    return None

mutants_x__find_matching__mutmut['_mutmut_orig'] = x__find_matching__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_1'] = x__find_matching__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_2'] = x__find_matching__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_3'] = x__find_matching__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_4'] = x__find_matching__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_5'] = x__find_matching__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_6'] = x__find_matching__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_matching__mutmut['x__find_matching__mutmut_7'] = x__find_matching__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_orig(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_1(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=None,
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_2(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=None,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_3(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=None,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_4(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=None,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_5(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=None,
        error=None,
    )


def x__to_response__mutmut_6(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_7(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_8(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_9(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_10(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        error=None,
    )


def x__to_response__mutmut_11(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(drift) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        )


def x__to_response__mutmut_12(report: ContainerImageDriftReport) -> DetectContainerImageDriftResponse:
    return DetectContainerImageDriftResponse(
        out_of_sync=[_to_drift_dict(None) for drift in report.out_of_sync],
        in_sync_count=report.in_sync_count,
        excluded_count=report.excluded_count,
        total_checked=report.total_checked,
        summary=report.summary,
        error=None,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_drift_dict__mutmut)
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


def x__to_drift_dict__mutmut_orig(drift: ContainerImageDrift) -> ContainerImageDriftDict:
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


def x__to_drift_dict__mutmut_1(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=None,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_2(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=None,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_3(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=None,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_4(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=None,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_5(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=None,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_6(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=None,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_7(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=None,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_8(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=None,
    )


def x__to_drift_dict__mutmut_9(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_10(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_11(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_12(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_13(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_14(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        drift_type=drift.drift_type,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_15(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        severity=drift.severity,
    )


def x__to_drift_dict__mutmut_16(drift: ContainerImageDrift) -> ContainerImageDriftDict:
    return ContainerImageDriftDict(
        deployment=drift.deployment,
        namespace=drift.namespace,
        container=drift.container,
        running_image=drift.running_image,
        declared_image=drift.declared_image,
        source_of_truth=drift.source_of_truth,
        drift_type=drift.drift_type,
        )

mutants_x__to_drift_dict__mutmut['_mutmut_orig'] = x__to_drift_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_1'] = x__to_drift_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_2'] = x__to_drift_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_3'] = x__to_drift_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_4'] = x__to_drift_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_5'] = x__to_drift_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_6'] = x__to_drift_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_7'] = x__to_drift_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_8'] = x__to_drift_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_9'] = x__to_drift_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_10'] = x__to_drift_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_11'] = x__to_drift_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_12'] = x__to_drift_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_13'] = x__to_drift_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_14'] = x__to_drift_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_15'] = x__to_drift_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_drift_dict__mutmut['x__to_drift_dict__mutmut_16'] = x__to_drift_dict__mutmut_16 # type: ignore # mutmut generated
