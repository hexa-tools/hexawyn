from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.command import (
    InvestigateTLSCertificateCommand,
)
from hexawyn.application.use_case.cert_manager.investigate_tls_certificate.response import (
    InvestigateTLSCertificateResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class InvestigateTLSCertificateUseCase:
    @_mutmut_mutated(mutants_xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port
    def xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port
    def xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort) -> None:
        self._k8s = None

    @_mutmut_mutated(mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut)
    def execute(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_orig(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_1(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=None,
            namespace=command.namespace,
            certificate_found=False,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_2(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=None,
            certificate_found=False,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_3(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=None,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_4(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status=None,
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_5(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            namespace=command.namespace,
            certificate_found=False,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_6(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            certificate_found=False,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_7(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_8(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_9(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=True,
            status="NotChecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_10(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status="XXNotCheckedXX",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_11(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status="notchecked",
        )

    def xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_12(
        self,
        command: InvestigateTLSCertificateCommand,
    ) -> InvestigateTLSCertificateResponse:
        return InvestigateTLSCertificateResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            certificate_found=False,
            status="NOTCHECKED",
        )

mutants_xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut['_mutmut_orig'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut['xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut_1'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['_mutmut_orig'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_1'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_2'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_3'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_4'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_5'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_6'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_7'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_8'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_9'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_10'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_11'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut['xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_12'] = InvestigateTLSCertificateUseCase.xǁInvestigateTLSCertificateUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
