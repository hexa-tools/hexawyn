from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("google.cloud.logging_v2")
from google.api_core.exceptions import PermissionDenied  # noqa: E402
from google.auth.exceptions import DefaultCredentialsError  # noqa: E402
from hexawyn.application.ports.driven.log_search_port import LogSearchPort  # noqa: E402
from hexawyn.domain.errors import (  # noqa: E402
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_PROJECT = "my-project"


def _entry(payload: str) -> MagicMock:
    entry = MagicMock()
    entry.payload = payload
    entry.timestamp = None
    entry.resource = MagicMock()
    entry.resource.labels = {}
    return entry


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.gcp.cloud_logging_adapter import GCPCloudLoggingAdapter

    return GCPCloudLoggingAdapter(project_id=_PROJECT, logging_client=client)


class TestContract:
    def test_is_a_log_search_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), LogSearchPort)


class TestFetchPodContainerLogs:
    def test_groups_lines_by_container(self) -> None:
        client = MagicMock()
        e1 = _entry("boot ok\nserving")
        e1.resource.labels = {"container_name": "app"}
        e2 = _entry("proxy up")
        e2.resource.labels = {"container_name": "sidecar"}
        client.list_entries.return_value = [e1, e2]
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        by_name = {c["container"]: c for c in result}
        assert by_name["app"]["lines"] == ["boot ok", "serving"]
        assert by_name["sidecar"]["lines"] == ["proxy up"]

    def test_uses_resource_names_and_filter(self) -> None:
        client = MagicMock()
        client.list_entries.return_value = []
        adapter = _adapter(client)

        adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        kwargs = client.list_entries.call_args.kwargs
        assert kwargs["resource_names"] == ["projects/my-project"]
        filter_ = kwargs["filter_"]
        assert "payments-api" in filter_
        assert "prod" in filter_

    def test_fallback_to_unknown_container(self) -> None:
        client = MagicMock()
        entry = _entry("bare line")
        entry.resource.labels = {}
        client.list_entries.return_value = [entry]
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert result[0]["container"] == "unknown"

    def test_non_dict_labels_fallback_to_unknown(self) -> None:
        client = MagicMock()
        entry = _entry("bare line")
        entry.resource.labels = None
        client.list_entries.return_value = [entry]
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert result[0]["container"] == "unknown"

    def test_paginates_all_entries(self) -> None:
        client = MagicMock()
        client.list_entries.return_value = [_entry("one"), _entry("two")]
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == 2

    def test_truncates_at_max_lines(self) -> None:
        from hexawyn.adapters.secondary.gcp import cloud_logging_adapter as module

        max_lines = module._MAX_LINES_PER_CONTAINER
        client = MagicMock()
        entries = [_entry(f"line-{i}") for i in range(max_lines + 10)]
        for entry in entries:
            entry.resource.labels = {"container_name": "app"}
        client.list_entries.return_value = entries
        adapter = _adapter(client)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == max_lines
        assert result[0]["truncated"] is True


class TestErrorTranslation:
    def test_access_denied_raises_insufficient_permissions(self) -> None:
        client = MagicMock()
        client.list_entries.side_effect = PermissionDenied("denied")
        adapter = _adapter(client)

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_missing_credentials_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.list_entries.side_effect = DefaultCredentialsError("no creds")
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError) as exc_info:
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert "gcloud auth" in str(exc_info.value).lower()

    def test_other_api_error_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        from google.api_core.exceptions import GoogleAPICallError

        client.list_entries.side_effect = GoogleAPICallError("boom")
        adapter = _adapter(client)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)


class TestLazyClientCreation:
    def test_lazily_creates_client(self) -> None:
        from hexawyn.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )

        created = MagicMock()
        created.list_entries.return_value = []
        adapter = GCPCloudLoggingAdapter(project_id=_PROJECT)

        with patch("google.cloud.logging_v2.Client", return_value=created) as client_cls:
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        client_cls.assert_called_once_with(project=_PROJECT)
