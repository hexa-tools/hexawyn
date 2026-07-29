from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
    KubernetesNetworkPolicyAdapter,
    _is_strict_mtls,
    _items,
    _to_network_policy_raw,
    _translate_error,
)
from hexawyn.application.ports.driven.network_policy_audit_port import (
    NetworkPolicyAuditPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestKubernetesNetworkPolicyAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesNetworkPolicyAdapter(), NetworkPolicyAuditPort)


class TestToNetworkPolicyRaw:
    def test_with_match_labels(self) -> None:
        item = _mk(
            metadata=_mk(name="np", namespace="ns"),
            spec=_mk(
                pod_selector=_mk(match_labels={"app": "web"}, match_expressions=[]),
                ingress=[_mk()],
                egress=[],
            ),
        )
        result = _to_network_policy_raw(item)
        assert result["name"] == "np"
        assert result["namespace"] == "ns"
        assert result["ingress_rule_count"] == 1
        assert result["egress_rule_count"] == 0
        assert result["has_empty_pod_selector"] is False

    def test_empty_pod_selector(self) -> None:
        item = _mk(
            metadata=_mk(name="np", namespace="ns"),
            spec=_mk(
                pod_selector=_mk(match_labels={}, match_expressions=[]),
                ingress=[],
                egress=[],
            ),
        )
        result = _to_network_policy_raw(item)
        assert result["has_empty_pod_selector"] is True

    def test_none_pod_selector(self) -> None:
        item = _mk(
            metadata=_mk(name="np", namespace="ns"),
            spec=_mk(pod_selector=None, ingress=[], egress=[]),
        )
        result = _to_network_policy_raw(item)
        assert result["has_empty_pod_selector"] is True


class TestItems:
    def test_returns_items_from_dict(self) -> None:
        assert _items({"items": [1, 2, 3]}) == [1, 2, 3]

    def test_not_dict_returns_empty(self) -> None:
        assert _items("bad") == []

    def test_no_items_key_returns_empty(self) -> None:
        assert _items({"other": "value"}) == []

    def test_items_not_list_returns_empty(self) -> None:
        assert _items({"items": "bad"}) == []


class TestIsStrictMtls:
    def test_strict_mtls(self) -> None:
        item = {"spec": {"mtls": {"mode": "STRICT"}}}
        assert _is_strict_mtls(item) is True

    def test_non_strict_mtls(self) -> None:
        item = {"spec": {"mtls": {"mode": "PERMISSIVE"}}}
        assert _is_strict_mtls(item) is False

    def test_not_dict_returns_false(self) -> None:
        assert _is_strict_mtls("bad") is False

    def test_no_spec_returns_false(self) -> None:
        assert _is_strict_mtls({"other": "value"}) is False

    def test_no_mtls_returns_false(self) -> None:
        assert _is_strict_mtls({"spec": {"other": "value"}}) is False

    def test_mtls_not_dict_returns_false(self) -> None:
        assert _is_strict_mtls({"spec": {"mtls": "bad"}}) is False


class TestNetworkPolicyTranslateError:
    def test_forbidden(self) -> None:
        assert isinstance(_translate_error(_mk(status=403)), InsufficientPermissionsError)

    def test_other(self) -> None:
        assert isinstance(_translate_error(Exception("err")), ClusterUnreachableError)
