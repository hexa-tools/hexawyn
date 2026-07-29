from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.service.container_image_drift_service import (
    ContainerImageDriftService,
)
from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (
    DetectContainerImageDriftResponse,
)


def _deployment(name: str, namespace: str, release: str = "my-release") -> dict[str, object]:
    return {
        "kind": "Deployment",
        "name": name,
        "namespace": namespace,
        "labels": {},
        "annotations": {"meta.helm.sh/release-name": release},
        "data": {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {"name": "app", "image": "nginx:1.25"},
                        ]
                    }
                }
            }
        },
    }


def _desired_manifest(
    kind: str, name: str, namespace: str, image: str = "nginx:1.25"
) -> dict[str, object]:
    return {
        "kind": kind,
        "name": name,
        "namespace": namespace,
        "data": {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {"name": "app", "image": image},
                        ]
                    }
                }
            }
        },
    }


class TestContainerImageDriftService:
    def test_detect_image_drift_returns_response_with_empty_deployments(self) -> None:
        live = MagicMock()
        live.list_live_resources.return_value = []
        helm = MagicMock()
        kustomize = MagicMock()
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert isinstance(result, DetectContainerImageDriftResponse)
        assert result.total_checked == 0  # noqa: PLR2004

    def test_detect_image_drift_no_deployments_in_live_resources(self) -> None:
        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "ConfigMap",
                "name": "config",
                "namespace": "default",
                "labels": {},
                "annotations": {},
                "data": {},
            }
        ]
        helm = MagicMock()
        kustomize = MagicMock()
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 0  # noqa: PLR2004

    def test_detect_image_drift_kustomize_match_in_sync(self) -> None:
        deployment = _deployment("my-app", "default")
        desired = _desired_manifest("Deployment", "my-app", "default")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = [desired]
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(
            DetectContainerImageDriftCommand(
                namespace="default", kustomize_paths=["/path/to/overlay"]
            )
        )

        assert result.total_checked == 1  # noqa: PLR2004
        assert result.in_sync_count == 1  # noqa: PLR2004
        assert len(result.out_of_sync) == 0  # noqa: PLR2004

    def test_detect_image_drift_kustomize_match_tag_mismatch(self) -> None:
        deployment = _deployment("my-app", "default")
        desired = _desired_manifest("Deployment", "my-app", "default", image="nginx:2.0")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = [desired]
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(
            DetectContainerImageDriftCommand(
                namespace="default", kustomize_paths=["/path/to/overlay"]
            )
        )

        assert result.total_checked == 1  # noqa: PLR2004
        assert len(result.out_of_sync) == 1  # noqa: PLR2004

    def test_detect_image_drift_helm_release_match(self) -> None:
        deployment = _deployment("my-app", "default", release="my-release")
        desired = _desired_manifest("Deployment", "my-app", "default")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [desired]
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 1  # noqa: PLR2004
        assert result.in_sync_count == 1  # noqa: PLR2004

    def test_detect_image_drift_helm_source_does_not_exist(self) -> None:
        deployment = _deployment("my-app", "default", release="gone-release")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        helm.source_exists.return_value = False
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 0  # noqa: PLR2004

    def test_detect_image_drift_missing_helm_annotation_skipped(self) -> None:
        deployment = {
            "kind": "Deployment",
            "name": "orphan-app",
            "namespace": "default",
            "labels": {},
            "annotations": {},
            "data": {},
        }
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 0  # noqa: PLR2004

    def test_detect_image_drift_missing_declared_container_skipped(self) -> None:
        deployment = _deployment("my-app", "default")
        desired = {
            "kind": "Deployment",
            "name": "my-app",
            "namespace": "default",
            "data": {
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {"name": "different-container", "image": "nginx:1.25"},
                            ]
                        }
                    }
                }
            },
        }
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = [desired]
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(
            DetectContainerImageDriftCommand(
                namespace="default", kustomize_paths=["/path/to/overlay"]
            )
        )

        assert result.total_checked == 0  # noqa: PLR2004
        assert result.in_sync_count == 0  # noqa: PLR2004

    def test_detect_image_drift_mutable_tag_excluded(self) -> None:
        deployment = {
            "kind": "Deployment",
            "name": "my-app",
            "namespace": "default",
            "labels": {},
            "annotations": {"meta.helm.sh/release-name": "my-release"},
            "data": {
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {"name": "app", "image": "nginx:latest"},
                            ]
                        }
                    }
                }
            },
        }
        desired = _desired_manifest("Deployment", "my-app", "default", image="nginx:1.25")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [desired]
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 0  # noqa: PLR2004
        assert result.excluded_count == 1  # noqa: PLR2004

    def test_detect_image_drift_helm_manifest_cache_reused(self) -> None:
        dep_a = _deployment("app-a", "default", release="shared-release")
        dep_b = _deployment("app-b", "default", release="shared-release")
        desired_a = _desired_manifest("Deployment", "app-a", "default")
        desired_b = _desired_manifest("Deployment", "app-b", "default")
        live = MagicMock()
        live.list_live_resources.return_value = [dep_a, dep_b]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [desired_a, desired_b]
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 2  # noqa: PLR2004
        assert helm.render_desired_manifests.call_count == 1  # noqa: PLR2004

    def test_detect_image_drift_helm_exists_cache_reused(self) -> None:
        dep_a = _deployment("app-a", "default", release="shared-release")
        dep_b = _deployment("app-b", "default", release="shared-release")
        live = MagicMock()
        live.list_live_resources.return_value = [dep_a, dep_b]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = []
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert helm.source_exists.call_count == 1  # noqa: PLR2004

    def test_detect_image_drift_digest_mismatch_via_image_id(self) -> None:
        deployment = _deployment("my-app", "default")
        desired = _desired_manifest("Deployment", "my-app", "default", image="nginx:1.25")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = [desired]
        images = MagicMock()
        images.list_resolved_container_images.return_value = [
            {
                "deployment": "my-app",
                "namespace": "default",
                "container": "app",
                "image_id": "sha256:abc123",
            }
        ]

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(
            DetectContainerImageDriftCommand(
                namespace="default", kustomize_paths=["/path/to/overlay"]
            )
        )

        assert result.total_checked == 1  # noqa: PLR2004

    def test_detect_image_drift_running_image_matches_declared_no_drift(self) -> None:
        deployment = _deployment("my-app", "default")
        desired = _desired_manifest("Deployment", "my-app", "default", image="nginx:1.25")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = [desired]
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(
            DetectContainerImageDriftCommand(
                namespace="default", kustomize_paths=["/path/to/overlay"]
            )
        )

        assert result.in_sync_count == 1  # noqa: PLR2004

    def test_detect_image_drift_multiple_containers(self) -> None:
        deployment = {
            "kind": "Deployment",
            "name": "multi-container-app",
            "namespace": "default",
            "labels": {},
            "annotations": {"meta.helm.sh/release-name": "my-release"},
            "data": {
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {"name": "app", "image": "nginx:1.25"},
                                {"name": "sidecar", "image": "redis:7.0"},
                            ]
                        }
                    }
                }
            },
        }
        desired = {
            "kind": "Deployment",
            "name": "multi-container-app",
            "namespace": "default",
            "data": {
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {"name": "app", "image": "nginx:1.25"},
                                {"name": "sidecar", "image": "redis:7.0"},
                            ]
                        }
                    }
                }
            },
        }
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [desired]
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        result = service.detect_image_drift(DetectContainerImageDriftCommand(namespace="default"))

        assert result.total_checked == 2  # noqa: PLR2004
        assert result.in_sync_count == 2  # noqa: PLR2004

    def test_detect_image_drift_renders_kustomize_paths(self) -> None:
        deployment = _deployment("my-app", "default", release="")
        live = MagicMock()
        live.list_live_resources.return_value = [deployment]
        helm = MagicMock()
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        images = MagicMock()
        images.list_resolved_container_images.return_value = []

        service = ContainerImageDriftService(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=images,
        )
        service.detect_image_drift(
            DetectContainerImageDriftCommand(
                namespace="default", kustomize_paths=["/overlay/prod", "/overlay/staging"]
            )
        )

        assert kustomize.render_desired_manifests.call_count == 2  # noqa: PLR2004
