from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    MachineConfigPoolCRDNotFoundError,
)

_FORBIDDEN = 403
_NOT_FOUND = 404


def _condition(cond_type: str, status: str, reason: str = "", ltt: str | None = None) -> dict:
    condition = {"type": cond_type, "status": status, "reason": reason}
    if ltt is not None:
        condition["lastTransitionTime"] = ltt
    return condition


def _pool(
    name: str,
    machine_count: int = 3,
    ready: int = 3,
    updated: int = 3,
    degraded_count: int = 0,
    current: str = "rendered-abc",
    desired: str = "rendered-abc",
    paused: bool = False,
    conditions: list[dict] | None = None,
) -> dict:
    return {
        "metadata": {"name": name},
        "spec": {"paused": paused, "configuration": {"name": desired}},
        "status": {
            "machineCount": machine_count,
            "readyMachineCount": ready,
            "updatedMachineCount": updated,
            "degradedMachineCount": degraded_count,
            "configuration": {"name": current},
            "conditions": conditions or [],
        },
    }


def _payload(items: list[dict]) -> dict:
    return {"items": items}


class TestPortImplementation:
    def test_is_a_machine_config_pool_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=MagicMock())

        assert isinstance(adapter, MachineConfigPoolPort)


class TestListMachineConfigPools:
    def test_parses_ready_pool(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                _pool(
                    "master",
                    conditions=[
                        _condition("Updated", "True"),
                        _condition("Updating", "False"),
                        _condition("Degraded", "False"),
                    ],
                )
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["name"] == "master"
        assert result[0]["updating"] is False
        assert result[0]["degraded"] is False
        assert result[0]["machine_count"] == 3
        assert result[0]["current_config"] == "rendered-abc"
        assert result[0]["desired_config"] == "rendered-abc"

    def test_parses_updating_pool_with_since(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                _pool(
                    "worker",
                    machine_count=5,
                    ready=3,
                    updated=2,
                    current="rendered-worker-old456",
                    desired="rendered-worker-new789",
                    conditions=[
                        _condition("Updating", "True", ltt="2026-06-16T01:00:00Z"),
                        _condition("Degraded", "False"),
                    ],
                )
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["updating"] is True
        assert result[0]["updated_machine_count"] == 2
        assert result[0]["updating_since"] == "2026-06-16T01:00:00Z"
        assert result[0]["current_config"] == "rendered-worker-old456"
        assert result[0]["desired_config"] == "rendered-worker-new789"

    def test_parses_degraded_pool_with_reason(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                _pool(
                    "infra",
                    machine_count=1,
                    ready=0,
                    updated=0,
                    degraded_count=1,
                    conditions=[
                        _condition(
                            "Degraded",
                            "True",
                            reason="failed to apply MachineConfig rendered-infra-xyz",
                        )
                    ],
                )
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["degraded"] is True
        assert result[0]["degraded_machine_count"] == 1
        assert result[0]["reason"] == "failed to apply MachineConfig rendered-infra-xyz"

    def test_parses_paused_pool(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload([_pool("worker", paused=True)])
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["paused"] is True

    def test_empty_pool_zero_machine_count(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [_pool("worker", machine_count=0, ready=0, updated=0)]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["machine_count"] == 0

    def test_pool_without_status_defaults_safely(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload([{"metadata": {"name": "bare"}}])
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["name"] == "bare"
        assert result[0]["machine_count"] == 0
        assert result[0]["updating"] is False
        assert result[0]["degraded"] is False
        assert result[0]["paused"] is False
        assert result[0]["updating_since"] is None

    def test_conditions_not_a_list_defaults_safely(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [{"metadata": {"name": "weird"}, "status": {"conditions": "nope"}}]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["updating"] is False
        assert result[0]["degraded"] is False

    def test_payload_without_items_list_returns_empty(self) -> None:
        api = MagicMock()
        api.list_cluster_custom_object.return_value = {"items": None}
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        assert adapter.list_machine_config_pools() == []

    def test_float_and_non_numeric_machine_counts_coerced(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                {
                    "metadata": {"name": "worker"},
                    "status": {
                        "machineCount": 5.0,
                        "readyMachineCount": "oops",
                        "conditions": [],
                    },
                }
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["machine_count"] == 5
        assert result[0]["ready_machine_count"] == 0

    def test_bool_machine_count_coerced_to_int(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                {
                    "metadata": {"name": "worker"},
                    "status": {"machineCount": True, "conditions": []},
                }
            ]
        )
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        result = adapter.list_machine_config_pools()

        assert result[0]["machine_count"] == 1


class TestErrorTranslation:
    def test_not_found_raises_crd_not_found(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.side_effect = _api_exception(_NOT_FOUND)
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        with pytest.raises(MachineConfigPoolCRDNotFoundError):
            adapter.list_machine_config_pools()

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.side_effect = _api_exception(_FORBIDDEN)
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_machine_config_pools()

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.side_effect = _api_exception(500)
        adapter = OpenShiftMachineConfigAdapter(custom_objects_api=api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_machine_config_pools()


class TestLazyClientCreation:
    def test_creates_custom_objects_api_when_not_injected(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
            OpenShiftMachineConfigAdapter,
        )

        fake_api = MagicMock()
        fake_api.list_cluster_custom_object.return_value = _payload([])
        fake_k8s = MagicMock()
        fake_k8s.CustomObjectsApi.return_value = fake_api
        adapter = OpenShiftMachineConfigAdapter()

        with patch.dict("sys.modules", {"kubernetes": MagicMock(client=fake_k8s)}):
            result = adapter.list_machine_config_pools()

        assert result == []
        fake_k8s.CustomObjectsApi.assert_called_once_with()


def _api_exception(status: int) -> Exception:
    exc = Exception("api error")
    exc.status = status  # type: ignore[attr-defined]
    return exc
