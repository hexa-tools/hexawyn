"""MCP tool: get_quota_usage — Get current quota usage."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.get_quota_usage.command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_quota_usage() -> dict[str, object]:
    from hexawyn.mcp.server import build_pricing_plan_adapter, build_usage_meter_adapter

    try:
        use_case = GetQuotaUsageUseCase(
            plan_port=build_pricing_plan_adapter(),
            usage_meter=build_usage_meter_adapter(),
        )
        response = use_case.execute(GetQuotaUsageCommand())
        quotas_list = [
            {
                "resource": quota.resource,
                "used": quota.used,
                "limit": quota.limit,
                "state": quota.state,
                "available_from_tier": quota.available_from_tier,
            }
            for quota in response.quotas
        ]
        return {
            "quotas": quotas_list,
            "investigations_used": response.investigations_used,
            "investigations_limit": response.investigations_limit,
            "error": None,
        }
    except Exception as exc:
        return {
            "quotas": [],
            "investigations_used": 0,
            "investigations_limit": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_quota_usage)
