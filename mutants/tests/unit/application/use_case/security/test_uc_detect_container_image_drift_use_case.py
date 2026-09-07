from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.response import (
    ContainerImageDriftDict,
    DetectContainerImageDriftResponse,
)


class TestDetectContainerImageDriftUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = []
        helm = MagicMock()
        helm.render_desired_manifests.return_value = []
        helm.source_exists.return_value = False
        kustomize = MagicMock()
        kustomize.render_desired_manifests.return_value = []
        kustomize.source_exists.return_value = False
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = []

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(
            DetectContainerImageDriftCommand(
                namespace="default",
                kustomize_paths=[],
            )
        )

        assert isinstance(result, DetectContainerImageDriftResponse)
        assert result.total_checked == 0
        assert result.in_sync_count == 0

    def test_execute_with_helm_release_all_in_sync(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "labels": {"app": "my-app"},
                "annotations": {"meta.helm.sh/release-name": "my-release"},
                "data": {},
            },
        ]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "data": {
                    "spec": {
                        "template": {
                            "spec": {
                                "containers": [
                                    {"name": "my-container", "image": "nginx:1.25"},
                                ],
                            },
                        },
                    },
                },
            },
        ]
        kustomize = MagicMock()
        kustomize.source_exists.return_value = False
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = [
            {
                "deployment": "my-app",
                "namespace": "default",
                "container": "my-container",
                "image_id": "nginx:1.25",
            },
        ]

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(DetectContainerImageDriftCommand(namespace="default"))

        assert result.in_sync_count == 1
        assert len(result.out_of_sync) == 0
        assert result.total_checked == 1

    def test_execute_detects_tag_mismatch(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "labels": {},
                "annotations": {"meta.helm.sh/release-name": "my-release"},
                "data": {},
            },
        ]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "data": {
                    "spec": {
                        "template": {
                            "spec": {
                                "containers": [
                                    {"name": "my-container", "image": "nginx:1.25"},
                                ],
                            },
                        },
                    },
                },
            },
        ]
        kustomize = MagicMock()
        kustomize.source_exists.return_value = False
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = [
            {
                "deployment": "my-app",
                "namespace": "default",
                "container": "my-container",
                "image_id": "nginx:1.24",
            },
        ]

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(DetectContainerImageDriftCommand(namespace="default"))

        assert len(result.out_of_sync) == 1
        drift_entry: ContainerImageDriftDict = result.out_of_sync[0]
        assert drift_entry["drift_type"] == "tag_mismatch"
        assert drift_entry["deployment"] == "my-app"
        assert drift_entry["container"] == "my-container"
        assert result.in_sync_count == 0
        assert result.total_checked == 1

    def test_execute_with_kustomize_source(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "labels": {},
                "annotations": {},
                "data": {},
            },
        ]
        helm = MagicMock()
        helm.source_exists.return_value = False
        kustomize = MagicMock()
        kustomize.source_exists.return_value = True
        kustomize.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "data": {
                    "spec": {
                        "template": {
                            "spec": {
                                "containers": [
                                    {"name": "my-container", "image": "alpine:3.19"},
                                ],
                            },
                        },
                    },
                },
            },
        ]
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = [
            {
                "deployment": "my-app",
                "namespace": "default",
                "container": "my-container",
                "image_id": "alpine:3.19",
            },
        ]

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(
            DetectContainerImageDriftCommand(
                namespace="default",
                kustomize_paths=["overlays/prod"],
            )
        )

        assert result.in_sync_count == 1
        assert result.total_checked == 1

    def test_execute_excluded_container_no_declared_image(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "labels": {},
                "annotations": {"meta.helm.sh/release-name": "my-release"},
                "data": {},
            },
        ]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "data": {
                    "spec": {
                        "template": {
                            "spec": {
                                "containers": [],
                            },
                        },
                    },
                },
            },
        ]
        kustomize = MagicMock()
        kustomize.source_exists.return_value = False
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = [
            {
                "deployment": "my-app",
                "namespace": "default",
                "container": "my-container",
                "image_id": "nginx:latest",
            },
        ]

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(DetectContainerImageDriftCommand(namespace="default"))

        assert result.excluded_count == 1
        assert result.total_checked == 0
        assert result.in_sync_count == 0

    def test_execute_digest_mismatch_detected(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "labels": {},
                "annotations": {"meta.helm.sh/release-name": "my-release"},
                "data": {},
            },
        ]
        helm = MagicMock()
        helm.source_exists.return_value = True
        helm.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "my-app",
                "namespace": "default",
                "data": {
                    "spec": {
                        "template": {
                            "spec": {
                                "containers": [
                                    {
                                        "name": "my-container",
                                        "image": "nginx@sha256:abc123def456",
                                    },
                                ],
                            },
                        },
                    },
                },
            },
        ]
        kustomize = MagicMock()
        kustomize.source_exists.return_value = False
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = [
            {
                "deployment": "my-app",
                "namespace": "default",
                "container": "my-container",
                "image_id": "docker-pullable://nginx@sha256:999888777666",
            },
        ]

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(DetectContainerImageDriftCommand(namespace="default"))

        assert len(result.out_of_sync) == 1
        assert result.out_of_sync[0]["drift_type"] == "digest_mismatch"

    def test_execute_multiple_deployments_mixed_results(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            DetectContainerImageDriftUseCase,
        )

        live = MagicMock()
        live.list_live_resources.return_value = [
            {
                "kind": "Deployment",
                "name": "app-a",
                "namespace": "default",
                "labels": {},
                "annotations": {"meta.helm.sh/release-name": "release-a"},
                "data": {},
            },
            {
                "kind": "Deployment",
                "name": "app-b",
                "namespace": "default",
                "labels": {},
                "annotations": {"meta.helm.sh/release-name": "release-b"},
                "data": {},
            },
        ]
        helm = MagicMock()

        def helm_side_effect(source: str, namespace: str) -> bool:
            return source == "release-a"

        helm.source_exists.side_effect = helm_side_effect
        helm.render_desired_manifests.return_value = [
            {
                "kind": "Deployment",
                "name": "app-a",
                "namespace": "default",
                "data": {
                    "spec": {
                        "template": {
                            "spec": {
                                "containers": [
                                    {"name": "ctr-a", "image": "nginx:1.25"},
                                ],
                            },
                        },
                    },
                },
            },
        ]
        kustomize = MagicMock()
        kustomize.source_exists.return_value = False
        image_drift = MagicMock()
        image_drift.list_resolved_container_images.return_value = [
            {
                "deployment": "app-a",
                "namespace": "default",
                "container": "ctr-a",
                "image_id": "nginx:1.25",
            },
            {
                "deployment": "app-b",
                "namespace": "default",
                "container": "ctr-b",
                "image_id": "alpine:3.18",
            },
        ]

        use_case = DetectContainerImageDriftUseCase(
            live_resource_port=live,
            helm_adapter=helm,
            kustomize_adapter=kustomize,
            image_drift_port=image_drift,
        )
        result = use_case.execute(DetectContainerImageDriftCommand(namespace="default"))

        assert result.in_sync_count == 1
        assert result.excluded_count == 1


class TestExtractContainerImages:
    def test_extracts_containers_from_normal_deployment(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {"name": "main", "image": "nginx:1.25"},
                            {"name": "sidecar", "image": "envoy:1.28"},
                        ],
                    },
                },
            },
        }
        result = _extract_container_images(data)
        assert result == {"main": "nginx:1.25", "sidecar": "envoy:1.28"}

    def test_returns_empty_on_missing_spec(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        assert _extract_container_images({}) == {}

    def test_returns_empty_on_non_dict_spec(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        assert _extract_container_images({"spec": "not-a-dict"}) == {}

    def test_returns_empty_on_non_dict_template(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {"spec": {"template": "bad"}}
        assert _extract_container_images(data) == {}

    def test_returns_empty_on_non_dict_pod_spec(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {"spec": {"template": {"spec": "bad"}}}
        assert _extract_container_images(data) == {}

    def test_returns_empty_on_non_list_containers(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {"spec": {"template": {"spec": {"containers": "bad"}}}}
        assert _extract_container_images(data) == {}

    def test_skips_non_dict_container(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            "bad-entry",
                            {"name": "ok", "image": "nginx:1.25"},
                        ],
                    },
                },
            },
        }
        result = _extract_container_images(data)
        assert result == {"ok": "nginx:1.25"}

    def test_skips_container_without_name(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {"image": "no-name:1.0"},
                        ],
                    },
                },
            },
        }
        assert _extract_container_images(data) == {}

    def test_skips_container_with_non_string_name_or_image(self) -> None:
        from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
            _extract_container_images,
        )

        data = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {"name": 123, "image": "ok:1.0"},
                            {"name": "ok", "image": 456},
                        ],
                    },
                },
            },
        }
        assert _extract_container_images(data) == {}
