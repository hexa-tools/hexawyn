from __future__ import annotations

from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_command import (
    CertsChallengesListCommand,
)
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_response import (
    CertsChallengesListResponse,
)
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_service_port import (
    CertsChallengesListServicePort,
)


class CertsChallengesListUseCase:
    def __init__(self, service: CertsChallengesListServicePort) -> None:
        self._service = service

    def execute(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        return self._service.list_challenges(command)
