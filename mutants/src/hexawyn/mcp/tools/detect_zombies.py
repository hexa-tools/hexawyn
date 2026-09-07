"""MCP tool: detect_zombies — identify idle workloads with zero network traffic."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.detect_zombies.command import DetectZombiesCommand
from hexawyn.application.use_case.troubleshooting.detect_zombies.detect_zombies_use_case import (
    DetectZombiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_zombies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_zombies__mutmut)
def detect_zombies(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_orig(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_1(analysis_window_hours: int = 25) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_2(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = None
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_3(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = None
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_4(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=None)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_5(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = None
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_6(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            None
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_7(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=None)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_8(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = None
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_9(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "XXanalysis_window_hoursXX": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_10(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "ANALYSIS_WINDOW_HOURS": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_11(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "XXzombie_countXX": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_12(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "ZOMBIE_COUNT": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_13(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "XXzombie_candidatesXX": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_14(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "ZOMBIE_CANDIDATES": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_15(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "XXpod_nameXX": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_16(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "POD_NAME": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_17(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "XXnamespaceXX": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_18(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "NAMESPACE": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_19(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "XXage_daysXX": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_20(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "AGE_DAYS": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_21(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "XXtraffic_rpsXX": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_22(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "TRAFFIC_RPS": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_23(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "XXcpu_coresXX": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_24(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "CPU_CORES": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_25(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "XXmemory_gbXX": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_26(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "MEMORY_GB": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_27(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "XXriskXX": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_28(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "RISK": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_29(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "XXreasonXX": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_30(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "REASON": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_31(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "XXtotal_wasted_coresXX": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_32(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "TOTAL_WASTED_CORES": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_33(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "XXtotal_wasted_gbXX": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_34(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "TOTAL_WASTED_GB": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_35(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "XXprometheus_availableXX": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_36(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "PROMETHEUS_AVAILABLE": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_37(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "XXdata_sourceXX": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_38(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "DATA_SOURCE": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_39(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_40(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_41(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXanalysis_window_hoursXX": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_42(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "ANALYSIS_WINDOW_HOURS": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_43(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 1,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_44(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "XXzombie_countXX": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_45(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "ZOMBIE_COUNT": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_46(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 1,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_47(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "XXzombie_candidatesXX": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_48(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "ZOMBIE_CANDIDATES": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_49(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "XXtotal_wasted_coresXX": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_50(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "TOTAL_WASTED_CORES": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_51(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 1.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_52(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "XXtotal_wasted_gbXX": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_53(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "TOTAL_WASTED_GB": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_54(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 1.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_55(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "XXprometheus_availableXX": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_56(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "PROMETHEUS_AVAILABLE": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_57(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": True,
            "data_source": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_58(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "XXdata_sourceXX": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_59(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "DATA_SOURCE": "estimated",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_60(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "XXestimatedXX",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_61(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "ESTIMATED",
            "error": str(exc),
        }


def x_detect_zombies__mutmut_62(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "XXerrorXX": str(exc),
        }


def x_detect_zombies__mutmut_63(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "ERROR": str(exc),
        }


def x_detect_zombies__mutmut_64(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(None),
        }

mutants_x_detect_zombies__mutmut['_mutmut_orig'] = x_detect_zombies__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_1'] = x_detect_zombies__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_2'] = x_detect_zombies__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_3'] = x_detect_zombies__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_4'] = x_detect_zombies__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_5'] = x_detect_zombies__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_6'] = x_detect_zombies__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_7'] = x_detect_zombies__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_8'] = x_detect_zombies__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_9'] = x_detect_zombies__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_10'] = x_detect_zombies__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_11'] = x_detect_zombies__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_12'] = x_detect_zombies__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_13'] = x_detect_zombies__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_14'] = x_detect_zombies__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_15'] = x_detect_zombies__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_16'] = x_detect_zombies__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_17'] = x_detect_zombies__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_18'] = x_detect_zombies__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_19'] = x_detect_zombies__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_20'] = x_detect_zombies__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_21'] = x_detect_zombies__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_22'] = x_detect_zombies__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_23'] = x_detect_zombies__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_24'] = x_detect_zombies__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_25'] = x_detect_zombies__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_26'] = x_detect_zombies__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_27'] = x_detect_zombies__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_28'] = x_detect_zombies__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_29'] = x_detect_zombies__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_30'] = x_detect_zombies__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_31'] = x_detect_zombies__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_32'] = x_detect_zombies__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_33'] = x_detect_zombies__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_34'] = x_detect_zombies__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_35'] = x_detect_zombies__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_36'] = x_detect_zombies__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_37'] = x_detect_zombies__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_38'] = x_detect_zombies__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_39'] = x_detect_zombies__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_40'] = x_detect_zombies__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_41'] = x_detect_zombies__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_42'] = x_detect_zombies__mutmut_42 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_43'] = x_detect_zombies__mutmut_43 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_44'] = x_detect_zombies__mutmut_44 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_45'] = x_detect_zombies__mutmut_45 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_46'] = x_detect_zombies__mutmut_46 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_47'] = x_detect_zombies__mutmut_47 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_48'] = x_detect_zombies__mutmut_48 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_49'] = x_detect_zombies__mutmut_49 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_50'] = x_detect_zombies__mutmut_50 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_51'] = x_detect_zombies__mutmut_51 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_52'] = x_detect_zombies__mutmut_52 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_53'] = x_detect_zombies__mutmut_53 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_54'] = x_detect_zombies__mutmut_54 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_55'] = x_detect_zombies__mutmut_55 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_56'] = x_detect_zombies__mutmut_56 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_57'] = x_detect_zombies__mutmut_57 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_58'] = x_detect_zombies__mutmut_58 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_59'] = x_detect_zombies__mutmut_59 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_60'] = x_detect_zombies__mutmut_60 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_61'] = x_detect_zombies__mutmut_61 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_62'] = x_detect_zombies__mutmut_62 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_63'] = x_detect_zombies__mutmut_63 # type: ignore # mutmut generated
mutants_x_detect_zombies__mutmut['x_detect_zombies__mutmut_64'] = x_detect_zombies__mutmut_64 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_zombies)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_zombies)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
