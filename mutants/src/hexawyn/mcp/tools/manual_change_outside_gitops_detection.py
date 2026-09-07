"""MCP tool: manual_change_outside_gitops_detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
    ManualChangeOutsideGitopsCommand,
)
from hexawyn.application.use_case.gitops.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (  # noqa: E501
    ManualChangeOutsideGitopsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_manual_changes_outside_gitops__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_manual_changes_outside_gitops__mutmut)
def detect_manual_changes_outside_gitops(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = None
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=None)
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = None
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            None
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=None)
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace and "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "XXXX")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "XXmanual_changesXX": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "MANUAL_CHANGES": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "XXtotal_manual_changesXX": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "TOTAL_MANUAL_CHANGES": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "XXexcluded_gitops_change_countXX": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "EXCLUDED_GITOPS_CHANGE_COUNT": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "XXused_managed_fields_fallbackXX": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "USED_MANAGED_FIELDS_FALLBACK": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_16(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "XXpartial_windowXX": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_17(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "PARTIAL_WINDOW": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_18(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "XXnotesXX": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_19(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "NOTES": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_20(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_21(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_22(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXmanual_changesXX": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_23(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "MANUAL_CHANGES": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_24(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "XXtotal_manual_changesXX": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_25(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "TOTAL_MANUAL_CHANGES": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_26(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 1,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_27(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "XXexcluded_gitops_change_countXX": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_28(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "EXCLUDED_GITOPS_CHANGE_COUNT": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_29(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 1,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_30(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "XXused_managed_fields_fallbackXX": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_31(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "USED_MANAGED_FIELDS_FALLBACK": False,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_32(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": True,
            "partial_window": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_33(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "XXpartial_windowXX": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_34(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "PARTIAL_WINDOW": False,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_35(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": True,
            "notes": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_36(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "XXnotesXX": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_37(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "NOTES": [],
            "error": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_38(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "XXerrorXX": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_39(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "ERROR": str(exc),
        }


def x_detect_manual_changes_outside_gitops__mutmut_40(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_audit_log_adapter

    try:
        use_case = ManualChangeOutsideGitopsUseCase(audit_port=build_audit_log_adapter())
        response = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace=namespace or "")
        )
        return {
            "manual_changes": response.manual_changes,
            "total_manual_changes": response.total_manual_changes,
            "excluded_gitops_change_count": response.excluded_gitops_change_count,
            "used_managed_fields_fallback": response.used_managed_fields_fallback,
            "partial_window": response.partial_window,
            "notes": response.notes,
            "error": None,
        }
    except Exception as exc:
        return {
            "manual_changes": [],
            "total_manual_changes": 0,
            "excluded_gitops_change_count": 0,
            "used_managed_fields_fallback": False,
            "partial_window": False,
            "notes": [],
            "error": str(None),
        }

mutants_x_detect_manual_changes_outside_gitops__mutmut['_mutmut_orig'] = x_detect_manual_changes_outside_gitops__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_1'] = x_detect_manual_changes_outside_gitops__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_2'] = x_detect_manual_changes_outside_gitops__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_3'] = x_detect_manual_changes_outside_gitops__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_4'] = x_detect_manual_changes_outside_gitops__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_5'] = x_detect_manual_changes_outside_gitops__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_6'] = x_detect_manual_changes_outside_gitops__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_7'] = x_detect_manual_changes_outside_gitops__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_8'] = x_detect_manual_changes_outside_gitops__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_9'] = x_detect_manual_changes_outside_gitops__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_10'] = x_detect_manual_changes_outside_gitops__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_11'] = x_detect_manual_changes_outside_gitops__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_12'] = x_detect_manual_changes_outside_gitops__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_13'] = x_detect_manual_changes_outside_gitops__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_14'] = x_detect_manual_changes_outside_gitops__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_15'] = x_detect_manual_changes_outside_gitops__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_16'] = x_detect_manual_changes_outside_gitops__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_17'] = x_detect_manual_changes_outside_gitops__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_18'] = x_detect_manual_changes_outside_gitops__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_19'] = x_detect_manual_changes_outside_gitops__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_20'] = x_detect_manual_changes_outside_gitops__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_21'] = x_detect_manual_changes_outside_gitops__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_22'] = x_detect_manual_changes_outside_gitops__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_23'] = x_detect_manual_changes_outside_gitops__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_24'] = x_detect_manual_changes_outside_gitops__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_25'] = x_detect_manual_changes_outside_gitops__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_26'] = x_detect_manual_changes_outside_gitops__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_27'] = x_detect_manual_changes_outside_gitops__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_28'] = x_detect_manual_changes_outside_gitops__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_29'] = x_detect_manual_changes_outside_gitops__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_30'] = x_detect_manual_changes_outside_gitops__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_31'] = x_detect_manual_changes_outside_gitops__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_32'] = x_detect_manual_changes_outside_gitops__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_33'] = x_detect_manual_changes_outside_gitops__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_34'] = x_detect_manual_changes_outside_gitops__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_35'] = x_detect_manual_changes_outside_gitops__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_36'] = x_detect_manual_changes_outside_gitops__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_37'] = x_detect_manual_changes_outside_gitops__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_38'] = x_detect_manual_changes_outside_gitops__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_39'] = x_detect_manual_changes_outside_gitops__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_manual_changes_outside_gitops__mutmut['x_detect_manual_changes_outside_gitops__mutmut_40'] = x_detect_manual_changes_outside_gitops__mutmut_40 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_manual_changes_outside_gitops)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_manual_changes_outside_gitops)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
