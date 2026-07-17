from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot


def _snapshot(
    used_cpu: float = 70.0,
    used_mem: float = 130.0,
    autoscaler: bool = False,
    node_count: int = 10,
) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=node_count,
        allocatable_cpu_cores=100.0,
        allocatable_memory_gb=200.0,
        used_cpu_cores=used_cpu,
        used_memory_gb=used_mem,
        autoscaler_enabled=autoscaler,
    )


class TestVerdict:
    def test_no_action_when_headroom_sufficient(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=20.0, used_mem=30.0),
            multiplier=2.0,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report.verdict == "no_action"
        assert report.recommended_nodes == 0

    def test_provision_when_spike_exceeds_capacity(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=70.0),
            multiplier=2.8,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report.verdict == "provision"
        assert report.recommended_nodes >= 1
        assert report.recommended_node_type == "compute_optimized"
        assert report.provisioning_deadline is not None


class TestAutoscaler:
    def test_autoscaler_handles_spike(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=70.0, autoscaler=True),
            multiplier=2.8,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report.verdict == "autoscaler_handles"
        assert report.autoscaler_sufficient is True
        assert report.recommended_nodes == 0


class TestFallbackMultiplier:
    def test_generic_fallback_flags_warning(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(),
            multiplier=3.0,
            multiplier_source="generic_fallback",
            event_date="2026-11-27",
        )

        assert "generic" in report.warning.lower() or "no historical" in report.warning.lower()

    def test_pessimistic_source_flags_warning(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(),
            multiplier=4.0,
            multiplier_source="pessimistic",
            event_date="2026-11-27",
        )

        assert report.warning != ""


class TestDeadline:
    def test_lead_time_factored_into_deadline(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=70.0),
            multiplier=2.8,
            multiplier_source="historical",
            event_date="2026-11-27",
            provider_lead_time_hours=24,
            safety_margin_days=3,
        )

        assert report.provisioning_deadline == "2026-11-23"

    def test_no_deadline_when_no_action(self) -> None:
        from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
            SpikeProvisioningService,
        )

        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=20.0, used_mem=30.0),
            multiplier=2.0,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report.provisioning_deadline is None
