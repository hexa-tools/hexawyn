"""Tests for RunConsolidation service + use case."""

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.run_consolidation.run_consolidation_command import (
    RunConsolidationCommand,
)
from hexawyn.application.ports.driving.run_consolidation.run_consolidation_service_port import (
    RunConsolidationServicePort,
)
from hexawyn.application.service.run_consolidation_service import (
    RunConsolidationService,
)
from hexawyn.application.use_case.run_consolidation.run_consolidation_use_case import (
    RunConsolidationUseCase,
)


class TestRunConsolidationService:
    def test_implements_service_port(self) -> None:
        service = RunConsolidationService(consolidation_port=MagicMock())
        assert isinstance(service, RunConsolidationServicePort)

    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.find_incident_groups.return_value = []
        service = RunConsolidationService(consolidation_port=port)
        result = service.execute(RunConsolidationCommand(cluster_name="test"))
        assert result.groups_found == 0
        assert result.consolidated == []

    def test_execute_with_groups(self) -> None:
        port = MagicMock()
        port.find_incident_groups.return_value = [("ns", "res", "tool", 3)]
        port.get_incidents_for_group.return_value = ["i1", "i2", "i3"]
        port.store_knowledge.return_value = None
        port.mark_consolidated.return_value = None

        service = RunConsolidationService(consolidation_port=port)
        result = service.execute(RunConsolidationCommand(cluster_name="prod-eu"))
        assert result.groups_found == 1
        assert len(result.consolidated) == 1
        assert result.consolidated[0].occurrence_count == 3

    def test_execute_handles_default_cluster_name(self) -> None:
        port = MagicMock()
        port.find_incident_groups.return_value = []
        service = RunConsolidationService(consolidation_port=port)
        result = service.execute(RunConsolidationCommand())
        assert result.groups_found == 0


class TestRunConsolidationUseCase:
    def test_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RunConsolidationServicePort)
        use_case = RunConsolidationUseCase(service=mock_service)
        cmd = RunConsolidationCommand(cluster_name="test")
        use_case.execute(cmd)
        mock_service.execute.assert_called_once_with(cmd)

    def test_exception_propagates_from_port(self) -> None:
        from unittest.mock import MagicMock

        import pytest

        port = MagicMock()
        port.find_incident_groups.side_effect = RuntimeError("db failure")
        service = RunConsolidationService(consolidation_port=port)
        with pytest.raises(RuntimeError, match="db failure"):
            service.execute(
                __import__(
                    "hexawyn.application.ports.driving.run_consolidation.run_consolidation_command",
                    fromlist=["RunConsolidationCommand"],
                ).RunConsolidationCommand()
            )


class TestRunConsolidationServiceEdgeCases:
    def test_multiple_groups_all_consolidated(self) -> None:
        port = MagicMock()
        port.find_incident_groups.return_value = [
            ("ns1", "res1", "tool1", 5),
            ("ns2", "res2", "tool2", 2),
            ("ns3", "res3", "tool3", 8),
        ]
        port.get_incidents_for_group.return_value = ["a", "b"]
        port.store_knowledge.return_value = None
        port.mark_consolidated.return_value = None
        service = RunConsolidationService(consolidation_port=port)

        result = service.execute(RunConsolidationCommand(cluster_name="multi"))

        assert result.groups_found == 3
        assert len(result.consolidated) == 3
        assert result.consolidated[0].occurrence_count == 5
