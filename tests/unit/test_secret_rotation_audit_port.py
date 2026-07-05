from __future__ import annotations

from abc import ABC

import pytest


class TestSecretRotationAuditPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.secret_rotation_audit_port import (
            SecretRotationAuditPort,
        )

        assert issubclass(SecretRotationAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.secret_rotation_audit_port import (
            SecretRotationAuditPort,
        )

        with pytest.raises(TypeError):
            SecretRotationAuditPort()  # type: ignore[abstract]
