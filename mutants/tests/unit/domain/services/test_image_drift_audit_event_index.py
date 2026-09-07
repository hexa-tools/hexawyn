from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import ResourceManifestRaw
from hexawyn.application.ports.driven.image_drift_port import ResolvedContainerImageRaw


class TestIndexResolvedImages:
    def test_happy_path_indexes_by_deployment_container(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import index_resolved_images

        resolved: list[ResolvedContainerImageRaw] = [
            {
                "deployment": "api-server",
                "namespace": "default",
                "container": "app",
                "image_id": "sha256:abc123",
            },
            {
                "deployment": "worker",
                "namespace": "jobs",
                "container": "processor",
                "image_id": "sha256:def456",
            },
        ]

        result = index_resolved_images(resolved)

        assert result[("api-server", "app")] == "sha256:abc123"
        assert result[("worker", "processor")] == "sha256:def456"

    def test_empty_list_returns_empty_dict(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import index_resolved_images

        result = index_resolved_images([])

        assert result == {}

    def test_single_item_returns_single_entry(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import index_resolved_images

        resolved: list[ResolvedContainerImageRaw] = [
            {
                "deployment": "solo",
                "namespace": "ns",
                "container": "main",
                "image_id": "sha256:111",
            },
        ]

        result = index_resolved_images(resolved)

        assert len(result) == 1
        assert result[("solo", "main")] == "sha256:111"

    def test_duplicate_key_last_wins(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import index_resolved_images

        resolved: list[ResolvedContainerImageRaw] = [
            {
                "deployment": "dup",
                "namespace": "ns",
                "container": "web",
                "image_id": "sha256:first",
            },
            {
                "deployment": "dup",
                "namespace": "ns",
                "container": "web",
                "image_id": "sha256:second",
            },
        ]

        result = index_resolved_images(resolved)

        assert result[("dup", "web")] == "sha256:second"


class TestFindMatching:
    def test_happy_path_finds_by_kind_and_name(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "api", "namespace": "default", "data": {}},
            {"kind": "Service", "name": "api", "namespace": "default", "data": {}},
        ]

        result = find_matching(manifests, "Deployment", "api")

        assert result is not None
        assert result["kind"] == "Deployment"
        assert result["name"] == "api"

    def test_no_match_returns_none(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "web", "namespace": "default", "data": {}},
        ]

        result = find_matching(manifests, "Service", "web")

        assert result is None

    def test_empty_manifest_list_returns_none(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        result = find_matching([], "Deployment", "any")

        assert result is None

    def test_first_match_returned_when_duplicates(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "dup", "namespace": "default", "data": {"order": 1}},
            {"kind": "Deployment", "name": "dup", "namespace": "default", "data": {"order": 2}},
        ]

        result = find_matching(manifests, "Deployment", "dup")

        assert result is not None
        assert result["data"]["order"] == 1  # type: ignore[index]

    def test_kind_case_sensitive(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "app", "namespace": "default", "data": {}},
        ]

        result = find_matching(manifests, "deployment", "app")

        assert result is None

    def test_name_case_sensitive(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "App-Name", "namespace": "default", "data": {}},
        ]

        result = find_matching(manifests, "Deployment", "app-name")

        assert result is None

    def test_only_kind_match_not_enough(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "correct", "namespace": "ns", "data": {}},
        ]

        result = find_matching(manifests, "Deployment", "wrong-name")

        assert result is None

    def test_only_name_match_not_enough(self) -> None:
        from hexawyn.domain.services.image_drift.audit_event_index import find_matching

        manifests: list[ResourceManifestRaw] = [
            {"kind": "Deployment", "name": "correct", "namespace": "ns", "data": {}},
        ]

        result = find_matching(manifests, "StatefulSet", "correct")

        assert result is None
