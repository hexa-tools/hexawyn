"""Unit tests for get_container_images — extracts every container's image
(unlike field_comparison.get_image, which is first-container-only)."""

from __future__ import annotations


def _deployment(containers: list[dict]) -> dict:
    return {"spec": {"template": {"spec": {"containers": containers}}}}


class TestMultipleContainers:
    def test_extracts_all_containers_by_name(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        data = _deployment(
            [
                {"name": "payment-app", "image": "payment:v1.2"},
                {"name": "sidecar", "image": "envoy:v1.20"},
            ]
        )

        assert get_container_images(data) == {
            "payment-app": "payment:v1.2",
            "sidecar": "envoy:v1.20",
        }

    def test_single_container(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        data = _deployment([{"name": "app", "image": "app:v1"}])

        assert get_container_images(data) == {"app": "app:v1"}


class TestMissingStructure:
    def test_missing_spec_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        assert get_container_images({}) == {}

    def test_non_dict_spec_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        assert get_container_images({"spec": "not-a-dict"}) == {}

    def test_missing_template_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        assert get_container_images({"spec": {}}) == {}

    def test_non_dict_template_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        assert get_container_images({"spec": {"template": "not-a-dict"}}) == {}

    def test_missing_pod_spec_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        assert get_container_images({"spec": {"template": {}}}) == {}

    def test_non_dict_pod_spec_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        assert get_container_images({"spec": {"template": {"spec": "not-a-dict"}}}) == {}

    def test_non_list_containers_returns_empty(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        data = {"spec": {"template": {"spec": {"containers": "not-a-list"}}}}
        assert get_container_images(data) == {}

    def test_non_dict_container_entry_is_skipped(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        data = _deployment(["not-a-dict", {"name": "app", "image": "app:v1"}])

        assert get_container_images(data) == {"app": "app:v1"}

    def test_container_missing_name_or_image_is_skipped(self) -> None:
        from hexawyn.domain.services.image_drift.container_image_extractor import (
            get_container_images,
        )

        data = _deployment([{"name": "no-image"}, {"image": "no-name:v1"}])

        assert get_container_images(data) == {}
