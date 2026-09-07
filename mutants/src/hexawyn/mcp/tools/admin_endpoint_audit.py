"""MCP tool: admin_endpoint_audit — Audit admin endpoints for security breaches."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.admin_endpoint_audit.admin_endpoint_audit_use_case import (  # noqa: E501
    AdminEndpointAuditUseCase,
)
from hexawyn.application.use_case.security.admin_endpoint_audit.command import (
    AdminEndpointAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_admin_endpoint_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_admin_endpoint_audit__mutmut)
def admin_endpoint_audit(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_orig(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_1(
    endpoint_pattern: str = "XX/adminXX",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_2(
    endpoint_pattern: str = "/ADMIN",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_3(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 31,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_4(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 6,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_5(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = None
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_6(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=None)
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_7(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = None
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_8(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            None
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_9(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=None,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_10(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=None,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_11(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=None,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_12(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_13(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_14(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_15(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "XXendpoint_patternXX": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_16(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "ENDPOINT_PATTERN": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_17(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "XXtotal_requestsXX": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_18(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "TOTAL_REQUESTS": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_19(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "XXtotal_403sXX": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_20(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "TOTAL_403S": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_21(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "XXrate_403_pctXX": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_22(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "RATE_403_PCT": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_23(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "XXflagged_callersXX": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_24(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "FLAGGED_CALLERS": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_25(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_26(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "ERROR": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_27(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"XXendpoint_patternXX": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_28(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"ENDPOINT_PATTERN": endpoint_pattern, "error": str(exc)}


def x_admin_endpoint_audit__mutmut_29(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "XXerrorXX": str(exc)}


def x_admin_endpoint_audit__mutmut_30(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "ERROR": str(exc)}


def x_admin_endpoint_audit__mutmut_31(
    endpoint_pattern: str = "/admin",
    time_window_minutes: int = 30,
    flag_threshold: int = 5,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_security_audit_adapter

    try:
        use_case = AdminEndpointAuditUseCase(port=build_security_audit_adapter())
        r = use_case.execute(
            AdminEndpointAuditCommand(
                endpoint_pattern=endpoint_pattern,
                time_window_minutes=time_window_minutes,
                flag_threshold=flag_threshold,
            )
        )
        return {
            "endpoint_pattern": r.endpoint_pattern,
            "total_requests": r.total_requests,
            "total_403s": r.total_403s,
            "rate_403_pct": r.rate_403_pct,
            "flagged_callers": r.flagged_callers,
            "error": None,
        }
    except Exception as exc:
        return {"endpoint_pattern": endpoint_pattern, "error": str(None)}

mutants_x_admin_endpoint_audit__mutmut['_mutmut_orig'] = x_admin_endpoint_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_1'] = x_admin_endpoint_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_2'] = x_admin_endpoint_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_3'] = x_admin_endpoint_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_4'] = x_admin_endpoint_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_5'] = x_admin_endpoint_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_6'] = x_admin_endpoint_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_7'] = x_admin_endpoint_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_8'] = x_admin_endpoint_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_9'] = x_admin_endpoint_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_10'] = x_admin_endpoint_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_11'] = x_admin_endpoint_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_12'] = x_admin_endpoint_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_13'] = x_admin_endpoint_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_14'] = x_admin_endpoint_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_15'] = x_admin_endpoint_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_16'] = x_admin_endpoint_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_17'] = x_admin_endpoint_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_18'] = x_admin_endpoint_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_19'] = x_admin_endpoint_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_20'] = x_admin_endpoint_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_21'] = x_admin_endpoint_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_22'] = x_admin_endpoint_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_23'] = x_admin_endpoint_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_24'] = x_admin_endpoint_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_25'] = x_admin_endpoint_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_26'] = x_admin_endpoint_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_27'] = x_admin_endpoint_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_28'] = x_admin_endpoint_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_29'] = x_admin_endpoint_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_30'] = x_admin_endpoint_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_admin_endpoint_audit__mutmut['x_admin_endpoint_audit__mutmut_31'] = x_admin_endpoint_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(admin_endpoint_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(admin_endpoint_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
