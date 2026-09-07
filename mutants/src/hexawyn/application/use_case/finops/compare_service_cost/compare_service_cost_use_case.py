from __future__ import annotations

from calendar import monthrange
from datetime import UTC, datetime

from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
from hexawyn.application.use_case.finops.compare_service_cost.command import (
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.finops.compare_service_cost.response import (
    CompareServiceCostResponse,
)
from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
    ServiceCostComparisonEngine,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCompareUseCaseCostUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CompareUseCaseCostUseCase:
    @_mutmut_mutated(mutants_xǁCompareUseCaseCostUseCaseǁ__init____mutmut)
    def __init__(self, cost_port: ServiceCostPort) -> None:
        self._port = cost_port
        self._engine = ServiceCostComparisonEngine()
    def xǁCompareUseCaseCostUseCaseǁ__init____mutmut_orig(self, cost_port: ServiceCostPort) -> None:
        self._port = cost_port
        self._engine = ServiceCostComparisonEngine()
    def xǁCompareUseCaseCostUseCaseǁ__init____mutmut_1(self, cost_port: ServiceCostPort) -> None:
        self._port = None
        self._engine = ServiceCostComparisonEngine()
    def xǁCompareUseCaseCostUseCaseǁ__init____mutmut_2(self, cost_port: ServiceCostPort) -> None:
        self._port = cost_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut)
    def execute(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_orig(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_1(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = None
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_2(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(None)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_3(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = None
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_4(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime(None)
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_5(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("XX%Y-%mXX")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_6(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_7(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%M")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_8(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = None

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_9(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month != 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_10(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 2:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_11(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = None
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_12(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year + 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_13(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 2}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_14(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = None
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_15(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 32
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_16(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = None
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_17(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month + 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_18(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 2:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_19(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = None

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_20(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(None, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_21(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, None)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_22(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_23(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, )[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_24(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month + 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_25(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 2)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_26(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[2]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_27(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = None
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_28(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(None, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_29(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, None)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_30(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_31(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, )
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_32(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = None

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_33(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(None, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_34(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, None)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_35(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_36(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, )

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_37(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = None
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_38(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(None) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_39(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = None

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_40(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(None) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_41(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = None
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_42(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=None,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_43(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=None,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_44(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=None,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_45(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=None,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_46(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=None,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_47(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=None,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_48(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=None,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_49(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=None,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_50(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=None,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_51(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_52(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_53(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_54(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_55(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_56(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_57(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_58(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_59(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            )
        return CompareServiceCostResponse(result=result)

    def xǁCompareUseCaseCostUseCaseǁexecute__mutmut_60(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=None)

mutants_xǁCompareUseCaseCostUseCaseǁ__init____mutmut['_mutmut_orig'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁ__init____mutmut['xǁCompareUseCaseCostUseCaseǁ__init____mutmut_1'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁ__init____mutmut['xǁCompareUseCaseCostUseCaseǁ__init____mutmut_2'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['_mutmut_orig'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_1'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_2'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_3'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_4'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_5'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_6'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_7'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_8'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_9'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_10'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_11'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_12'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_13'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_14'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_15'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_16'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_17'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_18'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_19'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_20'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_21'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_22'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_23'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_24'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_25'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_26'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_27'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_28'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_29'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_30'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_31'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_32'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_33'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_34'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_35'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_36'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_37'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_38'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_39'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_40'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_41'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_42'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_43'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_44'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_45'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_46'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_47'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_48'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_49'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_50'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_51'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_52'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_53'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_54'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_55'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_56'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_57'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_58'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_59'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁCompareUseCaseCostUseCaseǁexecute__mutmut['xǁCompareUseCaseCostUseCaseǁexecute__mutmut_60'] = CompareUseCaseCostUseCase.xǁCompareUseCaseCostUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
