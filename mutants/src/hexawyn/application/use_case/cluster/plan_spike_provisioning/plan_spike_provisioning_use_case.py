from __future__ import annotations

from hexawyn.application.ports.driven.spike_provisioning_port import (
    ClusterCapacityRaw,
    SpikeProvisioningPort,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.response import (  # noqa: E501
    PlanSpikeProvisioningResponse,
)
from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot
from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
    SpikeProvisioningService,
)

_GENERIC_MULTIPLIER = 3.0
_PESSIMISTIC_MULTIPLIER = 4.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut: MutantDict = {}  # type: ignore


class PlanSpikeProvisioningUseCase:
    @_mutmut_mutated(mutants_xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut)
    def __init__(self, spike_port: SpikeProvisioningPort) -> None:
        self._port = spike_port
        self._engine = SpikeProvisioningService()
    def xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_orig(self, spike_port: SpikeProvisioningPort) -> None:
        self._port = spike_port
        self._engine = SpikeProvisioningService()
    def xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_1(self, spike_port: SpikeProvisioningPort) -> None:
        self._port = None
        self._engine = SpikeProvisioningService()
    def xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_2(self, spike_port: SpikeProvisioningPort) -> None:
        self._port = spike_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut)
    def execute(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_orig(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_1(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = None
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_2(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = None
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_3(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(None)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_4(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = None
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_5(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=None,
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_6(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=None,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_7(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=None,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_8(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=None,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_9(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=None,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_10(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=None,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_11(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=None,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_12(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_13(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_14(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_15(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_16(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_17(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_18(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_19(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(None),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_20(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=None)  # type: ignore

    @_mutmut_mutated(mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut)
    def _resolve_multiplier(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_orig(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_1(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "XXpessimisticXX"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_2(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "PESSIMISTIC"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_3(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_4(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "XXprovidedXX"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_5(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "PROVIDED"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_6(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = None
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_7(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_8(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "XXhistoricalXX"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_9(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "HISTORICAL"
        return _GENERIC_MULTIPLIER, "generic_fallback"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_10(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "XXgeneric_fallbackXX"

    def xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_11(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "GENERIC_FALLBACK"

mutants_xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut['_mutmut_orig'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut['xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_1'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut['xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_2'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['_mutmut_orig'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_1'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_2'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_3'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_4'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_5'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_6'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_7'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_8'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_9'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_10'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_11'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_12'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_13'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_14'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_15'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_16'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_17'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_18'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_19'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut['xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_20'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated

mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['_mutmut_orig'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_1'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_2'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_3'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_4'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_5'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_6'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_7'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_8'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_9'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_10'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut['xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_11'] = PlanSpikeProvisioningUseCase.xǁPlanSpikeProvisioningUseCaseǁ_resolve_multiplier__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_snapshot__mutmut)
def _to_snapshot(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_orig(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_1(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=None,
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_2(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=None,
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_3(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=None,
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_4(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=None,
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_5(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=None,
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_6(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=None,
    )


def x__to_snapshot__mutmut_7(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_8(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_9(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_10(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_11(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_12(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        )


def x__to_snapshot__mutmut_13(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["XXnode_countXX"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_14(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["NODE_COUNT"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_15(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["XXallocatable_cpu_coresXX"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_16(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["ALLOCATABLE_CPU_CORES"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_17(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["XXallocatable_memory_gbXX"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_18(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["ALLOCATABLE_MEMORY_GB"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_19(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["XXused_cpu_coresXX"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_20(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["USED_CPU_CORES"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_21(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["XXused_memory_gbXX"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_22(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["USED_MEMORY_GB"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )


def x__to_snapshot__mutmut_23(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["XXautoscaler_enabledXX"],
    )


def x__to_snapshot__mutmut_24(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["AUTOSCALER_ENABLED"],
    )

mutants_x__to_snapshot__mutmut['_mutmut_orig'] = x__to_snapshot__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_1'] = x__to_snapshot__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_2'] = x__to_snapshot__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_3'] = x__to_snapshot__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_4'] = x__to_snapshot__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_5'] = x__to_snapshot__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_6'] = x__to_snapshot__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_7'] = x__to_snapshot__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_8'] = x__to_snapshot__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_9'] = x__to_snapshot__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_10'] = x__to_snapshot__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_11'] = x__to_snapshot__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_12'] = x__to_snapshot__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_13'] = x__to_snapshot__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_14'] = x__to_snapshot__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_15'] = x__to_snapshot__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_16'] = x__to_snapshot__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_17'] = x__to_snapshot__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_18'] = x__to_snapshot__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_19'] = x__to_snapshot__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_20'] = x__to_snapshot__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_21'] = x__to_snapshot__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_22'] = x__to_snapshot__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_23'] = x__to_snapshot__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_snapshot__mutmut['x__to_snapshot__mutmut_24'] = x__to_snapshot__mutmut_24 # type: ignore # mutmut generated
