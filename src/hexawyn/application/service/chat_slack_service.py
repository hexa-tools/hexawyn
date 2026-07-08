from hexawyn.application.ports.driven.runtime_port import InvestigationOutput, RuntimePort
from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.application.use_case.chat_slack.chat_slack_command import ChatSlackCommand
from hexawyn.application.use_case.chat_slack.chat_slack_response import ChatSlackResponse
from hexawyn.application.use_case.chat_slack.chat_slack_use_case import ChatSlackUseCase
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.infrastructure.config.license_manager import is_pro
from hexawyn.infrastructure.config.quota_manager import get_quota_display


class ChatSlackService(ChatSlackUseCase):
    """
    Orchestrates Slack chat investigations via RuntimePort.
    Never catches exceptions — lets QuotaExceededError and domain errors propagate.
    Primary adapter (SlackChatAdapter) handles the final catch for user display.
    No set_adapter() call — VPS has no kubeconfig, pods=[] sent to control-plane.
    """

    def __init__(self, runtime: RuntimePort | None = None) -> None:
        self._runtime = runtime or get_runtime()

    def execute(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=get_quota_display(),
            suggestions=list(output["suggestions"])[:4],
            is_pro=is_pro(),
        )

    def _run_investigation(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(query, ctx)
