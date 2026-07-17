from collections.abc import Callable
from typing import Any, Protocol

from textual.app import App
from textual.binding import Binding

from hexawyn.adapters.secondary.adapter_factory import build_adapters
from hexawyn.cli.presentation.asides import (
    failed_pod_count,
    pending_pod_count,
    running_pod_count,
    safe_pods,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
    KubernetesStartupStatus,
)


class ContextService(Protocol):
    def discover(self) -> list[KubernetesClusterContext]:
        """Return available Kubernetes contexts."""

    def switch_context(self, context_name: str) -> KubernetesContextSwitchResult:
        """Switch Hexawyn runtime context."""


class HexawynTUI(App[None]):
    CSS = """
    Header {
        display: none;
    }

    Screen {
        background: #05070d;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "clear_input", "Cancel", show=False),
        Binding("ctrl+q", "quit", "Quit", show=False),
    ]

    def __init__(
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def _generate_ai_suggestion(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.cli.screens.session import _is_error_narrative

                if not _is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def _fallback_suggestion(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            return None
        except Exception:
            return None

    def on_mount(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def _connect_and_scan(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def _refresh_aside_after_connect(self) -> None:
        try:
            if hasattr(self.screen, "_refresh_aside"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def action_clear_input(self) -> None:
        if isinstance(self.screen, WelcomeScreen | SessionScreen):
            self.screen.action_clear_input()


# ── Backwards-compatible re-exports ──────────────────────────────────────────
# Preserved so existing imports from hexawyn.cli.tui continue to work.
# ruff: noqa: F401, E402
from hexawyn.cli.presentation.asides import (
    crashloop_finding_count as _crashloop_finding_count,
)
from hexawyn.cli.presentation.asides import (
    failed_pod_count as _failed_pod_count,
)
from hexawyn.cli.presentation.asides import (
    finding_message as _finding_message,
)
from hexawyn.cli.presentation.asides import (
    issue_name as _issue_name,
)
from hexawyn.cli.presentation.asides import (
    issue_reason as _issue_reason,
)
from hexawyn.cli.presentation.asides import (
    kubectl_current_context as _kubectl_current_context,
)
from hexawyn.cli.presentation.asides import (
    mapping_int as _mapping_int,
)
from hexawyn.cli.presentation.asides import (
    mapping_text as _mapping_text,
)
from hexawyn.cli.presentation.asides import (
    namespace_count as _namespace_count,
)
from hexawyn.cli.presentation.asides import (
    pending_pod_count as _pending_pod_count,
)
from hexawyn.cli.presentation.asides import (
    restarting_finding_count as _restarting_finding_count,
)
from hexawyn.cli.presentation.asides import (
    running_pod_count as _running_pod_count,
)
from hexawyn.cli.presentation.asides import (
    safe_findings as _safe_findings,
)
from hexawyn.cli.presentation.asides import (
    safe_health_score as _safe_health_score,
)
from hexawyn.cli.presentation.asides import (
    safe_metrics as _safe_metrics,
)
from hexawyn.cli.presentation.asides import (
    safe_pods as _safe_pods,
)
from hexawyn.cli.presentation.asides import (
    safe_suggestions as _safe_suggestions,
)
from hexawyn.cli.presentation.constants import (
    _LOGO_BANNER,
    _POD_STATUS_COLORS,
)
from hexawyn.cli.presentation.formatting import (
    app_version as _app_version,
)
from hexawyn.cli.presentation.formatting import (
    compact_project_directory as _compact_project_directory,
)
from hexawyn.cli.presentation.formatting import (
    connection_line as _connection_line,
)
from hexawyn.cli.presentation.formatting import (
    context_line as _context_line,
)
from hexawyn.cli.presentation.formatting import (
    context_list_lines as _context_list_lines,
)
from hexawyn.cli.presentation.formatting import (
    current_context_from as _current_context_from,
)
from hexawyn.cli.presentation.formatting import (
    missing_context_lines as _missing_context_lines,
)
from hexawyn.cli.presentation.formatting import (
    startup_lines as _startup_lines,
)
from hexawyn.cli.presentation.formatting import (
    startup_status_from_switch as _startup_status_from_switch,
)
from hexawyn.cli.screens.context_picker import ContextPickerScreen
from hexawyn.cli.screens.provider_setup import ProviderSetupScreen
from hexawyn.cli.screens.session import SessionScreen
from hexawyn.cli.screens.welcome import WelcomeScreen
