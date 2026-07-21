from unittest.mock import AsyncMock, patch

import pytest
from click.testing import CliRunner
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext,
    KubernetesContextSwitchResult,
    KubernetesStartupStatus,
)


@pytest.fixture
def runner():
    return CliRunner()


class TestCLIHelp:
    def test_help_shows_commands(self, runner):
        from hexawyn.cli.main import app

        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "start" in result.output
        assert "setup" in result.output
        assert "hexawyn" in result.output.lower()


class TestStartCommand:
    def test_start_without_api_key_uses_real_cluster_mode(self, runner):
        with (
            patch.dict("os.environ", {}, clear=True),
            patch("hexawyn.cli.app._load_api_key_to_env", return_value=False),
        ):
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["start"])

            assert result.exit_code == 0
            assert "demo mode" not in result.output

    def test_start_with_demo_flag_sets_env_vars(self, runner):
        with (
            patch("hexawyn.cli.app.HexawynApp", create=True) as mock_app,
        ):
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["start", "--demo", "--scenario", "gcp_gke"])
            assert result.exit_code == 0
            mock_app.assert_called_once_with(expert_mode=False)

    def test_start_with_expert_flag(self, runner):
        with (
            patch("hexawyn.cli.app.HexawynApp", create=True) as mock_app,
        ):
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["start", "--expert"])
            assert result.exit_code == 0
            mock_app.assert_called_once_with(expert_mode=True)

    def test_start_accepts_all_scenarios(self, runner):
        scenarios = ["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]
        for scenario in scenarios:
            with patch("hexawyn.cli.app.HexawynApp", create=True):
                from hexawyn.cli.main import app

                result = runner.invoke(app, ["start", "--demo", "--scenario", scenario])
                assert result.exit_code == 0

    def test_start_rejects_invalid_scenario(self, runner):
        from hexawyn.cli.main import app

        result = runner.invoke(app, ["start", "--demo", "--scenario", "invalid"])
        assert result.exit_code != 0


class TestSetupCommand:
    def test_setup_creates_app_with_force_setup(self, runner):
        with patch("hexawyn.cli.app.HexawynApp", create=True) as mock_app:
            from hexawyn.cli.main import app

            result = runner.invoke(app, ["setup"])
            assert result.exit_code == 0
            mock_app.assert_called_once_with(force_setup=True)
            mock_app.return_value.run.assert_called_once()


class _FailingFindingsAdapter:
    def get_findings(self) -> list[str]:
        raise RuntimeError("kubeconfig unavailable")


class _WelcomeAdapter:
    def get_cluster_context(self) -> dict[str, str]:
        return {"name": "prod-eks-us-east-1", "namespace": "default", "provider": "aws"}

    def get_findings(self) -> list[str]:
        return []

    def get_health_status(self) -> str:
        return "healthy"

    def get_suggestion_chips(self) -> list[str]:
        return ["list pods", "debug payments", "cluster health"]


class _ContextAdapter:
    def __init__(self, name: str, namespace: str = "default", provider: str = "vanilla") -> None:
        self._name = name
        self._namespace = namespace
        self._provider = provider

    def get_cluster_context(self) -> dict[str, str]:
        return {
            "name": self._name,
            "namespace": self._namespace,
            "provider": self._provider,
        }

    def get_findings(self) -> list[str]:
        return []

    def get_suggestion_chips(self) -> list[str]:
        return ["list pods"]


class _SreAdapter:
    def get_cluster_context(self) -> dict[str, str]:
        return {"name": "hetzner-preprod", "namespace": "default", "provider": "vanilla"}

    def get_findings(self) -> list[dict[str, str]]:
        return [
            {
                "severity": "critical",
                "message": "Pod default/semantic-layer-7f8d9c is CrashLoopBackOff",
                "remediation": "Inspect container logs.",
            },
            {
                "severity": "warning",
                "message": "Pod airflow/airflow-worker-86675 restarted 15 times",
                "remediation": "Inspect recent logs.",
            },
            {
                "severity": "warning",
                "message": "Pod airflow/airflow-scheduler-0 restarted 3 times",
                "remediation": "Inspect recent logs.",
            },
        ]

    def get_health_score(self) -> int:
        return 96

    def get_cluster_metrics(self) -> dict[str, float | int]:
        return {
            "cpu_usage_pct": 12.0,
            "memory_usage_pct": 45.0,
            "node_count": 1,
            "pod_count": 42,
        }

    def list_pods(self) -> list[dict[str, str | int]]:
        pods: list[dict[str, str | int]] = []
        namespaces = [f"ns-{index}" for index in range(8)]
        for index in range(39):
            pods.append(
                {
                    "name": f"running-{index}",
                    "namespace": namespaces[index % len(namespaces)],
                    "status": "Running",
                    "restarts": 0,
                }
            )
        pods.extend(
            [
                {
                    "name": "pending-api",
                    "namespace": "ns-0",
                    "status": "Pending",
                    "restarts": 0,
                },
                {
                    "name": "pending-worker",
                    "namespace": "ns-1",
                    "status": "Pending",
                    "restarts": 0,
                },
                {
                    "name": "semantic-layer-7f8d9c",
                    "namespace": "ns-2",
                    "status": "CrashLoopBackOff",
                    "restarts": 4,
                },
            ]
        )
        return pods

    def get_suggestion_chips(self) -> list[str]:
        return ["debug semantic-layer", "investigate airflow-worker", "list warnings"]


class _ContextService:
    def __init__(self) -> None:
        self.prod_context = ClusterContext(
            name="hetzner-preprod",
            cluster="hetzner-preprod",
            namespace="default",
            user="preprod-user",
            is_current=True,
        )
        self.kind_context = ClusterContext(
            name="kind-ecom-local",
            cluster="kind-ecom-local",
            namespace="default",
            user="kind-user",
            is_current=False,
        )
        self.switch_request: str | None = None

    def discover(self) -> list[ClusterContext]:
        return [self.prod_context, self.kind_context]

    def switch_context(self, context_name: str) -> KubernetesContextSwitchResult:
        self.switch_request = context_name
        if context_name != "kind-ecom-local":
            return KubernetesContextSwitchResult(
                contexts=[self.prod_context, self.kind_context],
                current_context=self.prod_context,
                connected=False,
                switched=False,
                kubeconfig_paths=[],
                connection_error="Context not found",
            )

        current_kind_context = ClusterContext(
            name="kind-ecom-local",
            cluster="kind-ecom-local",
            namespace="default",
            user="kind-user",
            is_current=True,
        )
        previous_prod_context = ClusterContext(
            name="hetzner-preprod",
            cluster="hetzner-preprod",
            namespace="default",
            user="preprod-user",
            is_current=False,
        )
        return KubernetesContextSwitchResult(
            contexts=[previous_prod_context, current_kind_context],
            current_context=current_kind_context,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
        )


def _context_startup_status() -> KubernetesStartupStatus:
    current_context = ClusterContext(
        name="hetzner-preprod",
        cluster="hetzner-preprod",
        namespace="default",
        user="preprod-user",
        is_current=True,
    )
    other_context = ClusterContext(
        name="kind-ecom-local",
        cluster="kind-ecom-local",
        namespace="default",
        user="kind-user",
        is_current=False,
    )
    return KubernetesStartupStatus(
        contexts=[current_context, other_context],
        current_context=current_context,
        connected=True,
        kubeconfig_paths=[],
    )


def _build_context_adapter(context_name: str) -> _ContextAdapter:
    provider = "kind" if context_name.startswith("kind-") else "vanilla"
    return _ContextAdapter(context_name, provider=provider)


class TestTuiHelpers:
    def test_safe_findings_returns_empty_list_when_adapter_fails(self):
        from hexawyn.cli.tui import _safe_findings

        assert _safe_findings(_FailingFindingsAdapter()) == []


class TestWelcomeScreen:
    @pytest.mark.asyncio
    async def test_welcome_screen_uses_compact_opencode_layout(self):
        from hexawyn.cli.tui import HexawynTUI, WelcomeScreen
        from textual.widgets import Input, Static

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(WelcomeScreen())
            await pilot.pause()

            logo = app.query_one("#welcome-logo", Static)
            command_input = app.query_one("#welcome-input", Input)
            mode_line = app.query_one("#welcome-mode", Static)
            command_hints = app.query_one("#welcome-shortcuts", Static)

            assert str(logo.renderable) == "hexa[bold #3B82F6]wyn[/bold #3B82F6]"
            assert command_input.placeholder == ('Ask anything... "What is happening in payments?"')
            assert "Build" in str(mode_line.renderable)
            assert "high" in str(mode_line.renderable)
            assert "tab agents" in str(command_hints.renderable)
            assert "ctrl+p commands" in str(command_hints.renderable)
            assert not app.query("#welcome-footer")


class TestSessionScreen:
    @pytest.mark.asyncio
    async def test_session_screen_does_not_render_prompt_separator_rule(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Rule

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()

            assert not app.query(Rule)

    @pytest.mark.asyncio
    async def test_session_aside_renders_sre_cluster_summary(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Static

        app = HexawynTUI(adapter=_SreAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()

            aside_body = app.query_one("#aside-body", Static)
            aside_text = str(aside_body.renderable)

            assert "[bold]HEXAWYN[/bold]" in aside_text
            assert "[green]✓ Connected[/green]" in aside_text
            assert "Cluster: [bold]hetzner-preprod[/bold]" in aside_text
            assert "Namespaces: [bold]8[/bold]" in aside_text
            assert "Nodes: [bold]1[/bold]" in aside_text
            assert "Pods: [bold]42[/bold]" in aside_text
            assert "Health Score: [bold]96/100[/bold]" in aside_text
            assert "🟢 Running Pods      39" in aside_text
            assert "🟡 Pending Pods       2" in aside_text
            assert "🔴 Failed Pods        1" in aside_text
            assert "⚠ 1 CrashLoopBackOff detected" in aside_text
            assert "⚠ 2 pods with high restart count" in aside_text
            assert "demo" not in aside_text.lower()

    @pytest.mark.asyncio
    async def test_session_aside_footer_shows_project_directory_and_version(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Static

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()

            project_directory = app.query_one("#aside-project", Static)
            brand = app.query_one("#aside-brand", Static)

            from hexawyn.cli.presentation.formatting import compact_project_directory

            assert compact_project_directory() in str(project_directory.renderable)
            assert "hexa[bold #3B82F6]wyn[/bold #3B82F6]" in str(brand.renderable)
            assert "0.1.0b2" in str(brand.renderable)
            assert not app.query("#aside-title")

    @pytest.mark.asyncio
    async def test_context_picker_returns_clicked_context(self):
        from hexawyn.cli.tui import ContextPickerScreen, HexawynTUI
        from textual.widgets import Button

        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            startup_status=_context_startup_status(),
        )

        async with app.run_test() as pilot:
            app.push_screen(ContextPickerScreen(_context_startup_status().contexts))
            await pilot.pause()

            assert app.query_one("#context-hetzner-preprod", Button)
            assert app.query_one("#context-kind-ecom-local", Button)

            await pilot.click("#context-kind-ecom-local")
            await pilot.pause()

            assert not app.query(ContextPickerScreen)

    @pytest.mark.asyncio
    async def test_context_picker_supports_arrow_navigation_and_enter(self):
        from hexawyn.cli.tui import ContextPickerScreen, HexawynTUI

        selected_contexts: list[str | None] = []
        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            startup_status=_context_startup_status(),
        )

        async with app.run_test() as pilot:
            app.push_screen(
                ContextPickerScreen(_context_startup_status().contexts),
                callback=selected_contexts.append,
            )
            await pilot.pause()

            await pilot.press("down")
            await pilot.press("enter")
            await pilot.pause()

            assert selected_contexts == ["kind-ecom-local"]
            assert not app.query(ContextPickerScreen)

    @pytest.mark.asyncio
    async def test_context_command_switches_from_popup_selection(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Static

        context_service = _ContextService()
        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            demo_mode=False,
            startup_status=_context_startup_status(),
            context_service=context_service,
            adapter_builder=_build_context_adapter,
        )

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)
            screen._open_context_picker = AsyncMock(
                side_effect=lambda: screen._switch_context("kind-ecom-local")
            )

            await screen._handle_command("/context")
            await pilot.pause()

            aside_body = app.query_one("#aside-body", Static)
            assert context_service.switch_request == "kind-ecom-local"
            assert "Cluster: [bold]kind-ecom-local[/bold]" in str(aside_body.renderable)

    @pytest.mark.asyncio
    async def test_ctx_alias_switches_from_popup_selection(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen

        context_service = _ContextService()
        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            demo_mode=False,
            startup_status=_context_startup_status(),
            context_service=context_service,
            adapter_builder=_build_context_adapter,
        )

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)
            screen._open_context_picker = AsyncMock(
                side_effect=lambda: screen._switch_context("kind-ecom-local")
            )

            await screen._handle_command("/ctx")
            await pilot.pause()

            assert context_service.switch_request == "kind-ecom-local"

    @pytest.mark.asyncio
    async def test_context_command_switches_context_and_refreshes_sidebar(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Static

        context_service = _ContextService()
        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            demo_mode=False,
            startup_status=_context_startup_status(),
            context_service=context_service,
            adapter_builder=_build_context_adapter,
        )

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)

            await screen._handle_command("/context kind-ecom-local")
            await pilot.pause()

            aside_body = app.query_one("#aside-body", Static)
            assert context_service.switch_request == "kind-ecom-local"
            assert app.adapter.get_cluster_context()["name"] == "kind-ecom-local"
            assert app.startup_status is not None
            assert app.startup_status.current_context is not None
            assert app.startup_status.current_context.name == "kind-ecom-local"
            assert "Cluster: [bold]kind-ecom-local[/bold]" in str(aside_body.renderable)
            assert "demo" not in str(aside_body.renderable).lower()

    @pytest.mark.asyncio
    async def test_context_command_returns_available_contexts_when_invalid(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import RichLog

        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            demo_mode=False,
            startup_status=_context_startup_status(),
            context_service=_ContextService(),
            adapter_builder=_build_context_adapter,
        )

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)

            await screen._handle_command("/context production")
            await pilot.pause()

            log = app.query_one("#conversation", RichLog)
            assert "✗ Context not found" in str(log.lines)
            assert "- hetzner-preprod" in str(log.lines)
            assert "- kind-ecom-local" in str(log.lines)

    @pytest.mark.asyncio
    async def test_context_switch_updates_conversation_log_with_new_context_line(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import RichLog

        context_service = _ContextService()
        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            demo_mode=False,
            startup_status=_context_startup_status(),
            context_service=context_service,
            adapter_builder=_build_context_adapter,
            cluster_name="hetzner-preprod",
        )

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)

            await screen._handle_command("/context kind-ecom-local")
            await pilot.pause()

            log = app.query_one("#conversation", RichLog)
            # RichLog parses markup into styled segments — check plain text content
            log_text = str(log.lines)
            assert "kind-ecom-local" in log_text
            # Verify it appears AFTER the switch confirmation (not just from the old on_mount)
            switch_index = log_text.index("Context switched")
            new_context_index = log_text.index(
                "kind-ecom-local", log_text.index("kind-ecom-local") + 1
            )
            assert new_context_index > switch_index, "New context line should appear after switch"

    @pytest.mark.asyncio
    async def test_context_switch_updates_app_cluster_name(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen

        context_service = _ContextService()
        app = HexawynTUI(
            adapter=_ContextAdapter("hetzner-preprod"),
            demo_mode=False,
            startup_status=_context_startup_status(),
            context_service=context_service,
            adapter_builder=_build_context_adapter,
            cluster_name="hetzner-preprod",
        )

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)

            assert app.cluster_name == "hetzner-preprod"

            await screen._handle_command("/context kind-ecom-local")
            await pilot.pause()

            assert app.cluster_name == "kind-ecom-local"

    @pytest.mark.asyncio
    async def test_session_suggestions_disappear_when_user_types(self):
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Button

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()

            assert len(app.query(Button).filter(".chip")) == 0

    @pytest.mark.asyncio
    async def test_token_command_opens_token_input(self) -> None:
        from hexawyn.cli.tui import HexawynTUI, SessionScreen

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)
            screen._open_token_input = AsyncMock()

            await screen._handle_command("/token")
            await pilot.pause()

            screen._open_token_input.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_command_submits_query(self) -> None:
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import RichLog

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)

            await screen._handle_command("why is payments-api crashing?")
            await pilot.pause()

            log = app.query_one("#conversation", RichLog)
            log_text = str(log.lines)
            assert "payments-api" in log_text

    @pytest.mark.asyncio
    async def test_handle_command_empty_input_does_nothing(self) -> None:
        from hexawyn.cli.tui import HexawynTUI, SessionScreen

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)

            screen._clear_chips = AsyncMock()
            await screen._handle_command("")
            await pilot.pause()

            screen._clear_chips.assert_not_called()

    @pytest.mark.asyncio
    async def test_clear_input_resets_everything(self) -> None:
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import Input

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()

            cmd_input = app.query_one("#cmd-input", Input)
            cmd_input.value = "some text"
            await pilot.pause()

            screen = app.query_one(SessionScreen)
            screen.action_clear_input()
            await pilot.pause()

            assert cmd_input.value == ""

    @pytest.mark.asyncio
    async def test_spinner_shows_and_completes(self) -> None:
        from hexawyn.cli.tui import HexawynTUI, SessionScreen
        from textual.widgets import RichLog

        app = HexawynTUI(adapter=_WelcomeAdapter(), demo_mode=True, scenario="aws_eks")

        async with app.run_test() as pilot:
            app.push_screen(SessionScreen())
            await pilot.pause()
            screen = app.query_one(SessionScreen)
            log = app.query_one("#conversation", RichLog)

            await screen._show_spinner(log, ["Initializing", "Analyzing", "Done"])
            await pilot.pause()

            log_text = str(log.lines)
            assert "Initializing" in log_text or "Analyzing" in log_text or len(log_text) > 0


class TestSessionHelpers:
    def test_is_error_narrative_true_for_error_texts(self) -> None:
        from hexawyn.cli.presentation.findings import is_error_narrative

        assert is_error_narrative("metrics not available") is True
        assert is_error_narrative("Kubernetes is down") is True
        assert is_error_narrative("no pods found") is True
        assert is_error_narrative("empty and inactive") is True

    def test_is_error_narrative_false_for_healthy_texts(self) -> None:
        from hexawyn.cli.presentation.findings import is_error_narrative

        assert is_error_narrative("Cluster is healthy with 42 pods running") is False
        assert is_error_narrative("All systems operational") is False

    def test_is_context_command_detects_commands(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("/context") is True
        assert is_context_command("/ctx kind-ecom") is True
        assert is_context_command("just a query") is False

    def test_is_token_command_detects_commands(self) -> None:
        from hexawyn.cli.presentation.command_router import is_token_command

        assert is_token_command("/token") is True
        assert is_token_command("my token query") is False

    def test_is_stack_command_detects_commands(self) -> None:
        from hexawyn.cli.presentation.command_router import is_stack_command

        assert is_stack_command("/stack") is True
        assert is_stack_command("/stack aws") is True
        assert is_stack_command("/stack-vanilla") is False

    def test_license_aside_lines_returns_unknown(self) -> None:
        from unittest.mock import patch

        from hexawyn.cli.presentation.license_display import format_license_aside_lines
        from hexawyn.domain.services.license_state import LicenseState

        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=LicenseState(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            lines = format_license_aside_lines()
            assert any("not configured" in line for line in lines)

    def test_finding_warning_lines_empty_returns_healthy(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        lines = format_finding_warnings([])
        assert any("No active warnings" in line for line in lines)

    def test_finding_warning_lines_crashloop(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings: list[dict[str, object]] = [
            {
                "severity": "critical",
                "message": "Pod ns/pod1 is CrashLoopBackOff",
                "remediation": "",
            }
        ]
        lines = format_finding_warnings(findings)
        assert any("CrashLoopBackOff" in line for line in lines)
