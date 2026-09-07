# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import (
    WorkloadComplianceRaw,
)

_TLS_COMPLIANT_SEVERITY = "compliant"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTLSComplianceProviderǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTLSComplianceProviderǁcategory__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTLSComplianceProviderǁfetch__mutmut: MutantDict = {}  # type: ignore


class TLSComplianceProvider:
    """Normalizes the TLS compliance audit into posture records.
    A service whose severity is ``compliant`` passes; anything else (no TLS,
    expired cert, self-signed, ...) is a non-compliant TLS record.
    """

    @_mutmut_mutated(mutants_xǁTLSComplianceProviderǁ__init____mutmut)
    def __init__(self, service: object) -> None:
        self._service = service

    def xǁTLSComplianceProviderǁ__init____mutmut_orig(self, service: object) -> None:
        self._service = service

    def xǁTLSComplianceProviderǁ__init____mutmut_1(self, service: object) -> None:
        self._service = None

    @_mutmut_mutated(mutants_xǁTLSComplianceProviderǁcategory__mutmut)
    def category(self) -> str:
        return "tls"

    def xǁTLSComplianceProviderǁcategory__mutmut_orig(self) -> str:
        return "tls"

    def xǁTLSComplianceProviderǁcategory__mutmut_1(self) -> str:
        return "XXtlsXX"

    def xǁTLSComplianceProviderǁcategory__mutmut_2(self) -> str:
        return "TLS"

    @_mutmut_mutated(mutants_xǁTLSComplianceProviderǁfetch__mutmut)
    def fetch(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
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

    def xǁTLSComplianceProviderǁfetch__mutmut_orig(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
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

    def xǁTLSComplianceProviderǁfetch__mutmut_1(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = None  # type: ignore[attr-defined]
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

    def xǁTLSComplianceProviderǁfetch__mutmut_2(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(None).result  # type: ignore[attr-defined]
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

    def xǁTLSComplianceProviderǁfetch__mutmut_3(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=None,
                namespace=service.namespace,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_4(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=None,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_5(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category=None,
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_6(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                compliant=None,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_7(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=None,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_8(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
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
                detail=None,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_9(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                namespace=service.namespace,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_10(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_11(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_12(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_13(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_14(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
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
                )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_15(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="XXtlsXX",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_16(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="TLS",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_17(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                compliant=service.severity != _TLS_COMPLIANT_SEVERITY,
                exempt=False,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_18(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
            AuditTlsComplianceCommand,
        )

        report = self._service.audit(AuditTlsComplianceCommand()).result  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=service.service_name,
                namespace=service.namespace,
                category="tls",
                compliant=service.severity == _TLS_COMPLIANT_SEVERITY,
                exempt=True,
                detail="" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_19(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
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
                detail="XXXX" if service.severity == _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

    def xǁTLSComplianceProviderǁfetch__mutmut_20(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.audit_tls_compliance.command import (
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
                detail="" if service.severity != _TLS_COMPLIANT_SEVERITY else service.severity,
            )
            for service in report.services
        ]

mutants_xǁTLSComplianceProviderǁ__init____mutmut['_mutmut_orig'] = TLSComplianceProvider.xǁTLSComplianceProviderǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁ__init____mutmut['xǁTLSComplianceProviderǁ__init____mutmut_1'] = TLSComplianceProvider.xǁTLSComplianceProviderǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁTLSComplianceProviderǁcategory__mutmut['_mutmut_orig'] = TLSComplianceProvider.xǁTLSComplianceProviderǁcategory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁcategory__mutmut['xǁTLSComplianceProviderǁcategory__mutmut_1'] = TLSComplianceProvider.xǁTLSComplianceProviderǁcategory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁcategory__mutmut['xǁTLSComplianceProviderǁcategory__mutmut_2'] = TLSComplianceProvider.xǁTLSComplianceProviderǁcategory__mutmut_2 # type: ignore # mutmut generated

mutants_xǁTLSComplianceProviderǁfetch__mutmut['_mutmut_orig'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_1'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_2'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_3'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_4'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_5'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_6'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_7'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_8'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_9'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_10'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_11'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_12'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_13'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_14'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_15'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_16'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_17'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_18'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_19'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTLSComplianceProviderǁfetch__mutmut['xǁTLSComplianceProviderǁfetch__mutmut_20'] = TLSComplianceProvider.xǁTLSComplianceProviderǁfetch__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPodSecurityProviderǁcategory__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPodSecurityProviderǁfetch__mutmut: MutantDict = {}  # type: ignore


class PodSecurityProvider:
    """Normalizes the Pod Security Standards audit into posture records.
    The audit only returns findings for violating pods, so every finding maps
    to a non-compliant pod_security record.
    """

    @_mutmut_mutated(mutants_xǁPodSecurityProviderǁ__init____mutmut)
    def __init__(self, service: object) -> None:
        self._service = service

    def xǁPodSecurityProviderǁ__init____mutmut_orig(self, service: object) -> None:
        self._service = service

    def xǁPodSecurityProviderǁ__init____mutmut_1(self, service: object) -> None:
        self._service = None

    @_mutmut_mutated(mutants_xǁPodSecurityProviderǁcategory__mutmut)
    def category(self) -> str:
        return "pod_security"

    def xǁPodSecurityProviderǁcategory__mutmut_orig(self) -> str:
        return "pod_security"

    def xǁPodSecurityProviderǁcategory__mutmut_1(self) -> str:
        return "XXpod_securityXX"

    def xǁPodSecurityProviderǁcategory__mutmut_2(self) -> str:
        return "POD_SECURITY"

    @_mutmut_mutated(mutants_xǁPodSecurityProviderǁfetch__mutmut)
    def fetch(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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

    def xǁPodSecurityProviderǁfetch__mutmut_orig(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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

    def xǁPodSecurityProviderǁfetch__mutmut_1(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = None  # type: ignore[attr-defined]
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

    def xǁPodSecurityProviderǁfetch__mutmut_2(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(None)  # type: ignore[attr-defined]
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

    def xǁPodSecurityProviderǁfetch__mutmut_3(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=None,
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_4(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=None,
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_5(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category=None,
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_6(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=None,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_7(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=None,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_8(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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
                detail=None,
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_9(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_10(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_11(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_12(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_13(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_14(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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
                )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_15(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["XXpod_nameXX"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_16(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["POD_NAME"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_17(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["XXnamespaceXX"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_18(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["NAMESPACE"],
                category="pod_security",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_19(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="XXpod_securityXX",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_20(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="POD_SECURITY",
                compliant=False,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_21(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=True,
                exempt=False,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_22(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
            DetectPrivilegedPodsCommand,
        )

        response = self._service.audit_pod_security(DetectPrivilegedPodsCommand())  # type: ignore[attr-defined]
        return [
            WorkloadComplianceRaw(
                workload=finding["pod_name"],
                namespace=finding["namespace"],
                category="pod_security",
                compliant=False,
                exempt=True,
                detail="Pod Security Standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_23(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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
                detail="XXPod Security Standards violationXX",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_24(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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
                detail="pod security standards violation",
            )
            for finding in response.findings
        ]

    def xǁPodSecurityProviderǁfetch__mutmut_25(self) -> list[WorkloadComplianceRaw]:
        from hexawyn.application.use_case.security.detect_privileged_pods.command import (  # noqa: E501  # hexa-lazy-import
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
                detail="POD SECURITY STANDARDS VIOLATION",
            )
            for finding in response.findings
        ]

mutants_xǁPodSecurityProviderǁ__init____mutmut['_mutmut_orig'] = PodSecurityProvider.xǁPodSecurityProviderǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁ__init____mutmut['xǁPodSecurityProviderǁ__init____mutmut_1'] = PodSecurityProvider.xǁPodSecurityProviderǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPodSecurityProviderǁcategory__mutmut['_mutmut_orig'] = PodSecurityProvider.xǁPodSecurityProviderǁcategory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁcategory__mutmut['xǁPodSecurityProviderǁcategory__mutmut_1'] = PodSecurityProvider.xǁPodSecurityProviderǁcategory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁcategory__mutmut['xǁPodSecurityProviderǁcategory__mutmut_2'] = PodSecurityProvider.xǁPodSecurityProviderǁcategory__mutmut_2 # type: ignore # mutmut generated

mutants_xǁPodSecurityProviderǁfetch__mutmut['_mutmut_orig'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_1'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_2'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_3'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_4'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_5'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_6'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_7'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_8'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_9'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_10'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_11'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_12'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_13'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_14'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_15'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_16'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_17'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_18'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_19'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_20'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_21'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_22'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_23'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_24'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPodSecurityProviderǁfetch__mutmut['xǁPodSecurityProviderǁfetch__mutmut_25'] = PodSecurityProvider.xǁPodSecurityProviderǁfetch__mutmut_25 # type: ignore # mutmut generated
