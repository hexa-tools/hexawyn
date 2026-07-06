from __future__ import annotations

from hexawyn.domain.models.tls_compliance import TLSComplianceReport, TLSServiceStatus

_EXPIRY_WARNING_DAYS = 30
_SEVERITY_ORDER = {"critical": 0, "high_risk": 1, "warning": 2}


class TLSComplianceEngine:
    def compute(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("is_self_signed"))
            proxy = _as_bool(svc.get("proxy_tls_termination"))

            days_remaining = max(expiry, 0) if tls_ok else 0
            severity = _classify_severity(tls_ok, expiry)

            if severity != "compliant":
                total_issues += 1

            results.append(
                TLSServiceStatus(
                    service_name=name,
                    namespace=namespace,
                    tls_configured=tls_ok,
                    cert_expiry_days=expiry,
                    days_remaining=days_remaining,
                    severity=severity,
                    cert_issuer=issuer,
                    is_self_signed=self_signed,
                    proxy_tls_termination=proxy,
                )
            )

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )


def _classify_severity(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)
