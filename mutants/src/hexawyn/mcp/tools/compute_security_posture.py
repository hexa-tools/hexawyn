"""MCP tool: compute_security_posture."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.compute_security_posture.command import (
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.security.compute_security_posture.compute_security_posture_use_case import (  # noqa: E501
    ComputeSecurityPostureUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_security_posture__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_security_posture__mutmut)
def compute_security_posture() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = None  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=None)  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = None
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(None)
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = None
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "XXoverall_score_pctXX": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "OVERALL_SCORE_PCT": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "XXcategoriesXX": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "CATEGORIES": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "XXnameXX": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "NAME": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "XXscore_pctXX": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "SCORE_PCT": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "XXcompliantXX": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "COMPLIANT": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "XXnon_compliant_countXX": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "NON_COMPLIANT_COUNT": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "XXremediation_orderXX": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "REMEDIATION_ORDER": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"XXresourceXX": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"RESOURCE": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "XXnamespaceXX": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "NAMESPACE": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "XXcategoryXX": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "CATEGORY": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "XXtrendXX": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "TREND": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "XXprevious_score_pctXX": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "PREVIOUS_SCORE_PCT": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "XXpartialXX": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "PARTIAL": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "XXwarningXX": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "WARNING": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "XXerrorXX": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "ERROR": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "XXoverall_score_pctXX": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "OVERALL_SCORE_PCT": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "XXcategoriesXX": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "CATEGORIES": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "XXremediation_orderXX": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "REMEDIATION_ORDER": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "XXtrendXX": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "TREND": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "XXXX",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_45() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "XXprevious_score_pctXX": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_46() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "PREVIOUS_SCORE_PCT": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_47() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "XXpartialXX": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_48() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "PARTIAL": False,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_49() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": True,
            "warning": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_50() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "XXwarningXX": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_51() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "WARNING": "",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_52() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "XXXX",
            "error": str(exc),
        }


def x_compute_security_posture__mutmut_53() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "XXerrorXX": str(exc),
        }


def x_compute_security_posture__mutmut_54() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "ERROR": str(exc),
        }


def x_compute_security_posture__mutmut_55() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(None),
        }

mutants_x_compute_security_posture__mutmut['_mutmut_orig'] = x_compute_security_posture__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_1'] = x_compute_security_posture__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_2'] = x_compute_security_posture__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_3'] = x_compute_security_posture__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_4'] = x_compute_security_posture__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_5'] = x_compute_security_posture__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_6'] = x_compute_security_posture__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_7'] = x_compute_security_posture__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_8'] = x_compute_security_posture__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_9'] = x_compute_security_posture__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_10'] = x_compute_security_posture__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_11'] = x_compute_security_posture__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_12'] = x_compute_security_posture__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_13'] = x_compute_security_posture__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_14'] = x_compute_security_posture__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_15'] = x_compute_security_posture__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_16'] = x_compute_security_posture__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_17'] = x_compute_security_posture__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_18'] = x_compute_security_posture__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_19'] = x_compute_security_posture__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_20'] = x_compute_security_posture__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_21'] = x_compute_security_posture__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_22'] = x_compute_security_posture__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_23'] = x_compute_security_posture__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_24'] = x_compute_security_posture__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_25'] = x_compute_security_posture__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_26'] = x_compute_security_posture__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_27'] = x_compute_security_posture__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_28'] = x_compute_security_posture__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_29'] = x_compute_security_posture__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_30'] = x_compute_security_posture__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_31'] = x_compute_security_posture__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_32'] = x_compute_security_posture__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_33'] = x_compute_security_posture__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_34'] = x_compute_security_posture__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_35'] = x_compute_security_posture__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_36'] = x_compute_security_posture__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_37'] = x_compute_security_posture__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_38'] = x_compute_security_posture__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_39'] = x_compute_security_posture__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_40'] = x_compute_security_posture__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_41'] = x_compute_security_posture__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_42'] = x_compute_security_posture__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_43'] = x_compute_security_posture__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_44'] = x_compute_security_posture__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_45'] = x_compute_security_posture__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_46'] = x_compute_security_posture__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_47'] = x_compute_security_posture__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_48'] = x_compute_security_posture__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_49'] = x_compute_security_posture__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_50'] = x_compute_security_posture__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_51'] = x_compute_security_posture__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_52'] = x_compute_security_posture__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_53'] = x_compute_security_posture__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_54'] = x_compute_security_posture__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_security_posture__mutmut['x_compute_security_posture__mutmut_55'] = x_compute_security_posture__mutmut_55 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_security_posture)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compute_security_posture)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
