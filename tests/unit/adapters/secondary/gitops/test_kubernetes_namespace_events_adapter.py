from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
    KubernetesNamespaceEventsAdapter,
    _object_exists,
    _translate_error,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent


class TestKubernetesNamespaceEventsAdapter:
    def test_list_events_returns_namespace_events(self) -> None:
        adapter = KubernetesNamespaceEventsAdapter()
        request = GetNamespaceEventsRequest(namespace="default")

        mock_event = MagicMock()
        mock_event.type = "Warning"
        mock_event.reason = "OOMKilled"
        mock_event.message = "Container was OOMKilled"
        mock_event.count = 2
        mock_event.last_timestamp = None
        mock_event.event_time = None
        mock_event.first_timestamp = None

        mock_involved = MagicMock()
        mock_involved.kind = "Deployment"
        mock_involved.name = "my-deploy"
        mock_event.involved_object = mock_involved

        mock_core = MagicMock()
        mock_core.list_namespaced_event.return_value = MagicMock(items=[mock_event])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.list_events(request)

            assert len(result) == 1
            assert isinstance(result[0], NamespaceEvent)
            assert result[0].reason == "OOMKilled"
            assert result[0].count == 2  # noqa: PLR2004

    def test_list_events_not_found_raises(self) -> None:
        adapter = KubernetesNamespaceEventsAdapter()
        request = GetNamespaceEventsRequest(namespace="missing-ns")

        class NotFoundError(Exception):
            status = 404

        mock_core = MagicMock()
        mock_core.list_namespaced_event.side_effect = NotFoundError("not found")

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            with pytest.raises(ResourceNotFoundError):
                adapter.list_events(request)

    def test_list_events_forbidden_raises(self) -> None:
        adapter = KubernetesNamespaceEventsAdapter()
        request = GetNamespaceEventsRequest(namespace="default")

        class ForbiddenError(Exception):
            status = 403

        mock_core = MagicMock()
        mock_core.list_namespaced_event.side_effect = ForbiddenError("denied")

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_events(request)

    def test_list_events_other_error_raises_cluster_unreachable(self) -> None:
        adapter = KubernetesNamespaceEventsAdapter()
        request = GetNamespaceEventsRequest(namespace="default")

        mock_core = MagicMock()
        mock_core.list_namespaced_event.side_effect = RuntimeError("boom")

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            with pytest.raises(ClusterUnreachableError):
                adapter.list_events(request)

    def test_list_events_propagates_timestamps(self) -> None:
        adapter = KubernetesNamespaceEventsAdapter()
        request = GetNamespaceEventsRequest(namespace="default")

        mock_event = MagicMock()
        mock_event.type = "Normal"
        mock_event.reason = "Created"
        mock_event.message = "Pod created"
        mock_event.count = 1
        mock_event.first_timestamp = MagicMock()
        mock_event.first_timestamp.isoformat.return_value = "2024-01-01T00:00:00Z"
        mock_event.last_timestamp = None
        mock_event.event_time = None

        mock_involved = MagicMock()
        mock_involved.kind = "Deployment"
        mock_involved.name = "my-deploy"
        mock_event.involved_object = mock_involved

        mock_core = MagicMock()
        mock_core.list_namespaced_event.return_value = MagicMock(items=[mock_event])

        with patch("kubernetes.client.CoreV1Api", return_value=mock_core):
            result = adapter.list_events(request)

            assert result[0].last_seen == "2024-01-01T00:00:00Z"
            assert result[0].event_type == "Normal"
            assert result[0].object == "deployment/my-deploy"


class TestObjectExists:
    def test_non_pod_returns_true(self) -> None:
        mock_involved = MagicMock()
        mock_involved.kind = "Deployment"

        assert _object_exists(MagicMock(), mock_involved, "default") is True

    def test_pod_exists_returns_true(self) -> None:
        mock_involved = MagicMock()
        mock_involved.kind = "Pod"
        mock_involved.name = "my-pod"
        mock_core = MagicMock()
        mock_core.read_namespaced_pod.return_value = MagicMock()

        assert _object_exists(mock_core, mock_involved, "default") is True

    def test_pod_not_found_returns_false(self) -> None:
        mock_involved = MagicMock()
        mock_involved.kind = "Pod"
        mock_involved.name = "missing-pod"

        class NotFoundError(Exception):
            status = 404

        mock_core = MagicMock()
        mock_core.read_namespaced_pod.side_effect = NotFoundError("not found")

        assert _object_exists(mock_core, mock_involved, "default") is False

    def test_pod_other_error_returns_true(self) -> None:
        mock_involved = MagicMock()
        mock_involved.kind = "Pod"
        mock_involved.name = "my-pod"

        mock_core = MagicMock()
        mock_core.read_namespaced_pod.side_effect = RuntimeError("connection error")

        assert _object_exists(mock_core, mock_involved, "default") is True


class TestTranslateError:
    def test_not_found(self) -> None:
        class Exc(Exception):  # noqa: N818
            status = 404

        request = GetNamespaceEventsRequest(namespace="ns")
        result = _translate_error(Exc(), request)
        assert isinstance(result, ResourceNotFoundError)

    def test_forbidden(self) -> None:
        class Exc(Exception):  # noqa: N818
            status = 403

        request = GetNamespaceEventsRequest(namespace="ns")
        result = _translate_error(Exc(), request)
        assert isinstance(result, InsufficientPermissionsError)

    def test_other(self) -> None:
        request = GetNamespaceEventsRequest(namespace="ns")
        result = _translate_error(Exception("boom"), request)
        assert isinstance(result, ClusterUnreachableError)
