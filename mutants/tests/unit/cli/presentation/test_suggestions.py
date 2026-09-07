from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation.suggestions import format_suggestion_lines


class TestFormatSuggestionLines:
    def test_header_lines_always_present(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = None

        lines = format_suggestion_lines(app, [])

        assert "Suggestions" in "\n".join(lines)

    def test_ai_suggestion_appears_with_icon(self) -> None:
        app = MagicMock()
        app.ai_suggestion = "Check the resource limits"
        app.startup_result = None

        lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Check the resource limits" in joined

    def test_startup_suggestions_with_label_and_explanation(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {
                    "label": "Low memory",
                    "explanation": "Memory usage is above 90%",
                    "severity": "critical",
                },
            ],
        }

        lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Low memory" in joined
        assert "Memory usage is above 90%" in joined

    def test_startup_suggestion_warning_severity(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {
                    "label": "Disk space",
                    "explanation": "Disk at 85%",
                    "severity": "warning",
                },
            ],
        }

        lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Disk space" in joined

    def test_startup_suggestion_info_severity(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {
                    "label": "Update available",
                    "explanation": "New version 2.0",
                    "severity": "info",
                },
            ],
        }

        lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Update available" in joined

    def test_suggestion_label_only_no_explanation(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {"label": "Cleanup pods", "severity": "info"},
            ],
        }

        lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Cleanup pods" in joined

    def test_narrative_summary_when_not_error(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [],
            "narrative_summary": "Cluster looks healthy.",
        }

        with patch(
            "hexawyn.cli.presentation.suggestions.is_error_narrative",
            return_value=False,
        ):
            lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Cluster looks healthy." in joined

    def test_narrative_summary_skipped_when_error(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [],
            "narrative_summary": "Runtime not available",
        }

        with patch(
            "hexawyn.cli.presentation.suggestions.is_error_narrative",
            return_value=True,
        ):
            lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Runtime not available" not in joined

    def test_fallback_suggestions_when_few_lines(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = None

        suggestions = [
            "Clean up unused resources",
            "Review crash loops",
        ]

        lines = format_suggestion_lines(app, suggestions)

        joined = "\n".join(lines)
        assert "Clean up unused resources" in joined
        assert "Review crash loops" in joined

    def test_fallback_suggestions_max_four(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = None

        suggestions = ["A", "B", "C", "D", "E", "F"]

        lines = format_suggestion_lines(app, suggestions)

        joined = "\n".join(lines)
        assert "A" in joined
        assert "D" in joined
        assert "E" not in joined
        assert "F" not in joined

    def test_string_narrative_in_startup_result(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None

        mock_result = MagicMock()
        mock_result.get.side_effect = lambda k, default=None: {
            "suggestions": [],
            "narrative_summary": "Status: OK",
        }.get(k, default)
        app.startup_result = mock_result

        with patch(
            "hexawyn.cli.presentation.suggestions.is_error_narrative",
            return_value=False,
        ):
            lines = format_suggestion_lines(app, [])

        joined = "\n".join(lines)
        assert "Status: OK" in joined
