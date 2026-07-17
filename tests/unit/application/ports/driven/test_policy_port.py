from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.policy_port import PolicyPort


class TestPolicyPort:
    def test_is_abstract(self) -> None:
        assert issubclass(PolicyPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            PolicyPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for name in [
            "detect_engine",
            "list_policies",
            "get_policy",
            "list_violations",
            "explain_denial",
            "audit",
        ]:
            method = getattr(PolicyPort, name)
            assert getattr(method, "__isabstractmethod__", False)
