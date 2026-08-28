"""Tests for the CalicoEncryptionStatusServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_encryption_status.calico_encryption_status_service_port import (  # noqa: E501
    CalicoEncryptionStatusServicePort,
)


class TestCalicoEncryptionStatusServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoEncryptionStatusServicePort()  # type: ignore[abstract]

    def test_declares_encryption_status(self) -> None:
        assert "encryption_status" in CalicoEncryptionStatusServicePort.__abstractmethods__
