"""MCP tool: certs_issuers_list — List all Issuers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.certs_issuers_list.certs_issuers_list_use_case import (  # noqa: E501
    CertsIssuersListUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_issuers_list.command import (
    CertsIssuersListCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_certs_issuers_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_certs_issuers_list__mutmut)
def certs_issuers_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = None
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = None  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=None)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = None
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(None)
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=None))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"XXissuersXX": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"ISSUERS": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "XXerrorXX": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "ERROR": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"XXissuersXX": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"ISSUERS": [], "error": str(exc)}


def x_certs_issuers_list__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "XXerrorXX": str(exc)}


def x_certs_issuers_list__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "ERROR": str(exc)}


def x_certs_issuers_list__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cert_manager_adapter

    try:
        adapter = build_cert_manager_adapter()
        use_case = CertsIssuersListUseCase(cert_manager_port=adapter)  # type: ignore
        response = use_case.execute(CertsIssuersListCommand(namespace=namespace))
        return {"issuers": response.issuers, "error": response.error}
    except Exception as exc:
        return {"issuers": [], "error": str(None)}

mutants_x_certs_issuers_list__mutmut['_mutmut_orig'] = x_certs_issuers_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_1'] = x_certs_issuers_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_2'] = x_certs_issuers_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_3'] = x_certs_issuers_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_4'] = x_certs_issuers_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_5'] = x_certs_issuers_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_6'] = x_certs_issuers_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_7'] = x_certs_issuers_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_8'] = x_certs_issuers_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_9'] = x_certs_issuers_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_10'] = x_certs_issuers_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_11'] = x_certs_issuers_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_12'] = x_certs_issuers_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_13'] = x_certs_issuers_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_14'] = x_certs_issuers_list__mutmut_14 # type: ignore # mutmut generated
mutants_x_certs_issuers_list__mutmut['x_certs_issuers_list__mutmut_15'] = x_certs_issuers_list__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuers_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(certs_issuers_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
