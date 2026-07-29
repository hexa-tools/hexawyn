from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gcp.cloud_logging_adapter import GCPCloudLoggingAdapter


class TestGCPCloudLoggingAdapter:
    def test_container_name(self) -> None:
        adapter = GCPCloudLoggingAdapter(project_id="test")
        entry = Mock()
        entry.resource.labels = {"container_name": "my-app"}
        assert adapter._container_name(entry) == "my-app"

    def test_container_name_unknown(self) -> None:
        adapter = GCPCloudLoggingAdapter(project_id="test")
        entry = Mock()
        entry.resource.labels = {}
        assert adapter._container_name(entry) == "unknown"

    def test_container_name_no_labels(self) -> None:
        adapter = GCPCloudLoggingAdapter(project_id="test")
        entry = Mock()
        del entry.resource.labels  # triggers AttributeError → returns "unknown"
        entry.resource = Mock()
        entry.resource.labels = {"not_container": "x"}
        assert adapter._container_name(entry) == "unknown"
