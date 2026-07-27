from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_challenges_list.command import (
    CertsChallengesListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_challenges_list.response import (
    CertsChallengesListResponse,
)


class CertsChallengesListUseCase:
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def execute(self, command: CertsChallengesListCommand) -> CertsChallengesListResponse:
        challenges = self._port.list_challenges(namespace=command.namespace)
        return CertsChallengesListResponse(challenges=[asdict(ch) for ch in challenges])
