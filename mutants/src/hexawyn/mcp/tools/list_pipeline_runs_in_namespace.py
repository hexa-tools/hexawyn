"""MCP tool: list_pipeline_runs_in_namespace — Operational view of all PipelineRuns in a namespace."""  # noqa: E501

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_use_case import (  # noqa: E501
    ListPipelineRunsInNamespaceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_pipeline_runs_in_namespace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_pipeline_runs_in_namespace__mutmut)
def list_pipeline_runs_in_namespace(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_orig(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_1(namespace: str, limit: int = 101) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_2(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = None
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_3(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = None
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_4(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=None)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_5(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = None
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_6(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            None
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_7(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=None, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_8(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=None)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_9(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_10(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, )
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_11(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "XXrunsXX": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_12(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "RUNS": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_13(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "XXis_stuckXX": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_14(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "IS_STUCK": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_15(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["XXnameXX"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_16(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["NAME"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_17(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] not in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_18(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "XXstuck_runsXX": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_19(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "STUCK_RUNS": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_20(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "XXnoteXX": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_21(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "NOTE": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_22(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_23(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_24(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXrunsXX": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_25(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "RUNS": [],
            "stuck_runs": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_26(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "XXstuck_runsXX": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_27(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "STUCK_RUNS": [],
            "note": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_28(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_29(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "NOTE": None,
            "error": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_30(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_31(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "ERROR": str(exc),
        }


def x_list_pipeline_runs_in_namespace__mutmut_32(namespace: str, limit: int = 100) -> dict[str, object]:
    """List all PipelineRuns in a namespace sorted by status (Failed first, then Running, Succeeded).

    Args:
        namespace: The Kubernetes namespace to query.
        limit: Maximum number of runs to return (default: 100).
    """  # noqa: E501
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=adapter)
        response = use_case.execute(  # type: ignore
            ListPipelineRunsInNamespaceCommand(namespace=namespace, limit=limit)
        )
        return {
            "runs": [
                {**run, "is_stuck": run["name"] in response.stuck_runs} for run in response.runs
            ],
            "stuck_runs": response.stuck_runs,
            "note": response.note,
            "error": None,
        }
    except Exception as exc:
        return {
            "runs": [],
            "stuck_runs": [],
            "note": None,
            "error": str(None),
        }

mutants_x_list_pipeline_runs_in_namespace__mutmut['_mutmut_orig'] = x_list_pipeline_runs_in_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_1'] = x_list_pipeline_runs_in_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_2'] = x_list_pipeline_runs_in_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_3'] = x_list_pipeline_runs_in_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_4'] = x_list_pipeline_runs_in_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_5'] = x_list_pipeline_runs_in_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_6'] = x_list_pipeline_runs_in_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_7'] = x_list_pipeline_runs_in_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_8'] = x_list_pipeline_runs_in_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_9'] = x_list_pipeline_runs_in_namespace__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_10'] = x_list_pipeline_runs_in_namespace__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_11'] = x_list_pipeline_runs_in_namespace__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_12'] = x_list_pipeline_runs_in_namespace__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_13'] = x_list_pipeline_runs_in_namespace__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_14'] = x_list_pipeline_runs_in_namespace__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_15'] = x_list_pipeline_runs_in_namespace__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_16'] = x_list_pipeline_runs_in_namespace__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_17'] = x_list_pipeline_runs_in_namespace__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_18'] = x_list_pipeline_runs_in_namespace__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_19'] = x_list_pipeline_runs_in_namespace__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_20'] = x_list_pipeline_runs_in_namespace__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_21'] = x_list_pipeline_runs_in_namespace__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_22'] = x_list_pipeline_runs_in_namespace__mutmut_22 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_23'] = x_list_pipeline_runs_in_namespace__mutmut_23 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_24'] = x_list_pipeline_runs_in_namespace__mutmut_24 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_25'] = x_list_pipeline_runs_in_namespace__mutmut_25 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_26'] = x_list_pipeline_runs_in_namespace__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_27'] = x_list_pipeline_runs_in_namespace__mutmut_27 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_28'] = x_list_pipeline_runs_in_namespace__mutmut_28 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_29'] = x_list_pipeline_runs_in_namespace__mutmut_29 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_30'] = x_list_pipeline_runs_in_namespace__mutmut_30 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_31'] = x_list_pipeline_runs_in_namespace__mutmut_31 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs_in_namespace__mutmut['x_list_pipeline_runs_in_namespace__mutmut_32'] = x_list_pipeline_runs_in_namespace__mutmut_32 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    """Register list_pipeline_runs_in_namespace as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_pipeline_runs_in_namespace)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    """Register list_pipeline_runs_in_namespace as an MCP tool on the given FastMCP server."""
    mcp.tool()(list_pipeline_runs_in_namespace)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    """Register list_pipeline_runs_in_namespace as an MCP tool on the given FastMCP server."""
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
