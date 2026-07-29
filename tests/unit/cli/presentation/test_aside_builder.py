from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation.aside_builder import build_aside_lines


class TestBuildAsideLines:
    def _make_app(self) -> MagicMock:
        app = MagicMock()
        app.startup_status = "connected"
        ctx = {"name": "prod-eu", "namespace": "default"}
        app.adapter.get_cluster_context.return_value = ctx
        app.startup_result = None
        return app

    def test_header_contains_hexawyn(self) -> None:
        app = self._make_app()

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=0,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=["[green]OK[/green]"],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=10,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=1,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_health_score",
                return_value=85,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "HEXAWYN" in joined

    def test_cluster_info_displayed(self) -> None:
        app = self._make_app()

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=5,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=10,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=1,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_health_score",
                return_value=85,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "prod-eu" in joined
        assert "Namespaces" in joined
        assert "Nodes" in joined
        assert "Pods" in joined

    def test_health_score_from_startup_result_green(self) -> None:
        app = self._make_app()
        app.startup_result = {"health_score": 95}

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=0,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=10,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=1,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "95" in joined
        assert "green" in joined

    def test_health_score_yellow_when_between_50_and_80(self) -> None:
        app = self._make_app()
        app.startup_result = {"health_score": 65}

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=0,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=10,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=1,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "65" in joined
        assert "yellow" in joined

    def test_health_score_red_when_below_50(self) -> None:
        app = self._make_app()
        app.startup_result = {"health_score": 30}

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=0,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=10,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=1,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "30" in joined
        assert "red" in joined

    def test_fallback_health_score_from_adapter(self) -> None:
        app = self._make_app()
        app.startup_result = None

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=0,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=10,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=1,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_health_score",
                return_value=42,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "42" in joined

    def test_pod_status_counts_rendered(self) -> None:
        app = self._make_app()

        with (
            patch("hexawyn.cli.presentation.aside_builder.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.aside_builder.safe_metrics", return_value={}),
            patch("hexawyn.cli.presentation.aside_builder.safe_findings", return_value=[]),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_suggestions",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.mapping_int",
                return_value=0,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.kubectl_current_context",
                return_value="prod-eu",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.connection_line",
                return_value="",
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_license_aside_lines",
                return_value=[""],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_finding_warnings",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.format_suggestion_lines",
                return_value=[],
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.namespace_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.running_pod_count",
                return_value=8,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.pending_pod_count",
                return_value=3,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.failed_pod_count",
                return_value=2,
            ),
            patch(
                "hexawyn.cli.presentation.aside_builder.safe_health_score",
                return_value=85,
            ),
        ):
            lines = build_aside_lines(app)

        joined = "\n".join(lines)
        assert "Running Pods" in joined
        assert "8" in joined
        assert "Pending Pods" in joined
        assert "3" in joined
        assert "Failed Pods" in joined
        assert "2" in joined
