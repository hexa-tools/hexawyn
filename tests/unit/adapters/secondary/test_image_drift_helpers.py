from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
    _match_labels,
    _matches_selector,
    _translate_error,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestMatchLabels:
    def test_returns_match_labels_dict(self) -> None:
        deployment = _mk(spec=_mk(selector=_mk(match_labels={"app": "nginx"})))
        result = _match_labels(deployment)
        assert result == {"app": "nginx"}

    def test_returns_empty_dict_when_none(self) -> None:
        deployment = _mk(spec=None)
        result = _match_labels(deployment)
        assert result == {}

    def test_returns_empty_dict_when_selector_none(self) -> None:
        deployment = _mk(spec=_mk(selector=None))
        result = _match_labels(deployment)
        assert result == {}

    def test_returns_empty_dict_when_match_labels_none(self) -> None:
        deployment = _mk(spec=_mk(selector=_mk(match_labels=None)))
        result = _match_labels(deployment)
        assert result == {}


class TestMatchesSelector:
    def test_all_keys_match(self) -> None:
        assert _matches_selector({"app": "nginx", "env": "prod"}, {"app": "nginx"}) is True

    def test_one_key_mismatch(self) -> None:
        assert _matches_selector({"app": "nginx"}, {"app": "alpine"}) is False

    def test_missing_key_in_labels(self) -> None:
        assert _matches_selector({"app": "nginx"}, {"env": "prod"}) is False

    def test_empty_selector_matches_all(self) -> None:
        assert _matches_selector({"app": "nginx"}, {}) is True

    def test_value_is_none(self) -> None:
        assert _matches_selector({"app": None}, {"app": "nginx"}) is False


class TestImageDriftTranslateError:
    def test_forbidden(self) -> None:
        exc = _mk(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_other_returns_cluster_unreachable(self) -> None:
        exc = Exception("timeout")
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)
