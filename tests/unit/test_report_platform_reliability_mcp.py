"""RED → GREEN — MCP tool: report_platform_reliability."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
    ReliabilityData,
    ReliabilityIncidentRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _incident(
    severity: str = "minor",
    downtime: int = 12,
    resolution: int = 12,
    rc: str = "",
) -> ReliabilityIncidentRaw:
    return ReliabilityIncidentRaw(
        date="2026-06-14",
        severity=severity,
        downtime_minutes=downtime,
        resolution_minutes=resolution,
        root_cause=rc,
        resolved=True,
        planned_maintenance=False,
    )


def _data(
    incidents: list[ReliabilityIncidentRaw] | None = None,
    previous_avg: int | None = None,
    cost_per_minute: float | None = None,
) -> ReliabilityData:
    return ReliabilityData(
        period_minutes=43200,
        incidents=incidents if incidents is not None else [],
        previous_avg_resolution_minutes=previous_avg,
        cost_per_downtime_minute_eur=cost_per_minute,
    )


def _port(data: ReliabilityData) -> MagicMock:
    port = MagicMock(spec=PlatformReliabilityPort)
    port.get_reliability_data.return_value = data
    return port


class TestReportPlatformReliabilityTool:
    def test_healthy_month(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            return_value=_port(_data()),
        ):
            from hexawyn.mcp.tools.report_platform_reliability import (
                report_platform_reliability,
            )

            result = report_platform_reliability(period="2026-06")

        assert result["uptime_pct"] == 100.0
        assert result["total_incidents"] == 0
        assert "Aucun incident" in result["executive_summary"]
        assert result["error"] is None

    def test_two_minor_incidents(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            return_value=_port(
                _data(
                    incidents=[
                        _incident(downtime=15, resolution=10),
                        _incident(downtime=45, resolution=14),
                    ],
                    previous_avg=14,
                    cost_per_minute=0.0,
                )
            ),
        ):
            from hexawyn.mcp.tools.report_platform_reliability import (
                report_platform_reliability,
            )

            result = report_platform_reliability(period="2026-06")

        assert result["minor_count"] == 2
        assert result["avg_resolution_minutes"] == 12
        assert result["financial_impact_eur"] == 0.0

    def test_major_incident(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            return_value=_port(
                _data(
                    incidents=[
                        _incident(severity="major", downtime=120, resolution=120, rc="Panne base")
                    ]
                )
            ),
        ):
            from hexawyn.mcp.tools.report_platform_reliability import (
                report_platform_reliability,
            )

            result = report_platform_reliability(period="2026-06")

        assert result["has_major_incident"] is True
        assert result["uptime_pct"] == 99.72

    def test_no_financial_figure_without_pricing(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            return_value=_port(_data(incidents=[_incident(downtime=120)], cost_per_minute=None)),
        ):
            from hexawyn.mcp.tools.report_platform_reliability import (
                report_platform_reliability,
            )

            result = report_platform_reliability(period="2026-06")

        assert result["pricing_configured"] is False
        assert result["financial_impact_eur"] is None
        assert "\u20ac" not in result["executive_summary"]

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.report_platform_reliability import (
                report_platform_reliability,
            )

            result = report_platform_reliability(period="2026-06")

        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.report_platform_reliability import register

        assert callable(register)
