from __future__ import annotations

from collections.abc import Mapping
from unittest.mock import Mock, patch

import pytest
from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
    OpenShiftClusterOperatorAdapter,
    _condition_status,
    _conditions,
    _degraded_since,
    _find_condition,
    _items,
    _root_cause_message,
    _to_raw,
    _translate_error,
)
from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorStatusPort,
)
from hexawyn.domain.errors import (
    ClusterOperatorCRDNotFoundError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)


def _operator_item(  # noqa: PLR0913
    name: str,
    available: str = "True",
    progressing: str = "False",
    degraded: str = "False",
    message: str = "",
    degraded_since: str | None = None,
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Available", "status": available, "message": ""},
        {"type": "Progressing", "status": progressing, "message": ""},
        {
            "type": "Degraded",
            "status": degraded,
            "message": message,
            "lastTransitionTime": degraded_since,
        },
    ]
    return {
        "metadata": {"name": name},
        "status": {"conditions": conditions},
    }


def _api_mock(items: list[Mapping[str, object]] | None = None) -> Mock:
    api = Mock()
    payload = {"items": items or []}
    api.list_cluster_custom_object.return_value = payload
    return api


class TestOpenShiftClusterOperatorAdapter:
    def test_implements_port(self) -> None:
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=Mock())
        assert isinstance(adapter, ClusterOperatorStatusPort)

    def test_list_cluster_operators_returns_parsed_operators(self) -> None:
        api = _api_mock(
            [
                _operator_item(
                    "authentication", available="True", progressing="False", degraded="False"
                ),
                _operator_item(
                    "console",
                    available="False",
                    progressing="True",
                    degraded="False",
                    message="Updating console",
                ),
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        result = adapter.list_cluster_operators()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "authentication"
        assert result[0]["available"] is True
        assert result[0]["progressing"] is False
        assert result[0]["degraded"] is False
        assert result[0]["available_unknown"] is False
        assert result[1]["name"] == "console"
        assert result[1]["available"] is False

    def test_list_cluster_operators_empty(self) -> None:
        api = _api_mock([])
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        assert adapter.list_cluster_operators() == []

    def test_list_cluster_operators_degraded_with_message(self) -> None:
        api = _api_mock(
            [
                _operator_item(
                    "etcd",
                    available="True",
                    progressing="False",
                    degraded="True",
                    message="etcd members degraded",
                )
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        result = adapter.list_cluster_operators()

        assert result[0]["degraded"] is True
        assert result[0]["message"] == "etcd members degraded"

    def test_list_cluster_operators_available_unknown(self) -> None:
        api = _api_mock(
            [_operator_item("network", available="Unknown", progressing="False", degraded="False")]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        result = adapter.list_cluster_operators()

        assert result[0]["available"] is False
        assert result[0]["available_unknown"] is True

    def test_list_cluster_operators_degraded_since(self) -> None:
        api = _api_mock(
            [
                _operator_item(
                    "etcd",
                    available="True",
                    progressing="False",
                    degraded="True",
                    message="degraded",
                    degraded_since="2024-01-15T10:30:00Z",
                )
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        result = adapter.list_cluster_operators()

        assert result[0]["degraded_since"] == "2024-01-15T10:30:00Z"

    def test_list_cluster_operators_not_degraded_since_is_none(self) -> None:
        api = _api_mock(
            [_operator_item("console", available="True", progressing="False", degraded="False")]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        result = adapter.list_cluster_operators()

        assert result[0]["degraded_since"] is None

    def test_list_cluster_operators_root_cause_from_degraded(self) -> None:
        api = _api_mock(
            [
                _operator_item(
                    "storage",
                    available="True",
                    progressing="False",
                    degraded="True",
                    message="PersistentVolumeDegraded",
                )
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)
        result = adapter.list_cluster_operators()

        assert result[0]["message"] == "PersistentVolumeDegraded"

    # ── error translation ───────────────────────────────────

    def test_api_error_404_raises_crd_not_found(self) -> None:
        api = Mock()
        exc = Exception()
        exc.status = 404  # type: ignore[attr-defined]
        api.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        with pytest.raises(ClusterOperatorCRDNotFoundError):
            adapter.list_cluster_operators()

    def test_api_error_403_raises_insufficient_permissions(self) -> None:
        api = Mock()
        exc = Exception()
        exc.status = 403  # type: ignore[attr-defined]
        api.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_cluster_operators()

    def test_api_error_generic_raises_cluster_unreachable(self) -> None:
        api = Mock()
        exc = Exception()
        exc.status = 500  # type: ignore[attr-defined]
        api.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_cluster_operators()

    # ── lazy API construction ───────────────────────────────

    def test_lazy_api_construction(self) -> None:
        with patch("kubernetes.client.CustomObjectsApi") as mock_api_cls:
            mock_api_cls.return_value = _api_mock([_operator_item("console")])
            adapter = OpenShiftClusterOperatorAdapter()
            result = adapter.list_cluster_operators()
            assert len(result) == 1
            mock_api_cls.assert_called_once()


class TestHelperFunctions:
    def test_to_raw_default_values(self) -> None:
        item: dict[str, object] = {"metadata": {"name": "test"}}
        result = _to_raw(item)
        assert result["name"] == "test"
        assert result["available"] is False
        assert result["progressing"] is False
        assert result["degraded"] is False
        assert result["available_unknown"] is False
        assert result["message"] == ""
        assert result["degraded_since"] is None

    def test_conditions_returns_list(self) -> None:
        item: dict[str, object] = {
            "status": {"conditions": [{"type": "Available", "status": "True"}]}
        }
        result = _conditions(item)
        assert len(result) == 1
        assert result[0]["type"] == "Available"

    def test_conditions_no_status_returns_empty(self) -> None:
        assert _conditions({}) == []

    def test_conditions_no_conditions_key_returns_empty(self) -> None:
        assert _conditions({"status": {}}) == []

    def test_find_condition_finds_matching(self) -> None:
        conditions: list[Mapping[str, object]] = [{"type": "Available", "status": "True"}]
        result = _find_condition(conditions, "Available")
        assert result is not None
        assert result["status"] == "True"

    def test_find_condition_not_found_returns_none(self) -> None:
        conditions: list[Mapping[str, object]] = [{"type": "Available", "status": "True"}]
        assert _find_condition(conditions, "Degraded") is None

    def test_condition_status_returns_status_string(self) -> None:
        conditions: list[Mapping[str, object]] = [{"type": "Available", "status": "True"}]
        assert _condition_status(conditions, "Available") == "True"

    def test_condition_status_not_found_returns_empty(self) -> None:
        conditions: list[Mapping[str, object]] = []
        assert _condition_status(conditions, "Available") == ""

    def test_root_cause_message_returns_degraded_message_first(self) -> None:
        conditions: list[Mapping[str, object]] = [
            {"type": "Degraded", "status": "True", "message": "disk pressure"},
            {"type": "Progressing", "status": "True", "message": "updating"},
        ]
        assert _root_cause_message(conditions) == "disk pressure"

    def test_root_cause_message_falls_back_to_progressing(self) -> None:
        conditions: list[Mapping[str, object]] = [
            {"type": "Progressing", "status": "True", "message": "reconciling"},
        ]
        assert _root_cause_message(conditions) == "reconciling"

    def test_root_cause_message_no_message_returns_empty(self) -> None:
        conditions: list[Mapping[str, object]] = []
        assert _root_cause_message(conditions) == ""

    def test_degraded_since_when_degraded(self) -> None:
        conditions: list[Mapping[str, object]] = [
            {"type": "Degraded", "status": "True", "lastTransitionTime": "2024-06-01T00:00:00Z"}
        ]
        assert _degraded_since(conditions) == "2024-06-01T00:00:00Z"

    def test_degraded_since_not_degraded_returns_none(self) -> None:
        conditions: list[Mapping[str, object]] = [{"type": "Degraded", "status": "False"}]
        assert _degraded_since(conditions) is None

    def test_degraded_since_no_condition_returns_none(self) -> None:
        assert _degraded_since([]) is None

    def test_items_returns_list_of_mappings(self) -> None:
        payload: Mapping[str, object] = {"items": [{"name": "a"}, "not-a-mapping", {"name": "b"}]}
        assert len(_items(payload)) == 2  # noqa: PLR2004

    def test_items_no_items_key_returns_empty(self) -> None:
        assert _items({}) == []

    def test_items_not_a_list_returns_empty(self) -> None:
        assert _items({"items": "not-a-list"}) == []

    def test_translate_error_404(self) -> None:
        exc = Exception()
        exc.status = 404  # type: ignore[attr-defined]
        result = _translate_error(exc)
        assert isinstance(result, ClusterOperatorCRDNotFoundError)

    def test_translate_error_403(self) -> None:
        exc = Exception()
        exc.status = 403  # type: ignore[attr-defined]
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_translate_error_generic(self) -> None:
        exc = Exception()
        exc.status = 500  # type: ignore[attr-defined]
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)
