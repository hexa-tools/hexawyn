"""MCP tool: sensitive_data_audit — Audit access to sensitive endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.sensitive_data_audit.command import (
    SensitiveDataAuditCommand,
)
from hexawyn.application.use_case.security.sensitive_data_audit.sensitive_data_audit_use_case import (  # noqa: E501
    SensitiveDataAuditUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_sensitive_data_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_sensitive_data_audit__mutmut)
def sensitive_data_audit(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_orig(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_1(
    pattern: str, time_window_minutes: int = 11, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_2(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = None
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_3(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(None)] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_4(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split("XX,XX")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_5(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = None
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_6(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = None
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_7(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            None
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_8(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=None).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_9(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=None, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_10(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=None, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_11(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=None
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_12(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_13(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_14(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_15(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "XXpatternXX": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_16(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "PATTERN": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_17(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "XXtotal_matchesXX": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_18(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "TOTAL_MATCHES": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_19(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "XXflaggedXX": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_20(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "FLAGGED": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_21(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "XXunflaggedXX": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_22(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "UNFLAGGED": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_23(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "XXalert_levelXX": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_24(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "ALERT_LEVEL": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_25(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "XXerrorXX": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_26(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "ERROR": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_27(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"XXpatternXX": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_28(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"PATTERN": pattern, "error": str(exc)}


def x_sensitive_data_audit__mutmut_29(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "XXerrorXX": str(exc)}


def x_sensitive_data_audit__mutmut_30(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "ERROR": str(exc)}


def x_sensitive_data_audit__mutmut_31(
    pattern: str, time_window_minutes: int = 10, allowlist: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_compliance_audit_adapter

    try:
        lst = [s.strip() for s in allowlist.split(",")] if allowlist else []
        a = build_compliance_audit_adapter()
        r = SensitiveDataAuditUseCase(port=a).execute(
            SensitiveDataAuditCommand(
                pattern=pattern, time_window_minutes=time_window_minutes, allowlist=lst
            )
        )
        return {
            "pattern": r.pattern,
            "total_matches": r.total_matches,
            "flagged": r.flagged,
            "unflagged": r.unflagged,
            "alert_level": r.alert_level,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"pattern": pattern, "error": str(None)}

mutants_x_sensitive_data_audit__mutmut['_mutmut_orig'] = x_sensitive_data_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_1'] = x_sensitive_data_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_2'] = x_sensitive_data_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_3'] = x_sensitive_data_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_4'] = x_sensitive_data_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_5'] = x_sensitive_data_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_6'] = x_sensitive_data_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_7'] = x_sensitive_data_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_8'] = x_sensitive_data_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_9'] = x_sensitive_data_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_10'] = x_sensitive_data_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_11'] = x_sensitive_data_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_12'] = x_sensitive_data_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_13'] = x_sensitive_data_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_14'] = x_sensitive_data_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_15'] = x_sensitive_data_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_16'] = x_sensitive_data_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_17'] = x_sensitive_data_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_18'] = x_sensitive_data_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_19'] = x_sensitive_data_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_20'] = x_sensitive_data_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_21'] = x_sensitive_data_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_22'] = x_sensitive_data_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_23'] = x_sensitive_data_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_24'] = x_sensitive_data_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_25'] = x_sensitive_data_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_26'] = x_sensitive_data_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_27'] = x_sensitive_data_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_28'] = x_sensitive_data_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_29'] = x_sensitive_data_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_30'] = x_sensitive_data_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_sensitive_data_audit__mutmut['x_sensitive_data_audit__mutmut_31'] = x_sensitive_data_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(sensitive_data_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(sensitive_data_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
