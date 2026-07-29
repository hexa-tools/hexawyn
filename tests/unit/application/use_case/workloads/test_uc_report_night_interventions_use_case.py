from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.report_night_interventions.command import (
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.workloads.report_night_interventions.report_night_interventions_use_case import (  # noqa: E501
    ReportNightInterventionsUseCase,
)
from hexawyn.application.use_case.workloads.report_night_interventions.response import (
    ReportNightInterventionsResponse,
)


class TestReportNightInterventionsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_night_intervention_data.return_value = []
        use_case = ReportNightInterventionsUseCase(workload_port=port)
        result = use_case.execute(ReportNightInterventionsCommand())
        assert isinstance(result, ReportNightInterventionsResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.get_night_intervention_data.return_value = []
        use_case = ReportNightInterventionsUseCase(workload_port=port)
        result = use_case.execute(ReportNightInterventionsCommand())
        assert isinstance(result, ReportNightInterventionsResponse)
