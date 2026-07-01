from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_command import (
    CertsChallengesListCommand,
)
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_response import (
    CertsChallengesListResponse,
)


class CertsChallengesListServicePort(ABC):
    @abstractmethod
    def list_challenges(
        self, command: CertsChallengesListCommand
    ) -> CertsChallengesListResponse: ...
