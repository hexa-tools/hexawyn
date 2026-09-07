from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.cluster.resource_constraint.command import (
    ResourceConstraintCommand,
)
from hexawyn.application.use_case.cluster.resource_constraint.resource_constraint_use_case import (
    ResourceConstraintUseCase,
)
from hexawyn.application.use_case.cluster.resource_constraint.response import (
    ResourceConstraintResponse,
)


class TestResourceConstraintUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = []

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert isinstance(result, ResourceConstraintResponse)

    def test_execute_empty_namespace(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = []

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand())

        assert result.total_pods == 0  # noqa: PLR2004
        assert result.critical_count == 0  # noqa: PLR2004

    def test_execute_with_critical_container(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "high-cpu",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 950,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 100 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.total_pods == 1  # noqa: PLR2004
        assert result.total_containers == 1  # noqa: PLR2004
        assert result.critical_count == 1  # noqa: PLR2004

    def test_execute_with_ok_container(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "low-usage",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 100,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 50 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.critical_count == 0  # noqa: PLR2004
        assert result.total_containers == 1  # noqa: PLR2004

    def test_execute_with_no_limits_container(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "no-limits",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 500,
                "cpu_limit_millicores": None,
                "memory_usage_bytes": 100 * 1024 * 1024,
                "memory_limit_bytes": None,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.critical_count == 0  # noqa: PLR2004
        assert result.total_containers == 1  # noqa: PLR2004

    def test_execute_with_unlimited_cpu(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "unlimited-cpu",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 500,
                "cpu_limit_millicores": 0,
                "memory_usage_bytes": 100 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.total_containers == 1  # noqa: PLR2004

    def test_execute_with_memory_oom_risk(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "memory-hog",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 100,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 230 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.critical_count == 1  # noqa: PLR2004

    def test_execute_with_init_container(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "init-setup",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 100,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 50 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": True,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.total_containers == 1  # noqa: PLR2004

    def test_execute_multiple_pods(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "ctr-a",
                "pod_name": "pod-a",
                "namespace": "default",
                "cpu_usage_millicores": 100,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 50 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
            {
                "container_name": "ctr-b",
                "pod_name": "pod-b",
                "namespace": "default",
                "cpu_usage_millicores": 950,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 200 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
            {
                "container_name": "ctr-c",
                "pod_name": "pod-c",
                "namespace": "default",
                "cpu_usage_millicores": 500,
                "cpu_limit_millicores": None,
                "memory_usage_bytes": 100 * 1024 * 1024,
                "memory_limit_bytes": None,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.total_pods == 3  # noqa: PLR2004
        assert result.total_containers == 3  # noqa: PLR2004
        assert result.critical_count == 1  # noqa: PLR2004

    def test_check_resource_constraints_directly(self) -> None:
        from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
            CheckResourceConstraintsResponse,
        )

        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "my-ctr",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 100,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 50 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.check_resource_constraints(
            CheckResourceConstraintsCommand(
                namespace="default",
                cpu_threshold_pct=80,
                memory_threshold_pct=80,
            )
        )

        assert isinstance(result, CheckResourceConstraintsResponse)
        assert result.report is not None
        assert result.report.total_pods_scanned == 1  # noqa: PLR2004
        assert result.report.ok_count == 1  # noqa: PLR2004

    def test_execute_with_unlimited_memory(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "unlimited-mem",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 500,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 500 * 1024 * 1024,
                "memory_limit_bytes": 0,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert result.total_containers == 1  # noqa: PLR2004

    def test_check_resource_constraints_no_limits(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "no-limits-ctr",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 500,
                "cpu_limit_millicores": None,
                "memory_usage_bytes": 100 * 1024 * 1024,
                "memory_limit_bytes": None,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.check_resource_constraints(CheckResourceConstraintsCommand())

        assert result.report is not None
        assert result.report.no_limits_count == 1  # noqa: PLR2004

    def test_check_resource_constraints_custom_thresholds(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = [
            {
                "container_name": "moderate-usage",
                "pod_name": "my-pod",
                "namespace": "default",
                "cpu_usage_millicores": 600,
                "cpu_limit_millicores": 1000,
                "memory_usage_bytes": 150 * 1024 * 1024,
                "memory_limit_bytes": 256 * 1024 * 1024,
                "is_init_container": False,
            },
        ]

        use_case = ResourceConstraintUseCase(port=port)

        result_normal = use_case.check_resource_constraints(
            CheckResourceConstraintsCommand(cpu_threshold_pct=80, memory_threshold_pct=80)
        )
        assert result_normal.report is not None
        assert result_normal.report.ok_count == 1  # noqa: PLR2004

        result_strict = use_case.check_resource_constraints(
            CheckResourceConstraintsCommand(cpu_threshold_pct=50, memory_threshold_pct=50)
        )
        assert result_strict.report is not None
        assert result_strict.report.critical_count == 1  # noqa: PLR2004
