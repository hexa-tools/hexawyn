from operator import add
from typing import Annotated, TypedDict

from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.domain.models.investigation import InvestigationResult, InvestigationStatus
from hexawyn.domain.models.semantic import SemanticCheckResult


class AgentState(TypedDict):
    # ── Input ──────────────────────────────────────────────
    query: str  # raw user query
    cluster_context: ClusterContext  # current cluster + provider

    # ── Intent ─────────────────────────────────────────────
    intent: str  # parsed intent category
    tool_name: str  # MCP tool to call
    tool_args: dict[str, object]  # arguments for the MCP tool

    # ── Cache ──────────────────────────────────────────────
    cache_hit: bool  # True if DuckDB VSS found a match
    cached_result: InvestigationResult | None

    # ── Tool output ────────────────────────────────────────
    tool_output: dict[str, object]  # raw MCP tool response

    # ── LLM ────────────────────────────────────────────────
    llm_response: str  # raw LLM answer
    retry_count: int  # number of generate_response retries

    # ── Verification ───────────────────────────────────────
    checker_result: SemanticCheckResult | None
    judge_result: SemanticCheckResult | None

    # ── Output ─────────────────────────────────────────────
    final_result: InvestigationResult | None
    suggestions: Annotated[list[str], add]  # suggestion chips (accumulated)
    status: InvestigationStatus
    error: str | None
