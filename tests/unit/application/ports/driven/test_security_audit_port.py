from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort


class TestSecurityAuditPort:
    def test_is_abstract(self) -> None:
        assert issubclass(SecurityAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SecurityAuditPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for n in ["fetch_failed_admin_calls", "fetch_total_requests"]:
            assert getattr(getattr(SecurityAuditPort, n), "__isabstractmethod__", False)
