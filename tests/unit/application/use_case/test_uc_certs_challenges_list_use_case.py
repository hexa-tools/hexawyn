"""Unit tests for CertsChallengesListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_challenges_list.certs_challenges_list_service_port import (
    CertsChallengesListServicePort,
)
from hexawyn.application.use_case.certs_challenges_list.certs_challenges_list_use_case import (
    CertsChallengesListUseCase,
)


class TestCertsChallengesListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsChallengesListServicePort)
        use_case = CertsChallengesListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_challenges.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsChallengesListServicePort)
        mock_service.list_challenges.side_effect = RuntimeError("test error")
        use_case = CertsChallengesListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
