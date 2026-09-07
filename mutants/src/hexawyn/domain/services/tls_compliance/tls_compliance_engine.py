from __future__ import annotations

from hexawyn.domain.models.tls_compliance import TLSComplianceReport, TLSServiceStatus

_EXPIRY_WARNING_DAYS = 30
_SEVERITY_ORDER = {"critical": 0, "high_risk": 1, "warning": 2}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTLSComplianceEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class TLSComplianceEngine:
    @_mutmut_mutated(mutants_xǁTLSComplianceEngineǁcompute__mutmut)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_orig(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_1(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_2(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = None

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
    def xǁTLSComplianceEngineǁcompute__mutmut_3(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 1

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
    def xǁTLSComplianceEngineǁcompute__mutmut_4(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_5(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(None)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_6(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get(None, ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_7(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", None))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_8(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get(""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_9(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_10(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("XXservice_nameXX", ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_11(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("SERVICE_NAME", ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_12(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", "XXXX"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_13(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_14(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(None)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_15(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get(None, ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_16(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", None))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_17(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get(""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_18(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_19(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("XXnamespaceXX", ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_20(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("NAMESPACE", ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_21(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", "XXXX"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_22(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_23(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(None)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_24(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get(None))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_25(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("XXtls_configuredXX"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_26(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("TLS_CONFIGURED"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_27(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_28(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(None)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_29(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get(None))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_30(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("XXcert_expiry_daysXX"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_31(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("CERT_EXPIRY_DAYS"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_32(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_33(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(None)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_34(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get(None, ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_35(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", None))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_36(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get(""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_37(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_38(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("XXcert_issuerXX", ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_39(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("CERT_ISSUER", ""))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_40(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", "XXXX"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_41(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_42(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(None)
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
    def xǁTLSComplianceEngineǁcompute__mutmut_43(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get(None))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_44(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("XXis_self_signedXX"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_45(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("IS_SELF_SIGNED"))
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
    def xǁTLSComplianceEngineǁcompute__mutmut_46(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("is_self_signed"))
            proxy = None

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
    def xǁTLSComplianceEngineǁcompute__mutmut_47(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("is_self_signed"))
            proxy = _as_bool(None)

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
    def xǁTLSComplianceEngineǁcompute__mutmut_48(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("is_self_signed"))
            proxy = _as_bool(svc.get(None))

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
    def xǁTLSComplianceEngineǁcompute__mutmut_49(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("is_self_signed"))
            proxy = _as_bool(svc.get("XXproxy_tls_terminationXX"))

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
    def xǁTLSComplianceEngineǁcompute__mutmut_50(self, services: list[dict[str, object]]) -> TLSComplianceReport:
        results: list[TLSServiceStatus] = []
        total_issues = 0

        for svc in services:
            name = str(svc.get("service_name", ""))
            namespace = str(svc.get("namespace", ""))
            tls_ok = _as_bool(svc.get("tls_configured"))
            expiry = _as_int(svc.get("cert_expiry_days"))
            issuer = str(svc.get("cert_issuer", ""))
            self_signed = _as_bool(svc.get("is_self_signed"))
            proxy = _as_bool(svc.get("PROXY_TLS_TERMINATION"))

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
    def xǁTLSComplianceEngineǁcompute__mutmut_51(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = None
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
    def xǁTLSComplianceEngineǁcompute__mutmut_52(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = max(None, 0) if tls_ok else 0
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
    def xǁTLSComplianceEngineǁcompute__mutmut_53(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = max(expiry, None) if tls_ok else 0
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
    def xǁTLSComplianceEngineǁcompute__mutmut_54(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = max(0) if tls_ok else 0
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
    def xǁTLSComplianceEngineǁcompute__mutmut_55(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = max(expiry, ) if tls_ok else 0
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
    def xǁTLSComplianceEngineǁcompute__mutmut_56(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = max(expiry, 1) if tls_ok else 0
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
    def xǁTLSComplianceEngineǁcompute__mutmut_57(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            days_remaining = max(expiry, 0) if tls_ok else 1
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
    def xǁTLSComplianceEngineǁcompute__mutmut_58(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            severity = None

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
    def xǁTLSComplianceEngineǁcompute__mutmut_59(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            severity = _classify_severity(None, expiry)

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
    def xǁTLSComplianceEngineǁcompute__mutmut_60(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            severity = _classify_severity(tls_ok, None)

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
    def xǁTLSComplianceEngineǁcompute__mutmut_61(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            severity = _classify_severity(expiry)

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
    def xǁTLSComplianceEngineǁcompute__mutmut_62(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            severity = _classify_severity(tls_ok, )

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
    def xǁTLSComplianceEngineǁcompute__mutmut_63(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            if severity == "compliant":
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
    def xǁTLSComplianceEngineǁcompute__mutmut_64(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            if severity != "XXcompliantXX":
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
    def xǁTLSComplianceEngineǁcompute__mutmut_65(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

            if severity != "COMPLIANT":
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
    def xǁTLSComplianceEngineǁcompute__mutmut_66(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                total_issues = 1

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
    def xǁTLSComplianceEngineǁcompute__mutmut_67(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                total_issues -= 1

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
    def xǁTLSComplianceEngineǁcompute__mutmut_68(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                total_issues += 2

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
    def xǁTLSComplianceEngineǁcompute__mutmut_69(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                None
            )

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_70(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    service_name=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_71(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    namespace=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_72(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    tls_configured=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_73(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    cert_expiry_days=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_74(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    days_remaining=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_75(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    severity=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_76(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    cert_issuer=None,
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
    def xǁTLSComplianceEngineǁcompute__mutmut_77(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    is_self_signed=None,
                    proxy_tls_termination=proxy,
                )
            )

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_78(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    proxy_tls_termination=None,
                )
            )

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_79(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_80(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_81(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_82(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_83(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_84(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_85(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
    def xǁTLSComplianceEngineǁcompute__mutmut_86(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    proxy_tls_termination=proxy,
                )
            )

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_87(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
                    )
            )

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_88(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=None)

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_89(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=lambda s: None)

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_90(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=lambda s: _SEVERITY_ORDER.get(None, 99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_91(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, None))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_92(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=lambda s: _SEVERITY_ORDER.get(99))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_93(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, ))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_94(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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

        results.sort(key=lambda s: _SEVERITY_ORDER.get(s.severity, 100))

        return TLSComplianceReport(
            services=results,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_95(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            services=None,
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_96(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            all_compliant=None,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_97(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            total_issues=None,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_98(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            all_compliant=total_issues == 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_99(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_100(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            )
    def xǁTLSComplianceEngineǁcompute__mutmut_101(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            all_compliant=total_issues != 0,
            total_issues=total_issues,
        )
    def xǁTLSComplianceEngineǁcompute__mutmut_102(self, services: list[dict[str, object]]) -> TLSComplianceReport:
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
            all_compliant=total_issues == 1,
            total_issues=total_issues,
        )

mutants_xǁTLSComplianceEngineǁcompute__mutmut['_mutmut_orig'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_1'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_2'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_3'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_4'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_5'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_6'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_7'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_8'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_9'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_10'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_11'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_12'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_13'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_14'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_15'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_16'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_17'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_18'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_19'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_20'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_21'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_22'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_23'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_24'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_25'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_26'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_27'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_28'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_29'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_30'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_31'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_32'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_33'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_34'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_35'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_36'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_37'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_38'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_39'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_40'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_41'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_42'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_43'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_44'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_45'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_46'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_47'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_48'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_49'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_50'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_51'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_52'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_53'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_54'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_55'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_56'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_57'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_58'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_59'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_60'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_61'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_62'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_63'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_64'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_65'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_66'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_67'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_68'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_69'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_70'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_71'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_72'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_73'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_74'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_75'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_76'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_77'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_78'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_79'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_80'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_81'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_82'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_83'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_84'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_85'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_86'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_87'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_88'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_89'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_90'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_91'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_92'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_93'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_94'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_95'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_96'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_97'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_98'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_99'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_99 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_100'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_100 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_101'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_101 # type: ignore # mutmut generated
mutants_xǁTLSComplianceEngineǁcompute__mutmut['xǁTLSComplianceEngineǁcompute__mutmut_102'] = TLSComplianceEngine.xǁTLSComplianceEngineǁcompute__mutmut_102 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_severity__mutmut)
def _classify_severity(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_orig(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_1(tls_configured: bool, expiry_days: int) -> str:
    if tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_2(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "XXhigh_riskXX"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_3(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "HIGH_RISK"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_4(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days < 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_5(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 1:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_6(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "XXcriticalXX"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_7(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "CRITICAL"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_8(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days < _EXPIRY_WARNING_DAYS:
        return "warning"
    return "compliant"


def x__classify_severity__mutmut_9(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "XXwarningXX"
    return "compliant"


def x__classify_severity__mutmut_10(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "WARNING"
    return "compliant"


def x__classify_severity__mutmut_11(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "XXcompliantXX"


def x__classify_severity__mutmut_12(tls_configured: bool, expiry_days: int) -> str:
    if not tls_configured:
        return "high_risk"
    if expiry_days <= 0:
        return "critical"
    if expiry_days <= _EXPIRY_WARNING_DAYS:
        return "warning"
    return "COMPLIANT"

mutants_x__classify_severity__mutmut['_mutmut_orig'] = x__classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_1'] = x__classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_2'] = x__classify_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_3'] = x__classify_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_4'] = x__classify_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_5'] = x__classify_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_6'] = x__classify_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_7'] = x__classify_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_8'] = x__classify_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_9'] = x__classify_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_10'] = x__classify_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_11'] = x__classify_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_12'] = x__classify_severity__mutmut_12 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_orig(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_1(value: object) -> int:
    if value is not None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_2(value: object) -> int:
    if value is None:
        return 1
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_3(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_4(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_5(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_4'] = x__as_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_5'] = x__as_int__mutmut_5 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_bool__mutmut)
def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_orig(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_1(value: object) -> bool:
    if value is not None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_2(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_3(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(None)

mutants_x__as_bool__mutmut['_mutmut_orig'] = x__as_bool__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_1'] = x__as_bool__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_2'] = x__as_bool__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_3'] = x__as_bool__mutmut_3 # type: ignore # mutmut generated
