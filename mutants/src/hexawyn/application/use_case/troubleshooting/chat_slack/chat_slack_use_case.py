from hexawyn.application.ports.driven.runtime_port import InvestigationOutput, RuntimePort
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_command import (
    ChatSlackCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_response import (
    ChatSlackResponse,
)
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.cluster import ClusterContext


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁChatSlackUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁChatSlackUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut: MutantDict = {}  # type: ignore


class ChatSlackUseCase:
    """
    Orchestrates Slack chat investigations via RuntimePort.
    Never catches exceptions — lets QuotaExceededError and domain errors propagate.
    Primary adapter (SlackChatAdapter) handles the final catch for user display.
    No set_adapter() call — VPS has no kubeconfig, pods=[] sent to control-plane.
    """

    @_mutmut_mutated(mutants_xǁChatSlackUseCaseǁ__init____mutmut)
    def __init__(self, runtime: RuntimePort | None = None) -> None:
        if runtime is None:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
        self._runtime = runtime

    def xǁChatSlackUseCaseǁ__init____mutmut_orig(self, runtime: RuntimePort | None = None) -> None:
        if runtime is None:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
        self._runtime = runtime

    def xǁChatSlackUseCaseǁ__init____mutmut_1(self, runtime: RuntimePort | None = None) -> None:
        if runtime is not None:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
        self._runtime = runtime

    def xǁChatSlackUseCaseǁ__init____mutmut_2(self, runtime: RuntimePort | None = None) -> None:
        if runtime is None:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = None
        self._runtime = runtime

    def xǁChatSlackUseCaseǁ__init____mutmut_3(self, runtime: RuntimePort | None = None) -> None:
        if runtime is None:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
        self._runtime = None

    @_mutmut_mutated(mutants_xǁChatSlackUseCaseǁexecute__mutmut)
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

    def xǁChatSlackUseCaseǁexecute__mutmut_orig(self, command: ChatSlackCommand) -> ChatSlackResponse:
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

    def xǁChatSlackUseCaseǁexecute__mutmut_1(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = None
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

    def xǁChatSlackUseCaseǁexecute__mutmut_2(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if quota_result["allowed"]:
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

    def xǁChatSlackUseCaseǁexecute__mutmut_3(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["XXallowedXX"]:
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

    def xǁChatSlackUseCaseǁexecute__mutmut_4(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["ALLOWED"]:
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

    def xǁChatSlackUseCaseǁexecute__mutmut_5(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=None,
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_6(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=None,
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_7(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_8(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_9(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["XXusedXX"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_10(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["USED"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_11(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["XXlimitXX"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_12(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["LIMIT"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_13(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = None
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_14(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(None, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_15(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, None)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_16(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_17(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, )
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_18(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=None,
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_19(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=None,
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_20(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            suggestions=None,
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_21(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            is_pro=None,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_22(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_23(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_24(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_25(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            )

    def xǁChatSlackUseCaseǁexecute__mutmut_26(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["XXanswerXX"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_27(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["ANSWER"],
            quota_display=f"{quota_result['used']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_28(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['XXusedXX']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_29(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['USED']} / {quota_result['limit']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_30(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['XXlimitXX']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_31(self, command: ChatSlackCommand) -> ChatSlackResponse:
        quota_result = self._runtime.check_quota()
        if not quota_result["allowed"]:
            raise QuotaExceededError(
                used=quota_result["used"],
                limit=quota_result["limit"],
            )
        output = self._run_investigation(command.query, command.cluster_name)
        return ChatSlackResponse(
            message=output["answer"],
            quota_display=f"{quota_result['used']} / {quota_result['LIMIT']}",
            suggestions=list(output["suggestions"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_32(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            suggestions=list(None)[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_33(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            suggestions=list(output["XXsuggestionsXX"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_34(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            suggestions=list(output["SUGGESTIONS"])[:4],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_35(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            suggestions=list(output["suggestions"])[:5],
            is_pro=quota_result["limit"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_36(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            is_pro=quota_result["XXlimitXX"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_37(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            is_pro=quota_result["LIMIT"] > 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_38(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            is_pro=quota_result["limit"] >= 50,  # noqa: PLR2004
        )

    def xǁChatSlackUseCaseǁexecute__mutmut_39(self, command: ChatSlackCommand) -> ChatSlackResponse:
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
            is_pro=quota_result["limit"] > 51,  # noqa: PLR2004
        )

    @_mutmut_mutated(mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut)
    def _run_investigation(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(query, ctx)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_orig(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(query, ctx)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_1(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = None
        return self._runtime.run_investigation(query, ctx)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_2(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=None)
        return self._runtime.run_investigation(query, ctx)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_3(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(None, ctx)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_4(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(query, None)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_5(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(ctx)

    def xǁChatSlackUseCaseǁ_run_investigation__mutmut_6(self, query: str, cluster_name: str) -> InvestigationOutput:
        ctx = ClusterContext(name=cluster_name)
        return self._runtime.run_investigation(query, )

mutants_xǁChatSlackUseCaseǁ__init____mutmut['_mutmut_orig'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ__init____mutmut['xǁChatSlackUseCaseǁ__init____mutmut_1'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ__init____mutmut['xǁChatSlackUseCaseǁ__init____mutmut_2'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ__init____mutmut['xǁChatSlackUseCaseǁ__init____mutmut_3'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁChatSlackUseCaseǁexecute__mutmut['_mutmut_orig'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_1'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_2'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_3'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_4'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_5'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_6'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_7'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_8'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_9'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_10'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_11'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_12'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_13'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_14'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_15'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_16'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_17'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_18'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_19'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_20'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_21'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_22'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_23'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_24'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_25'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_26'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_27'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_28'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_29'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_30'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_31'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_32'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_33'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_34'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_35'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_36'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_37'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_38'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁexecute__mutmut['xǁChatSlackUseCaseǁexecute__mutmut_39'] = ChatSlackUseCase.xǁChatSlackUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated

mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['_mutmut_orig'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['xǁChatSlackUseCaseǁ_run_investigation__mutmut_1'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['xǁChatSlackUseCaseǁ_run_investigation__mutmut_2'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['xǁChatSlackUseCaseǁ_run_investigation__mutmut_3'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['xǁChatSlackUseCaseǁ_run_investigation__mutmut_4'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['xǁChatSlackUseCaseǁ_run_investigation__mutmut_5'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChatSlackUseCaseǁ_run_investigation__mutmut['xǁChatSlackUseCaseǁ_run_investigation__mutmut_6'] = ChatSlackUseCase.xǁChatSlackUseCaseǁ_run_investigation__mutmut_6 # type: ignore # mutmut generated
