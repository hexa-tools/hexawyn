"""MCP tool: compute_team_cost — aggregate resource cost per team."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_team_cost.command import ComputeTeamCostCommand
from hexawyn.application.use_case.finops.compute_team_cost.compute_team_cost_use_case import (
    ComputeTeamCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_team_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_team_cost__mutmut)
def compute_team_cost(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_orig(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_1(
    cpu_price_per_core_hour: float = 1.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_2(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 1.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_3(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 1.1,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_4(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = None
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_5(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = None  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_6(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=None)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_7(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = None
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_8(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            None
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_9(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=None,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_10(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=None,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_11(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=None,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_12(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_13(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_14(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_15(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = None
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_16(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "XXmonthXX": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_17(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "MONTH": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_18(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "XXtotal_costXX": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_19(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "TOTAL_COST": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_20(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "XXunattributed_costXX": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_21(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "UNATTRIBUTED_COST": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_22(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "XXteamsXX": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_23(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "TEAMS": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_24(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "XXteam_nameXX": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_25(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "TEAM_NAME": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_26(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "XXtotal_costXX": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_27(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "TOTAL_COST": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_28(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "XXcpu_costXX": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_29(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "CPU_COST": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_30(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "XXmemory_costXX": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_31(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "MEMORY_COST": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_32(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "XXstorage_costXX": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_33(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "STORAGE_COST": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_34(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "XXnamespace_countXX": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_35(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "NAMESPACE_COUNT": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_36(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "XXdays_activeXX": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_37(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "DAYS_ACTIVE": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_38(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "XXis_proratedXX": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_39(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "IS_PRORATED": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_40(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "XXprevious_month_teamsXX": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_41(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "PREVIOUS_MONTH_TEAMS": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_42(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "XXteam_nameXX": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_43(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "TEAM_NAME": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_44(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "XXtotal_costXX": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_45(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "TOTAL_COST": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_46(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_47(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_48(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "XXmonthXX": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_49(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "MONTH": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_50(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "XXXX",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_51(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "XXtotal_costXX": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_52(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "TOTAL_COST": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_53(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 1.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_54(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "XXunattributed_costXX": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_55(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "UNATTRIBUTED_COST": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_56(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 1.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_57(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "XXteamsXX": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_58(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "TEAMS": [],
            "previous_month_teams": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_59(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "XXprevious_month_teamsXX": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_60(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "PREVIOUS_MONTH_TEAMS": [],
            "error": str(exc),
        }


def x_compute_team_cost__mutmut_61(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "XXerrorXX": str(exc),
        }


def x_compute_team_cost__mutmut_62(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "ERROR": str(exc),
        }


def x_compute_team_cost__mutmut_63(
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
    storage_price_per_gb_month: float = 0.10,
) -> dict[str, object]:
    """Aggregate cluster resource cost per team.

    Maps namespaces to teams via K8s labels, computes CPU/memory/storage
    cost per team, ranks from highest to lowest cost, and includes
    month-over-month comparison.

    Args:
        cpu_price_per_core_hour: CPU pricing per core per hour.
        memory_price_per_gb_hour: Memory pricing per GB per hour.
        storage_price_per_gb_month: Storage pricing per GB per month.
    """
    from hexawyn.mcp.server import build_team_cost_adapter

    try:
        adapter = build_team_cost_adapter()
        use_case = ComputeTeamCostUseCase(port=adapter)  # type: ignore
        response = use_case.execute(
            ComputeTeamCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
                storage_price_per_gb_month=storage_price_per_gb_month,
            )
        )
        r = response.result
        return {
            "month": r.month,
            "total_cost": r.total_cost,
            "unattributed_cost": r.unattributed_cost,  # type: ignore
            "teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                    "cpu_cost": t.cpu_cost,
                    "memory_cost": t.memory_cost,
                    "storage_cost": t.storage_cost,
                    "namespace_count": t.namespace_count,
                    "days_active": t.days_active,  # type: ignore
                    "is_prorated": t.is_prorated,  # type: ignore
                }
                for t in r.teams
            ],
            "previous_month_teams": [
                {
                    "team_name": t.team_name,
                    "total_cost": t.total_cost,
                }
                for t in r.previous_month_teams  # type: ignore
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "month": "",
            "total_cost": 0.0,
            "unattributed_cost": 0.0,
            "teams": [],
            "previous_month_teams": [],
            "error": str(None),
        }

mutants_x_compute_team_cost__mutmut['_mutmut_orig'] = x_compute_team_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_1'] = x_compute_team_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_2'] = x_compute_team_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_3'] = x_compute_team_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_4'] = x_compute_team_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_5'] = x_compute_team_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_6'] = x_compute_team_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_7'] = x_compute_team_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_8'] = x_compute_team_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_9'] = x_compute_team_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_10'] = x_compute_team_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_11'] = x_compute_team_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_12'] = x_compute_team_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_13'] = x_compute_team_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_14'] = x_compute_team_cost__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_15'] = x_compute_team_cost__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_16'] = x_compute_team_cost__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_17'] = x_compute_team_cost__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_18'] = x_compute_team_cost__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_19'] = x_compute_team_cost__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_20'] = x_compute_team_cost__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_21'] = x_compute_team_cost__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_22'] = x_compute_team_cost__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_23'] = x_compute_team_cost__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_24'] = x_compute_team_cost__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_25'] = x_compute_team_cost__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_26'] = x_compute_team_cost__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_27'] = x_compute_team_cost__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_28'] = x_compute_team_cost__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_29'] = x_compute_team_cost__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_30'] = x_compute_team_cost__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_31'] = x_compute_team_cost__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_32'] = x_compute_team_cost__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_33'] = x_compute_team_cost__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_34'] = x_compute_team_cost__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_35'] = x_compute_team_cost__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_36'] = x_compute_team_cost__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_37'] = x_compute_team_cost__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_38'] = x_compute_team_cost__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_39'] = x_compute_team_cost__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_40'] = x_compute_team_cost__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_41'] = x_compute_team_cost__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_42'] = x_compute_team_cost__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_43'] = x_compute_team_cost__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_44'] = x_compute_team_cost__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_45'] = x_compute_team_cost__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_46'] = x_compute_team_cost__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_47'] = x_compute_team_cost__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_48'] = x_compute_team_cost__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_49'] = x_compute_team_cost__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_50'] = x_compute_team_cost__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_51'] = x_compute_team_cost__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_52'] = x_compute_team_cost__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_53'] = x_compute_team_cost__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_54'] = x_compute_team_cost__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_55'] = x_compute_team_cost__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_56'] = x_compute_team_cost__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_57'] = x_compute_team_cost__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_58'] = x_compute_team_cost__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_59'] = x_compute_team_cost__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_60'] = x_compute_team_cost__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_61'] = x_compute_team_cost__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_62'] = x_compute_team_cost__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_team_cost__mutmut['x_compute_team_cost__mutmut_63'] = x_compute_team_cost__mutmut_63 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_team_cost)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compute_team_cost)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
