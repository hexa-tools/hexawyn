from __future__ import annotations

from abc import ABC

import pytest


class TestPodSecurityContextAuditPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.pod_security_context_audit_port import (
            PodSecurityContextAuditPort,
        )

        assert issubclass(PodSecurityContextAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.pod_security_context_audit_port import (
            PodSecurityContextAuditPort,
        )

        with pytest.raises(TypeError):
            PodSecurityContextAuditPort()  # type: ignore[abstract]
