from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_challenges_list.command import (
    CertsChallengesListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_challenges_list.response import (
    CertsChallengesListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsChallengesListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsChallengesListUseCase:
    @_mutmut_mutated(mutants_xǁCertsChallengesListUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsChallengesListUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsChallengesListUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut)
    def execute(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=command.namespace)
        return CertsChallengesListResponse(challenges=[asdict(ch) for ch in challenges])

    def xǁCertsChallengesListUseCaseǁexecute__mutmut_orig(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=command.namespace)
        return CertsChallengesListResponse(challenges=[asdict(ch) for ch in challenges])

    def xǁCertsChallengesListUseCaseǁexecute__mutmut_1(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = None
        return CertsChallengesListResponse(challenges=[asdict(ch) for ch in challenges])

    def xǁCertsChallengesListUseCaseǁexecute__mutmut_2(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=None)
        return CertsChallengesListResponse(challenges=[asdict(ch) for ch in challenges])

    def xǁCertsChallengesListUseCaseǁexecute__mutmut_3(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=command.namespace)
        return CertsChallengesListResponse(challenges=None)

    def xǁCertsChallengesListUseCaseǁexecute__mutmut_4(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=command.namespace)
        return CertsChallengesListResponse(challenges=[asdict(None) for ch in challenges])

mutants_xǁCertsChallengesListUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsChallengesListUseCaseǁ__init____mutmut['xǁCertsChallengesListUseCaseǁ__init____mutmut_1'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut['xǁCertsChallengesListUseCaseǁexecute__mutmut_1'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut['xǁCertsChallengesListUseCaseǁexecute__mutmut_2'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut['xǁCertsChallengesListUseCaseǁexecute__mutmut_3'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsChallengesListUseCaseǁexecute__mutmut['xǁCertsChallengesListUseCaseǁexecute__mutmut_4'] = CertsChallengesListUseCase.xǁCertsChallengesListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
