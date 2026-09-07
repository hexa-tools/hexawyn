"""MCP tool: check_disruption_risks — predicted service disruption risks."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.check_disruption_risks.check_disruption_risks_use_case import (  # noqa: E501
    CheckDisruptionRisksUseCase,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.command import (
    CheckDisruptionRisksCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.disruption_risk import RiskEvent


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_check_disruption_risks__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_disruption_risks__mutmut)
def check_disruption_risks(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_orig(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_1(warning_days: int = 8) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_2(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = None
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_3(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = None
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_4(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=None)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_5(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = None  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_6(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=None)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_7(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = None
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_8(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(None)
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_9(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=None))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_10(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = None
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_11(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "XXperiod_labelXX": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_12(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "PERIOD_LABEL": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_13(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "XXhas_risksXX": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_14(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "HAS_RISKS": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_15(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "XXhas_dataXX": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_16(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "HAS_DATA": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_17(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "XXrisksXX": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_18(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "RISKS": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_19(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(None) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_20(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "XXwarningXX": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_21(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "WARNING": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_22(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_23(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_24(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXperiod_labelXX": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_25(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "PERIOD_LABEL": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_26(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "XXSemaine en coursXX",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_27(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_28(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "SEMAINE EN COURS",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_29(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "XXhas_risksXX": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_30(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "HAS_RISKS": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_31(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": True,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_32(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "XXhas_dataXX": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_33(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "HAS_DATA": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_34(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": True,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_35(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "XXrisksXX": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_36(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "RISKS": [],
            "warning": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_37(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "XXwarningXX": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_38(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "WARNING": "",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_39(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "XXXX",
            "error": str(exc),
        }


def x_check_disruption_risks__mutmut_40(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "XXerrorXX": str(exc),
        }


def x_check_disruption_risks__mutmut_41(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "ERROR": str(exc),
        }


def x_check_disruption_risks__mutmut_42(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksUseCase(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)  # type: ignore
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(None),
        }

mutants_x_check_disruption_risks__mutmut['_mutmut_orig'] = x_check_disruption_risks__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_1'] = x_check_disruption_risks__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_2'] = x_check_disruption_risks__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_3'] = x_check_disruption_risks__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_4'] = x_check_disruption_risks__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_5'] = x_check_disruption_risks__mutmut_5 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_6'] = x_check_disruption_risks__mutmut_6 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_7'] = x_check_disruption_risks__mutmut_7 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_8'] = x_check_disruption_risks__mutmut_8 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_9'] = x_check_disruption_risks__mutmut_9 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_10'] = x_check_disruption_risks__mutmut_10 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_11'] = x_check_disruption_risks__mutmut_11 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_12'] = x_check_disruption_risks__mutmut_12 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_13'] = x_check_disruption_risks__mutmut_13 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_14'] = x_check_disruption_risks__mutmut_14 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_15'] = x_check_disruption_risks__mutmut_15 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_16'] = x_check_disruption_risks__mutmut_16 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_17'] = x_check_disruption_risks__mutmut_17 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_18'] = x_check_disruption_risks__mutmut_18 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_19'] = x_check_disruption_risks__mutmut_19 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_20'] = x_check_disruption_risks__mutmut_20 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_21'] = x_check_disruption_risks__mutmut_21 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_22'] = x_check_disruption_risks__mutmut_22 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_23'] = x_check_disruption_risks__mutmut_23 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_24'] = x_check_disruption_risks__mutmut_24 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_25'] = x_check_disruption_risks__mutmut_25 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_26'] = x_check_disruption_risks__mutmut_26 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_27'] = x_check_disruption_risks__mutmut_27 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_28'] = x_check_disruption_risks__mutmut_28 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_29'] = x_check_disruption_risks__mutmut_29 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_30'] = x_check_disruption_risks__mutmut_30 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_31'] = x_check_disruption_risks__mutmut_31 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_32'] = x_check_disruption_risks__mutmut_32 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_33'] = x_check_disruption_risks__mutmut_33 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_34'] = x_check_disruption_risks__mutmut_34 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_35'] = x_check_disruption_risks__mutmut_35 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_36'] = x_check_disruption_risks__mutmut_36 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_37'] = x_check_disruption_risks__mutmut_37 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_38'] = x_check_disruption_risks__mutmut_38 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_39'] = x_check_disruption_risks__mutmut_39 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_40'] = x_check_disruption_risks__mutmut_40 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_41'] = x_check_disruption_risks__mutmut_41 # type: ignore # mutmut generated
mutants_x_check_disruption_risks__mutmut['x_check_disruption_risks__mutmut_42'] = x_check_disruption_risks__mutmut_42 # type: ignore # mutmut generated
mutants_x__serialize__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__serialize__mutmut)
def _serialize(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_orig(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_1(risk: RiskEvent) -> dict[str, object]:
    return {
        "XXbusiness_service_nameXX": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_2(risk: RiskEvent) -> dict[str, object]:
    return {
        "BUSINESS_SERVICE_NAME": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_3(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "XXrisk_typeXX": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_4(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "RISK_TYPE": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_5(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "XXpredicted_dateXX": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_6(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "PREDICTED_DATE": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_7(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "XXdays_from_nowXX": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_8(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "DAYS_FROM_NOW": risk.days_from_now,
        "detail": risk.detail,
    }


def x__serialize__mutmut_9(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "XXdetailXX": risk.detail,
    }


def x__serialize__mutmut_10(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "DETAIL": risk.detail,
    }

mutants_x__serialize__mutmut['_mutmut_orig'] = x__serialize__mutmut_orig # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_1'] = x__serialize__mutmut_1 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_2'] = x__serialize__mutmut_2 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_3'] = x__serialize__mutmut_3 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_4'] = x__serialize__mutmut_4 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_5'] = x__serialize__mutmut_5 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_6'] = x__serialize__mutmut_6 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_7'] = x__serialize__mutmut_7 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_8'] = x__serialize__mutmut_8 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_9'] = x__serialize__mutmut_9 # type: ignore # mutmut generated
mutants_x__serialize__mutmut['x__serialize__mutmut_10'] = x__serialize__mutmut_10 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(check_disruption_risks)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(check_disruption_risks)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
