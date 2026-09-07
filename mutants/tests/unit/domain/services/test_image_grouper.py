from __future__ import annotations

from hexawyn.application.ports.driven.image_inventory_port import RunningImageRaw


class TestGroupByImage:
    def test_happy_path_groups_pods_by_image(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        images: list[RunningImageRaw] = [
            {"image": "nginx:1.25", "namespace": "default", "pod_name": "nginx-1"},
            {"image": "nginx:1.25", "namespace": "default", "pod_name": "nginx-2"},
            {"image": "redis:7", "namespace": "cache", "pod_name": "redis-1"},
        ]

        result = group_by_image(images)

        assert "nginx:1.25" in result
        assert "redis:7" in result
        namespaces_nginx, pods_nginx = result["nginx:1.25"]
        assert namespaces_nginx == {"default"}
        assert pods_nginx == {"nginx-1", "nginx-2"}

        namespaces_redis, pods_redis = result["redis:7"]
        assert namespaces_redis == {"cache"}
        assert pods_redis == {"redis-1"}

    def test_empty_list_returns_empty_dict(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        result = group_by_image([])

        assert result == {}

    def test_multiple_namespaces_same_image(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        images: list[RunningImageRaw] = [
            {"image": "shared:latest", "namespace": "ns-a", "pod_name": "pod-a"},
            {"image": "shared:latest", "namespace": "ns-b", "pod_name": "pod-b"},
            {"image": "shared:latest", "namespace": "ns-c", "pod_name": "pod-c"},
        ]

        result = group_by_image(images)

        namespaces, pods = result["shared:latest"]
        assert namespaces == {"ns-a", "ns-b", "ns-c"}
        assert len(pods) == 3  # noqa: PLR2004

    def test_single_image_single_pod(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        images: list[RunningImageRaw] = [
            {"image": "alpine:3.19", "namespace": "tools", "pod_name": "alpine-pod"},
        ]

        result = group_by_image(images)

        assert len(result) == 1
        namespaces, pods = result["alpine:3.19"]
        assert namespaces == {"tools"}
        assert pods == {"alpine-pod"}

    def test_same_pod_name_different_namespaces(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        images: list[RunningImageRaw] = [
            {"image": "envoy:1.28", "namespace": "dev", "pod_name": "proxy"},
            {"image": "envoy:1.28", "namespace": "prod", "pod_name": "proxy"},
        ]

        result = group_by_image(images)

        namespaces, pods = result["envoy:1.28"]
        assert namespaces == {"dev", "prod"}
        assert pods == {"proxy"}  # set deduplication, same name = one entry

    def test_distinct_images_yield_separate_groups(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        images: list[RunningImageRaw] = [
            {"image": "app:v1", "namespace": "ns", "pod_name": "app-v1"},
            {"image": "app:v2", "namespace": "ns", "pod_name": "app-v2"},
        ]

        result = group_by_image(images)

        assert len(result) == 2  # noqa: PLR2004
        assert "app:v1" in result
        assert "app:v2" in result

    def test_return_type_matches_signature(self) -> None:
        from hexawyn.domain.services.image_vulnerability.image_grouper import group_by_image

        result = group_by_image([])

        assert isinstance(result, dict)
