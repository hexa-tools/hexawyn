"""MCP tool: get_quota_usage — Get current quota usage."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.get_quota_usage.command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_quota_usage__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_quota_usage__mutmut)
def get_quota_usage() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_orig() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_1() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = None
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_2() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=None)
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_3() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = None
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_4() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=None,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_5() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=None,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_6() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_7() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_8() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = None
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_9() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(None)
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_10() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = None
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_11() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "XXresourceXX": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_12() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "RESOURCE": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_13() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "XXusedXX": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_14() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "USED": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_15() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "XXlimitXX": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_16() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "LIMIT": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_17() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "XXstateXX": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_18() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "STATE": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_19() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "XXavailable_from_tierXX": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_20() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "AVAILABLE_FROM_TIER": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_21() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "XXquotasXX": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_22() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "QUOTAS": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_23() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "XXinvestigations_usedXX": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_24() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "INVESTIGATIONS_USED": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_25() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "XXinvestigations_limitXX": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_26() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "INVESTIGATIONS_LIMIT": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_27() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_28() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_29() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXquotasXX": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_30() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "QUOTAS": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_31() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "XXinvestigations_usedXX": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_32() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "INVESTIGATIONS_USED": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_33() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 1,
            "investigations_limit": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_34() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "XXinvestigations_limitXX": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_35() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "INVESTIGATIONS_LIMIT": None,
            "error": str(exc),
        }


def x_get_quota_usage__mutmut_36() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "XXerrorXX": str(exc),
        }


def x_get_quota_usage__mutmut_37() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "ERROR": str(exc),
        }


def x_get_quota_usage__mutmut_38() -> dict[str, object]:
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource

    try:
        quota_source = RuntimeQuotaSource(runtime=get_runtime())
        use_case = GetQuotaUsageUseCase(
            plan_port=quota_source,
            usage_meter=quota_source,
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(None),
        }

mutants_x_get_quota_usage__mutmut['_mutmut_orig'] = x_get_quota_usage__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_1'] = x_get_quota_usage__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_2'] = x_get_quota_usage__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_3'] = x_get_quota_usage__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_4'] = x_get_quota_usage__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_5'] = x_get_quota_usage__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_6'] = x_get_quota_usage__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_7'] = x_get_quota_usage__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_8'] = x_get_quota_usage__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_9'] = x_get_quota_usage__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_10'] = x_get_quota_usage__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_11'] = x_get_quota_usage__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_12'] = x_get_quota_usage__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_13'] = x_get_quota_usage__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_14'] = x_get_quota_usage__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_15'] = x_get_quota_usage__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_16'] = x_get_quota_usage__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_17'] = x_get_quota_usage__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_18'] = x_get_quota_usage__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_19'] = x_get_quota_usage__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_20'] = x_get_quota_usage__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_21'] = x_get_quota_usage__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_22'] = x_get_quota_usage__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_23'] = x_get_quota_usage__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_24'] = x_get_quota_usage__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_25'] = x_get_quota_usage__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_26'] = x_get_quota_usage__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_27'] = x_get_quota_usage__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_28'] = x_get_quota_usage__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_29'] = x_get_quota_usage__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_30'] = x_get_quota_usage__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_31'] = x_get_quota_usage__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_32'] = x_get_quota_usage__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_33'] = x_get_quota_usage__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_34'] = x_get_quota_usage__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_35'] = x_get_quota_usage__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_36'] = x_get_quota_usage__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_37'] = x_get_quota_usage__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_quota_usage__mutmut['x_get_quota_usage__mutmut_38'] = x_get_quota_usage__mutmut_38 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_quota_usage)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_quota_usage)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
