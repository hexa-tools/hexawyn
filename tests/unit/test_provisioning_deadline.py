from __future__ import annotations


class TestProvisioningDeadline:
    def test_deadline_before_event_by_lead_time_and_margin(self) -> None:
        from hexawyn.domain.services.spike_provisioning.provisioning_deadline import (
            compute_deadline,
        )

        # Event 2026-11-27, 24h lead time + 3 day safety margin → 2026-11-23.
        deadline = compute_deadline(
            event_date="2026-11-27", provider_lead_time_hours=24, safety_margin_days=3
        )

        assert deadline == "2026-11-23"

    def test_longer_lead_time_pushes_deadline_earlier(self) -> None:
        from hexawyn.domain.services.spike_provisioning.provisioning_deadline import (
            compute_deadline,
        )

        deadline = compute_deadline(
            event_date="2026-11-27", provider_lead_time_hours=72, safety_margin_days=0
        )

        assert deadline == "2026-11-24"

    def test_zero_lead_time_and_margin_is_event_date(self) -> None:
        from hexawyn.domain.services.spike_provisioning.provisioning_deadline import (
            compute_deadline,
        )

        deadline = compute_deadline(
            event_date="2026-11-27", provider_lead_time_hours=0, safety_margin_days=0
        )

        assert deadline == "2026-11-27"

    def test_invalid_event_date_returns_none(self) -> None:
        from hexawyn.domain.services.spike_provisioning.provisioning_deadline import (
            compute_deadline,
        )

        deadline = compute_deadline(
            event_date="not-a-date", provider_lead_time_hours=24, safety_margin_days=3
        )

        assert deadline is None

    def test_crosses_month_boundary(self) -> None:
        from hexawyn.domain.services.spike_provisioning.provisioning_deadline import (
            compute_deadline,
        )

        deadline = compute_deadline(
            event_date="2026-12-02", provider_lead_time_hours=24, safety_margin_days=3
        )

        assert deadline == "2026-11-28"
