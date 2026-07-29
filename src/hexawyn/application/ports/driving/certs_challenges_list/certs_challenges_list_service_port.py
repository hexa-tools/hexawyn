from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_challenges_list.command import (
    CertsChallengesListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_challenges_list.response import (
    CertsChallengesListResponse,
)


class CertsChallengesListServicePort(ABC):
    @abstractmethod
    def list_challenges(
        self, command: CertsChallengesListCommand
    ) -> CertsChallengesListResponse: ...
