from __future__ import annotations

from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
from hexawyn.application.ports.driven.external_exposure_audit_port import (
    ExternalExposureAuditPort,
)
from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort
from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    ImageVulnerabilityScanPort,
)
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
from hexawyn.application.ports.driven.network_policy_audit_port import (
    NetworkPolicyAuditPort,
)
from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    PodSecurityContextAuditPort,
)
from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
from hexawyn.application.ports.driven.rbac_security_audit_port import RBACSecurityAuditPort
from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRotationAuditPort
from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.application.ports.driven.security_posture_port import SecurityPosturePort
from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort
from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort
from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort
from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.mcp.providers.detector import context_name


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def build_rbac_audit_adapter() -> RBACSecurityAuditPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_rbac_adapter import (
        KubernetesRBACAdapter,
    )

    return KubernetesRBACAdapter()


def build_pod_security_adapter() -> PodSecurityContextAuditPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
        KubernetesPodSecurityAdapter,
    )

    return KubernetesPodSecurityAdapter()


def build_secret_rotation_audit_adapter() -> SecretRotationAuditPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
        KubernetesSecretAuditAdapter,
    )

    return KubernetesSecretAuditAdapter()


def build_security_audit_adapter() -> SecurityAuditPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_security_audit_adapter import (
        OTelSecurityAuditAdapter,
    )

    return OTelSecurityAuditAdapter()
mutants_x_build_security_posture_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_security_posture_adapter__mutmut)
def build_security_posture_adapter() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditUseCase(pod_security_port=build_pod_security_adapter())
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_orig() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditUseCase(pod_security_port=build_pod_security_adapter())
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_1() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = None
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_2() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=None
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditUseCase(pod_security_port=build_pod_security_adapter())
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_3() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceUseCase(tls_port=None)
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditUseCase(pod_security_port=build_pod_security_adapter())
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_4() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        ),
        PodSecurityProvider(
            service=None
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_5() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditUseCase(pod_security_port=None)
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def x_build_security_posture_adapter__mutmut_6() -> SecurityPosturePort:
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.infrastructure.adapters.secondary.security_posture.security_posture_adapter import (  # noqa: E501
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceUseCase(tls_port=build_tls_compliance_adapter())
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditUseCase(pod_security_port=build_pod_security_adapter())
        ),
    ]
    return SecurityPostureAdapter(providers=None)

mutants_x_build_security_posture_adapter__mutmut['_mutmut_orig'] = x_build_security_posture_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_security_posture_adapter__mutmut['x_build_security_posture_adapter__mutmut_1'] = x_build_security_posture_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_security_posture_adapter__mutmut['x_build_security_posture_adapter__mutmut_2'] = x_build_security_posture_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_security_posture_adapter__mutmut['x_build_security_posture_adapter__mutmut_3'] = x_build_security_posture_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_security_posture_adapter__mutmut['x_build_security_posture_adapter__mutmut_4'] = x_build_security_posture_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_security_posture_adapter__mutmut['x_build_security_posture_adapter__mutmut_5'] = x_build_security_posture_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_security_posture_adapter__mutmut['x_build_security_posture_adapter__mutmut_6'] = x_build_security_posture_adapter__mutmut_6 # type: ignore # mutmut generated


def build_compliance_audit_adapter() -> ComplianceAuditPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_compliance_audit_adapter import (
        OTelComplianceAuditAdapter,
    )

    return OTelComplianceAuditAdapter()


def build_external_exposure_audit_adapter() -> ExternalExposureAuditPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_external_exposure_adapter import (
        KubernetesExternalExposureAdapter,
    )

    return KubernetesExternalExposureAdapter()


def build_network_policy_audit_adapter() -> NetworkPolicyAuditPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_network_policy_adapter import (
        KubernetesNetworkPolicyAdapter,
    )

    return KubernetesNetworkPolicyAdapter()
mutants_x_build_critical_cve_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_critical_cve_adapter__mutmut)
def build_critical_cve_adapter() -> CriticalCvePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.critical_cve_adapter import (
        CriticalCveAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.critical_cve_source import (
        EmptyCriticalCveSource,
    )

    return CriticalCveAdapter(source=EmptyCriticalCveSource())


def x_build_critical_cve_adapter__mutmut_orig() -> CriticalCvePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.critical_cve_adapter import (
        CriticalCveAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.critical_cve_source import (
        EmptyCriticalCveSource,
    )

    return CriticalCveAdapter(source=EmptyCriticalCveSource())


def x_build_critical_cve_adapter__mutmut_1() -> CriticalCvePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.critical_cve_adapter import (
        CriticalCveAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.critical_cve_source import (
        EmptyCriticalCveSource,
    )

    return CriticalCveAdapter(source=None)

mutants_x_build_critical_cve_adapter__mutmut['_mutmut_orig'] = x_build_critical_cve_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_critical_cve_adapter__mutmut['x_build_critical_cve_adapter__mutmut_1'] = x_build_critical_cve_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_stale_credentials_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_stale_credentials_adapter__mutmut)
def build_stale_credentials_adapter() -> StaleCredentialsPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.stale_credentials_adapter import (
        StaleCredentialsAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.stale_credentials_source import (
        EmptyStaleCredentialsSource,
    )

    return StaleCredentialsAdapter(source=EmptyStaleCredentialsSource())


def x_build_stale_credentials_adapter__mutmut_orig() -> StaleCredentialsPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.stale_credentials_adapter import (
        StaleCredentialsAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.stale_credentials_source import (
        EmptyStaleCredentialsSource,
    )

    return StaleCredentialsAdapter(source=EmptyStaleCredentialsSource())


def x_build_stale_credentials_adapter__mutmut_1() -> StaleCredentialsPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.stale_credentials_adapter import (
        StaleCredentialsAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.stale_credentials_source import (
        EmptyStaleCredentialsSource,
    )

    return StaleCredentialsAdapter(source=None)

mutants_x_build_stale_credentials_adapter__mutmut['_mutmut_orig'] = x_build_stale_credentials_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_stale_credentials_adapter__mutmut['x_build_stale_credentials_adapter__mutmut_1'] = x_build_stale_credentials_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_unauthorized_access_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_unauthorized_access_adapter__mutmut)
def build_unauthorized_access_adapter() -> UnauthorizedAccessPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.unauthorized_access_adapter import (
        UnauthorizedAccessAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.unauthorized_access_source import (
        EmptyUnauthorizedAccessSource,
    )

    return UnauthorizedAccessAdapter(source=EmptyUnauthorizedAccessSource())


def x_build_unauthorized_access_adapter__mutmut_orig() -> UnauthorizedAccessPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.unauthorized_access_adapter import (
        UnauthorizedAccessAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.unauthorized_access_source import (
        EmptyUnauthorizedAccessSource,
    )

    return UnauthorizedAccessAdapter(source=EmptyUnauthorizedAccessSource())


def x_build_unauthorized_access_adapter__mutmut_1() -> UnauthorizedAccessPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.unauthorized_access_adapter import (
        UnauthorizedAccessAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.unauthorized_access_source import (
        EmptyUnauthorizedAccessSource,
    )

    return UnauthorizedAccessAdapter(source=None)

mutants_x_build_unauthorized_access_adapter__mutmut['_mutmut_orig'] = x_build_unauthorized_access_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_unauthorized_access_adapter__mutmut['x_build_unauthorized_access_adapter__mutmut_1'] = x_build_unauthorized_access_adapter__mutmut_1 # type: ignore # mutmut generated


def build_image_vulnerability_scan_adapter() -> ImageVulnerabilityScanPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.trivy_cve_scan_adapter import (
        TrivyCVEScanAdapter,
    )

    return TrivyCVEScanAdapter()


def build_tls_compliance_adapter() -> TLSCompliancePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.tls_compliance_adapter import (
        TLSComplianceAdapter,
    )

    return TLSComplianceAdapter()
mutants_x_build_probe_audit_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_probe_audit_adapter__mutmut)
def build_probe_audit_adapter() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_probe_audit_adapter__mutmut_orig() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_probe_audit_adapter__mutmut_1() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_probe_audit_adapter__mutmut_2() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_probe_audit_adapter__mutmut_3() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_probe_audit_adapter__mutmut_4() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_probe_audit_adapter__mutmut_5() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_probe_audit_adapter__mutmut_6() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_probe_audit_adapter__mutmut_7() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_probe_audit_adapter__mutmut_8() -> ProbeAuditPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_probe_audit_adapter__mutmut['_mutmut_orig'] = x_build_probe_audit_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_1'] = x_build_probe_audit_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_2'] = x_build_probe_audit_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_3'] = x_build_probe_audit_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_4'] = x_build_probe_audit_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_5'] = x_build_probe_audit_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_6'] = x_build_probe_audit_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_7'] = x_build_probe_audit_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_probe_audit_adapter__mutmut['x_build_probe_audit_adapter__mutmut_8'] = x_build_probe_audit_adapter__mutmut_8 # type: ignore # mutmut generated


def build_version_regression_adapter() -> VersionRegressionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_version_regression_adapter import (
        OTelVersionRegressionAdapter,
    )

    return OTelVersionRegressionAdapter()


def build_audit_log_adapter() -> GitOpsDriftAuditPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
        KubernetesAuditLogAdapter,
    )

    return KubernetesAuditLogAdapter()


def build_image_drift_adapter() -> ImageDriftPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
        KubernetesImageDriftAdapter,
    )

    return KubernetesImageDriftAdapter()


def build_image_inventory_adapter() -> ImageInventoryPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (  # noqa: E501
        KubernetesImageInventoryAdapter,
    )

    return KubernetesImageInventoryAdapter()


def build_live_resource_adapter() -> LiveResourcePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
        KubernetesLiveResourceAdapter,
    )

    return KubernetesLiveResourceAdapter()
