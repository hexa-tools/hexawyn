"""MCP tool: certs_get — Get detailed status of a specific certificate."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.certs_get.certs_get_use_case import CertsGetUseCase
from hexawyn.application.use_case.cert_manager.certs_get.command import CertsGetCommand

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_certs_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_certs_get__mutmut)
def certs_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_orig(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_1(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = None
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_2(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = None  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_3(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=None)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_4(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = None
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_5(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(None)
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_6(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=None, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_7(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=None))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_8(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_9(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, ))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_10(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "XXnameXX": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_11(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "NAME": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_12(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "XXnamespaceXX": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_13(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "NAMESPACE": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_14(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "XXstatusXX": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_15(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "STATUS": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_16(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "XXissuer_nameXX": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_17(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "ISSUER_NAME": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_18(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "XXissuer_typeXX": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_19(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "ISSUER_TYPE": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_20(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "XXdns_namesXX": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_21(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "DNS_NAMES": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_22(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "XXnot_beforeXX": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_23(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "NOT_BEFORE": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_24(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "XXnot_afterXX": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_25(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "NOT_AFTER": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_26(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "XXdays_until_expiryXX": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_27(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "DAYS_UNTIL_EXPIRY": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_28(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "XXrenewal_timeXX": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_29(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "RENEWAL_TIME": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_30(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "XXauto_renewXX": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_31(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "AUTO_RENEW": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_32(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "XXmessageXX": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_33(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "MESSAGE": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_34(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_35(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_36(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXnameXX": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_37(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"NAME": "", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_38(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "XXXX", "namespace": "", "error": str(exc)}


def x_certs_get__mutmut_39(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "XXnamespaceXX": "", "error": str(exc)}


def x_certs_get__mutmut_40(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "NAMESPACE": "", "error": str(exc)}


def x_certs_get__mutmut_41(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "XXXX", "error": str(exc)}


def x_certs_get__mutmut_42(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "XXerrorXX": str(exc)}


def x_certs_get__mutmut_43(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "ERROR": str(exc)}


def x_certs_get__mutmut_44(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        uc = CertsGetUseCase(cert_manager_port=adapter)  # type: ignore
        r = uc.execute(CertsGetCommand(name=name, namespace=namespace))
        return {
            "name": r.name,
            "namespace": r.namespace,
            "status": r.status,
            "issuer_name": r.issuer_name,
            "issuer_type": r.issuer_type,
            "dns_names": r.dns_names,
            "not_before": r.not_before,
            "not_after": r.not_after,
            "days_until_expiry": r.days_until_expiry,
            "renewal_time": r.renewal_time,
            "auto_renew": r.auto_renew,
            "message": r.message,
            "error": r.error,
        }
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(None)}

mutants_x_certs_get__mutmut['_mutmut_orig'] = x_certs_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_1'] = x_certs_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_2'] = x_certs_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_3'] = x_certs_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_4'] = x_certs_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_5'] = x_certs_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_6'] = x_certs_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_7'] = x_certs_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_8'] = x_certs_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_9'] = x_certs_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_10'] = x_certs_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_11'] = x_certs_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_12'] = x_certs_get__mutmut_12 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_13'] = x_certs_get__mutmut_13 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_14'] = x_certs_get__mutmut_14 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_15'] = x_certs_get__mutmut_15 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_16'] = x_certs_get__mutmut_16 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_17'] = x_certs_get__mutmut_17 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_18'] = x_certs_get__mutmut_18 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_19'] = x_certs_get__mutmut_19 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_20'] = x_certs_get__mutmut_20 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_21'] = x_certs_get__mutmut_21 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_22'] = x_certs_get__mutmut_22 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_23'] = x_certs_get__mutmut_23 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_24'] = x_certs_get__mutmut_24 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_25'] = x_certs_get__mutmut_25 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_26'] = x_certs_get__mutmut_26 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_27'] = x_certs_get__mutmut_27 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_28'] = x_certs_get__mutmut_28 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_29'] = x_certs_get__mutmut_29 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_30'] = x_certs_get__mutmut_30 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_31'] = x_certs_get__mutmut_31 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_32'] = x_certs_get__mutmut_32 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_33'] = x_certs_get__mutmut_33 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_34'] = x_certs_get__mutmut_34 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_35'] = x_certs_get__mutmut_35 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_36'] = x_certs_get__mutmut_36 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_37'] = x_certs_get__mutmut_37 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_38'] = x_certs_get__mutmut_38 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_39'] = x_certs_get__mutmut_39 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_40'] = x_certs_get__mutmut_40 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_41'] = x_certs_get__mutmut_41 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_42'] = x_certs_get__mutmut_42 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_43'] = x_certs_get__mutmut_43 # type: ignore # mutmut generated
mutants_x_certs_get__mutmut['x_certs_get__mutmut_44'] = x_certs_get__mutmut_44 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(certs_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
