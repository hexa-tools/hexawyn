from typing import Any

from hexawyn.adapters.secondary.runtime_client import RuntimeClient
from hexawyn.application.ports.driven.runtime_port import (
    InvestigationOutput,
    RuntimePort,
    StartupScanResult,
)
from hexawyn.domain.models.cluster import ClusterContext


class HttpRuntimeAdapter(RuntimePort):
    def __init__(self, endpoint: str) -> None:
        self._client = RuntimeClient(endpoint=endpoint)

    def close(self) -> None:
        self._client.close()

    def set_adapter(self, adapter: Any) -> None:
        pass

    def run_investigation(self, query: str, cluster_context: ClusterContext) -> InvestigationOutput:
        try:
            job_id = self._client.post_investigation(
                query=query,
                cluster_name=cluster_context.name,
                provider=cluster_context.provider.value,
            )
            response = self._client.poll_investigation(job_id)
            return self._translate_response(response)
        except Exception as exc:
            return InvestigationOutput(
                answer="",
                cause="",
                solution="",
                status="error",
                suggestions=[],
                error=str(exc),
            )

    def run_startup_scan(self, cluster_name: str) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Startup scan not available via HTTP runtime.",
            provider_badge="[remote]",
            top_issues=["Startup scan is only available in embedded mode."],
        )

    def _translate_response(self, response: dict[str, object]) -> InvestigationOutput:
        api_status = str(response.get("status", "error"))
        result = response.get("result")
        if not isinstance(result, dict):
            return InvestigationOutput(
                answer="",
                cause="",
                solution="",
                status="error" if api_status == "failed" else api_status,
                suggestions=[],
                error="No result in response",
            )
        return InvestigationOutput(
            answer=str(result.get("answer", "")),
            cause=str(result.get("cause", "")),
            solution=str(result.get("solution", "")),
            status="error" if api_status == "failed" else str(result.get("status", api_status)),
            suggestions=_extract_string_list(result.get("suggestions")),
            error=str(result.get("error")) if result.get("error") else None,
        )


def _extract_string_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    return []
