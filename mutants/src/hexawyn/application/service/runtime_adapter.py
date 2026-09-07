from collections.abc import Callable
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut: MutantDict = {}  # type: ignore


class StubRuntimeAdapter(RuntimePort):
    def set_adapter(self, adapter: Any) -> None:
        pass

    @_mutmut_mutated(mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut)
    def run_investigation(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_orig(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_1(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer=None,  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_2(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause=None,
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_3(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution=None,
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_4(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status=None,
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_5(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=None,
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_6(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error=None,
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_7(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=None,
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_8(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage=None,
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_9(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_10(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_11(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_12(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_13(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_14(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_15(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_16(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_17(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="XXRuntime not available — install hexawyn-control-plane for AI-powered investigations.XX",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_18(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="runtime not available — install hexawyn-control-plane for ai-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_19(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="RUNTIME NOT AVAILABLE — INSTALL HEXAWYN-CONTROL-PLANE FOR AI-POWERED INVESTIGATIONS.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_20(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="XXXX",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_21(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="XXXX",
            status="unavailable",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_22(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="XXunavailableXX",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_23(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="UNAVAILABLE",
            suggestions=[],
            error="LangGraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_24(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="XXLangGraph runtime has been moved to the private repository.XX",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_25(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="langgraph runtime has been moved to the private repository.",
            embedding=[],
            usage={},
        )

    def xǁStubRuntimeAdapterǁrun_investigation__mutmut_26(
        self,
        query: str,
        cluster_context: ClusterContext,
        conversation_history: list[dict[str, str]] | None = None,
        on_progress: Callable[[str, str], None] | None = None,
    ) -> InvestigationOutput:
        return InvestigationOutput(  # type: ignore
            answer="Runtime not available — install hexawyn-control-plane for AI-powered investigations.",  # noqa: E501
            cause="",
            solution="",
            status="unavailable",
            suggestions=[],
            error="LANGGRAPH RUNTIME HAS BEEN MOVED TO THE PRIVATE REPOSITORY.",
            embedding=[],
            usage={},
        )

    @_mutmut_mutated(mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut)
    def run_startup_scan(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_orig(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_1(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=None,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_2(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary=None,
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_3(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge=None,
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_4(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=None,
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_5(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_6(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_7(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_8(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_9(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=1,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_10(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="XXRuntime not available — install hexawyn-control-plane.XX",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_11(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_12(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="RUNTIME NOT AVAILABLE — INSTALL HEXAWYN-CONTROL-PLANE.",
            provider_badge="[offline]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_13(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="XX[offline]XX",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_14(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[OFFLINE]",
            top_issues=["Runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_15(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["XXRuntime unavailable — startup scan requires hexawyn-control-planeXX"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_16(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["runtime unavailable — startup scan requires hexawyn-control-plane"],
        )

    def xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_17(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> StartupScanResult:
        return StartupScanResult(
            health_score=0,
            narrative_summary="Runtime not available — install hexawyn-control-plane.",
            provider_badge="[offline]",
            top_issues=["RUNTIME UNAVAILABLE — STARTUP SCAN REQUIRES HEXAWYN-CONTROL-PLANE"],
        )

    @_mutmut_mutated(mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut)
    def check_quota(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_orig(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_1(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=None, used=0, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_2(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=None, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_3(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=None, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_4(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=None)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_5(self) -> QuotaCheckResult:
        return QuotaCheckResult(used=0, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_6(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_7(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_8(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, )

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_9(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=False, used=0, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_10(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=1, limit=-1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_11(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=+1, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_12(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-2, remaining=-1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_13(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=+1)

    def xǁStubRuntimeAdapterǁcheck_quota__mutmut_14(self) -> QuotaCheckResult:
        return QuotaCheckResult(allowed=True, used=0, limit=-1, remaining=-2)

    def increment_quota(self) -> None:
        pass

mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['_mutmut_orig'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_1'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_2'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_3'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_4'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_5'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_6'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_7'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_8'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_9'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_10'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_11'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_12'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_13'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_14'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_15'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_16'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_17'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_18'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_19'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_20'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_21'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_22'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_23'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_24'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_25'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_investigation__mutmut['xǁStubRuntimeAdapterǁrun_investigation__mutmut_26'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_investigation__mutmut_26 # type: ignore # mutmut generated

mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['_mutmut_orig'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_1'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_2'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_3'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_4'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_5'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_6'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_7'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_8'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_9'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_10'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_11'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_12'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_13'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_14'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_15'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_16'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁrun_startup_scan__mutmut['xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_17'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁrun_startup_scan__mutmut_17 # type: ignore # mutmut generated

mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['_mutmut_orig'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_1'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_2'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_3'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_4'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_5'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_6'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_7'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_8'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_9'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_10'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_11'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_12'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_13'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStubRuntimeAdapterǁcheck_quota__mutmut['xǁStubRuntimeAdapterǁcheck_quota__mutmut_14'] = StubRuntimeAdapter.xǁStubRuntimeAdapterǁcheck_quota__mutmut_14 # type: ignore # mutmut generated


_runtime_instance: RuntimePort | None = None
mutants_x_get_runtime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_runtime__mutmut)
def get_runtime() -> RuntimePort:
    global _runtime_instance
    if _runtime_instance is None:
        _runtime_instance = _resolve_runtime()
    return _runtime_instance


def x_get_runtime__mutmut_orig() -> RuntimePort:
    global _runtime_instance
    if _runtime_instance is None:
        _runtime_instance = _resolve_runtime()
    return _runtime_instance


def x_get_runtime__mutmut_1() -> RuntimePort:
    global _runtime_instance
    if _runtime_instance is not None:
        _runtime_instance = _resolve_runtime()
    return _runtime_instance


def x_get_runtime__mutmut_2() -> RuntimePort:
    global _runtime_instance
    if _runtime_instance is None:
        _runtime_instance = None
    return _runtime_instance

mutants_x_get_runtime__mutmut['_mutmut_orig'] = x_get_runtime__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_runtime__mutmut['x_get_runtime__mutmut_1'] = x_get_runtime__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_runtime__mutmut['x_get_runtime__mutmut_2'] = x_get_runtime__mutmut_2 # type: ignore # mutmut generated
mutants_x_set_runtime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_set_runtime__mutmut)
def set_runtime(runtime: RuntimePort) -> None:
    global _runtime_instance
    _runtime_instance = runtime


def x_set_runtime__mutmut_orig(runtime: RuntimePort) -> None:
    global _runtime_instance
    _runtime_instance = runtime


def x_set_runtime__mutmut_1(runtime: RuntimePort) -> None:
    global _runtime_instance
    _runtime_instance = None

mutants_x_set_runtime__mutmut['_mutmut_orig'] = x_set_runtime__mutmut_orig # type: ignore # mutmut generated
mutants_x_set_runtime__mutmut['x_set_runtime__mutmut_1'] = x_set_runtime__mutmut_1 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__resolve_runtime__mutmut)
def _resolve_runtime() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_orig() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_1() -> RuntimePort:
    mode = None
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_2() -> RuntimePort:
    mode = get_runtime_mode()
    if mode != "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_3() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "XXremoteXX":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_4() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "REMOTE":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_5() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = None
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_6() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_7() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                None
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_8() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "XXRuntime mode is 'remote' but no endpoint configured.\nXX"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_9() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_10() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "RUNTIME MODE IS 'REMOTE' BUT NO ENDPOINT CONFIGURED.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_11() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "XXAdd 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml.XX"
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_12() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_13() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "ADD 'ENDPOINT: HTTP://LOCALHOST:8000' UNDER 'RUNTIME:' IN CONFIG.YAML."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=endpoint)
    return StubRuntimeAdapter()


def x__resolve_runtime__mutmut_14() -> RuntimePort:
    mode = get_runtime_mode()
    if mode == "remote":
        endpoint = get_runtime_endpoint()
        if not endpoint:
            raise ValueError(
                "Runtime mode is 'remote' but no endpoint configured.\n"
                "Add 'endpoint: http://localhost:8000' under 'runtime:' in config.yaml."
            )
        from hexawyn.application.service.http_runtime_adapter import (
            HttpRuntimeAdapter,  # hexa-lazy-import
        )

        return HttpRuntimeAdapter(endpoint=None)
    return StubRuntimeAdapter()

mutants_x__resolve_runtime__mutmut['_mutmut_orig'] = x__resolve_runtime__mutmut_orig # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_1'] = x__resolve_runtime__mutmut_1 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_2'] = x__resolve_runtime__mutmut_2 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_3'] = x__resolve_runtime__mutmut_3 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_4'] = x__resolve_runtime__mutmut_4 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_5'] = x__resolve_runtime__mutmut_5 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_6'] = x__resolve_runtime__mutmut_6 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_7'] = x__resolve_runtime__mutmut_7 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_8'] = x__resolve_runtime__mutmut_8 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_9'] = x__resolve_runtime__mutmut_9 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_10'] = x__resolve_runtime__mutmut_10 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_11'] = x__resolve_runtime__mutmut_11 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_12'] = x__resolve_runtime__mutmut_12 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_13'] = x__resolve_runtime__mutmut_13 # type: ignore # mutmut generated
mutants_x__resolve_runtime__mutmut['x__resolve_runtime__mutmut_14'] = x__resolve_runtime__mutmut_14 # type: ignore # mutmut generated
