"""Unit tests for classify_incident_cause — keyword-based incident cause classification."""

from __future__ import annotations

from hexawyn.domain.models.incident_triage import IncidentCauseCategory
from hexawyn.domain.services.incident_triage.root_cause_classifier import (
    classify_incident_cause,
    remediation_for,
)


class TestClassifyIncidentCause:
    def test_connection_pool_exhausted_classified_as_database(self) -> None:
        category = classify_incident_cause("connection pool exhausted for postgres")
        assert category == IncidentCauseCategory.DATABASE

    def test_oomkilled_classified_as_resource_exhaustion(self) -> None:
        category = classify_incident_cause("Container was OOMKilled, out of memory")
        assert category == IncidentCauseCategory.RESOURCE_EXHAUSTION

    def test_connection_refused_classified_as_network(self) -> None:
        category = classify_incident_cause("dial tcp: connection refused")
        assert category == IncidentCauseCategory.NETWORK

    def test_image_pull_error_classified_as_image_or_config(self) -> None:
        category = classify_incident_cause("Failed to pull image: ErrImagePull")
        assert category == IncidentCauseCategory.IMAGE_OR_CONFIG

    def test_crashloopbackoff_classified_as_deployment(self) -> None:
        category = classify_incident_cause("Back-off restarting failed container: CrashLoopBackOff")
        assert category == IncidentCauseCategory.DEPLOYMENT

    def test_unrecognized_message_classified_as_unknown(self) -> None:
        category = classify_incident_cause("something unexpected happened")
        assert category == IncidentCauseCategory.UNKNOWN

    def test_database_keyword_checked_before_network_keyword(self) -> None:
        category = classify_incident_cause("database connection timeout to postgres:5432")
        assert category == IncidentCauseCategory.DATABASE


class TestRemediationFor:
    def test_database_remediation_mentions_restore_and_database(self) -> None:
        remediation = remediation_for(IncidentCauseCategory.DATABASE)
        lowered = remediation.lower()
        assert "restore" in lowered
        assert "database" in lowered

    def test_every_category_has_a_remediation(self) -> None:
        for category in IncidentCauseCategory:
            assert remediation_for(category)
