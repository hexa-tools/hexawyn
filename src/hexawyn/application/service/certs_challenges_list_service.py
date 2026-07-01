from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_command import (
    CertsChallengesListCommand,
)
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_response import (
    CertsChallengesListResponse,
)
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_service_port import (
    CertsChallengesListServicePort,
)


class CertsChallengesListService(CertsChallengesListServicePort):
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def list_challenges(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=command.namespace)
        return CertsChallengesListResponse(challenges=[asdict(ch) for ch in challenges])
