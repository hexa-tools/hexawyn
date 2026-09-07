from hexawyn.domain.models.certificate import CertificateInfo, CertificateStatus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertificateCheckerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertificateCheckerǁcheck__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertificateCheckerǁassess__mutmut: MutantDict = {}  # type: ignore


class CertificateChecker:
    """Business logic for certificate health assessment.

    Categorizes certificates based on days remaining until expiry.
    Provides a full assessment report including self-signed detection,
    key size validation, and SAN presence.
    """

    @_mutmut_mutated(mutants_xǁCertificateCheckerǁ__init____mutmut)
    def __init__(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_orig(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_1(
        self,
        warning_days: int = 31,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_2(
        self,
        warning_days: int = 30,
        critical_days: int = 8,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_3(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2049,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_4(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = None
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_5(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = None
        self.min_key_size = min_key_size

    def xǁCertificateCheckerǁ__init____mutmut_6(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = None

    @_mutmut_mutated(mutants_xǁCertificateCheckerǁcheck__mutmut)
    def check(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining < 0:
            return CertificateStatus.EXPIRED
        if cert.days_remaining <= self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining <= self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    def xǁCertificateCheckerǁcheck__mutmut_orig(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining < 0:
            return CertificateStatus.EXPIRED
        if cert.days_remaining <= self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining <= self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    def xǁCertificateCheckerǁcheck__mutmut_1(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining <= 0:
            return CertificateStatus.EXPIRED
        if cert.days_remaining <= self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining <= self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    def xǁCertificateCheckerǁcheck__mutmut_2(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining < 1:
            return CertificateStatus.EXPIRED
        if cert.days_remaining <= self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining <= self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    def xǁCertificateCheckerǁcheck__mutmut_3(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining < 0:
            return CertificateStatus.EXPIRED
        if cert.days_remaining < self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining <= self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    def xǁCertificateCheckerǁcheck__mutmut_4(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining < 0:
            return CertificateStatus.EXPIRED
        if cert.days_remaining <= self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining < self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    @_mutmut_mutated(mutants_xǁCertificateCheckerǁassess__mutmut)
    def assess(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_orig(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_1(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = None
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_2(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(None)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_3(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "XXstatusXX": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_4(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "STATUS": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_5(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "XXdays_remainingXX": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_6(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "DAYS_REMAINING": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_7(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "XXsubject_cnXX": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_8(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "SUBJECT_CN": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_9(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "XXissuer_cnXX": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_10(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "ISSUER_CN": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_11(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "XXis_self_signedXX": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_12(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "IS_SELF_SIGNED": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_13(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn != cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_14(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "XXis_caXX": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_15(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "IS_CA": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_16(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "XXkey_sizeXX": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_17(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "KEY_SIZE": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_18(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "XXkey_size_okXX": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_19(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "KEY_SIZE_OK": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_20(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size > self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_21(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "XXhas_sanXX": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_22(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "HAS_SAN": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_23(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) >= 0,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_24(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 1,
            "san_count": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_25(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "XXsan_countXX": len(cert.san_list),
        }

    def xǁCertificateCheckerǁassess__mutmut_26(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "SAN_COUNT": len(cert.san_list),
        }

mutants_xǁCertificateCheckerǁ__init____mutmut['_mutmut_orig'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁ__init____mutmut['xǁCertificateCheckerǁ__init____mutmut_1'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁ__init____mutmut['xǁCertificateCheckerǁ__init____mutmut_2'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁ__init____mutmut['xǁCertificateCheckerǁ__init____mutmut_3'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁ__init____mutmut['xǁCertificateCheckerǁ__init____mutmut_4'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁ__init____mutmut['xǁCertificateCheckerǁ__init____mutmut_5'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁ__init____mutmut['xǁCertificateCheckerǁ__init____mutmut_6'] = CertificateChecker.xǁCertificateCheckerǁ__init____mutmut_6 # type: ignore # mutmut generated

mutants_xǁCertificateCheckerǁcheck__mutmut['_mutmut_orig'] = CertificateChecker.xǁCertificateCheckerǁcheck__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁcheck__mutmut['xǁCertificateCheckerǁcheck__mutmut_1'] = CertificateChecker.xǁCertificateCheckerǁcheck__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁcheck__mutmut['xǁCertificateCheckerǁcheck__mutmut_2'] = CertificateChecker.xǁCertificateCheckerǁcheck__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁcheck__mutmut['xǁCertificateCheckerǁcheck__mutmut_3'] = CertificateChecker.xǁCertificateCheckerǁcheck__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁcheck__mutmut['xǁCertificateCheckerǁcheck__mutmut_4'] = CertificateChecker.xǁCertificateCheckerǁcheck__mutmut_4 # type: ignore # mutmut generated

mutants_xǁCertificateCheckerǁassess__mutmut['_mutmut_orig'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_1'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_2'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_3'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_4'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_5'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_6'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_7'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_8'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_9'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_10'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_11'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_12'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_13'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_14'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_15'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_16'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_17'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_18'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_19'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_20'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_21'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_22'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_23'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_24'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_25'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCertificateCheckerǁassess__mutmut['xǁCertificateCheckerǁassess__mutmut_26'] = CertificateChecker.xǁCertificateCheckerǁassess__mutmut_26 # type: ignore # mutmut generated
