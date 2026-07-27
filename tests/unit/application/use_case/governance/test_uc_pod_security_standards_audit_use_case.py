from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.pod_security_standards_audit.command import (
    PodSecurityStandardsAuditCommand,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
    PodSecurityStandardsAuditUseCase,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.response import (
    PodSecurityStandardsAuditResponse,
)


class TestPodSecurityStandardsAuditUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = []
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(
            pod_security_port=port,
        )
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        assert isinstance(result, PodSecurityStandardsAuditResponse)
