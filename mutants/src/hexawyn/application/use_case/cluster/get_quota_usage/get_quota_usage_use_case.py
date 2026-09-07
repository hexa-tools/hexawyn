from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
from hexawyn.application.use_case.cluster.get_quota_usage.command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.use_case.cluster.get_quota_usage.response import (
    GetQuotaUsageResponse,
)
from hexawyn.domain.models.quota import QuotaUsage

_RESOURCES = [
    "investigations",
    "slack_alerts",
]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetQuotaUsageUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GetQuotaUsageUseCase:
    @_mutmut_mutated(mutants_xǁGetQuotaUsageUseCaseǁ__init____mutmut)
    def __init__(self, plan_port: PlanPort, usage_meter: UsageMeterPort) -> None:
        self._plan = plan_port
        self._meter = usage_meter
    def xǁGetQuotaUsageUseCaseǁ__init____mutmut_orig(self, plan_port: PlanPort, usage_meter: UsageMeterPort) -> None:
        self._plan = plan_port
        self._meter = usage_meter
    def xǁGetQuotaUsageUseCaseǁ__init____mutmut_1(self, plan_port: PlanPort, usage_meter: UsageMeterPort) -> None:
        self._plan = None
        self._meter = usage_meter
    def xǁGetQuotaUsageUseCaseǁ__init____mutmut_2(self, plan_port: PlanPort, usage_meter: UsageMeterPort) -> None:
        self._plan = plan_port
        self._meter = None

    @_mutmut_mutated(mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut)
    def execute(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_orig(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_1(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = None
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_2(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = None
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_3(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(None)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_4(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = None
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_5(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(None)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_6(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = None

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_7(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(None, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_8(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, None)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_9(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_10(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, )

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_11(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = ""
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_12(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state != QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_13(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(None, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_14(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, None):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_15(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_16(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, ):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_17(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(1, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_18(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 1):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_19(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = None

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_20(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(None)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_21(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                None
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_22(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=None,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_23(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=None,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_24(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_25(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=None,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_26(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=None,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_27(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_28(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_29(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_30(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_31(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_32(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None or limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_33(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_34(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit != -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_35(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == +1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_36(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -2 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=quotas)

    def xǁGetQuotaUsageUseCaseǁexecute__mutmut_37(self, command: GetQuotaUsageCommand) -> GetQuotaUsageResponse:
        quotas: list[QuotaUsage] = []
        for resource in _RESOURCES:
            limit = self._plan.get_limit(resource)
            used = self._meter.get_usage(resource)
            state = QuotaUsage.compute_state(used, limit)

            available_from_tier: str | None = None
            if state == QuotaUsage.compute_state(0, 0):
                available_from_tier = self._plan.tier_required_for(resource)

            quotas.append(
                QuotaUsage(
                    resource=resource,
                    used=used,
                    limit=None if limit is not None and limit == -1 else limit,
                    state=state,
                    available_from_tier=available_from_tier,
                )
            )
        return GetQuotaUsageResponse(quotas=None)

mutants_xǁGetQuotaUsageUseCaseǁ__init____mutmut['_mutmut_orig'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁ__init____mutmut['xǁGetQuotaUsageUseCaseǁ__init____mutmut_1'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁ__init____mutmut['xǁGetQuotaUsageUseCaseǁ__init____mutmut_2'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['_mutmut_orig'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_1'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_2'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_3'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_4'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_5'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_6'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_7'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_8'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_9'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_10'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_11'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_12'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_13'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_14'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_15'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_16'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_17'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_18'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_19'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_20'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_21'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_22'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_23'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_24'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_25'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_26'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_27'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_28'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_29'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_30'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_31'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_32'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_33'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_34'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_35'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_36'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetQuotaUsageUseCaseǁexecute__mutmut['xǁGetQuotaUsageUseCaseǁexecute__mutmut_37'] = GetQuotaUsageUseCase.xǁGetQuotaUsageUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
