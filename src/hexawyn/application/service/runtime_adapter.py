from typing import Any

from hexawyn.application.ports.driven.runtime_port import (
    InvestigationOutput,
    QuotaCheckResult,
    RuntimePort,
    StartupScanResult,
)
from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.infrastructure.config.config_manager import (
    get_runtime_endpoint,
    get_runtime_mode,
)


class StubRuntimeAdapter(RuntimePort):
    def set_adapter(self, adapter: Any) -> None:
        pass

    def run_investigation(self, query: str, cluster_context: ClusterContext) -> InvestigationOutput:
        return InvestigationOutput(
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
        )

    def run_startup_scan(self, cluster_name: str) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def check_quota(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=-1)

    def increment_quota(self) -> None:
        pass

    def sync_tools(self, tools_payload: list[dict[str, object]]) -> None:
        pass


_runtime_instance: RuntimePort | None = None


def get_runtime() -> RuntimePort:
    global _runtime_instance
    if _runtime_instance is None:
        _runtime_instance = _resolve_runtime()
    return _runtime_instance


def set_runtime(runtime: RuntimePort) -> None:
    global _runtime_instance
    _runtime_instance = runtime


def _resolve_runtime() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()
