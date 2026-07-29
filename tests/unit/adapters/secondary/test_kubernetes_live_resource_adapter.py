from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
    _to_live_resource,
    _translate_error,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


class MockObj:
    def __init__(self, **kwargs: object) -> None:
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def to_dict(self) -> dict[str, object]:
        return getattr(self, "_to_dict_data", {})


class TestToLiveResource:
    def test_deployment(self) -> None:
        item = MockObj(
            metadata=MockObj(name="my-deploy", namespace="ns", labels={"app": "x"}, annotations={}),
            to_dict=MockObj(to_dict=lambda: {"spec": {"replicas": 3}}),
        )
        result = _to_live_resource("Deployment", item)
        assert result["kind"] == "Deployment"
        assert result["name"] == "my-deploy"
        assert result["namespace"] == "ns"
        assert result["labels"] == {"app": "x"}

    def test_no_metadata(self) -> None:
        item = MockObj(to_dict=MockObj(to_dict=lambda: {}))
        result = _to_live_resource("ConfigMap", item)
        assert result["name"] == ""
        assert result["labels"] == {}


class TestTranslateError:
    def test_forbidden(self) -> None:
        exc = MockObj(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_other(self) -> None:
        exc = MockObj(status=500)
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)

    def test_no_status(self) -> None:
        exc = MockObj()
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)
