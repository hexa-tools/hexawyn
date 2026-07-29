"""Unit tests for mcp/adapters/security_adapters.py — every build_*_adapter() function."""

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


class TestSecurityAdapters:
    """Verify each builder returns the correct port type."""

    def test_build_rbac_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_rbac_audit_adapter

        result = build_rbac_audit_adapter()
        assert isinstance(result, RBACSecurityAuditPort)

    def test_build_pod_security_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_pod_security_adapter

        result = build_pod_security_adapter()
        assert isinstance(result, PodSecurityContextAuditPort)

    def test_build_secret_rotation_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_secret_rotation_audit_adapter,
        )

        result = build_secret_rotation_audit_adapter()
        assert isinstance(result, SecretRotationAuditPort)

    def test_build_security_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_security_audit_adapter

        result = build_security_audit_adapter()
        assert isinstance(result, SecurityAuditPort)

    def test_build_security_posture_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_security_posture_adapter,
        )

        result = build_security_posture_adapter()
        assert isinstance(result, SecurityPosturePort)

    def test_build_compliance_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_compliance_audit_adapter,
        )

        result = build_compliance_audit_adapter()
        assert isinstance(result, ComplianceAuditPort)

    def test_build_external_exposure_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_external_exposure_audit_adapter,
        )

        result = build_external_exposure_audit_adapter()
        assert isinstance(result, ExternalExposureAuditPort)

    def test_build_network_policy_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_network_policy_audit_adapter,
        )

        result = build_network_policy_audit_adapter()
        assert isinstance(result, NetworkPolicyAuditPort)

    def test_build_critical_cve_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_critical_cve_adapter

        result = build_critical_cve_adapter()
        assert isinstance(result, CriticalCvePort)

    def test_build_stale_credentials_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_stale_credentials_adapter,
        )

        result = build_stale_credentials_adapter()
        assert isinstance(result, StaleCredentialsPort)

    def test_build_unauthorized_access_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_unauthorized_access_adapter,
        )

        result = build_unauthorized_access_adapter()
        assert isinstance(result, UnauthorizedAccessPort)

    def test_build_image_vulnerability_scan_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_image_vulnerability_scan_adapter,
        )

        result = build_image_vulnerability_scan_adapter()
        assert isinstance(result, ImageVulnerabilityScanPort)

    def test_build_tls_compliance_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_tls_compliance_adapter

        result = build_tls_compliance_adapter()
        assert isinstance(result, TLSCompliancePort)

    def test_build_probe_audit_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_probe_audit_adapter

        result = build_probe_audit_adapter()
        assert isinstance(result, ProbeAuditPort)

    def test_build_version_regression_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_version_regression_adapter,
        )

        result = build_version_regression_adapter()
        assert isinstance(result, VersionRegressionPort)

    def test_build_audit_log_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_audit_log_adapter

        result = build_audit_log_adapter()
        assert isinstance(result, GitOpsDriftAuditPort)

    def test_build_image_drift_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import build_image_drift_adapter

        result = build_image_drift_adapter()
        assert isinstance(result, ImageDriftPort)

    def test_build_image_inventory_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_image_inventory_adapter,
        )

        result = build_image_inventory_adapter()
        assert isinstance(result, ImageInventoryPort)

    def test_build_live_resource_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.security_adapters import (
            build_live_resource_adapter,
        )

        result = build_live_resource_adapter()
        assert isinstance(result, LiveResourcePort)
