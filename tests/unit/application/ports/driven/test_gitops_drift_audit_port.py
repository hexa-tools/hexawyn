from __future__ import annotations

from abc import ABC

import pytest


class TestGitOpsDriftAuditPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort

        assert issubclass(GitOpsDriftAuditPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort

        with pytest.raises(TypeError):
            GitOpsDriftAuditPort()  # type: ignore[abstract]
