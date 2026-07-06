from __future__ import annotations

from abc import ABC

import pytest


class TestExternalExposureAuditPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.external_exposure_audit_port import (
            ExternalExposureAuditPort,
        )

        assert issubclass(ExternalExposureAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.external_exposure_audit_port import (
            ExternalExposureAuditPort,
        )

        with pytest.raises(TypeError):
            ExternalExposureAuditPort()  # type: ignore[abstract]
