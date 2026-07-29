from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.openshift.list_openshift_imagestreams.command import (
    ListOpenshiftImagestreamsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_imagestreams.list_openshift_imagestreams_use_case import (  # noqa: E501
    ListOpenshiftImagestreamsUseCase,
)
from hexawyn.application.use_case.openshift.list_openshift_imagestreams.response import (
    ListOpenshiftImagestreamsResponse,
)


class TestListOpenshiftImagestreamsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_image_streams.return_value = []
        use_case = ListOpenshiftImagestreamsUseCase(port=port)
        result = use_case.execute(ListOpenshiftImagestreamsCommand())
        assert isinstance(result, ListOpenshiftImagestreamsResponse)

    def test_execute_empty_list(self) -> None:
        port = MagicMock()
        port.list_image_streams.return_value = []
        use_case = ListOpenshiftImagestreamsUseCase(port=port)
        result = use_case.execute(ListOpenshiftImagestreamsCommand())
        assert result.count == 0

    def test_execute_handles_exception(self) -> None:
        port = MagicMock()
        port.list_image_streams.side_effect = Exception("boom")

        use_case = ListOpenshiftImagestreamsUseCase(port=port)
        result = use_case.execute(ListOpenshiftImagestreamsCommand())

        assert result.error == "boom"
