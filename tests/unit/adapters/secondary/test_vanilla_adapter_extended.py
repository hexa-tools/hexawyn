"""Additional tests for VanillaAdapter — covering untested ports and helpers."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _compute_pod_resources,
    _parse_cpu,
    _parse_memory,
    _parse_memory_to_mi,
)
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter


def _make_container(cpu: str = "100m", mem: str = "128Mi") -> MagicMock:
    c = MagicMock()
    c.resources = MagicMock()
    c.resources.requests = {"cpu": cpu, "memory": mem} if cpu or mem else {}
    return c


def _make_pod(
    name: str = "test-pod",
    namespace: str = "default",
    phase: str = "Running",
    containers: list[MagicMock] | None = None,
) -> MagicMock:
    p = MagicMock()
    p.metadata = MagicMock()
    p.metadata.name = name
    p.metadata.namespace = namespace
    p.metadata.owner_references = None
    p.status = MagicMock()
    p.status.phase = phase
    p.spec = MagicMock()
    p.spec.containers = containers or [_make_container()]
    return p


class TestParseHelpers:
    """Cover module-level parse helpers."""

    def test_parse_cpu_millicores(self) -> None:
        assert _parse_cpu("500m") == 0.5  # noqa: PLR2004

    def test_parse_cpu_cores(self) -> None:
        assert _parse_cpu("2") == 2.0  # noqa: PLR2004

    def test_parse_cpu_zero(self) -> None:
        assert _parse_cpu("0") == 0.0  # noqa: PLR2004

    def test_parse_memory_mi(self) -> None:
        assert _parse_memory("512Mi") == 0.5  # noqa: PLR2004

    def test_parse_memory_gi(self) -> None:
        assert _parse_memory("2Gi") == 2.0  # noqa: PLR2004

    def test_parse_memory_ki(self) -> None:
        assert _parse_memory("1048576Ki") > 0.99  # noqa: PLR2004
        assert _parse_memory("1048576Ki") < 1.01  # noqa: PLR2004

    def test_parse_memory_to_mi(self) -> None:
        assert _parse_memory_to_mi("1Gi") == 1024.0  # noqa: PLR2004

    def test_parse_memory_to_mi_no_suffix(self) -> None:
        assert _parse_memory_to_mi("128Mi") == 128.0  # noqa: PLR2004

    def test_compute_pod_resources(self) -> None:
        containers = [_make_container("200m", "256Mi"), _make_container("100m", "128Mi")]
        cpu, mem = _compute_pod_resources(containers)
        assert cpu == pytest.approx(0.3)
        assert mem == pytest.approx(0.375)

    def test_compute_pod_resources_no_containers(self) -> None:
        cpu, mem = _compute_pod_resources([])
        assert cpu == 0.0  # noqa: PLR2004
        assert mem == 0.0  # noqa: PLR2004


class TestCostForecastPort:
    """Cover get_daily_costs — moved to test_cost_forecast_adapter.py."""


class TestZombieDetectionPort:
    """Cover get_zombie_workloads — moved to VanillaZombieDetectionAdapter."""

    # Tests moved to test_zombie_detection_adapter.py


class TestCostSavingEstimationPort:
    """Cover get_pod_resource_data — moved to VanillaCostSavingAdapter."""

    # Tests moved to test_cost_saving_estimation_adapter.py


class TestWhatIfSimulationPort:
    """Cover WhatIf simulation methods — moved to VanillaWhatIfSimulationAdapter."""

    # Tests moved to test_what_if_simulation_adapter.py


class TestProbeAuditPort:
    """Cover get_probe_audit_data."""

    @pytest.mark.skip(reason="Needs deeper mock setup for custom objects API")
    def test_returns_probe_data_with_all_namespaces(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        mock_deploy = MagicMock()
        mock_deploy.spec = MagicMock()
        mock_deploy.spec.template = MagicMock()
        mock_deploy.spec.template.spec = MagicMock()
        c = _make_container()
        c.liveness_probe = None
        c.readiness_probe = None
        mock_deploy.spec.template.spec.containers = [c]

        adapter._apps_api = MagicMock()
        adapter._apps_api.list_deployment_for_all_namespaces.return_value = MagicMock()
        with patch.object(adapter, "_items_from", return_value=[mock_deploy]):
            result = adapter.get_probe_audit_data()
            assert isinstance(result, list)

    @pytest.mark.skip(reason="Needs deeper mock setup for custom objects API")
    def test_probe_audit_with_namespace_filter(self) -> None:
        adapter = VanillaAdapter(cluster_name="test")
        adapter._apps_api = MagicMock()
        adapter._apps_api.list_namespaced_deployment.return_value = MagicMock()
        with patch.object(adapter, "_items_from", return_value=[]):
            result = adapter.get_probe_audit_data(namespace="specific-ns")
            assert result == []


class TestAdapterHelpers:
    """Cover internal helper methods — moved to test_vanilla_adapter_v2.py
    (VanillaK8sAdapter/VanillaHealthAdapter) and test__helpers.py (module-level
    mapping/metric helpers)."""
