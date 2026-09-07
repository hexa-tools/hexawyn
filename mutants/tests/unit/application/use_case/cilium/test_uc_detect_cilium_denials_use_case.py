from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.detect_cilium_denials.command import (
    DetectCiliumDenialsCommand,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.detect_cilium_denials_use_case import (  # noqa: E501
    DetectCiliumDenialsUseCase,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.response import (
    DetectCiliumDenialsResponse,
)
from hexawyn.domain.models.cilium import CiliumDenialGroup, CiliumDenialsResult


class TestDetectCiliumDenialsUseCase:
    def test_execute_returns_groups(self) -> None:
        result = CiliumDenialsResult(
            installed=True,
            status="present",
            total_denials=2,
            groups=[
                CiliumDenialGroup(
                    policy="default/deny-all",
                    source="web-0",
                    destination="db-0",
                    source_namespace="payments",
                    destination_namespace="payments",
                    reason="Policy denied",
                    count=2,
                )
            ],
            note=None,
        )
        port = MagicMock()
        port.detect_denials.return_value = result

        response = DetectCiliumDenialsUseCase(port=port).execute(
            DetectCiliumDenialsCommand(namespace="payments")
        )

        assert isinstance(response, DetectCiliumDenialsResponse)
        assert response.status == "present"
        assert response.total_denials == 2  # noqa: PLR2004
        assert response.groups == [
            {
                "policy": "default/deny-all",
                "source": "web-0",
                "destination": "db-0",
                "source_namespace": "payments",
                "destination_namespace": "payments",
                "reason": "Policy denied",
                "count": 2,  # noqa: PLR2004
            }
        ]

    def test_execute_not_installed(self) -> None:
        result = CiliumDenialsResult(
            installed=False,
            status="not_installed",
            total_denials=0,
            groups=[],
            note="Hubble relay is not available in this cluster",
        )
        port = MagicMock()
        port.detect_denials.return_value = result

        response = DetectCiliumDenialsUseCase(port=port).execute(DetectCiliumDenialsCommand())

        assert response.installed is False
        assert response.status == "not_installed"
        assert response.groups == []
