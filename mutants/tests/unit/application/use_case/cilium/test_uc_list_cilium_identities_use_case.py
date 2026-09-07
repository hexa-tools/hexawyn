from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.list_cilium_identities.command import (
    ListCiliumIdentitiesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_identities.list_cilium_identities_use_case import (  # noqa: E501
    ListCiliumIdentitiesUseCase,
)
from hexawyn.application.use_case.cilium.list_cilium_identities.response import (
    ListCiliumIdentitiesResponse,
)
from hexawyn.domain.models.cilium import CiliumIdentitiesResult, CiliumIdentityInfo


class TestListCiliumIdentitiesUseCase:
    def test_execute_returns_identities(self) -> None:
        result = CiliumIdentitiesResult(
            installed=True,
            status="present",
            total_identities=1,
            identities=[CiliumIdentityInfo(id="100", labels=("a", "b"), endpoint_count=3)],
            note=None,
        )
        port = MagicMock()
        port.list_identities.return_value = result

        response = ListCiliumIdentitiesUseCase(port=port).execute(ListCiliumIdentitiesCommand())

        assert isinstance(response, ListCiliumIdentitiesResponse)
        assert response.status == "present"
        assert response.total_identities == 1  # noqa: PLR2004
        assert response.identities == [
            {"id": "100", "labels": ["a", "b"], "endpoint_count": 3}  # noqa: PLR2004
        ]

    def test_execute_not_installed(self) -> None:
        result = CiliumIdentitiesResult(
            installed=False,
            status="not_installed",
            total_identities=0,
            identities=[],
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.list_identities.return_value = result

        response = ListCiliumIdentitiesUseCase(port=port).execute(ListCiliumIdentitiesCommand())

        assert response.installed is False
        assert response.status == "not_installed"
        assert response.identities == []
