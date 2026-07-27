from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_triggerauth_get.command import (
    KedaTriggerauthGetCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_get.keda_triggerauth_get_use_case import (  # noqa: E501
    KedaTriggerauthGetUseCase,
)
from hexawyn.application.use_case.keda.keda_triggerauth_get.response import (
    KedaTriggerauthGetResponse,
)


class TestKedaTriggerauthGetUseCase:
    def test_execute_returns_response(self) -> None:
        auth = MagicMock()
        auth.name = "ta"
        auth.namespace = "default"
        auth.kind = "TriggerAuthentication"
        auth.auth_type = MagicMock()
        auth.auth_type.value = "Secret"
        auth.secret_names = ["keda-secret"]
        auth.environment_names = []
        auth.pod_identity_provider = ""
        auth.ready = True
        auth.message = None

        port = MagicMock()
        port.get_trigger_auth.return_value = auth

        use_case = KedaTriggerauthGetUseCase(port=port)
        result = use_case.execute(KedaTriggerauthGetCommand(name="ta", namespace="default"))

        assert isinstance(result, KedaTriggerauthGetResponse)
        assert result.ready is True
