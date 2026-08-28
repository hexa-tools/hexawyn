"""Tests for the CalicoSegmentationAuditServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_segmentation_audit.calico_segmentation_audit_service_port import (  # noqa: E501
    CalicoSegmentationAuditServicePort,
)


class TestCalicoSegmentationAuditServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoSegmentationAuditServicePort()  # type: ignore[abstract]

    def test_declares_audit(self) -> None:
        assert "audit" in CalicoSegmentationAuditServicePort.__abstractmethods__
