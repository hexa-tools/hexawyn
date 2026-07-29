from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
    TeamCostKubernetesAdapter,
)


class TestTeamCostKubernetesAdapter:
    def test_fetch_namespace_resources_with_data(self) -> None:
        with (
            patch("kubernetes.config.load_kube_config"),
            patch("kubernetes.client.CoreV1Api") as mock_api,
        ):  # noqa: E501
            mock_v1 = MagicMock()

            ns_a = MagicMock()
            ns_a.metadata = MagicMock()
            ns_a.metadata.name = "prod"

            mock_v1.list_namespace.return_value = MagicMock(items=[ns_a])

            pod_with_cpu = MagicMock()
            pod_with_cpu.spec = MagicMock()
            container = MagicMock()
            container.resources = MagicMock(requests={"cpu": "500m", "memory": "256Mi"})
            pod_with_cpu.spec.containers = [container]

            mock_v1.list_namespaced_pod.return_value = MagicMock(items=[pod_with_cpu])

            mock_api.return_value = mock_v1

            adapter = TeamCostKubernetesAdapter()
            result = adapter.fetch_namespace_resources("2026-07")

            assert len(result) == 1
            assert result[0]["namespace"] == "prod"
            assert result[0]["pod_count"] == 1

    def test_fetch_namespace_resources_empty_on_error(self) -> None:
        with (
            patch("kubernetes.config.load_kube_config"),
            patch("kubernetes.client.CoreV1Api", side_effect=Exception("no cluster")),
        ):  # noqa: E501
            adapter = TeamCostKubernetesAdapter()
            result = adapter.fetch_namespace_resources("2026-07")
            assert result == []

    def test_fetch_namespace_resources_no_pods(self) -> None:
        with (
            patch("kubernetes.config.load_kube_config"),
            patch("kubernetes.client.CoreV1Api") as mock_api,
        ):  # noqa: E501
            mock_v1 = MagicMock()
            ns_a = MagicMock()
            ns_a.metadata = MagicMock()
            ns_a.metadata.name = "empty-ns"
            mock_v1.list_namespace.return_value = MagicMock(items=[ns_a])
            mock_v1.list_namespaced_pod.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            adapter = TeamCostKubernetesAdapter()
            result = adapter.fetch_namespace_resources("2026-07")

            assert result == []

    def test_fetch_namespace_resources_missing_metadata(self) -> None:
        with (
            patch("kubernetes.config.load_kube_config"),
            patch("kubernetes.client.CoreV1Api") as mock_api,
        ):  # noqa: E501
            mock_v1 = MagicMock()
            ns_no_meta = MagicMock()
            ns_no_meta.metadata = None
            mock_v1.list_namespace.return_value = MagicMock(items=[ns_no_meta])
            mock_api.return_value = mock_v1

            adapter = TeamCostKubernetesAdapter()
            result = adapter.fetch_namespace_resources("2026-07")
            assert result == []

    def test_parse_cpu_values(self) -> None:
        from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
            _parse_cpu,
        )

        assert _parse_cpu("500m") == 500  # noqa: PLR2004
        assert _parse_cpu("1") == 1000  # noqa: PLR2004
        assert _parse_cpu("2.5") == 2500  # noqa: PLR2004
        assert _parse_cpu("invalid") == 0
        assert _parse_cpu("") == 0

    def test_parse_memory_values(self) -> None:
        from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
            _parse_memory,
        )

        assert _parse_memory("256Mi") == 256  # noqa: PLR2004
        assert _parse_memory("1Gi") == 1024  # noqa: PLR2004
        assert _parse_memory("512Ki") == 0
        assert _parse_memory("invalid") == 0
        assert _parse_memory("") == 0
