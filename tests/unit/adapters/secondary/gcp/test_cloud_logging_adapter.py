from __future__ import annotations

from unittest.mock import MagicMock, Mock

import pytest
from hexawyn.adapters.secondary.gcp.cloud_logging_adapter import (
    GCPCloudLoggingAdapter,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


class TestGCPCloudLoggingAdapter:
    @staticmethod
    def _adapter(
        project_id: str = "proj-123",
        logging_client: object | None = None,
    ) -> GCPCloudLoggingAdapter:
        return GCPCloudLoggingAdapter(
            project_id=project_id,
            logging_client=logging_client,
        )

    @staticmethod
    def _log_entry(
        payload: str = "log line",
        container_name: str = "app",
    ) -> Mock:
        entry = Mock()
        entry.payload = payload
        entry.timestamp = None
        entry.resource = Mock()
        entry.resource.labels = {"container_name": container_name}
        return entry

    def test_fetch_pod_container_logs_empty_entries_returns_empty(self) -> None:
        mock_client = MagicMock()
        mock_client.list_entries.return_value = []
        adapter = self._adapter(logging_client=mock_client)

        result = adapter.fetch_pod_container_logs(
            pod_name="my-pod", namespace="default", time_window_minutes=30
        )

        assert result == []

    def test_fetch_pod_container_logs_groups_by_container(self) -> None:
        mock_client = MagicMock()
        mock_client.list_entries.return_value = [
            self._log_entry("line 1", "app"),
            self._log_entry("line 2", "app"),
            self._log_entry("sidecar started", "sidecar"),
        ]
        adapter = self._adapter(logging_client=mock_client)

        result = adapter.fetch_pod_container_logs(
            pod_name="my-pod", namespace="default", time_window_minutes=30
        )

        assert len(result) == 2  # noqa: PLR2004
        container_names = {entry["container"] for entry in result}
        assert container_names == {"app", "sidecar"}

    def test_fetch_pod_container_logs_filters_filter_includes_pod_and_namespace(self) -> None:
        mock_client = MagicMock()
        mock_client.list_entries.return_value = []
        adapter = self._adapter(logging_client=mock_client)

        adapter.fetch_pod_container_logs(
            pod_name="my-pod", namespace="prod", time_window_minutes=30
        )

        call_kwargs = mock_client.list_entries.call_args.kwargs
        assert call_kwargs["filter_"] is not None
        assert "my-pod" in str(call_kwargs["filter_"])
        assert "prod" in str(call_kwargs["filter_"])
        assert "k8s_container" in str(call_kwargs["filter_"])

    def test_group_by_container_respects_max_lines(self) -> None:
        adapter = self._adapter()
        entries = [self._log_entry(f"line {i}", "bursty") for i in range(6000)]
        result = adapter._group_by_container(entries)

        assert len(result) == 1  # noqa: PLR2004
        assert len(result[0]["lines"]) == 5000  # noqa: PLR2004
        assert result[0]["truncated"] is True

    def test_group_by_container_strips_blank_lines(self) -> None:
        adapter = self._adapter()
        entry = Mock()
        entry.payload = "  first  \n\n  second  \n   "
        entry.resource = Mock()
        entry.resource.labels = {"container_name": "app"}

        result = adapter._group_by_container([entry])

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["lines"] == ["first", "second"]

    def test_container_name_returns_from_labels(self) -> None:
        adapter = self._adapter()
        entry = self._log_entry("msg", "sidecar")

        assert adapter._container_name(entry) == "sidecar"

    def test_container_name_returns_unknown_for_missing_labels(self) -> None:
        adapter = self._adapter()
        entry = Mock()
        entry.resource = Mock()
        entry.resource.labels = {}

        assert adapter._container_name(entry) == "unknown"

    def test_container_name_returns_unknown_for_non_dict_labels(self) -> None:
        adapter = self._adapter()
        entry = Mock()
        entry.resource = Mock()
        entry.resource.labels = "not-a-dict"

        assert adapter._container_name(entry) == "unknown"

    def test_credentials_error_raises_cluster_unreachable(self) -> None:
        import sys

        mock_auth = Mock()
        creds_error = type("DefaultCredentialsError", (Exception,), {})
        mock_auth.DefaultCredentialsError = creds_error

        mock_client = MagicMock()
        mock_client.list_entries.side_effect = creds_error("no creds")
        adapter = self._adapter(logging_client=mock_client)

        with pytest.MonkeyPatch.context() as mp:
            mp.setitem(sys.modules, "google.auth.exceptions", mock_auth)
            with pytest.raises(ClusterUnreachableError, match="credentials"):
                adapter.fetch_pod_container_logs("pod", "ns", 30)

    def test_permission_denied_raises_insufficient_permissions(self) -> None:
        import sys

        mock_api_core = Mock()
        mock_api_core.GoogleAPICallError = type("GoogleAPICallError", (Exception,), {})
        perm_error = type("PermissionDenied", (Exception,), {})
        mock_api_core.PermissionDenied = perm_error

        mock_auth = Mock()
        mock_auth.DefaultCredentialsError = type("DefaultCredentialsError", (Exception,), {})

        mock_client = MagicMock()
        mock_client.list_entries.side_effect = perm_error("access denied")
        adapter = self._adapter(logging_client=mock_client)

        with pytest.MonkeyPatch.context() as mp:
            mp.setitem(sys.modules, "google.api_core.exceptions", mock_api_core)
            mp.setitem(sys.modules, "google.auth.exceptions", mock_auth)
            with pytest.raises(InsufficientPermissionsError, match="Access denied"):
                adapter.fetch_pod_container_logs("pod", "ns", 30)

    def test_api_error_raises_cluster_unreachable(self) -> None:
        import sys

        mock_api_core = Mock()
        api_error = type("GoogleAPICallError", (Exception,), {})
        mock_api_core.GoogleAPICallError = api_error
        mock_api_core.PermissionDenied = type("PermissionDenied", (Exception,), {})

        mock_auth = Mock()
        mock_auth.DefaultCredentialsError = type("DefaultCredentialsError", (Exception,), {})

        mock_client = MagicMock()
        mock_client.list_entries.side_effect = api_error("api error")
        adapter = self._adapter(logging_client=mock_client)

        with pytest.MonkeyPatch.context() as mp:
            mp.setitem(sys.modules, "google.api_core.exceptions", mock_api_core)
            mp.setitem(sys.modules, "google.auth.exceptions", mock_auth)
            with pytest.raises(ClusterUnreachableError, match="Cloud Logging"):
                adapter.fetch_pod_container_logs("pod", "ns", 30)

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = MagicMock()
        adapter = self._adapter(logging_client=mock_client)

        result = adapter._client_or_create()

        assert result is mock_client
