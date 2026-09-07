"""Tests for the CalicoBgpAuditServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_bgp_audit.calico_bgp_audit_service_port import (
    CalicoBgpAuditServicePort,
)


class TestCalicoBgpAuditServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoBgpAuditServicePort()  # type: ignore[abstract]

    def test_declares_audit(self) -> None:
        assert "audit" in CalicoBgpAuditServicePort.__abstractmethods__
