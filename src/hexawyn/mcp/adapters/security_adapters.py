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


def build_rbac_audit_adapter() -> RBACSecurityAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
        KubernetesRBACAdapter,
    )

    return KubernetesRBACAdapter()


def build_pod_security_adapter() -> PodSecurityContextAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
        KubernetesPodSecurityAdapter,
    )

    return KubernetesPodSecurityAdapter()


def build_secret_rotation_audit_adapter() -> SecretRotationAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
        KubernetesSecretAuditAdapter,
    )

    return KubernetesSecretAuditAdapter()


def build_security_audit_adapter() -> SecurityAuditPort:
    from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
        OTelSecurityAuditAdapter,
    )

    return OTelSecurityAuditAdapter()


def build_security_posture_adapter() -> SecurityPosturePort:
    from hexawyn.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )
    from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
        PodSecurityStandardsAuditUseCase,
    )
    from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
        AuditTLSComplianceUseCase,
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


def build_compliance_audit_adapter() -> ComplianceAuditPort:
    from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
        OTelComplianceAuditAdapter,
    )

    return OTelComplianceAuditAdapter()


def build_external_exposure_audit_adapter() -> ExternalExposureAuditPort:
    from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
        KubernetesExternalExposureAdapter,
    )

    return KubernetesExternalExposureAdapter()


def build_network_policy_audit_adapter() -> NetworkPolicyAuditPort:
    from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
        KubernetesNetworkPolicyAdapter,
    )

    return KubernetesNetworkPolicyAdapter()


def build_critical_cve_adapter() -> CriticalCvePort:
    from hexawyn.adapters.secondary.gitops.critical_cve_adapter import (
        CriticalCveAdapter,
    )
    from hexawyn.adapters.secondary.gitops.critical_cve_source import (
        EmptyCriticalCveSource,
    )

    return CriticalCveAdapter(source=EmptyCriticalCveSource())


def build_stale_credentials_adapter() -> StaleCredentialsPort:
    from hexawyn.adapters.secondary.gitops.stale_credentials_adapter import (
        StaleCredentialsAdapter,
    )
    from hexawyn.adapters.secondary.gitops.stale_credentials_source import (
        EmptyStaleCredentialsSource,
    )

    return StaleCredentialsAdapter(source=EmptyStaleCredentialsSource())


def build_unauthorized_access_adapter() -> UnauthorizedAccessPort:
    from hexawyn.adapters.secondary.gitops.unauthorized_access_adapter import (
        UnauthorizedAccessAdapter,
    )
    from hexawyn.adapters.secondary.gitops.unauthorized_access_source import (
        EmptyUnauthorizedAccessSource,
    )

    return UnauthorizedAccessAdapter(source=EmptyUnauthorizedAccessSource())


def build_image_vulnerability_scan_adapter() -> ImageVulnerabilityScanPort:
    from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

    return TrivyCVEScanAdapter()


def build_tls_compliance_adapter() -> TLSCompliancePort:
    from hexawyn.adapters.secondary.gitops.tls_compliance_adapter import (
        TLSComplianceAdapter,
    )

    return TLSComplianceAdapter()


def build_probe_audit_adapter() -> ProbeAuditPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_version_regression_adapter() -> VersionRegressionPort:
    from hexawyn.adapters.secondary.gitops.otel_version_regression_adapter import (
        OTelVersionRegressionAdapter,
    )

    return OTelVersionRegressionAdapter()


def build_audit_log_adapter() -> GitOpsDriftAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
        KubernetesAuditLogAdapter,
    )

    return KubernetesAuditLogAdapter()


def build_image_drift_adapter() -> ImageDriftPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
        KubernetesImageDriftAdapter,
    )

    return KubernetesImageDriftAdapter()


def build_image_inventory_adapter() -> ImageInventoryPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
        KubernetesImageInventoryAdapter,
    )

    return KubernetesImageInventoryAdapter()


def build_live_resource_adapter() -> LiveResourcePort:
    from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
        KubernetesLiveResourceAdapter,
    )

    return KubernetesLiveResourceAdapter()
