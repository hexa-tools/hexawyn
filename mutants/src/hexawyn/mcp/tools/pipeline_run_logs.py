"""MCP tool: pipeline_run_logs — Get logs of a PipelineRun with failed step highlighting."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.pipeline_run_logs.command import PipelineRunLogsCommand
from hexawyn.application.use_case.pipelines.pipeline_run_logs.pipeline_run_logs_use_case import (
    PipelineRunLogsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_pipeline_run_logs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_pipeline_run_logs__mutmut)
def pipeline_run_logs(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_orig(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_1(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = None
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_2(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = None
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_3(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            None
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_4(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=None).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_5(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=None, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_6(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=None)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_7(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_8(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, )
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_9(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "XXpipeline_run_nameXX": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_10(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "PIPELINE_RUN_NAME": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_11(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "XXnamespaceXX": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_12(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "NAMESPACE": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_13(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "XXpipeline_run_foundXX": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_14(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "PIPELINE_RUN_FOUND": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_15(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "XXis_still_runningXX": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_16(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "IS_STILL_RUNNING": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_17(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "XXfailed_step_countXX": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_18(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "FAILED_STEP_COUNT": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_19(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "XXtotal_step_countXX": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_20(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "TOTAL_STEP_COUNT": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_21(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "XXstepsXX": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_22(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "STEPS": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_23(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_24(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_25(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXpipeline_run_nameXX": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_26(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"PIPELINE_RUN_NAME": pipeline_run_name, "error": str(exc)}


def x_pipeline_run_logs__mutmut_27(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "XXerrorXX": str(exc)}


def x_pipeline_run_logs__mutmut_28(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "ERROR": str(exc)}


def x_pipeline_run_logs__mutmut_29(pipeline_run_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_pipeline_run_logs_adapter

    try:
        a = build_pipeline_run_logs_adapter()
        r = PipelineRunLogsUseCase(port=a).execute(
            PipelineRunLogsCommand(pipeline_run_name=pipeline_run_name, namespace=namespace)
        )
        return {
            "pipeline_run_name": r.pipeline_run_name,
            "namespace": r.namespace,
            "pipeline_run_found": r.pipeline_run_found,
            "is_still_running": r.is_still_running,
            "failed_step_count": r.failed_step_count,
            "total_step_count": r.total_step_count,
            "steps": r.steps,
            "error": r.error,
        }
    except Exception as exc:
        return {"pipeline_run_name": pipeline_run_name, "error": str(None)}

mutants_x_pipeline_run_logs__mutmut['_mutmut_orig'] = x_pipeline_run_logs__mutmut_orig # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_1'] = x_pipeline_run_logs__mutmut_1 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_2'] = x_pipeline_run_logs__mutmut_2 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_3'] = x_pipeline_run_logs__mutmut_3 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_4'] = x_pipeline_run_logs__mutmut_4 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_5'] = x_pipeline_run_logs__mutmut_5 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_6'] = x_pipeline_run_logs__mutmut_6 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_7'] = x_pipeline_run_logs__mutmut_7 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_8'] = x_pipeline_run_logs__mutmut_8 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_9'] = x_pipeline_run_logs__mutmut_9 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_10'] = x_pipeline_run_logs__mutmut_10 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_11'] = x_pipeline_run_logs__mutmut_11 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_12'] = x_pipeline_run_logs__mutmut_12 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_13'] = x_pipeline_run_logs__mutmut_13 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_14'] = x_pipeline_run_logs__mutmut_14 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_15'] = x_pipeline_run_logs__mutmut_15 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_16'] = x_pipeline_run_logs__mutmut_16 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_17'] = x_pipeline_run_logs__mutmut_17 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_18'] = x_pipeline_run_logs__mutmut_18 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_19'] = x_pipeline_run_logs__mutmut_19 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_20'] = x_pipeline_run_logs__mutmut_20 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_21'] = x_pipeline_run_logs__mutmut_21 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_22'] = x_pipeline_run_logs__mutmut_22 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_23'] = x_pipeline_run_logs__mutmut_23 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_24'] = x_pipeline_run_logs__mutmut_24 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_25'] = x_pipeline_run_logs__mutmut_25 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_26'] = x_pipeline_run_logs__mutmut_26 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_27'] = x_pipeline_run_logs__mutmut_27 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_28'] = x_pipeline_run_logs__mutmut_28 # type: ignore # mutmut generated
mutants_x_pipeline_run_logs__mutmut['x_pipeline_run_logs__mutmut_29'] = x_pipeline_run_logs__mutmut_29 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_run_logs)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(pipeline_run_logs)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
