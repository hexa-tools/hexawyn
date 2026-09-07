"""MCP tool: certs_status_explain — Explain in natural language why a cert is failing."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.certs_status_explain.certs_status_explain_use_case import (  # noqa: E501
    CertsStatusExplainUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_status_explain.command import (
    CertsStatusExplainCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_certs_status_explain__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_certs_status_explain__mutmut)
def certs_status_explain(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_orig(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_1(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = None
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_2(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = None  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_3(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=None)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_4(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = None
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_5(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(None)
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_6(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=None, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_7(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=None))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_8(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_9(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, ))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_10(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "XXstatusXX": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_11(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "STATUS": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_12(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "XXmessageXX": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_13(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "MESSAGE": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_14(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "XXexplanationXX": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_15(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "EXPLANATION": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_16(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "XXfix_suggestionXX": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_17(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "FIX_SUGGESTION": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_18(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_19(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_20(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "XXstatusXX": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_21(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "STATUS": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_22(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "XXunknownXX",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_23(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "UNKNOWN",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_24(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "XXmessageXX": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_25(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "MESSAGE": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_26(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "XXexplanationXX": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_27(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "EXPLANATION": "",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_28(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "XXXX",
            "fix_suggestion": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_29(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "XXfix_suggestionXX": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_30(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "FIX_SUGGESTION": "",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_31(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "XXXX",
            "error": str(exc),
        }


def x_certs_status_explain__mutmut_32(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "XXerrorXX": str(exc),
        }


def x_certs_status_explain__mutmut_33(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "ERROR": str(exc),
        }


def x_certs_status_explain__mutmut_34(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsStatusExplainUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsStatusExplainCommand(name=name, namespace=namespace))
        return {
            "status": r.status,
            "message": r.message,
            "explanation": r.explanation,
            "fix_suggestion": r.fix_suggestion,
            "error": r.error,
        }
    except Exception as exc:
        return {
            "status": "unknown",
            "message": None,
            "explanation": "",
            "fix_suggestion": "",
            "error": str(None),
        }

mutants_x_certs_status_explain__mutmut['_mutmut_orig'] = x_certs_status_explain__mutmut_orig # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_1'] = x_certs_status_explain__mutmut_1 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_2'] = x_certs_status_explain__mutmut_2 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_3'] = x_certs_status_explain__mutmut_3 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_4'] = x_certs_status_explain__mutmut_4 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_5'] = x_certs_status_explain__mutmut_5 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_6'] = x_certs_status_explain__mutmut_6 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_7'] = x_certs_status_explain__mutmut_7 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_8'] = x_certs_status_explain__mutmut_8 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_9'] = x_certs_status_explain__mutmut_9 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_10'] = x_certs_status_explain__mutmut_10 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_11'] = x_certs_status_explain__mutmut_11 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_12'] = x_certs_status_explain__mutmut_12 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_13'] = x_certs_status_explain__mutmut_13 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_14'] = x_certs_status_explain__mutmut_14 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_15'] = x_certs_status_explain__mutmut_15 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_16'] = x_certs_status_explain__mutmut_16 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_17'] = x_certs_status_explain__mutmut_17 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_18'] = x_certs_status_explain__mutmut_18 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_19'] = x_certs_status_explain__mutmut_19 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_20'] = x_certs_status_explain__mutmut_20 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_21'] = x_certs_status_explain__mutmut_21 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_22'] = x_certs_status_explain__mutmut_22 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_23'] = x_certs_status_explain__mutmut_23 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_24'] = x_certs_status_explain__mutmut_24 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_25'] = x_certs_status_explain__mutmut_25 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_26'] = x_certs_status_explain__mutmut_26 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_27'] = x_certs_status_explain__mutmut_27 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_28'] = x_certs_status_explain__mutmut_28 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_29'] = x_certs_status_explain__mutmut_29 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_30'] = x_certs_status_explain__mutmut_30 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_31'] = x_certs_status_explain__mutmut_31 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_32'] = x_certs_status_explain__mutmut_32 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_33'] = x_certs_status_explain__mutmut_33 # type: ignore # mutmut generated
mutants_x_certs_status_explain__mutmut['x_certs_status_explain__mutmut_34'] = x_certs_status_explain__mutmut_34 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_status_explain)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(certs_status_explain)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
