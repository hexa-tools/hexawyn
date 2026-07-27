from __future__ import annotations

from unittest.mock import MagicMock


class TestTLSComplianceProvider:
    def test_category_is_tls(self) -> None:
        from hexawyn.adapters.secondary.security_posture.category_providers import (
            TLSComplianceProvider,
        )

        provider = TLSComplianceProvider(service=MagicMock())

        assert provider.category() == "tls"

    def test_fetch_normalizes_services(self) -> None:
        from hexawyn.adapters.secondary.security_posture.category_providers import (
            TLSComplianceProvider,
        )

        service = MagicMock()
        report = MagicMock()
        report.services = [
            _tls_service("web", "production", severity="compliant"),
            _tls_service("api", "production", severity="high_risk"),
        ]
        service.audit.return_value = MagicMock(result=report)
        provider = TLSComplianceProvider(service=service)

        records = provider.fetch()

        assert len(records) == 2  # noqa: PLR2004
        web = next(r for r in records if r["workload"] == "web")
        api = next(r for r in records if r["workload"] == "api")
        assert web["compliant"] is True
        assert api["compliant"] is False
        assert api["category"] == "tls"


class TestPodSecurityProvider:
    def test_category_is_pod_security(self) -> None:
        from hexawyn.adapters.secondary.security_posture.category_providers import (
            PodSecurityProvider,
        )

        provider = PodSecurityProvider(service=MagicMock())

        assert provider.category() == "pod_security"

    def test_fetch_marks_findings_non_compliant(self) -> None:
        from hexawyn.adapters.secondary.security_posture.category_providers import (
            PodSecurityProvider,
        )

        service = MagicMock()
        response = MagicMock()
        response.findings = [
            {"pod_name": "root-pod", "namespace": "production"},
        ]
        service.audit_pod_security.return_value = response
        provider = PodSecurityProvider(service=service)

        records = provider.fetch()

        assert records[0]["workload"] == "root-pod"
        assert records[0]["category"] == "pod_security"
        assert records[0]["compliant"] is False


def _tls_service(name: str, namespace: str, severity: str) -> MagicMock:
    svc = MagicMock()
    svc.service_name = name
    svc.namespace = namespace
    svc.severity = severity
    return svc
