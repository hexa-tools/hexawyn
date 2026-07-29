from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
    _translate_pod_error,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestTranslatePodError:
    def test_not_found(self) -> None:
        assert isinstance(
            _translate_pod_error(_mk(status=404), "p", "n"),
            ResourceNotFoundError,
        )

    def test_forbidden(self) -> None:
        assert isinstance(
            _translate_pod_error(_mk(status=403), "p", "n"),
            InsufficientPermissionsError,
        )

    def test_other(self) -> None:
        assert isinstance(
            _translate_pod_error(Exception("err"), "p", "n"),
            ClusterUnreachableError,
        )
