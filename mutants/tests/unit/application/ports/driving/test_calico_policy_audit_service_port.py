"""Tests for the CalicoPolicyAuditServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_policy_audit.calico_policy_audit_service_port import (
    CalicoPolicyAuditServicePort,
)


class TestCalicoPolicyAuditServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoPolicyAuditServicePort()  # type: ignore[abstract]

    def test_declares_audit(self) -> None:
        assert "audit" in CalicoPolicyAuditServicePort.__abstractmethods__
