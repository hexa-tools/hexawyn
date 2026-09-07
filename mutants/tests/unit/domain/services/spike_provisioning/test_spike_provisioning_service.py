from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import (
    ClusterCapacitySnapshot,
    SpikeProvisioningReport,
)
from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
    SpikeProvisioningService,
    _decide_verdict,
    _warning,
)


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


class TestExactReportPayload:
    def test_no_action_full_payload(self) -> None:
        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=20.0, used_mem=30.0),
            multiplier=2.0,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report == SpikeProvisioningReport(
            traffic_multiplier=2.0,
            multiplier_source="historical",
            verdict="no_action",
            current_cpu_headroom_pct=80.0,
            current_memory_headroom_pct=85.0,
            projected_cpu_pct=40.0,
            projected_memory_pct=30.0,
            recommended_nodes=0,
            recommended_node_type="balanced",
            binding_constraint="None",
            autoscaler_sufficient=False,
            provisioning_deadline=None,
            warning="",
        )

    def test_provision_full_payload(self) -> None:
        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=70.0),
            multiplier=2.8,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report == SpikeProvisioningReport(
            traffic_multiplier=2.8,
            multiplier_source="historical",
            verdict="provision",
            current_cpu_headroom_pct=30.0,
            current_memory_headroom_pct=35.0,
            projected_cpu_pct=196.0,
            projected_memory_pct=182.0,
            recommended_nodes=14,
            recommended_node_type="compute_optimized",
            binding_constraint="CPU",
            autoscaler_sufficient=False,
            provisioning_deadline="2026-11-23",
            warning="",
        )

    def test_autoscaler_full_payload(self) -> None:
        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=70.0, autoscaler=True),
            multiplier=2.8,
            multiplier_source="historical",
            event_date="2026-11-27",
        )

        assert report == SpikeProvisioningReport(
            traffic_multiplier=2.8,
            multiplier_source="historical",
            verdict="autoscaler_handles",
            current_cpu_headroom_pct=30.0,
            current_memory_headroom_pct=35.0,
            projected_cpu_pct=196.0,
            projected_memory_pct=182.0,
            recommended_nodes=0,
            recommended_node_type="compute_optimized",
            binding_constraint="CPU",
            autoscaler_sufficient=True,
            provisioning_deadline=None,
            warning="",
        )

    def test_fallback_warning_exact_payload(self) -> None:
        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(),
            multiplier=3.0,
            multiplier_source="generic_fallback",
            event_date="2026-11-27",
        )

        assert report.warning == (
            "No historical spike data for this event — using a generic 3x traffic "
            "multiplier. Treat the recommendation as conservative guidance."
        )

    def test_historical_source_has_no_warning(self) -> None:
        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=70.0),
            multiplier=2.8,
            multiplier_source="historical",
            event_date="2026-11-27",
        )
        assert report.warning == ""


class TestDecideVerdict:
    def test_no_capacity_needed_no_action_not_autoscaler(self) -> None:
        assert _decide_verdict(False, True) == ("no_action", False)

    def test_provision_without_autoscaler_not_sufficient(self) -> None:
        assert _decide_verdict(True, False) == ("provision", False)

    def test_autoscaler_handles_with_autoscaler(self) -> None:
        assert _decide_verdict(True, True) == ("autoscaler_handles", True)


class TestWarningFunction:
    def test_empty_for_unknown_source(self) -> None:
        assert _warning("provided") == ""

    def test_pessimistic_warning(self) -> None:
        result = _warning("pessimistic")
        assert result == (
            "Traffic is unpredictable (e.g. a new product launch) — a pessimistic "
            "multiplier is applied by default; real demand may differ."
        )


class TestCustomSafeThreshold:
    def test_custom_threshold_passed_to_demand_projection(self) -> None:
        report = SpikeProvisioningService().plan(
            snapshot=_snapshot(used_cpu=40.0, used_mem=80.0),
            multiplier=2.0,
            multiplier_source="historical",
            event_date="2026-11-27",
            safe_threshold_pct=50.0,
        )

        assert report.verdict == "provision"
        assert report.binding_constraint == "CPU"
        assert report.projected_cpu_pct == 80.0  # noqa: PLR2004
