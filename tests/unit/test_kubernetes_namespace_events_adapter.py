from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest


def _event(
    event_type: str = "Warning",
    reason: str = "BackOff",
    message: str = "Back-off restarting failed container",
    count: int = 12,
    kind: str = "Pod",
    name: str = "payment-api",
) -> MagicMock:
    item = MagicMock()
    item.type = event_type
    item.reason = reason
    item.message = message
    item.count = count
    item.last_timestamp = datetime(2024, 1, 1, 15, 0, 0, tzinfo=UTC)
    item.event_time = None
    item.first_timestamp = None
    item.involved_object.kind = kind
    item.involved_object.name = name
    return item


class TestKubernetesNamespaceEventsAdapterIsPort:
    def test_is_namespace_events_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        assert isinstance(KubernetesNamespaceEventsAdapter(), NamespaceEventsPort)


class TestKubernetesNamespaceEventsAdapterHappyPath:
    def test_list_events_maps_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        core_api = MagicMock()
        event_list = MagicMock()
        event_list.items = [_event()]
        core_api.list_namespaced_event.return_value = event_list
        core_api.read_namespaced_pod.return_value = MagicMock()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNamespaceEventsAdapter()
            events = adapter.list_events(GetNamespaceEventsRequest(namespace="production"))

        assert len(events) == 1
        assert events[0].event_type == "Warning"
        assert events[0].reason == "BackOff"
        assert events[0].object == "pod/payment-api"
        assert events[0].count == 12
        assert events[0].object_exists is True

    def test_list_events_deleted_pod_marked_object_missing(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        class _NotFoundError(Exception):
            status = 404

        core_api = MagicMock()
        event_list = MagicMock()
        event_list.items = [_event(name="ghost-pod")]
        core_api.list_namespaced_event.return_value = event_list
        core_api.read_namespaced_pod.side_effect = _NotFoundError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNamespaceEventsAdapter()
            events = adapter.list_events(GetNamespaceEventsRequest(namespace="production"))

        assert events[0].object_exists is False

    def test_non_pod_object_assumed_to_exist_without_lookup(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        core_api = MagicMock()
        event_list = MagicMock()
        event_list.items = [_event(kind="ReplicaSet", name="payment-api-abc123")]
        core_api.list_namespaced_event.return_value = event_list

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNamespaceEventsAdapter()
            events = adapter.list_events(GetNamespaceEventsRequest(namespace="production"))

        assert events[0].object_exists is True
        core_api.read_namespaced_pod.assert_not_called()


class TestKubernetesNamespaceEventsAdapterErrors:
    def test_namespace_not_found_raises_resource_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        class _NotFoundError(Exception):
            status = 404

        core_api = MagicMock()
        core_api.list_namespaced_event.side_effect = _NotFoundError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNamespaceEventsAdapter()
            with pytest.raises(ResourceNotFoundError) as exc_info:
                adapter.list_events(GetNamespaceEventsRequest(namespace="ghost"))

        assert "ghost" in str(exc_info.value)

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        """TC4: RBAC denies event access → explicit permission error."""
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        class _ForbiddenError(Exception):
            status = 403

        core_api = MagicMock()
        core_api.list_namespaced_event.side_effect = _ForbiddenError()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNamespaceEventsAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_events(GetNamespaceEventsRequest(namespace="production"))

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
            KubernetesNamespaceEventsAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespaced_event.side_effect = TimeoutError("boom")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesNamespaceEventsAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_events(GetNamespaceEventsRequest(namespace="production"))
