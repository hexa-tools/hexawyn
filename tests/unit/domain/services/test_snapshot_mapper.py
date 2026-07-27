from __future__ import annotations

import pytest
from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot


class TestToSnapshot:
    def test_happy_path_maps_all_fields(self) -> None:
        from hexawyn.domain.services.spike_provisioning.snapshot_mapper import to_snapshot

        raw = {
            "node_count": 5,
            "allocatable_cpu_cores": 20.0,
            "allocatable_memory_gb": 64.0,
            "used_cpu_cores": 12.0,
            "used_memory_gb": 40.0,
            "autoscaler_enabled": True,
        }

        result = to_snapshot(raw)

        assert isinstance(result, ClusterCapacitySnapshot)
        assert result.node_count == 5  # noqa: PLR2004
        assert result.allocatable_cpu_cores == 20.0  # noqa: PLR2004
        assert result.allocatable_memory_gb == 64.0  # noqa: PLR2004
        assert result.used_cpu_cores == 12.0  # noqa: PLR2004
        assert result.used_memory_gb == 40.0  # noqa: PLR2004
        assert result.autoscaler_enabled is True

    def test_zero_values_returned_as_is(self) -> None:
        from hexawyn.domain.services.spike_provisioning.snapshot_mapper import to_snapshot

        raw = {
            "node_count": 0,
            "allocatable_cpu_cores": 0.0,
            "allocatable_memory_gb": 0.0,
            "used_cpu_cores": 0.0,
            "used_memory_gb": 0.0,
            "autoscaler_enabled": False,
        }

        result = to_snapshot(raw)

        assert result.node_count == 0
        assert result.allocatable_cpu_cores == 0.0
        assert result.used_cpu_cores == 0.0
        assert result.autoscaler_enabled is False

    def test_autoscaler_disabled(self) -> None:
        from hexawyn.domain.services.spike_provisioning.snapshot_mapper import to_snapshot

        raw = {
            "node_count": 3,
            "allocatable_cpu_cores": 12.0,
            "allocatable_memory_gb": 48.0,
            "used_cpu_cores": 10.0,
            "used_memory_gb": 30.0,
            "autoscaler_enabled": False,
        }

        result = to_snapshot(raw)

        assert result.autoscaler_enabled is False

    def test_float_precision_preserved(self) -> None:
        from hexawyn.domain.services.spike_provisioning.snapshot_mapper import to_snapshot

        raw = {
            "node_count": 1,
            "allocatable_cpu_cores": 3.14159,
            "allocatable_memory_gb": 7.89012,
            "used_cpu_cores": 1.23456,
            "used_memory_gb": 5.67890,
            "autoscaler_enabled": True,
        }

        result = to_snapshot(raw)

        assert result.allocatable_cpu_cores == 3.14159  # noqa: PLR2004
        assert result.allocatable_memory_gb == 7.89012  # noqa: PLR2004

    def test_large_node_count(self) -> None:
        from hexawyn.domain.services.spike_provisioning.snapshot_mapper import to_snapshot

        raw = {
            "node_count": 1000,
            "allocatable_cpu_cores": 4000.0,
            "allocatable_memory_gb": 16000.0,
            "used_cpu_cores": 3500.0,
            "used_memory_gb": 14000.0,
            "autoscaler_enabled": True,
        }

        result = to_snapshot(raw)

        assert result.node_count == 1000  # noqa: PLR2004
        assert result.allocatable_cpu_cores == 4000.0  # noqa: PLR2004

    def test_result_is_frozen(self) -> None:
        from hexawyn.domain.services.spike_provisioning.snapshot_mapper import to_snapshot

        raw = {
            "node_count": 2,
            "allocatable_cpu_cores": 4.0,
            "allocatable_memory_gb": 8.0,
            "used_cpu_cores": 3.0,
            "used_memory_gb": 5.0,
            "autoscaler_enabled": False,
        }

        result = to_snapshot(raw)

        with pytest.raises(Exception):
            result.node_count = 999  # type: ignore[misc]
