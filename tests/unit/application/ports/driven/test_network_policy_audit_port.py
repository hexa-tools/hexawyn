from __future__ import annotations

from abc import ABC

import pytest


class TestNetworkPolicyAuditPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.network_policy_audit_port import (
            NetworkPolicyAuditPort,
        )

        assert issubclass(NetworkPolicyAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.network_policy_audit_port import (
            NetworkPolicyAuditPort,
        )

        with pytest.raises(TypeError):
            NetworkPolicyAuditPort()  # type: ignore[abstract]
