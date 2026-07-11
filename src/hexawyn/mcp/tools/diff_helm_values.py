"""MCP tool: diff_helm_values — compares effective Helm values between two
environments (e.g. staging vs production), grouped by impact severity."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.use_case.diff_helm_values.diff_helm_values_use_case import (
    DiffHelmValuesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.helm_values_diff import ValueDiff


def diff_helm_values(
    release: str,
    source_namespace: str,
    target_namespace: str,
    source_env: str = "staging",
    target_env: str = "production",
) -> dict[str, object]:
    """Diff the effective Helm values of a release between two environments.

    Retrieves the effective values (helm get values -a) for the release in the
    source and target namespaces, computes a structured diff grouped by impact
    (critical / warning / informational), redacts secret values, flags type
    mismatches, and suggests which differences could explain behaviour gaps.
    """
    from hexawyn.application.service.diff_helm_values_service import (
        DiffHelmValuesService,
    )
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        adapter = build_helm_values_diff_adapter()
        service = DiffHelmValuesService(helm_values_port=adapter)
        use_case = DiffHelmValuesUseCase(service=service)
        response = use_case.execute(
            DiffHelmValuesCommand(
                release=release,
                source_namespace=source_namespace,
                target_namespace=target_namespace,
                source_env=source_env,
                target_env=target_env,
            )
        )
        report = response.result
        return {
            "release": report.release,
            "source_env": report.source_env,
            "target_env": report.target_env,
            "in_sync": report.in_sync,
            "total_differences": report.total_differences,
            "critical": [_serialize(diff) for diff in report.critical],
            "warning": [_serialize(diff) for diff in report.warning],
            "informational": [_serialize(diff) for diff in report.informational],
            "error": None,
        }
    except Exception as exc:
        return {
            "release": release,
            "source_env": source_env,
            "target_env": target_env,
            "in_sync": False,
            "total_differences": 0,
            "critical": [],
            "warning": [],
            "informational": [],
            "error": str(exc),
        }


def _serialize(diff: ValueDiff) -> dict[str, object]:
    return {
        "key_path": diff.key_path,
        "source_value": diff.source_value,
        "target_value": diff.target_value,
        "change_type": diff.change_type,
        "severity": diff.severity,
        "is_secret": diff.is_secret,
        "type_mismatch": diff.type_mismatch,
        "suggestion": diff.suggestion,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(diff_helm_values)
