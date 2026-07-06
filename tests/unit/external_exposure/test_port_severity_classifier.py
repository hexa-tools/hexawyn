"""Unit tests for classify_base_severity. Checker case 6: severity is
determined by the port number, never confusing a DB service (5432) with a
web service (3000) regardless of the service's own name."""

from __future__ import annotations

_CRITICAL_PORTS = (5432, 3306, 27017, 6379)
_MEDIUM_PORTS = (80, 443, 3000)


class TestClassifyBaseSeverity:
    def test_postgres_port_is_critical(self) -> None:
        from hexawyn.domain.services.external_exposure.port_severity_classifier import (
            classify_base_severity,
        )

        result = classify_base_severity([5432], _CRITICAL_PORTS, _MEDIUM_PORTS)

        assert result == "critical"

    def test_redis_port_is_critical(self) -> None:
        """AC5: cache services exposed externally are critical (before any
        exposure-type/namespace downgrade is applied)."""
        from hexawyn.domain.services.external_exposure.port_severity_classifier import (
            classify_base_severity,
        )

        result = classify_base_severity([6379], _CRITICAL_PORTS, _MEDIUM_PORTS)

        assert result == "critical"

    def test_grafana_port_is_medium_not_critical(self) -> None:
        """Checker case 6's exact scenario: port 3000 (grafana) must never
        be classified critical."""
        from hexawyn.domain.services.external_exposure.port_severity_classifier import (
            classify_base_severity,
        )

        result = classify_base_severity([3000], _CRITICAL_PORTS, _MEDIUM_PORTS)

        assert result == "medium"

    def test_unrecognized_port_defaults_to_medium(self) -> None:
        from hexawyn.domain.services.external_exposure.port_severity_classifier import (
            classify_base_severity,
        )

        result = classify_base_severity([9999], _CRITICAL_PORTS, _MEDIUM_PORTS)

        assert result == "medium"

    def test_any_critical_port_among_several_wins(self) -> None:
        from hexawyn.domain.services.external_exposure.port_severity_classifier import (
            classify_base_severity,
        )

        result = classify_base_severity([80, 5432], _CRITICAL_PORTS, _MEDIUM_PORTS)

        assert result == "critical"

    def test_no_ports_defaults_to_medium(self) -> None:
        from hexawyn.domain.services.external_exposure.port_severity_classifier import (
            classify_base_severity,
        )

        assert classify_base_severity([], _CRITICAL_PORTS, _MEDIUM_PORTS) == "medium"
