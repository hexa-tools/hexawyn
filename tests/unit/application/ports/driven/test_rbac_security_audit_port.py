from __future__ import annotations

from abc import ABC

import pytest


class TestRBACSecurityAuditPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.rbac_security_audit_port import (
            RBACSecurityAuditPort,
        )

        assert issubclass(RBACSecurityAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.rbac_security_audit_port import (
            RBACSecurityAuditPort,
        )

        with pytest.raises(TypeError):
            RBACSecurityAuditPort()  # type: ignore[abstract]
