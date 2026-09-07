"""MCP tool: tls_certificate_diagnosis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.tls_certificate_diagnosis_use_case import (  # noqa: E501
    TLSCertificateDiagnosisUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_tls_certificate_diagnosis__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_tls_certificate_diagnosis__mutmut)
def tls_certificate_diagnosis(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_orig(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_1(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = None  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_2(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=None)  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_3(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_4(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            None
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_5(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=None, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_6(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=None)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_7(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_8(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_9(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_10(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_tls_certificate_diagnosis__mutmut_11(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_tls_certificate_diagnosis__mutmut_12(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_tls_certificate_diagnosis__mutmut_13(ingress_name: str, namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = TLSCertificateDiagnosisUseCase(port=build_k8s_adapter())  # type: ignore
        _ = use_case.execute(
            TLSCertificateDiagnosisCommand(ingress_name=ingress_name, namespace=namespace)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_tls_certificate_diagnosis__mutmut['_mutmut_orig'] = x_tls_certificate_diagnosis__mutmut_orig # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_1'] = x_tls_certificate_diagnosis__mutmut_1 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_2'] = x_tls_certificate_diagnosis__mutmut_2 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_3'] = x_tls_certificate_diagnosis__mutmut_3 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_4'] = x_tls_certificate_diagnosis__mutmut_4 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_5'] = x_tls_certificate_diagnosis__mutmut_5 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_6'] = x_tls_certificate_diagnosis__mutmut_6 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_7'] = x_tls_certificate_diagnosis__mutmut_7 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_8'] = x_tls_certificate_diagnosis__mutmut_8 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_9'] = x_tls_certificate_diagnosis__mutmut_9 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_10'] = x_tls_certificate_diagnosis__mutmut_10 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_11'] = x_tls_certificate_diagnosis__mutmut_11 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_12'] = x_tls_certificate_diagnosis__mutmut_12 # type: ignore # mutmut generated
mutants_x_tls_certificate_diagnosis__mutmut['x_tls_certificate_diagnosis__mutmut_13'] = x_tls_certificate_diagnosis__mutmut_13 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(tls_certificate_diagnosis)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(tls_certificate_diagnosis)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
