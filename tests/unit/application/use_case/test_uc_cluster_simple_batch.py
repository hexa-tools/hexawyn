from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.check_cluster_operator_health.check_cluster_operator_health_use_case import (  # noqa: E501
    CheckClusterOperatorHealthUseCase,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.command import (
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.response import (
    CheckClusterOperatorHealthResponse,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.check_disruption_risks_use_case import (  # noqa: E501
    CheckDisruptionRisksUseCase,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.command import (
    CheckDisruptionRisksCommand,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.response import (
    CheckDisruptionRisksResponse,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (  # noqa: E501
    CheckMachineConfigPoolStatusUseCase,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.command import (
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.response import (
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.check_resource_constraints_use_case import (  # noqa: E501
    CheckResourceConstraintsUseCase,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
    CheckResourceConstraintsResponse,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.command import (
    DiffClusterResourcesCommand,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.diff_cluster_resources_use_case import (  # noqa: E501
    DiffClusterResourcesUseCase,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.response import (
    DiffClusterResourcesResponse,
)
from hexawyn.application.use_case.cluster.resource_yaml.command import (
    ResourceYamlCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.resource_yaml_use_case import (  # noqa: E501
    ResourceYAMLUseCase,
)
from hexawyn.application.use_case.cluster.resource_yaml.response import (
    ResourceYamlResponse,
)
from hexawyn.application.use_case.cluster.run_consolidation.command import (
    RunConsolidationCommand,
)
from hexawyn.application.use_case.cluster.run_consolidation.response import (
    RunConsolidationResponse,
)
from hexawyn.application.use_case.cluster.run_consolidation.run_consolidation_use_case import (  # noqa: E501
    RunConsolidationUseCase,
)


class TestCheckClusterOperatorHealthUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_operator_statuses.return_value = []

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        assert isinstance(result, CheckClusterOperatorHealthResponse)

    def test_execute_empty_operators(self) -> None:
        port = MagicMock()
        port.get_operator_statuses.return_value = []

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        assert isinstance(result, CheckClusterOperatorHealthResponse)


class TestCheckDisruptionRisksUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_disruption_risks.return_value = []

        use_case = CheckDisruptionRisksUseCase(disruption_risk_port=port)
        result = use_case.execute(CheckDisruptionRisksCommand())

        assert isinstance(result, CheckDisruptionRisksResponse)

    def test_execute_zero_warning_days(self) -> None:
        port = MagicMock()
        port.get_disruption_risks.return_value = []

        use_case = CheckDisruptionRisksUseCase(disruption_risk_port=port)
        result = use_case.execute(CheckDisruptionRisksCommand(warning_days=0))

        assert isinstance(result, CheckDisruptionRisksResponse)


class TestCheckMachineConfigPoolStatusUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_machine_config_pools.return_value = []

        use_case = CheckMachineConfigPoolStatusUseCase(
            machine_config_pool_port=port,
        )
        result = use_case.execute(CheckMachineConfigPoolStatusCommand())

        assert isinstance(result, CheckMachineConfigPoolStatusResponse)


class TestCheckResourceConstraintsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_pod_resource_metrics.return_value = []

        use_case = CheckResourceConstraintsUseCase(port=port)
        result = use_case.execute(CheckResourceConstraintsCommand())

        assert isinstance(result, CheckResourceConstraintsResponse)


class TestDiffClusterResourcesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_resource_inventory.return_value = {"cluster_name": "test", "resources": []}

        use_case = DiffClusterResourcesUseCase(cluster_diff_port=port)
        result = use_case.execute(
            DiffClusterResourcesCommand(
                source_context="prod-eu",
                target_context="prod-us",
            )
        )

        assert isinstance(result, DiffClusterResourcesResponse)

    def test_execute_empty_inventories(self) -> None:
        port = MagicMock()
        port.get_resource_inventory.return_value = {"cluster_name": "test", "resources": []}

        use_case = DiffClusterResourcesUseCase(cluster_diff_port=port)
        result = use_case.execute(
            DiffClusterResourcesCommand(
                source_context="staging",
                target_context="staging",
            )
        )

        assert isinstance(result, DiffClusterResourcesResponse)


class TestResourceYAMLUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.resource_exists.return_value = True
        port.get_resource_yaml.return_value = ""

        use_case = ResourceYAMLUseCase(port=port)
        result = use_case.execute(
            ResourceYamlCommand(
                kind="Deployment",
                name="nginx",
                namespace="default",
            )
        )

        assert isinstance(result, ResourceYamlResponse)

    def test_execute_resource_not_found(self) -> None:
        port = MagicMock()
        port.resource_exists.return_value = False

        use_case = ResourceYAMLUseCase(port=port)
        result = use_case.execute(
            ResourceYamlCommand(
                kind="Deployment",
                name="nonexistent",
                namespace="default",
            )
        )

        assert isinstance(result, ResourceYamlResponse)
        assert result.resource_found is False


class TestRunConsolidationUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_pod_inventory.return_value = []

        use_case = RunConsolidationUseCase(consolidation_port=port)
        result = use_case.execute(RunConsolidationCommand())

        assert isinstance(result, RunConsolidationResponse)

    def test_execute_no_pods_to_consolidate(self) -> None:
        port = MagicMock()
        port.get_pod_inventory.return_value = []

        use_case = RunConsolidationUseCase(consolidation_port=port)
        result = use_case.execute(RunConsolidationCommand())

        assert isinstance(result, RunConsolidationResponse)
