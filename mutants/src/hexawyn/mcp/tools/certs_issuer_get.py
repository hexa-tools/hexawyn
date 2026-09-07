"""MCP tool: certs_issuer_get — Get detail of a specific Issuer."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.certs_issuer_get.certs_issuer_get_use_case import (
    CertsIssuerGetUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_issuer_get.command import CertsIssuerGetCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_certs_issuer_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_certs_issuer_get__mutmut)
def certs_issuer_get(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_orig(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_1(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = None
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_2(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = None  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_3(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=None)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_4(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = None
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_5(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(None)
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_6(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=None, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_7(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=None))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_8(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_9(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, ))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_10(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "XXnameXX": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_11(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "NAME": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_12(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "XXnamespaceXX": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_13(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "NAMESPACE": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_14(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "XXkindXX": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_15(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "KIND": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_16(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "XXissuer_typeXX": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_17(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "ISSUER_TYPE": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_18(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "XXreadyXX": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_19(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "READY": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_20(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "XXserverXX": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_21(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "SERVER": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_22(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "XXmessageXX": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_23(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "MESSAGE": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_24(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_25(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_26(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXnameXX": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_27(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"NAME": "", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_28(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "XXXX", "namespace": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_29(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "XXnamespaceXX": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_30(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "NAMESPACE": None, "error": str(exc)}


def x_certs_issuer_get__mutmut_31(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "XXerrorXX": str(exc)}


def x_certs_issuer_get__mutmut_32(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "ERROR": str(exc)}


def x_certs_issuer_get__mutmut_33(name: str, namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsIssuerGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsIssuerGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "kind": r.kind,
            "issuer_type": r.issuer_type,
            "ready": r.ready,
            "server": r.server,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": None, "error": str(None)}

mutants_x_certs_issuer_get__mutmut['_mutmut_orig'] = x_certs_issuer_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_1'] = x_certs_issuer_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_2'] = x_certs_issuer_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_3'] = x_certs_issuer_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_4'] = x_certs_issuer_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_5'] = x_certs_issuer_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_6'] = x_certs_issuer_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_7'] = x_certs_issuer_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_8'] = x_certs_issuer_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_9'] = x_certs_issuer_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_10'] = x_certs_issuer_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_11'] = x_certs_issuer_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_12'] = x_certs_issuer_get__mutmut_12 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_13'] = x_certs_issuer_get__mutmut_13 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_14'] = x_certs_issuer_get__mutmut_14 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_15'] = x_certs_issuer_get__mutmut_15 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_16'] = x_certs_issuer_get__mutmut_16 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_17'] = x_certs_issuer_get__mutmut_17 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_18'] = x_certs_issuer_get__mutmut_18 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_19'] = x_certs_issuer_get__mutmut_19 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_20'] = x_certs_issuer_get__mutmut_20 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_21'] = x_certs_issuer_get__mutmut_21 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_22'] = x_certs_issuer_get__mutmut_22 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_23'] = x_certs_issuer_get__mutmut_23 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_24'] = x_certs_issuer_get__mutmut_24 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_25'] = x_certs_issuer_get__mutmut_25 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_26'] = x_certs_issuer_get__mutmut_26 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_27'] = x_certs_issuer_get__mutmut_27 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_28'] = x_certs_issuer_get__mutmut_28 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_29'] = x_certs_issuer_get__mutmut_29 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_30'] = x_certs_issuer_get__mutmut_30 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_31'] = x_certs_issuer_get__mutmut_31 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_32'] = x_certs_issuer_get__mutmut_32 # type: ignore # mutmut generated
mutants_x_certs_issuer_get__mutmut['x_certs_issuer_get__mutmut_33'] = x_certs_issuer_get__mutmut_33 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuer_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuer_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
