from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.domain.errors import ComponentNotInstalledError
from hexawyn.domain.models.certificates import (
    AcmeChallenge,
    Certificate,
    CertificateIssuer,
    CertManagerDetectionResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertManagerDetectorǁdetect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertManagerDetectorǁget_certificate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertManagerDetectorǁget_issuer__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertManagerDetectorǁlist_requests__mutmut: MutantDict = {}  # type: ignore


class CertManagerDetector(CertManagerPort):
    """Auto-detects Cert-Manager via CRDs. All read-only — never triggers renewal."""

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁdetect__mutmut)
    def detect(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_orig(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_1(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=None,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_2(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=None,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_3(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=None,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_4(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=None,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_5(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=None,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_6(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=None,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_7(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_8(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_9(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_10(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_11(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_12(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_13(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_14(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            )

    def xǁCertManagerDetectorǁdetect__mutmut_15(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=True,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_16(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=1,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_17(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=1,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_18(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=1,
            failed_certs=0,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_19(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=1,
            active_challenges=0,
        )

    def xǁCertManagerDetectorǁdetect__mutmut_20(self) -> CertManagerDetectionResult:
        return CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=1,
        )

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁlist_certificates__mutmut)
    def list_certificates(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_orig(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_1(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            None, "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_2(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", None
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_3(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_4(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_5(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "XXCert-ManagerXX", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_6(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "cert-manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_7(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "CERT-MANAGER", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_8(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "XXhttps://cert-manager.io/docs/installation/XX"
        )

    def xǁCertManagerDetectorǁlist_certificates__mutmut_9(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "HTTPS://CERT-MANAGER.IO/DOCS/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁget_certificate__mutmut)
    def get_certificate(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_orig(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_1(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            None, "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_2(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "Cert-Manager", None
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_3(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_4(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "Cert-Manager", )

    def xǁCertManagerDetectorǁget_certificate__mutmut_5(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "XXCert-ManagerXX", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_6(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "cert-manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_7(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "CERT-MANAGER", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_8(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "Cert-Manager", "XXhttps://cert-manager.io/docs/installation/XX"
        )

    def xǁCertManagerDetectorǁget_certificate__mutmut_9(self, name: str, namespace: str) -> Certificate:
        raise ComponentNotInstalledError(
            "Cert-Manager", "HTTPS://CERT-MANAGER.IO/DOCS/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁlist_issuers__mutmut)
    def list_issuers(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_orig(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_1(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            None, "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_2(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "Cert-Manager", None
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_3(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_4(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "Cert-Manager", )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_5(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "XXCert-ManagerXX", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_6(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "cert-manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_7(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "CERT-MANAGER", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_8(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "XXhttps://cert-manager.io/docs/installation/XX"
        )

    def xǁCertManagerDetectorǁlist_issuers__mutmut_9(self, namespace: str | None = None) -> list[CertificateIssuer]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "HTTPS://CERT-MANAGER.IO/DOCS/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁget_issuer__mutmut)
    def get_issuer(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_orig(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_1(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            None, "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_2(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "Cert-Manager", None
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_3(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_4(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "Cert-Manager", )

    def xǁCertManagerDetectorǁget_issuer__mutmut_5(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "XXCert-ManagerXX", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_6(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "cert-manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_7(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "CERT-MANAGER", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_8(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "Cert-Manager", "XXhttps://cert-manager.io/docs/installation/XX"
        )

    def xǁCertManagerDetectorǁget_issuer__mutmut_9(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        raise ComponentNotInstalledError(
            "Cert-Manager", "HTTPS://CERT-MANAGER.IO/DOCS/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁlist_challenges__mutmut)
    def list_challenges(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_orig(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_1(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            None, "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_2(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "Cert-Manager", None
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_3(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_4(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "Cert-Manager", )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_5(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "XXCert-ManagerXX", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_6(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "cert-manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_7(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "CERT-MANAGER", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_8(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "XXhttps://cert-manager.io/docs/installation/XX"
        )

    def xǁCertManagerDetectorǁlist_challenges__mutmut_9(self, namespace: str | None = None) -> list[AcmeChallenge]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "HTTPS://CERT-MANAGER.IO/DOCS/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁCertManagerDetectorǁlist_requests__mutmut)
    def list_requests(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_orig(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_1(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            None, "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_2(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", None
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_3(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_4(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", )

    def xǁCertManagerDetectorǁlist_requests__mutmut_5(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "XXCert-ManagerXX", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_6(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "cert-manager", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_7(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "CERT-MANAGER", "https://cert-manager.io/docs/installation/"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_8(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "XXhttps://cert-manager.io/docs/installation/XX"
        )

    def xǁCertManagerDetectorǁlist_requests__mutmut_9(self, namespace: str | None = None) -> list[Certificate]:
        raise ComponentNotInstalledError(
            "Cert-Manager", "HTTPS://CERT-MANAGER.IO/DOCS/INSTALLATION/"
        )

mutants_xǁCertManagerDetectorǁdetect__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_10'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_11'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_12'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_13'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_14'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_15'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_16'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_17'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_18'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_19'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁdetect__mutmut['xǁCertManagerDetectorǁdetect__mutmut_20'] = CertManagerDetector.xǁCertManagerDetectorǁdetect__mutmut_20 # type: ignore # mutmut generated

mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_certificates__mutmut['xǁCertManagerDetectorǁlist_certificates__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁlist_certificates__mutmut_9 # type: ignore # mutmut generated

mutants_xǁCertManagerDetectorǁget_certificate__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_certificate__mutmut['xǁCertManagerDetectorǁget_certificate__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁget_certificate__mutmut_9 # type: ignore # mutmut generated

mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_issuers__mutmut['xǁCertManagerDetectorǁlist_issuers__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁlist_issuers__mutmut_9 # type: ignore # mutmut generated

mutants_xǁCertManagerDetectorǁget_issuer__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁget_issuer__mutmut['xǁCertManagerDetectorǁget_issuer__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁget_issuer__mutmut_9 # type: ignore # mutmut generated

mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_challenges__mutmut['xǁCertManagerDetectorǁlist_challenges__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁlist_challenges__mutmut_9 # type: ignore # mutmut generated

mutants_xǁCertManagerDetectorǁlist_requests__mutmut['_mutmut_orig'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_1'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_2'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_3'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_4'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_5'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_6'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_7'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_8'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertManagerDetectorǁlist_requests__mutmut['xǁCertManagerDetectorǁlist_requests__mutmut_9'] = CertManagerDetector.xǁCertManagerDetectorǁlist_requests__mutmut_9 # type: ignore # mutmut generated
