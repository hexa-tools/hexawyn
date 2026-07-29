from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
    _extract_container_status,
    _translate_error,
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


class TestExtractContainerStatus:
    def test_sum_of_all_restart_counts(self) -> None:
        pod = _mk(
            status=_mk(
                container_statuses=[
                    _mk(restart_count=2, last_state=_mk(terminated=None)),
                    _mk(restart_count=3, last_state=_mk(terminated=None)),
                ]
            )
        )
        restart_count, last_reason = _extract_container_status(pod)
        assert restart_count == 5  # noqa: PLR2004
        assert last_reason is None

    def test_restart_count_zero_for_none(self) -> None:
        pod = _mk(
            status=_mk(
                container_statuses=[
                    _mk(restart_count=None, last_state=_mk(terminated=None)),
                ]
            )
        )
        restart_count, _ = _extract_container_status(pod)
        assert restart_count == 0

    def test_empty_statuses(self) -> None:
        pod = _mk(status=_mk(container_statuses=[]))
        restart_count, last_reason = _extract_container_status(pod)
        assert restart_count == 0
        assert last_reason is None

    def test_none_statuses(self) -> None:
        pod = _mk(status=_mk(container_statuses=None))
        restart_count, last_reason = _extract_container_status(pod)
        assert restart_count == 0
        assert last_reason is None

    def test_detects_last_termination_reason(self) -> None:
        pod = _mk(
            status=_mk(
                container_statuses=[
                    _mk(restart_count=0, last_state=_mk(terminated=_mk(reason="OOMKilled"))),
                ]
            )
        )
        _, last_reason = _extract_container_status(pod)
        assert last_reason == "OOMKilled"

    def test_returns_first_termination_reason_only(self) -> None:
        pod = _mk(
            status=_mk(
                container_statuses=[
                    _mk(restart_count=1, last_state=_mk(terminated=_mk(reason="Error"))),
                    _mk(restart_count=1, last_state=_mk(terminated=_mk(reason="OOMKilled"))),
                ]
            )
        )
        _, last_reason = _extract_container_status(pod)
        assert last_reason == "Error"


class TestTranslateErrorAdaptive:
    def test_not_found_returns_resource_not_found(self) -> None:
        exc = _mk(status=404)
        result = _translate_error(exc, "default", "my-pod")
        assert isinstance(result, ResourceNotFoundError)

    def test_forbidden_returns_insufficient_permissions(self) -> None:
        exc = _mk(status=403)
        result = _translate_error(exc, "default", "my-pod")
        assert isinstance(result, InsufficientPermissionsError)

    def test_other_status_returns_cluster_unreachable(self) -> None:
        exc = _mk(status=500)
        result = _translate_error(exc, "default", "my-pod")
        assert isinstance(result, ClusterUnreachableError)

    def test_no_status_returns_cluster_unreachable(self) -> None:
        exc = Exception("network error")
        result = _translate_error(exc, "default", "my-pod")
        assert isinstance(result, ClusterUnreachableError)
