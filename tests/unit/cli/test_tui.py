from __future__ import annotations

from unittest.mock import MagicMock, PropertyMock, patch

from hexawyn.cli.tui import HexawynTUI


class TestHexawynTUI:
    @staticmethod
    def _create_tui(**kwargs: object) -> HexawynTUI:
        with patch("hexawyn.cli.tui.App.__init__", return_value=None):
            tui = HexawynTUI.__new__(HexawynTUI)
            defaults = {
                "adapter": MagicMock(),
                "expert_mode": False,
                "demo_mode": False,
                "scenario": "aws_eks",
                "extra_chip": None,
                "startup_status": None,
                "context_service": None,
                "adapter_builder": MagicMock(),
                "run_startup_scan": False,
                "cluster_name": "unknown",
                "needs_setup": False,
                "startup_result": None,
                "ai_suggestion": None,
            }
            for k, v in defaults.items():
                setattr(tui, k, v)
            for k, v in kwargs.items():
                setattr(tui, k, v)
            return tui

    def test_init_with_adapter(self) -> None:
        adapter = MagicMock()
        tui = self._create_tui(adapter=adapter, cluster_name="prod")
        assert tui.adapter is adapter
        assert tui.cluster_name == "prod"
        assert tui.expert_mode is False
        assert tui.demo_mode is False
        assert tui.ai_suggestion is None

    def test_init_expert_mode(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), expert_mode=True, cluster_name="prod")
        assert tui.expert_mode is True

    def test_init_demo_mode(self) -> None:
        tui = self._create_tui(
            adapter=MagicMock(), demo_mode=True, scenario="azure_aks", cluster_name="prod"
        )
        assert tui.demo_mode is True
        assert tui.scenario == "azure_aks"

    def test_init_with_context_service(self) -> None:
        svc = MagicMock()
        tui = self._create_tui(adapter=MagicMock(), context_service=svc, cluster_name="prod")
        assert tui.context_service is svc

    def test_init_with_extra_chip(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), extra_chip="DB: 2GB", cluster_name="prod")
        assert tui.extra_chip == "DB: 2GB"

    def test_init_with_startup_status(self) -> None:
        status = MagicMock()
        tui = self._create_tui(adapter=MagicMock(), startup_status=status, cluster_name="prod")
        assert tui.startup_status is status

    def test_fallback_suggestion_no_pods(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        with patch("hexawyn.cli.tui.safe_pods", return_value=[]):
            assert tui._fallback_suggestion() is None

    def test_fallback_suggestion_failed_pods(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        pods = [{"name": "crash", "status": "CrashLoopBackOff", "namespace": "default"}]
        with (
            patch("hexawyn.cli.tui.safe_pods", return_value=pods),
            patch("hexawyn.cli.tui.running_pod_count", return_value=0),
            patch("hexawyn.cli.tui.pending_pod_count", return_value=0),
            patch("hexawyn.cli.tui.failed_pod_count", return_value=1),
        ):
            result = tui._fallback_suggestion()
            assert result is not None
            assert "failed" in result.lower()

    def test_fallback_suggestion_pending_pods(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        pods = [{"name": "waiting", "status": "Pending", "namespace": "default"}]
        with (
            patch("hexawyn.cli.tui.safe_pods", return_value=pods),
            patch("hexawyn.cli.tui.running_pod_count", return_value=0),
            patch("hexawyn.cli.tui.pending_pod_count", return_value=1),
            patch("hexawyn.cli.tui.failed_pod_count", return_value=0),
        ):
            result = tui._fallback_suggestion()
            assert result is not None
            assert "pending" in result.lower()

    def test_fallback_suggestion_all_healthy(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        pods = [{"name": "nginx", "status": "Running", "namespace": "default"}]
        with (
            patch("hexawyn.cli.tui.safe_pods", return_value=pods),
            patch("hexawyn.cli.tui.running_pod_count", return_value=1),
            patch("hexawyn.cli.tui.pending_pod_count", return_value=0),
            patch("hexawyn.cli.tui.failed_pod_count", return_value=0),
        ):
            result = tui._fallback_suggestion()
            assert result is not None
            assert "healthy" in result.lower()

    def test_fallback_suggestion_other_pods_returns_narrative(self) -> None:
        """Pods that are neither Running nor Failed (Succeeded/Terminating) must
        still yield a useful suggestion instead of returning None."""
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        pods = [
            {"name": "nginx", "status": "Running", "namespace": "default"},
            {"name": "succeeded-job", "status": "Succeeded", "namespace": "default"},
            {"name": "terminating-pod", "status": "Terminating", "namespace": "default"},
        ]
        with (
            patch("hexawyn.cli.tui.safe_pods", return_value=pods),
            patch("hexawyn.cli.tui.running_pod_count", return_value=1),
            patch("hexawyn.cli.tui.pending_pod_count", return_value=0),
            patch("hexawyn.cli.tui.failed_pod_count", return_value=0),
        ):
            result = tui._fallback_suggestion()
            assert result is not None

    def test_fallback_suggestion_exception_returns_none(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        with patch("hexawyn.cli.tui.safe_pods", side_effect=RuntimeError("boom")):
            assert tui._fallback_suggestion() is None

    def test_generate_ai_suggestion_with_scan_suggestions(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        mock_runtime = MagicMock()
        mock_scan = MagicMock()
        mock_scan.suggestions = [{"value": "Check OOM"}]
        mock_scan.health_score = 50
        mock_runtime.run_startup_scan.return_value = mock_scan

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch("hexawyn.cli.tui.safe_pods", return_value=[]),
        ):
            tui._generate_ai_suggestion()
            assert tui.ai_suggestion == "Check OOM"

    def test_generate_ai_suggestion_falls_back_to_narrative(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        mock_runtime = MagicMock()
        mock_scan = MagicMock()
        mock_scan.suggestions = []
        mock_scan.health_score = 80
        mock_scan.narrative_summary = "Cluster looks good"
        mock_runtime.run_startup_scan.return_value = mock_scan

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch("hexawyn.cli.tui.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.findings.is_error_narrative", return_value=False),
        ):
            tui._generate_ai_suggestion()
            assert tui.ai_suggestion == "Cluster looks good"

    def test_generate_ai_suggestion_handles_exception(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        with patch(
            "hexawyn.application.service.runtime_adapter.get_runtime",
            side_effect=RuntimeError("boom"),
        ):
            tui._generate_ai_suggestion()
            assert tui.ai_suggestion is None

    def test_connect_and_scan_skips_demo_mode(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), demo_mode=True, cluster_name="prod")
        tui._connect_and_scan()

    def test_connect_and_scan_skips_no_context_service(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        tui._connect_and_scan()

    def test_connect_and_scan_with_connection(self) -> None:
        svc = MagicMock()
        status = MagicMock()
        status.connected = True
        svc.startup_status.return_value = status
        tui = self._create_tui(adapter=MagicMock(), context_service=svc, cluster_name="prod")

        with patch("hexawyn.application.service.runtime_adapter.get_runtime") as mock_runtime:
            mock_runtime.return_value = MagicMock()
            tui._connect_and_scan()
            assert tui.startup_status is status
            assert tui.run_startup_scan is True

    def test_connect_and_scan_not_connected(self) -> None:
        svc = MagicMock()
        status = MagicMock()
        status.connected = False
        svc.startup_status.return_value = status
        tui = self._create_tui(adapter=MagicMock(), context_service=svc, cluster_name="prod")
        tui._connect_and_scan()
        assert tui.run_startup_scan is False

    def test_connect_and_scan_handles_exception(self) -> None:
        svc = MagicMock()
        svc.startup_status.side_effect = RuntimeError("boom")
        tui = self._create_tui(adapter=MagicMock(), context_service=svc, cluster_name="prod")
        tui._connect_and_scan()

    def test_refresh_aside_after_connect_with_refresh(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        mock_screen = MagicMock()
        mock_screen._refresh_aside = MagicMock()
        with patch.object(
            HexawynTUI, "screen", new_callable=PropertyMock, return_value=mock_screen
        ):
            tui._refresh_aside_after_connect()
            mock_screen._refresh_aside.assert_called_once()

    def test_refresh_aside_after_connect_no_refresh_method(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        mock_screen = MagicMock(spec=[])
        with patch.object(
            HexawynTUI, "screen", new_callable=PropertyMock, return_value=mock_screen
        ):
            tui._refresh_aside_after_connect()

    def test_generate_ai_suggestion_skips_error_narrative(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        mock_runtime = MagicMock()
        mock_scan = MagicMock()
        mock_scan.suggestions = []
        mock_scan.health_score = 80
        mock_scan.narrative_summary = "Error: cluster down"
        mock_runtime.run_startup_scan.return_value = mock_scan

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch("hexawyn.cli.tui.safe_pods", return_value=[]),
            patch("hexawyn.cli.presentation.findings.is_error_narrative", return_value=True),
            patch.object(tui, "_fallback_suggestion", return_value="fallback"),
        ):
            tui._generate_ai_suggestion()
            assert tui.ai_suggestion == "fallback"

    def test_generate_ai_suggestion_empty_scan_fallback(self) -> None:
        tui = self._create_tui(adapter=MagicMock(), cluster_name="prod")
        mock_runtime = MagicMock()
        mock_scan = MagicMock()
        mock_scan.suggestions = []
        mock_scan.health_score = 0
        mock_scan.narrative_summary = ""
        mock_runtime.run_startup_scan.return_value = mock_scan

        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch("hexawyn.cli.tui.safe_pods", return_value=[]),
            patch.object(tui, "_fallback_suggestion", return_value="default"),
        ):
            tui._generate_ai_suggestion()
            assert tui.ai_suggestion == "default"
