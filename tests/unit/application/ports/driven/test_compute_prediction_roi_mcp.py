"""RED → GREEN — MCP tool: compute_prediction_roi."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PredictionRoiPort,
    PreventedIncidentRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _detection(
    ref: str = "PRED-1",
    downtime: int = 120,
    prevented: bool = True,
) -> PreventedIncidentRaw:
    return PreventedIncidentRaw(
        incident_ref=ref,
        business_service_name="Service Paiement",
        detected_at="2026-06-10",
        avoided_downtime_minutes=downtime,
        confidence_pct=90.0,
        prevented=prevented,
    )


def _data(
    detections: list[PreventedIncidentRaw] | None = None,
    revenue: float | None = 500.0,
    infra: float = 2000.0,
) -> PredictionRoiData:
    return PredictionRoiData(
        detections=detections if detections is not None else [],
        infrastructure_cost_eur=infra,
        revenue_per_minute=revenue,
    )


def _port(data: PredictionRoiData) -> MagicMock:
    port = MagicMock(spec=PredictionRoiPort)
    port.get_prediction_roi_data.return_value = data
    return port


class TestComputePredictionRoiTool:
    def test_demo_scenario(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_prediction_roi_adapter",
            return_value=_port(
                _data(
                    detections=[
                        _detection("a", downtime=120),
                        _detection("b", prevented=False),
                        _detection("c", prevented=False),
                        _detection("d", prevented=False),
                    ]
                )
            ),
        ):
            from hexawyn.mcp.tools.compute_prediction_roi import compute_prediction_roi

            result = compute_prediction_roi(period="2026-06")

        assert result["detected_count"] == 4
        assert result["prevented_incident_count"] == 1
        assert result["avoided_downtime_minutes"] == 120
        assert result["total_avoided_cost_eur"] == 60000.0
        assert result["roi_eur"] == 58000.0
        assert result["error"] is None

    def test_ticket_major_prevented(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_prediction_roi_adapter",
            return_value=_port(
                _data(
                    detections=[
                        _detection("a", downtime=360),
                        _detection("b", prevented=False),
                        _detection("c", prevented=False),
                        _detection("d", prevented=False),
                    ],
                    infra=0.0,
                )
            ),
        ):
            from hexawyn.mcp.tools.compute_prediction_roi import compute_prediction_roi

            result = compute_prediction_roi(period="2026-06")

        assert result["total_avoided_cost_eur"] == 180000.0
        assert result["prevented_incidents"][0]["incident_ref"] == "a"

    def test_missing_revenue_no_amount(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_prediction_roi_adapter",
            return_value=_port(_data(detections=[_detection(prevented=False)], revenue=None)),
        ):
            from hexawyn.mcp.tools.compute_prediction_roi import compute_prediction_roi

            result = compute_prediction_roi(period="2026-06")

        assert result["config_available"] is False
        assert result["total_avoided_cost_eur"] is None

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_prediction_roi_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_prediction_roi import compute_prediction_roi

            result = compute_prediction_roi(period="2026-06")

        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_prediction_roi import register

        assert callable(register)
