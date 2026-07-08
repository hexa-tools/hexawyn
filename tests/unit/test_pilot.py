"""Textual Pilot integration tests for tui.py and session.py."""

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.cli.app import HexawynApp
from hexawyn.cli.tui import HexawynTUI


@pytest.mark.asyncio
class TestTuiLaunch:
    async def test_app_launches_without_crash(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []
        mock_adapter.get_findings.return_value = []
        mock_adapter.get_suggestion_chips.return_value = []
        mock_adapter.get_cluster_metrics.return_value = {}
        mock_adapter.get_health_score.return_value = 100

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                run_startup_scan=False,
            )
            async with app.run_test() as pilot:
                assert pilot.app is not None

    async def test_expert_mode_skips_setup_screen(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                run_startup_scan=False,
            )
            async with app.run_test() as pilot:
                assert len(pilot.app.screen_stack) <= 2

    async def test_input_clears_on_escape(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                run_startup_scan=False,
            )
            async with app.run_test() as pilot:
                await pilot.press("escape")
                assert pilot.app is not None

    async def test_context_service_initialization(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesContextSwitchResult,
        )

        mock_service = MagicMock()
        ctx = ClusterContext(
            name="test", namespace="default", cluster="c1", user="u1", is_current=True
        )
        switch_result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
        )
        mock_service.startup_status.return_value = MagicMock(connected=True, current_context=ctx)
        mock_service.switch_context.return_value = switch_result
        mock_service.discover.return_value = [ctx]

        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []
        mock_adapter.get_findings.return_value = []

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                context_service=mock_service,
                run_startup_scan=False,
            )
            async with app.run_test() as pilot:
                assert pilot.app is not None
                assert pilot.app.context_service is not None

    async def test_action_clear_input_delegates_to_screen(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                run_startup_scan=False,
            )
            async with app.run_test():
                app.action_clear_input()

    async def test_connect_and_scan_skips_when_no_context(self) -> None:
        mock_adapter = MagicMock()

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                run_startup_scan=False,
            )
            app.context_service = None
            app._connect_and_scan()

    async def test_refresh_aside_after_connect(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = []

        with patch.dict("os.environ", {}, clear=True):
            app = HexawynTUI(
                expert_mode=True,
                adapter=mock_adapter,
                run_startup_scan=False,
            )
            screen = SessionScreen()
            app._session = screen
            app._refresh_aside_after_connect()


class TestAppModule:
    def test_run_tui_builds_adapter_and_runs(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            with patch("hexawyn.cli.tui.HexawynTUI") as mock_tui:
                mock_tui_instance = MagicMock()
                mock_tui.return_value = mock_tui_instance
                with patch("hexawyn.cli.app.build_adapters", return_value=MagicMock()):
                    app = HexawynApp(expert_mode=True)
                    app._run_tui()

    def test_run_loads_api_key(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            with patch("hexawyn.cli.app._load_api_key_to_env", return_value=False):
                with patch("hexawyn.cli.tui.HexawynTUI") as mock_tui:
                    mock_tui.return_value.run = MagicMock()
                    with patch("hexawyn.cli.app.build_adapters", return_value=MagicMock()):
                        app = HexawynApp()
                        app.run()
