from __future__ import annotations

from collections.abc import Mapping
from unittest.mock import Mock, patch

import pytest
from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
    OpenShiftMachineConfigAdapter,
    _as_int,
    _conditions,
    _find_condition,
    _is_true,
    _items,
    _reason,
    _to_raw,
    _transition_time,
    _translate_error,
)
from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    MachineConfigPoolCRDNotFoundError,
)


def _mcp_item(  # noqa: PLR0913
    name: str,
    machine_count: int = 3,
    ready_machine_count: int = 3,
    updated_machine_count: int = 3,
    degraded_machine_count: int = 0,
    updating: bool = False,
    degraded: bool = False,
    paused: bool = False,
    current_config: str = "",
    desired_config: str = "",
    reason: str = "",
    updating_since: str | None = None,
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Updating", "status": "True" if updating else "False", "reason": ""},
        {"type": "Degraded", "status": "True" if degraded else "False", "reason": reason},
    ]
    if updating:
        conditions[0]["lastTransitionTime"] = updating_since
    if degraded:
        conditions[1]["lastTransitionTime"] = updating_since
    return {
        "metadata": {"name": name},
        "spec": {
            "paused": paused,
            "configuration": {"name": desired_config},
        },
        "status": {
            "machineCount": machine_count,
            "readyMachineCount": ready_machine_count,
            "updatedMachineCount": updated_machine_count,
            "degradedMachineCount": degraded_machine_count,
            "configuration": {"name": current_config},
            "conditions": conditions,
        },
    }


def _api_mock(items: list[Mapping[str, object]] | None = None) -> Mock:
    api = Mock()
    payload = {"items": items or []}
    api.list_cluster_custom_object.return_value = payload
    return api


class TestOpenShiftMachineConfigAdapter:
    def test_implements_port(self) -> None:
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=Mock())
        assert isinstance(adapter, MachineConfigPoolPort)

    def test_list_machine_config_pools_returns_parsed_pools(self) -> None:
        api = _api_mock(
            [
                _mcp_item(
                    "master",
                    machine_count=3,
                    ready_machine_count=3,
                    updated_machine_count=3,
                    current_config="rendered-master-abc",
                    desired_config="rendered-master-abc",
                ),
                _mcp_item(
                    "worker",
                    machine_count=5,
                    ready_machine_count=4,
                    updated_machine_count=3,
                    degraded_machine_count=1,
                    updating=True,
                    degraded=True,
                    reason="NodeDegraded",
                    current_config="rendered-worker-old",
                    desired_config="rendered-worker-new",
                    updating_since="2024-01-15T10:00:00Z",
                ),
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)
        result = adapter.list_machine_config_pools()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "master"
        assert result[0]["machine_count"] == 3  # noqa: PLR2004
        assert result[0]["ready_machine_count"] == 3  # noqa: PLR2004
        assert result[0]["updated_machine_count"] == 3  # noqa: PLR2004
        assert result[0]["degraded_machine_count"] == 0
        assert result[0]["updating"] is False
        assert result[0]["degraded"] is False
        assert result[0]["paused"] is False
        assert result[0]["current_config"] == "rendered-master-abc"
        assert result[0]["desired_config"] == "rendered-master-abc"

        assert result[1]["name"] == "worker"
        assert result[1]["degraded"] is True
        assert result[1]["degraded_machine_count"] == 1
        assert result[1]["reason"] == "NodeDegraded"
        assert result[1]["updating_since"] == "2024-01-15T10:00:00Z"

    def test_list_machine_config_pools_empty(self) -> None:
        api = _api_mock([])
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)
        assert adapter.list_machine_config_pools() == []

    def test_list_machine_config_pools_updating(self) -> None:
        api = _api_mock(
            [
                _mcp_item(
                    "worker",
                    machine_count=3,
                    updated_machine_count=1,
                    updating=True,
                    updating_since="2024-02-01T12:00:00Z",
                )
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)
        result = adapter.list_machine_config_pools()

        assert result[0]["updating"] is True
        assert result[0]["updating_since"] == "2024-02-01T12:00:00Z"

    def test_list_machine_config_pools_paused(self) -> None:
        api = _api_mock([_mcp_item("worker", paused=True)])
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)
        result = adapter.list_machine_config_pools()

        assert result[0]["paused"] is True

    def test_list_machine_config_pools_default_values_when_missing(self) -> None:
        api = _api_mock([{"metadata": {"name": "worker"}, "spec": {}, "status": {}}])
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)
        result = adapter.list_machine_config_pools()

        assert result[0]["name"] == "worker"
        assert result[0]["machine_count"] == 0
        assert result[0]["ready_machine_count"] == 0
        assert result[0]["updated_machine_count"] == 0
        assert result[0]["degraded_machine_count"] == 0
        assert result[0]["updating"] is False
        assert result[0]["degraded"] is False
        assert result[0]["current_config"] == ""
        assert result[0]["desired_config"] == ""
        assert result[0]["reason"] == ""

    # ── error translation ───────────────────────────────────

    def test_api_error_404_raises_crd_not_found(self) -> None:
        api = Mock()
        exc = Exception()
        exc.status = 404  # type: ignore[attr-defined]
        api.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        with pytest.raises(MachineConfigPoolCRDNotFoundError):
            adapter.list_machine_config_pools()

    def test_api_error_403_raises_insufficient_permissions(self) -> None:
        api = Mock()
        exc = Exception()
        exc.status = 403  # type: ignore[attr-defined]
        api.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_machine_config_pools()

    def test_api_error_generic_raises_cluster_unreachable(self) -> None:
        api = Mock()
        exc = Exception()
        exc.status = 500  # type: ignore[attr-defined]
        api.list_cluster_custom_object.side_effect = exc
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_machine_config_pools()

    # ── lazy API construction ───────────────────────────────

    def test_lazy_api_construction(self) -> None:
        with patch("kubernetes.client.CustomObjectsApi") as mock_api_cls:
            mock_api_cls.return_value = _api_mock([_mcp_item("worker")])
            adapter = OpenShiftMachineConfigAdapter()
            result = adapter.list_machine_config_pools()
            assert len(result) == 1
            mock_api_cls.assert_called_once()


class TestHelperFunctions:
    def test_as_int_int(self) -> None:
        assert _as_int(5) == 5  # noqa: PLR2004

    def test_as_int_float(self) -> None:
        assert _as_int(3.7) == 3  # noqa: PLR2004

    def test_as_int_bool_true(self) -> None:
        assert _as_int(True) == 1

    def test_as_int_bool_false(self) -> None:
        assert _as_int(False) == 0

    def test_as_int_str_returns_zero(self) -> None:
        assert _as_int("not-a-number") == 0

    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_is_true_with_true_status(self) -> None:
        condition: Mapping[str, object] = {"type": "Updating", "status": "True"}
        assert _is_true(condition) is True

    def test_is_true_with_false_status(self) -> None:
        condition: Mapping[str, object] = {"type": "Updating", "status": "False"}
        assert _is_true(condition) is False

    def test_is_true_none_returns_false(self) -> None:
        assert _is_true(None) is False

    def test_is_true_no_status_returns_false(self) -> None:
        condition: Mapping[str, object] = {"type": "Updating"}
        assert _is_true(condition) is False

    def test_reason_returns_reason_string(self) -> None:
        condition: Mapping[str, object] = {"type": "Degraded", "reason": "NodeNotReady"}
        assert _reason(condition) == "NodeNotReady"

    def test_reason_none_returns_empty(self) -> None:
        assert _reason(None) == ""

    def test_reason_no_reason_key_returns_empty(self) -> None:
        condition: Mapping[str, object] = {"type": "Degraded"}
        assert _reason(condition) == ""

    def test_transition_time_updating(self) -> None:
        condition: Mapping[str, object] = {
            "type": "Updating",
            "status": "True",
            "lastTransitionTime": "2024-03-01T08:00:00Z",
        }
        assert _transition_time(condition) == "2024-03-01T08:00:00Z"

    def test_transition_time_not_updating_returns_none(self) -> None:
        condition: Mapping[str, object] = {
            "type": "Updating",
            "status": "False",
            "lastTransitionTime": "2024-03-01T08:00:00Z",
        }
        assert _transition_time(condition) is None

    def test_transition_time_none_returns_none(self) -> None:
        assert _transition_time(None) is None

    def test_conditions_returns_list(self) -> None:
        status: Mapping[str, object] = {"conditions": [{"type": "Updating", "status": "False"}]}
        assert len(_conditions(status)) == 1

    def test_conditions_no_conditions_key_returns_empty(self) -> None:
        assert _conditions({}) == []

    def test_conditions_not_a_list_returns_empty(self) -> None:
        assert _conditions({"conditions": "not-a-list"}) == []

    def test_find_condition_finds_matching(self) -> None:
        conditions: list[Mapping[str, object]] = [{"type": "Degraded", "status": "True"}]
        result = _find_condition(conditions, "Degraded")
        assert result is not None
        assert result["status"] == "True"

    def test_find_condition_not_found_returns_none(self) -> None:
        conditions: list[Mapping[str, object]] = [{"type": "Updating", "status": "False"}]
        assert _find_condition(conditions, "Degraded") is None

    def test_items_returns_list_of_mappings(self) -> None:
        payload: Mapping[str, object] = {"items": [{"name": "a"}, "not-a-map", {"name": "b"}]}
        assert len(_items(payload)) == 2  # noqa: PLR2004

    def test_items_no_items_key_returns_empty(self) -> None:
        assert _items({}) == []

    def test_items_not_a_list_returns_empty(self) -> None:
        assert _items({"items": 123}) == []

    def test_to_raw_with_missing_fields(self) -> None:
        item: dict[str, object] = {"metadata": {"name": "pool"}, "spec": {}, "status": {}}
        result = _to_raw(item)
        assert result["name"] == "pool"
        assert result["updating"] is False
        assert result["degraded"] is False
        assert result["paused"] is False

    def test_translate_error_404(self) -> None:
        exc = Exception()
        exc.status = 404  # type: ignore[attr-defined]
        result = _translate_error(exc)
        assert isinstance(result, MachineConfigPoolCRDNotFoundError)

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
