from __future__ import annotations

from calendar import monthrange
from datetime import UTC, datetime

from hexawyn.application.ports.driven.team_cost_port import TeamCostPort
from hexawyn.application.use_case.finops.compute_team_cost.command import (
    ComputeTeamCostCommand,
)
from hexawyn.application.use_case.finops.compute_team_cost.response import (
    ComputeTeamCostResponse,
)
from hexawyn.domain.services.team_cost.team_cost_aggregation_engine import (
    TeamCostAggregationEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeTeamCostUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputeTeamCostUseCase:
    @_mutmut_mutated(mutants_xǁComputeTeamCostUseCaseǁ__init____mutmut)
    def __init__(self, cost_port: TeamCostPort) -> None:
        self._port = cost_port
        self._engine = TeamCostAggregationEngine()
    def xǁComputeTeamCostUseCaseǁ__init____mutmut_orig(self, cost_port: TeamCostPort) -> None:
        self._port = cost_port
        self._engine = TeamCostAggregationEngine()
    def xǁComputeTeamCostUseCaseǁ__init____mutmut_1(self, cost_port: TeamCostPort) -> None:
        self._port = None
        self._engine = TeamCostAggregationEngine()
    def xǁComputeTeamCostUseCaseǁ__init____mutmut_2(self, cost_port: TeamCostPort) -> None:
        self._port = cost_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut)
    def execute(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_orig(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_1(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = None
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_2(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(None)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_3(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = None
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_4(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime(None)
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_5(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("XX%Y-%mXX")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_6(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_7(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%M")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_8(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = None

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_9(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(None, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_10(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, None)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_11(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_12(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, )

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_13(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = None
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_14(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(None)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_15(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = None

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_16(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(None) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_17(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = None
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_18(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(None, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_19(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, None)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_20(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_21(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, )
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_22(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = None
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_23(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(None)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_24(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = None

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_25(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(None) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_26(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = None
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_27(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=None,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_28(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=None,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_29(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=None,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_30(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=None,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_31(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=None,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_32(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=None,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_33(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=None,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_34(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_35(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_36(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_37(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_38(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_39(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_40(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            )
        return ComputeTeamCostResponse(result=result)  # type: ignore

    def xǁComputeTeamCostUseCaseǁexecute__mutmut_41(self, command: ComputeTeamCostCommand) -> ComputeTeamCostResponse:
        now = datetime.now(UTC)
        month = now.strftime("%Y-%m")
        days_in_month = _days_in_month(now.year, now.month)

        ns_raw = self._port.fetch_namespace_resources(month)
        nss: list[dict[str, object]] = [dict(n) for n in ns_raw]

        prev_month_str = _previous_month(now.year, now.month)
        prev_ns_raw = self._port.fetch_namespace_resources(prev_month_str)
        prev_nss: list[dict[str, object]] = [dict(n) for n in prev_ns_raw]

        result = self._engine.compute(
            namespaces=nss,
            month=month,
            days_in_month=days_in_month,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
            storage_price_per_gb_month=command.storage_price_per_gb_month,
            previous_namespaces=prev_nss,
        )
        return ComputeTeamCostResponse(result=None)  # type: ignore

mutants_xǁComputeTeamCostUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁ__init____mutmut['xǁComputeTeamCostUseCaseǁ__init____mutmut_1'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁ__init____mutmut['xǁComputeTeamCostUseCaseǁ__init____mutmut_2'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_1'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_2'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_3'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_4'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_5'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_6'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_7'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_8'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_9'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_10'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_11'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_12'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_13'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_14'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_15'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_16'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_17'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_18'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_19'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_20'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_21'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_22'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_23'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_24'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_25'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_26'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_27'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_28'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_29'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_30'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_31'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_32'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_33'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_34'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_35'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_36'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_37'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_38'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_39'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_40'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁComputeTeamCostUseCaseǁexecute__mutmut['xǁComputeTeamCostUseCaseǁexecute__mutmut_41'] = ComputeTeamCostUseCase.xǁComputeTeamCostUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_x__days_in_month__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__days_in_month__mutmut)
def _days_in_month(year: int, month: int) -> int:
    return monthrange(year, month)[1]


def x__days_in_month__mutmut_orig(year: int, month: int) -> int:
    return monthrange(year, month)[1]


def x__days_in_month__mutmut_1(year: int, month: int) -> int:
    return monthrange(None, month)[1]


def x__days_in_month__mutmut_2(year: int, month: int) -> int:
    return monthrange(year, None)[1]


def x__days_in_month__mutmut_3(year: int, month: int) -> int:
    return monthrange(month)[1]


def x__days_in_month__mutmut_4(year: int, month: int) -> int:
    return monthrange(year, )[1]


def x__days_in_month__mutmut_5(year: int, month: int) -> int:
    return monthrange(year, month)[2]

mutants_x__days_in_month__mutmut['_mutmut_orig'] = x__days_in_month__mutmut_orig # type: ignore # mutmut generated
mutants_x__days_in_month__mutmut['x__days_in_month__mutmut_1'] = x__days_in_month__mutmut_1 # type: ignore # mutmut generated
mutants_x__days_in_month__mutmut['x__days_in_month__mutmut_2'] = x__days_in_month__mutmut_2 # type: ignore # mutmut generated
mutants_x__days_in_month__mutmut['x__days_in_month__mutmut_3'] = x__days_in_month__mutmut_3 # type: ignore # mutmut generated
mutants_x__days_in_month__mutmut['x__days_in_month__mutmut_4'] = x__days_in_month__mutmut_4 # type: ignore # mutmut generated
mutants_x__days_in_month__mutmut['x__days_in_month__mutmut_5'] = x__days_in_month__mutmut_5 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__previous_month__mutmut)
def _previous_month(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_orig(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_1(year: int, month: int) -> str:
    if month != 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_2(year: int, month: int) -> str:
    if month == 2:
        return f"{year - 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_3(year: int, month: int) -> str:
    if month == 1:
        return f"{year + 1}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_4(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 2}-12"
    return f"{year}-{month - 1:02d}"


def x__previous_month__mutmut_5(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month + 1:02d}"


def x__previous_month__mutmut_6(year: int, month: int) -> str:
    if month == 1:
        return f"{year - 1}-12"
    return f"{year}-{month - 2:02d}"

mutants_x__previous_month__mutmut['_mutmut_orig'] = x__previous_month__mutmut_orig # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_1'] = x__previous_month__mutmut_1 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_2'] = x__previous_month__mutmut_2 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_3'] = x__previous_month__mutmut_3 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_4'] = x__previous_month__mutmut_4 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_5'] = x__previous_month__mutmut_5 # type: ignore # mutmut generated
mutants_x__previous_month__mutmut['x__previous_month__mutmut_6'] = x__previous_month__mutmut_6 # type: ignore # mutmut generated
