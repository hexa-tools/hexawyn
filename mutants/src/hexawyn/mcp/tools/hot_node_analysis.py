"""MCP tool: hot_node_analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.hot_node_analysis.command import HotNodeAnalysisCommand
from hexawyn.application.use_case.cluster.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_hot_node_analysis__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_hot_node_analysis__mutmut)
def hot_node_analysis() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = None
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=None,
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=None,
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = None
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(None)
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "XXhot_nodesXX": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "HOT_NODES": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "XXhealthy_node_countXX": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "HEALTHY_NODE_COUNT": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "XXexcluded_cordoned_nodesXX": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "EXCLUDED_CORDONED_NODES": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "XXwarningsXX": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "WARNINGS": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "XXsummaryXX": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "SUMMARY": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXhot_nodesXX": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "HOT_NODES": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "XXhealthy_node_countXX": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "HEALTHY_NODE_COUNT": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 1,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "XXexcluded_cordoned_nodesXX": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "EXCLUDED_CORDONED_NODES": [],
            "warnings": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "XXwarningsXX": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "WARNINGS": [],
            "summary": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "XXsummaryXX": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "SUMMARY": "",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "XXXX",
            "error": str(exc),
        }


def x_hot_node_analysis__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "XXerrorXX": str(exc),
        }


def x_hot_node_analysis__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "ERROR": str(exc),
        }


def x_hot_node_analysis__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_cluster_resource_metrics_adapter,
        build_node_analysis_adapter,
    )

    try:
        use_case = HotNodeAnalysisUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            node_port=build_node_analysis_adapter(),
        )
        response = use_case.execute(HotNodeAnalysisCommand())
        return {
            "hot_nodes": response.hot_nodes,
            "healthy_node_count": response.healthy_node_count,
            "excluded_cordoned_nodes": response.excluded_cordoned_nodes,
            "warnings": response.warnings,
            "summary": response.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "hot_nodes": [],
            "healthy_node_count": 0,
            "excluded_cordoned_nodes": [],
            "warnings": [],
            "summary": "",
            "error": str(None),
        }

mutants_x_hot_node_analysis__mutmut['_mutmut_orig'] = x_hot_node_analysis__mutmut_orig # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_1'] = x_hot_node_analysis__mutmut_1 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_2'] = x_hot_node_analysis__mutmut_2 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_3'] = x_hot_node_analysis__mutmut_3 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_4'] = x_hot_node_analysis__mutmut_4 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_5'] = x_hot_node_analysis__mutmut_5 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_6'] = x_hot_node_analysis__mutmut_6 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_7'] = x_hot_node_analysis__mutmut_7 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_8'] = x_hot_node_analysis__mutmut_8 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_9'] = x_hot_node_analysis__mutmut_9 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_10'] = x_hot_node_analysis__mutmut_10 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_11'] = x_hot_node_analysis__mutmut_11 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_12'] = x_hot_node_analysis__mutmut_12 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_13'] = x_hot_node_analysis__mutmut_13 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_14'] = x_hot_node_analysis__mutmut_14 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_15'] = x_hot_node_analysis__mutmut_15 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_16'] = x_hot_node_analysis__mutmut_16 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_17'] = x_hot_node_analysis__mutmut_17 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_18'] = x_hot_node_analysis__mutmut_18 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_19'] = x_hot_node_analysis__mutmut_19 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_20'] = x_hot_node_analysis__mutmut_20 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_21'] = x_hot_node_analysis__mutmut_21 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_22'] = x_hot_node_analysis__mutmut_22 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_23'] = x_hot_node_analysis__mutmut_23 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_24'] = x_hot_node_analysis__mutmut_24 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_25'] = x_hot_node_analysis__mutmut_25 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_26'] = x_hot_node_analysis__mutmut_26 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_27'] = x_hot_node_analysis__mutmut_27 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_28'] = x_hot_node_analysis__mutmut_28 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_29'] = x_hot_node_analysis__mutmut_29 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_30'] = x_hot_node_analysis__mutmut_30 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_31'] = x_hot_node_analysis__mutmut_31 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_32'] = x_hot_node_analysis__mutmut_32 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_33'] = x_hot_node_analysis__mutmut_33 # type: ignore # mutmut generated
mutants_x_hot_node_analysis__mutmut['x_hot_node_analysis__mutmut_34'] = x_hot_node_analysis__mutmut_34 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(hot_node_analysis)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(hot_node_analysis)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
