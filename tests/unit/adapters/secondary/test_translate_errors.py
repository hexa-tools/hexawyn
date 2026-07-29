"""Tests for all _translate_error functions across adapters."""

from __future__ import annotations

from unittest.mock import Mock

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
    _translate_error as _adaptive_inv_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
    _translate_error as _audit_log_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
    _translate_error as _capacity_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
    _translate_error as _headroom_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
    _translate_error as _image_drift_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
    _translate_error as _image_inv_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
    _translate_error as _ns_events_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
    _translate_error as _node_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
    _translate_pod_error,
)
from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
    _translate_error as _pod_logs_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
    _translate_error as _pod_sec_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
    _translate_error as _rbac_translate,
)
from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
    _translate_error as _secret_translate,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


def _exc(status: int | None = None) -> Exception:
    e = Mock()
    if status is not None:
        type(e).status = status
    return e


class TestTranslateErrors:
    @pytest.mark.parametrize(
        "fn,args",
        [
            (_adaptive_inv_translate, (_exc(403), "ns", "pod")),
            (_adaptive_inv_translate, (_exc(500), "ns", "pod")),
            (_audit_log_translate, (_exc(403),)),
            (_audit_log_translate, (_exc(500),)),
            (_capacity_translate, (_exc(403),)),
            (_capacity_translate, (_exc(500),)),
            (_headroom_translate, (_exc(403),)),
            (_headroom_translate, (_exc(500),)),
            (_image_drift_translate, (_exc(403),)),
            (_image_drift_translate, (_exc(500),)),
            (_image_inv_translate, (_exc(403),)),
            (_image_inv_translate, (_exc(500),)),
            (_ns_events_translate, (_exc(404), Mock())),
            (_ns_events_translate, (_exc(500), Mock())),
            (_node_translate, (_exc(403),)),
            (_node_translate, (_exc(500),)),
            (_pod_sec_translate, (_exc(403),)),
            (_pod_sec_translate, (_exc(500),)),
            (_rbac_translate, (_exc(403),)),
            (_rbac_translate, (_exc(500),)),
            (_secret_translate, (_exc(403),)),
            (_secret_translate, (_exc(500),)),
        ],
    )
    def test_returns_hexawyn_error(self, fn: object, args: tuple[object, ...]) -> None:
        result = fn(*args)
        assert isinstance(  # noqa: UP038
            result,
            (
                ClusterUnreachableError,
                InsufficientPermissionsError,
                ResourceNotFoundError,
                type(None),
            ),
        )

    def test_pod_logs_translate_returns_error(self) -> None:
        e = _exc(500)
        from unittest.mock import Mock as Mk

        result = _pod_logs_translate(e, Mk())
        assert isinstance(result, ClusterUnreachableError)

    def test_pod_log_search_translate_returns_error(self) -> None:
        result = _translate_pod_error(_exc(404), "pod", "ns")
        assert isinstance(result, ResourceNotFoundError)
