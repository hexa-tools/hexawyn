"""RetrievalGate — heuristic pre-cache classifier.

Decides whether a query needs VSS memory retrieval without any LLM or embeddings.
Uses regex patterns to classify queries as 'needs_memory' (investigation, diagnostic)
or 'skip_memory' (list, count, describe). Classification < 1ms per query.
"""

import re

NEEDS_MEMORY_PATTERNS = [
    r"\b(why|crash|fail|error|debug|diagnose|fix|troubleshoot|investigate)\b",
    r"\b(oom|oomkilled|crashloop|imagepull|pending|notready|evicted|crashloopbackoff)\b",
    r"\b(what('?s| is) (wrong|happening|causing)|root cause|explain)\b",
    r"\b(last (24h|week|month|7 days)|yesterday|history|trend)\b",
]

SKIP_MEMORY_PATTERNS = [
    r"^(list|show|get|count|how many)\s",
    r"\b(what is|version|status of|how much CPU|how much memory)\b",
    r"^(show me|display|print|output)\s",
    r"^(what|which) namespaces\b",
]

MAX_QUERY_LENGTH = 500


class RetrievalGate:
    """Decides if a query needs VSS memory retrieval, without LLM."""

    def should_retrieve(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4
