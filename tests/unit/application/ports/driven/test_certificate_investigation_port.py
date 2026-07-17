from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)


class TestCertificateInvestigationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(CertificateInvestigationPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            CertificateInvestigationPort()  # type: ignore[abstract]
