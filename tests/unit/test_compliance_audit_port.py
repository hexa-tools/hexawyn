from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort


class TestComplianceAuditPort:
    def test_is_abstract(self) -> None:
        assert issubclass(ComplianceAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ComplianceAuditPort()  # type: ignore[abstract]
