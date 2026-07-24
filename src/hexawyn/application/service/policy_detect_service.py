from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_detect.command import (
    PolicyDetectCommand,
)
from hexawyn.application.use_case.policy_detect.response import (
    PolicyDetectResponse,
)
from hexawyn.application.ports.driving.policy_detect.policy_detect_service_port import (
    PolicyDetectServicePort,
)


class PolicyDetectService(PolicyDetectServicePort):
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def detect(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )
