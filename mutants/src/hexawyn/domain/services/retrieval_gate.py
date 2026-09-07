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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRetrievalGateǁshould_retrieve__mutmut: MutantDict = {}  # type: ignore


class RetrievalGate:
    """Decides if a query needs VSS memory retrieval, without LLM."""

    @_mutmut_mutated(mutants_xǁRetrievalGateǁshould_retrieve__mutmut)
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

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_orig(self, query: str) -> bool:
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

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_1(self, query: str) -> bool:
        lowered = None

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

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_2(self, query: str) -> bool:
        lowered = query.upper().strip()

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

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_3(self, query: str) -> bool:
        lowered = query.lower().strip()

        if lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_4(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return True

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_5(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) >= MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_6(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = None

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_7(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(None, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_8(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, None):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_9(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_10(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, ):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_11(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_12(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(None, lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_13(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, None):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_14(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(lowered):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_15(self, query: str) -> bool:
        lowered = query.lower().strip()

        if not lowered:
            return False

        if len(lowered) > MAX_QUERY_LENGTH:
            lowered = lowered[:MAX_QUERY_LENGTH]

        for pattern in NEEDS_MEMORY_PATTERNS:
            if re.search(pattern, lowered):
                return True

        for pattern in SKIP_MEMORY_PATTERNS:
            if re.search(pattern, ):
                return False

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_16(self, query: str) -> bool:
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
                return True

        return len(lowered.split()) >= 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_17(self, query: str) -> bool:
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

        return len(lowered.split()) > 4  # noqa: PLR2004

    def xǁRetrievalGateǁshould_retrieve__mutmut_18(self, query: str) -> bool:
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

        return len(lowered.split()) >= 5  # noqa: PLR2004

mutants_xǁRetrievalGateǁshould_retrieve__mutmut['_mutmut_orig'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_1'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_2'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_3'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_4'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_5'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_6'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_7'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_8'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_9'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_10'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_11'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_12'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_13'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_14'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_15'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_16'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_17'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRetrievalGateǁshould_retrieve__mutmut['xǁRetrievalGateǁshould_retrieve__mutmut_18'] = RetrievalGate.xǁRetrievalGateǁshould_retrieve__mutmut_18 # type: ignore # mutmut generated
