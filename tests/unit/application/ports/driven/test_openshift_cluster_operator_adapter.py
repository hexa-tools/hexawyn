from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorStatusPort,
)
from hexawyn.domain.errors import (
    ClusterOperatorCRDNotFoundError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_FORBIDDEN = 403
_NOT_FOUND = 404


def _condition(cond_type: str, status: str, message: str = "", ltt: str | None = None) -> dict:
    condition = {"type": cond_type, "status": status, "message": message}
    if ltt is not None:
        condition["lastTransitionTime"] = ltt
    return condition


def _operator(name: str, conditions: list[dict]) -> dict:
    return {"metadata": {"name": name}, "status": {"conditions": conditions}}


def _payload(items: list[dict]) -> dict:
    return {"items": items}


class TestPortImplementation:
    def test_is_a_cluster_operator_status_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=MagicMock())

        assert isinstance(adapter, ClusterOperatorStatusPort)


class TestListClusterOperators:
    def test_parses_healthy_operator(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                _operator(
                    "authentication",
                    [
                        _condition("Available", "True"),
                        _condition("Progressing", "False"),
                        _condition("Degraded", "False"),
                    ],
                )
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        result = adapter.list_cluster_operators()

        assert result[0]["name"] == "authentication"
        assert result[0]["available"] is True
        assert result[0]["progressing"] is False
        assert result[0]["degraded"] is False
        assert result[0]["available_unknown"] is False

    def test_parses_degraded_operator_with_message_and_since(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                _operator(
                    "etcd",
                    [
                        _condition("Available", "True"),
                        _condition(
                            "Degraded",
                            "True",
                            message="etcd member ip-10-0-1-5 is not responding",
                            ltt="2026-06-16T01:00:00Z",
                        ),
                    ],
                )
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        result = adapter.list_cluster_operators()

        assert result[0]["degraded"] is True
        assert result[0]["message"] == "etcd member ip-10-0-1-5 is not responding"
        assert result[0]["degraded_since"] == "2026-06-16T01:00:00Z"

    def test_progressing_message_used_when_not_degraded(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [
                _operator(
                    "ingress",
                    [
                        _condition("Available", "True"),
                        _condition("Progressing", "True", message="Updating router deployment"),
                        _condition("Degraded", "False"),
                    ],
                )
            ]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        result = adapter.list_cluster_operators()

        assert result[0]["progressing"] is True
        assert result[0]["message"] == "Updating router deployment"

    def test_available_unknown_flagged(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [_operator("kube-apiserver", [_condition("Available", "Unknown")])]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        result = adapter.list_cluster_operators()

        assert result[0]["available"] is False
        assert result[0]["available_unknown"] is True

    def test_operator_without_conditions_defaults_safely(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload([{"metadata": {"name": "bare"}}])
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        result = adapter.list_cluster_operators()

        assert result[0]["name"] == "bare"
        assert result[0]["available"] is False
        assert result[0]["degraded"] is False

    def test_payload_without_items_list_returns_empty(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = {"items": None}
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        assert adapter.list_cluster_operators() == []

    def test_conditions_not_a_list_defaults_safely(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.return_value = _payload(
            [{"metadata": {"name": "weird"}, "status": {"conditions": "not-a-list"}}]
        )
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        result = adapter.list_cluster_operators()

        assert result[0]["name"] == "weird"
        assert result[0]["available"] is False


class TestErrorTranslation:
    def test_not_found_raises_crd_not_found(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.side_effect = _api_exception(_NOT_FOUND)
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        with pytest.raises(ClusterOperatorCRDNotFoundError):
            adapter.list_cluster_operators()

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.side_effect = _api_exception(_FORBIDDEN)
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.list_cluster_operators()

    def test_other_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        api = MagicMock()
        api.list_cluster_custom_object.side_effect = _api_exception(500)
        adapter = OpenShiftClusterOperatorAdapter(custom_objects_api=api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_cluster_operators()


class TestLazyClientCreation:
    def test_creates_custom_objects_api_when_not_injected(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
            OpenShiftClusterOperatorAdapter,
        )

        fake_api = MagicMock()
        fake_api.list_cluster_custom_object.return_value = _payload([])
        fake_k8s = MagicMock()
        fake_k8s.CustomObjectsApi.return_value = fake_api
        adapter = OpenShiftClusterOperatorAdapter()

        with patch.dict("sys.modules", {"kubernetes": MagicMock(client=fake_k8s)}):
            result = adapter.list_cluster_operators()

        assert result == []
        fake_k8s.CustomObjectsApi.assert_called_once_with()


def _api_exception(status: int) -> Exception:
    exc = Exception("api error")
    exc.status = status  # type: ignore[attr-defined]
    return exc
