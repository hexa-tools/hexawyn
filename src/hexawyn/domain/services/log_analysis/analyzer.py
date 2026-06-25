from hexawyn.domain.models.constants import (
    LogAnalysisConstants,
    PodPrioritizationConstants,
)

_log = LogAnalysisConstants()
_pod = PodPrioritizationConstants()


class AdaptiveLogProcessor:
    """Manages token budget for LLM-bound log processing.

    Enforces a safety buffer on the max budget to prevent
    overshooting context limits. Tracks consumption across multiple
    operations and provides budget-aware decisions.

    Prediction helpers estimate token usage and prioritize pods
    to focus processing on the most relevant sources first.
    """

    def __init__(self, max_token_budget: int | None = None) -> None:
        self.max_token_budget = max_token_budget or _log.token_budget
        self.safety_buffer: float = _log.token_safety_buffer
        self.used_tokens: int = 0

    @property
    def effective_budget(self) -> int:
        return int(self.max_token_budget * self.safety_buffer)

    def can_process_more(self, estimated_tokens: int) -> bool:
        return (self.used_tokens + estimated_tokens) <= self.effective_budget

    def record_usage(self, actual_tokens: int) -> None:
        if not self.can_process_more(actual_tokens):
            raise ValueError(
                f"Token budget exceeded: {self.used_tokens + actual_tokens} "
                f"> {self.effective_budget} (effective budget)"
            )
        self.used_tokens += actual_tokens

    def get_remaining_budget(self) -> int:
        return max(0, self.effective_budget - self.used_tokens)

    def get_usage_percentage(self) -> float:
        return min(100.0, (self.used_tokens / self.effective_budget) * 100)

    def get_usage_ratio(self) -> float:
        return self.get_usage_percentage() / 100.0

    @staticmethod
    def estimate_tokens_from_lines(lines: list[str]) -> int:
        if not lines:
            return 0
        sample = lines[: min(_log.token_sample_max_lines, len(lines))]
        avg_chars = sum(len(line) for line in sample) / len(sample)
        tokens_per_line = max(1, avg_chars / _log.chars_per_token_divisor)
        return int(len(lines) * tokens_per_line)

    @staticmethod
    def prioritize_pods(
        pods: list[dict[str, str | int]],
    ) -> list[dict[str, str | int]]:
        def _priority(pod: dict[str, str | int]) -> int:
            score = 0
            status = str(pod.get("status", ""))
            restart_count = int(pod.get("restart_count", 0))

            if status in (
                "CrashLoopBackOff",
                "Error",
                "ImagePullBackOff",
                "OOMKilled",
            ):
                score += _pod.failed_status_score
            elif status in ("Pending", "Terminating"):
                score += _pod.pending_status_score
            elif status != "Running":
                score += _pod.other_status_score

            score += min(
                restart_count * _pod.restart_weight,
                _pod.max_restart_bonus,
            )
            return score

        return sorted(pods, key=_priority, reverse=True)
