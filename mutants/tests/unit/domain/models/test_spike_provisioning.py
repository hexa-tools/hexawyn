from dataclasses import fields


class TestClusterCapacitySnapshot:
    def test_is_frozen_dataclass_with_expected_fields(self) -> None:
        from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot

        field_names = {f.name for f in fields(ClusterCapacitySnapshot)}

        assert field_names == {
            "node_count",
            "allocatable_cpu_cores",
            "allocatable_memory_gb",
            "used_cpu_cores",
            "used_memory_gb",
            "autoscaler_enabled",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot

        snapshot = ClusterCapacitySnapshot(
            node_count=10,
            allocatable_cpu_cores=100.0,
            allocatable_memory_gb=200.0,
            used_cpu_cores=70.0,
            used_memory_gb=130.0,
            autoscaler_enabled=False,
        )

        assert snapshot.node_count == 10  # noqa: PLR2004
        assert snapshot.used_cpu_cores == 70.0  # noqa: PLR2004


class TestSpikeProvisioningReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.spike_provisioning import SpikeProvisioningReport

        report = SpikeProvisioningReport(
            traffic_multiplier=2.8,
            multiplier_source="historical",
            verdict="no_action",
        )

        assert report.traffic_multiplier == 2.8  # noqa: PLR2004
        assert report.multiplier_source == "historical"
        assert report.verdict == "no_action"
        assert report.recommended_nodes == 0
        assert report.recommended_node_type == "balanced"
        assert report.binding_constraint == "None"
        assert report.autoscaler_sufficient is False
        assert report.provisioning_deadline is None
        assert report.warning == ""

    def test_holds_recommendation(self) -> None:
        from hexawyn.domain.models.spike_provisioning import SpikeProvisioningReport

        report = SpikeProvisioningReport(
            traffic_multiplier=2.8,
            multiplier_source="historical",
            verdict="provision",
            current_cpu_headroom_pct=30.0,
            current_memory_headroom_pct=35.0,
            projected_cpu_pct=196.0,
            projected_memory_pct=182.0,
            recommended_nodes=3,
            recommended_node_type="compute_optimized",
            binding_constraint="CPU",
            provisioning_deadline="2026-11-20",
        )

        assert report.recommended_nodes == 3  # noqa: PLR2004
        assert report.recommended_node_type == "compute_optimized"
        assert report.binding_constraint == "CPU"
        assert report.provisioning_deadline == "2026-11-20"
