from collections.abc import Callable
from typing import Any

from hexawyn.adapters.secondary.runtime_client import RuntimeClient
from hexawyn.application.ports.driven.runtime_port import (
    InvestigationOutput,
    QuotaCheckResult,
    RuntimePort,
    StartupScanResult,
)
from hexawyn.domain.models.cluster import ClusterContext


class HttpRuntimeAdapter(RuntimePort):
    def __init__(self, endpoint: str) -> None:
        from hexawyn.infrastructure.config.config_manager import get_api_key  # hexa-lazy-import

        self._client = RuntimeClient(endpoint=endpoint, api_key=get_api_key())
        self._adapter: Any = None

    def close(self) -> None:
        self._client.close()

    def set_adapter(self, adapter: Any) -> None:
        self._adapter = adapter

    def _fetch_pods(self) -> list[dict[str, object]]:
        result: list[dict[str, object]] = []
        if self._adapter is None or not hasattr(self._adapter, "list_pods"):
            result = []
        else:
            try:
                result = [dict(p) for p in self._adapter.list_pods()]
            except Exception:
                pass
        with open("/tmp/hexawyn_pods.log", "a") as f:
            f.write(
                f"adapter={type(self._adapter).__name__ if self._adapter else 'None'} pods={len(result)}\n"  # noqa: E501
            )
        return result

    def run_investigation(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        try:
            provider_raw = getattr(cluster_context, "provider", "vanilla")
            provider = getattr(provider_raw, "value", str(provider_raw))

            report_output: dict[str, object] = {}
            for node_name, output in self._client.stream_investigation(
                query=query,
                cluster_name=getattr(cluster_context, "name", "unknown"),
                provider=provider,
                pods=self._fetch_pods(),
                conversation_history=conversation_history,
            ):
                if on_progress:
                    label = node_name.title()
                    on_progress(node_name, label)
                if node_name == "report":
                    report_output = output if isinstance(output, dict) else {}
                elif node_name == "error":
                    return InvestigationOutput(
                        answer="",
                        cause="",
                        solution="",
                        status="error",
                        suggestions=[],
                        error=str(output.get("error", "stream error")),
                        embedding=[],
                        usage={},
                        predicted_intents=[],
                    )

            usage_raw = report_output.get("usage")
            usage_dict: dict[str, int | str] = {}
            if isinstance(usage_raw, dict):
                usage_dict = {
                    str(k): int(v)
                    if isinstance(v, int | float) and not isinstance(v, bool)
                    else str(v)
                    for k, v in usage_raw.items()
                }

            return InvestigationOutput(
                answer=str(report_output.get("llm_response", "")),
                cause=str(report_output.get("cause", "")),
                solution=str(report_output.get("solution", "")),
                status=str(report_output.get("status", "complete")),
                suggestions=list(report_output.get("suggestions", []))  # type: ignore[call-overload]
                if isinstance(report_output.get("suggestions"), list)
                else [],
                error=None,
                embedding=_extract_float_list(report_output.get("embedding")),
                usage=usage_dict,
                predicted_intents=_extract_string_list(report_output.get("predicted_intents")),
            )
        except Exception as exc:
            return InvestigationOutput(
                answer="",
                cause="",
                solution="",
                status="error",
                suggestions=[],
                error=str(exc),
                embedding=[],
                usage={},
                predicted_intents=[],
            )

    def check_quota(self) -> QuotaCheckResult:
        try:
            raw = self._client.check_quota()
            allowed_val = raw.get("allowed", True)
            used_val = raw.get("used", 0)
            limit_val = raw.get("limit", -1)
            remaining_val = raw.get("remaining", -1)
            return QuotaCheckResult(
                allowed=bool(allowed_val),
                used=int(str(used_val)) if used_val is not None else 0,
                limit=int(str(limit_val)) if limit_val is not None else -1,
                remaining=int(str(remaining_val)) if remaining_val is not None else -1,
            )
        except Exception:
            return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=-1)

    def increment_quota(self) -> None:
        try:
            self._client.increment_quota()
        except Exception:
            pass

    def run_startup_scan(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        try:
            local_pods = pods if pods is not None else self._fetch_pods()
            raw = self._client.startup_scan(cluster_name, pods=local_pods)
            suggestions_raw = raw.get("suggestions")
            suggestions: list[dict[str, str]] = []
            if isinstance(suggestions_raw, list):
                for s in suggestions_raw:
                    if isinstance(s, dict):
                        suggestions.append(
                            {
                                "label": str(s.get("label", "")),
                                "value": str(s.get("value", "")),
                            }
                        )
            return StartupScanResult(
                health_score=int(str(raw.get("health_score", 0))),
                narrative_summary=str(raw.get("narrative_summary", "")),
                provider_badge=str(raw.get("provider_badge", "[remote]")),
                top_issues=_extract_string_list(raw.get("top_issues")),
                suggestions=suggestions,
                provider=str(raw.get("provider", "")),
                provider_display=str(raw.get("provider_display", "")),
            )
        except Exception:
            return StartupScanResult(
                health_score=0,
                narrative_summary="Startup scan unavailable — control plane reachable?",
                provider_badge="[remote]",
                top_issues=["Could not reach control plane for startup scan."],
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
                embedding=[],
                usage={},
                predicted_intents=[],
            )
        return InvestigationOutput(
            answer=str(result.get("answer", "")),
            cause=str(result.get("cause", "")),
            solution=str(result.get("solution", "")),
            status="error" if api_status == "failed" else str(result.get("status", api_status)),
            suggestions=_extract_string_list(result.get("suggestions")),
            error=str(result.get("error")) if result.get("error") else None,
            embedding=_extract_float_list(result.get("embedding")),
            usage={},
            predicted_intents=_extract_string_list(result.get("predicted_intents")),
        )


def _extract_string_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def _extract_float_list(value: object) -> list[float]:
    if isinstance(value, list):
        result: list[float] = []
        for item in value:
            if isinstance(item, int | float) and not isinstance(item, bool):
                result.append(float(item))
        return result
    return []
