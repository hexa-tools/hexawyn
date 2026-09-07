"""Unit tests for extract_field_paths — walks a K8s managedFields fieldsV1
tree into dotted field paths, e.g. {"f:data": {"f:KEY": {}}} -> ["data.KEY"]."""

from __future__ import annotations


class TestSimpleLeaf:
    def test_single_nested_field_becomes_dotted_path(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        fields_v1 = {"f:data": {"f:DATABASE_URL": {}}}

        assert extract_field_paths(fields_v1) == ["data.DATABASE_URL"]

    def test_multiple_sibling_fields_all_extracted(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        fields_v1 = {"f:data": {"f:DATABASE_URL": {}, "f:LOG_LEVEL": {}}}

        assert sorted(extract_field_paths(fields_v1)) == ["data.DATABASE_URL", "data.LOG_LEVEL"]

    def test_multiple_top_level_fields(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        fields_v1 = {"f:data": {"f:password": {}}, "f:type": {}}

        assert sorted(extract_field_paths(fields_v1)) == ["data.password", "type"]


class TestAtomicSetMarker:
    def test_dot_marker_means_whole_field_was_set_atomically(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        fields_v1 = {"f:data": {".": {}}}

        assert extract_field_paths(fields_v1) == ["data"]


class TestListItemMarkersAreSkipped:
    def test_k_prefixed_list_item_key_does_not_produce_a_deep_path(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        fields_v1 = {"f:data": {"f:items": {'k:{"name":"x"}': {"f:image": {}}}}}

        assert extract_field_paths(fields_v1) == ["data.items"]


class TestEmptyInput:
    def test_empty_mapping_returns_no_paths(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        assert extract_field_paths({}) == []

    def test_non_mapping_input_returns_no_paths(self) -> None:
        from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
            extract_field_paths,
        )

        assert extract_field_paths(None) == []  # type: ignore[arg-type]
