from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
    _to_running_images,
    _translate_error,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestToRunningImages:
    def test_single_container(self) -> None:
        pod = _mk(
            metadata=_mk(namespace="default", name="my-pod"),
            spec=_mk(
                init_containers=[],
                containers=[_mk(image="nginx:1.21")],
                ephemeral_containers=[],
            ),
        )
        result = _to_running_images(pod)
        assert len(result) == 1
        assert result[0]["image"] == "nginx:1.21"
        assert result[0]["namespace"] == "default"
        assert result[0]["pod_name"] == "my-pod"

    def test_init_and_regular_containers(self) -> None:
        pod = _mk(
            metadata=_mk(namespace="ns", name="pod"),
            spec=_mk(
                init_containers=[_mk(image="init:1")],
                containers=[_mk(image="main:1")],
                ephemeral_containers=[],
            ),
        )
        result = _to_running_images(pod)
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["image"] == "init:1"
        assert result[1]["image"] == "main:1"

    def test_ephemeral_container(self) -> None:
        pod = _mk(
            metadata=_mk(namespace="ns", name="pod"),
            spec=_mk(
                init_containers=[],
                containers=[],
                ephemeral_containers=[_mk(image="debug:latest")],
            ),
        )
        result = _to_running_images(pod)
        assert len(result) == 1
        assert result[0]["image"] == "debug:latest"

    def test_none_containers_handled(self) -> None:
        pod = _mk(
            metadata=_mk(namespace="ns", name="pod"),
            spec=_mk(
                init_containers=None,
                containers=None,
                ephemeral_containers=None,
            ),
        )
        result = _to_running_images(pod)
        assert result == []


class TestInventoryTranslateError:
    def test_forbidden(self) -> None:
        exc = _mk(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_other_returns_cluster_unreachable(self) -> None:
        exc = Exception("timeout")
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)
