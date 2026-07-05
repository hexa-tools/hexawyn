from __future__ import annotations

from abc import ABC

import pytest


class TestAuditSecretRotationServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_service_port import (
            AuditSecretRotationServicePort,
        )

        assert issubclass(AuditSecretRotationServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_service_port import (
            AuditSecretRotationServicePort,
        )

        with pytest.raises(TypeError):
            AuditSecretRotationServicePort()  # type: ignore[abstract]
