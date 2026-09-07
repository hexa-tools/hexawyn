"""MCP tool: detect_privileged_pods."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.detect_privileged_pods.command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.security.detect_privileged_pods.detect_privileged_pods_use_case import (  # noqa: E501
    DetectPrivilegedPodsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_privileged_pods__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_privileged_pods__mutmut)
def detect_privileged_pods() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = None
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=None)
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_privileged_pods__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_detect_privileged_pods__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_detect_privileged_pods__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_detect_privileged_pods__mutmut['_mutmut_orig'] = x_detect_privileged_pods__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_1'] = x_detect_privileged_pods__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_2'] = x_detect_privileged_pods__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_3'] = x_detect_privileged_pods__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_4'] = x_detect_privileged_pods__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_5'] = x_detect_privileged_pods__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_6'] = x_detect_privileged_pods__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_7'] = x_detect_privileged_pods__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_8'] = x_detect_privileged_pods__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_privileged_pods__mutmut['x_detect_privileged_pods__mutmut_9'] = x_detect_privileged_pods__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_privileged_pods)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_privileged_pods)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
