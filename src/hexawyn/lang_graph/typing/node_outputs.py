from typing import TypedDict

from hexawyn.domain.models.semantic import SemanticCheckResult


class ParseIntentOutput(TypedDict):
    intent: str
    tool_name: str
    tool_args: dict[str, str]
    retry_count: int


class CheckCacheOutput(TypedDict):
    cache_hit: bool


class RetrieveContextOutput(TypedDict):
    tool_output: dict[str, str]


class ExecuteToolOutput(TypedDict):
    tool_output: dict[str, str]


class GenerateResponseOutput(TypedDict):
    llm_response: str
    retry_count: int


class SemanticCheckerOutput(TypedDict):
    checker_result: SemanticCheckResult | None


class LLMJudgeOutput(TypedDict):
    judge_result: SemanticCheckResult | None


class StoreMemoryOutput(TypedDict):
    pass


class FormatResponseOutput(TypedDict):
    pass
