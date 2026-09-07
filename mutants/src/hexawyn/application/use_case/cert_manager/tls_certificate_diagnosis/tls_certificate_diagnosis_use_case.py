from __future__ import annotations

from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.response import (
    TLSCertificateDiagnosisResponse,
)
from hexawyn.domain.models.tls_certificate_diagnosis import (
    CertificateDiagnosis,
    TLSCertificateDiagnosticRequest,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class TLSCertificateDiagnosisUseCase:
    @_mutmut_mutated(mutants_xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut)
    def __init__(self, port: CertificateInvestigationPort) -> None:
        self._port = port
    def xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut_orig(self, port: CertificateInvestigationPort) -> None:
        self._port = port
    def xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut_1(self, port: CertificateInvestigationPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut)
    def execute(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_orig(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_1(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = None
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_2(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=None, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_3(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=None
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_4(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_5(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_6(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = None
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_7(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(None)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_8(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = None
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_9(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(None)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_10(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = None
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_11(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=None, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_12(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=None, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_13(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=None)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_14(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_15(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_16(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, )
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_17(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=None,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_18(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=None,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_19(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=None,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_20(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=None,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_21(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=None,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_22(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=None,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_23(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=None,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_24(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=None,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_25(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_26(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_27(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_28(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_29(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_30(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_31(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            san_list=r.san_list,
        )

    def xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_32(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            )

mutants_xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut['_mutmut_orig'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut['xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut_1'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['_mutmut_orig'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_1'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_2'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_3'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_4'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_5'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_6'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_7'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_8'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_9'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_10'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_11'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_12'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_13'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_14'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_15'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_16'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_17'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_18'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_19'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_20'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_21'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_22'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_23'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_24'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_25'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_26'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_27'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_28'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_29'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_30'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_31'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut['xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_32'] = TLSCertificateDiagnosisUseCase.xǁTLSCertificateDiagnosisUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
