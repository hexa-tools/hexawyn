from hexawyn.application.ports.driven.runtime_port import InvestigationOutput, RuntimePort
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_command import (
    ChatSlackCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_response import (
    ChatSlackResponse,
)
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.cluster import ClusterContext


class ChatSlackUseCase:
    """
    Orchestrates Slack chat investigations via RuntimePort.
    Never catches exceptions — lets QuotaExceededError and domain errors propagate.
    Primary adapter (SlackChatAdapter) handles the final catch for user display.
    No set_adapter() call — VPS has no kubeconfig, pods=[] sent to control-plane.
    """

    def __init__(self, runtime: RuntimePort | None = None) -> None:
        if runtime is None:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
        self._runtime = runtime

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
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def _run_investigation(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(query, ctx)
