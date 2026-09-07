"""MCP tool: version_regression — Detect latency/error regressions between service versions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.version_regression.command import (
    VersionRegressionCommand,
)
from hexawyn.application.use_case.pipelines.version_regression.version_regression_use_case import (
    VersionRegressionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_version_regression__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_version_regression__mutmut)
def version_regression(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_orig(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_1(service_name: str, time_window_minutes: int = 121) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_2(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = None
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_3(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = None
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_4(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            None
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_5(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=None).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_6(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=None, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_7(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=None
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_8(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_9(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_10(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "XXservice_nameXX": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_11(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "SERVICE_NAME": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_12(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "XXbaseline_versionXX": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_13(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "BASELINE_VERSION": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_14(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "XXcurrent_versionXX": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_15(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "CURRENT_VERSION": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_16(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "XXverdictXX": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_17(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "VERDICT": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_18(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "XXp99_delta_pctXX": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_19(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "P99_DELTA_PCT": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_20(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "XXerror_delta_pctXX": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_21(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "ERROR_DELTA_PCT": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_22(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "XXflagsXX": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_23(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "FLAGS": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_24(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_25(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def x_version_regression__mutmut_26(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXservice_nameXX": service_name, "error": str(exc)}


def x_version_regression__mutmut_27(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"SERVICE_NAME": service_name, "error": str(exc)}


def x_version_regression__mutmut_28(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "XXerrorXX": str(exc)}


def x_version_regression__mutmut_29(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "ERROR": str(exc)}


def x_version_regression__mutmut_30(service_name: str, time_window_minutes: int = 120) -> dict[str, object]:
    from hexawyn.mcp.server import build_version_regression_adapter

    try:
        a = build_version_regression_adapter()
        r = VersionRegressionUseCase(port=a).execute(
            VersionRegressionCommand(
                service_name=service_name, time_window_minutes=time_window_minutes
            )
        )
        return {
            "service_name": r.service_name,
            "baseline_version": r.baseline_version,
            "current_version": r.current_version,
            "verdict": r.verdict,
            "p99_delta_pct": r.p99_delta_pct,
            "error_delta_pct": r.error_delta_pct,
            "flags": r.flags,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(None)}

mutants_x_version_regression__mutmut['_mutmut_orig'] = x_version_regression__mutmut_orig # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_1'] = x_version_regression__mutmut_1 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_2'] = x_version_regression__mutmut_2 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_3'] = x_version_regression__mutmut_3 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_4'] = x_version_regression__mutmut_4 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_5'] = x_version_regression__mutmut_5 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_6'] = x_version_regression__mutmut_6 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_7'] = x_version_regression__mutmut_7 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_8'] = x_version_regression__mutmut_8 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_9'] = x_version_regression__mutmut_9 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_10'] = x_version_regression__mutmut_10 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_11'] = x_version_regression__mutmut_11 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_12'] = x_version_regression__mutmut_12 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_13'] = x_version_regression__mutmut_13 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_14'] = x_version_regression__mutmut_14 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_15'] = x_version_regression__mutmut_15 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_16'] = x_version_regression__mutmut_16 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_17'] = x_version_regression__mutmut_17 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_18'] = x_version_regression__mutmut_18 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_19'] = x_version_regression__mutmut_19 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_20'] = x_version_regression__mutmut_20 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_21'] = x_version_regression__mutmut_21 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_22'] = x_version_regression__mutmut_22 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_23'] = x_version_regression__mutmut_23 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_24'] = x_version_regression__mutmut_24 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_25'] = x_version_regression__mutmut_25 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_26'] = x_version_regression__mutmut_26 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_27'] = x_version_regression__mutmut_27 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_28'] = x_version_regression__mutmut_28 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_29'] = x_version_regression__mutmut_29 # type: ignore # mutmut generated
mutants_x_version_regression__mutmut['x_version_regression__mutmut_30'] = x_version_regression__mutmut_30 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(version_regression)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(version_regression)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
