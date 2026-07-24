from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import WorkloadComplianceRaw

_TLS_COMPLIANT_SEVERITY = "compliant"


class TLSComplianceProvider:
    """Normalizes the TLS compliance audit into posture records.

    A service whose severity is ``compliant`` passes; anything else (no TLS,
    expired cert, self-signed, ...) is a non-compliant TLS record.
    """

    def __init__(self, service: object) -> None:
        self._service = service

    def category(self) -> str:
        return "tls"

    def fetch(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]


class PodSecurityProvider:
    """Normalizes the Pod Security Standards audit into posture records.

    The audit only returns findings for violating pods, so every finding maps
    to a non-compliant pod_security record.
    """

    def __init__(self, service: object) -> None:
        self._service = service

    def category(self) -> str:
        return "pod_security"

    def fetch(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]
