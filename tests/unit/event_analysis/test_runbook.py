"""Unit tests for RunbookSuggestionEngine — maps event REASON to a runbook."""

from __future__ import annotations

from hexawyn.domain.services.event_analysis.runbook import (
    RunbookSuggestion,
    RunbookSuggestionEngine,
)


class TestRunbookSuggestionEngine:
    def test_oomkilling_suggests_memory_runbook(self) -> None:
        """TC2: event REASON "OOMKilling" → runbook "Increase memory limit or investigate memory leak"."""
        engine = RunbookSuggestionEngine()

        suggestion = engine.suggest("OOMKilling")

        assert suggestion.runbook_id == "runbook-memory-001"
        assert suggestion.title == "Increase memory limit or investigate memory leak"

    def test_backoff_suggests_crashloop_runbook(self) -> None:
        engine = RunbookSuggestionEngine()

        suggestion = engine.suggest("BackOff")

        assert suggestion.runbook_id == "runbook-crashloop-001"

    def test_unknown_reason_returns_generic_fallback(self) -> None:
        """TC4: No runbook found for event REASON → returns generic troubleshooting steps."""
        engine = RunbookSuggestionEngine()

        suggestion = engine.suggest("SomeUnknownReason")

        assert suggestion.runbook_id == "runbook-generic-001"
        assert len(suggestion.steps) > 0

    def test_exotic_crd_event_no_match_does_not_crash(self) -> None:
        """Edge case: no match for exotic CRD event → graceful fallback, no crash."""
        engine = RunbookSuggestionEngine()

        suggestion = engine.suggest("CustomResourceDefinitionFrobnicated")

        assert isinstance(suggestion, RunbookSuggestion)
        assert suggestion.runbook_id == "runbook-generic-001"
