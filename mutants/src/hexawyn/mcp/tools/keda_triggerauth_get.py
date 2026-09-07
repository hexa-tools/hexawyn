"""keda_triggerauth_get.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda.keda_triggerauth_get.command import KedaTriggerauthGetCommand
from hexawyn.application.use_case.keda.keda_triggerauth_get.keda_triggerauth_get_use_case import (
    KedaTriggerauthGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_keda_triggerauth_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_keda_triggerauth_get__mutmut)
def keda_triggerauth_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_orig(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_1(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = None
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_2(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = None
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_3(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=None)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_4(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = None
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_5(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(None)
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_6(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(None, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_7(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, None))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_8(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_9(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, ))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_triggerauth_get__mutmut_10(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_keda_triggerauth_get__mutmut_11(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_keda_triggerauth_get__mutmut_12(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        uc = KedaTriggerauthGetUseCase(port=a)
        r = uc.execute(KedaTriggerauthGetCommand(name, namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_keda_triggerauth_get__mutmut['_mutmut_orig'] = x_keda_triggerauth_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_1'] = x_keda_triggerauth_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_2'] = x_keda_triggerauth_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_3'] = x_keda_triggerauth_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_4'] = x_keda_triggerauth_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_5'] = x_keda_triggerauth_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_6'] = x_keda_triggerauth_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_7'] = x_keda_triggerauth_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_8'] = x_keda_triggerauth_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_9'] = x_keda_triggerauth_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_10'] = x_keda_triggerauth_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_11'] = x_keda_triggerauth_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_keda_triggerauth_get__mutmut['x_keda_triggerauth_get__mutmut_12'] = x_keda_triggerauth_get__mutmut_12 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_triggerauth_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(keda_triggerauth_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
