from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_challenges_list.command import (
    CertsChallengesListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_challenges_list.response import (
    CertsChallengesListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CertsChallengesListServicePort(ABC):
    @abstractmethod
    def list_challenges(
        self, command: CertsChallengesListCommand
    ) -> CertsChallengesListResponse: ...
