from hexawyn.domain.models.cache import CacheEntry


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCacheL1Repositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCacheL1Repositoryǁget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCacheL1Repositoryǁset__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCacheL1Repositoryǁinvalidate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCacheL1Repositoryǁsize__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCacheL1Repositoryǁevict_expired__mutmut: MutantDict = {}  # type: ignore


class CacheL1Repository:
    """
    In-memory Cache L1 repository — exact match by query hash.

    Storage: Python dict (not DuckDB — must be sub-millisecond).
    Scope: current hexawyn session only (cleared on restart).
    TTL: 5 minutes per entry (enforced by CacheEntry.is_valid).

    Thread safety: not required — hexawyn is single-user CLI.

    Used by:
    - cache_manager.get_l1() → called by check_cache LangGraph node
    - cache_manager.set_l1() → called by store_memory LangGraph node
    """

    @_mutmut_mutated(mutants_xǁCacheL1Repositoryǁ__init____mutmut)
    def __init__(self) -> None:
        self._store: dict[str, CacheEntry] = {}

    def xǁCacheL1Repositoryǁ__init____mutmut_orig(self) -> None:
        self._store: dict[str, CacheEntry] = {}

    def xǁCacheL1Repositoryǁ__init____mutmut_1(self) -> None:
        self._store: dict[str, CacheEntry] = None

    @_mutmut_mutated(mutants_xǁCacheL1Repositoryǁget__mutmut)
    def get(self, query_hash: str) -> CacheEntry | None:
        entry = self._store.get(query_hash)
        if entry is None:
            return None
        if not entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    def xǁCacheL1Repositoryǁget__mutmut_orig(self, query_hash: str) -> CacheEntry | None:
        entry = self._store.get(query_hash)
        if entry is None:
            return None
        if not entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    def xǁCacheL1Repositoryǁget__mutmut_1(self, query_hash: str) -> CacheEntry | None:
        entry = None
        if entry is None:
            return None
        if not entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    def xǁCacheL1Repositoryǁget__mutmut_2(self, query_hash: str) -> CacheEntry | None:
        entry = self._store.get(None)
        if entry is None:
            return None
        if not entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    def xǁCacheL1Repositoryǁget__mutmut_3(self, query_hash: str) -> CacheEntry | None:
        entry = self._store.get(query_hash)
        if entry is not None:
            return None
        if not entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    def xǁCacheL1Repositoryǁget__mutmut_4(self, query_hash: str) -> CacheEntry | None:
        entry = self._store.get(query_hash)
        if entry is None:
            return None
        if entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    @_mutmut_mutated(mutants_xǁCacheL1Repositoryǁset__mutmut)
    def set(self, query_hash: str, entry: CacheEntry) -> None:
        self._store[query_hash] = entry

    def xǁCacheL1Repositoryǁset__mutmut_orig(self, query_hash: str, entry: CacheEntry) -> None:
        self._store[query_hash] = entry

    def xǁCacheL1Repositoryǁset__mutmut_1(self, query_hash: str, entry: CacheEntry) -> None:
        self._store[query_hash] = None

    @_mutmut_mutated(mutants_xǁCacheL1Repositoryǁinvalidate__mutmut)
    def invalidate(self, query_hash: str) -> None:
        self._store.pop(query_hash, None)

    def xǁCacheL1Repositoryǁinvalidate__mutmut_orig(self, query_hash: str) -> None:
        self._store.pop(query_hash, None)

    def xǁCacheL1Repositoryǁinvalidate__mutmut_1(self, query_hash: str) -> None:
        self._store.pop(None, None)

    def xǁCacheL1Repositoryǁinvalidate__mutmut_2(self, query_hash: str) -> None:
        self._store.pop(None)

    def xǁCacheL1Repositoryǁinvalidate__mutmut_3(self, query_hash: str) -> None:
        self._store.pop(query_hash, )

    def clear(self) -> None:
        self._store.clear()

    @_mutmut_mutated(mutants_xǁCacheL1Repositoryǁsize__mutmut)
    def size(self) -> int:
        return sum(1 for e in self._store.values() if e.is_valid)

    def xǁCacheL1Repositoryǁsize__mutmut_orig(self) -> int:
        return sum(1 for e in self._store.values() if e.is_valid)

    def xǁCacheL1Repositoryǁsize__mutmut_1(self) -> int:
        return sum(None)

    def xǁCacheL1Repositoryǁsize__mutmut_2(self) -> int:
        return sum(2 for e in self._store.values() if e.is_valid)

    @_mutmut_mutated(mutants_xǁCacheL1Repositoryǁevict_expired__mutmut)
    def evict_expired(self) -> int:
        expired_keys = [k for k, v in self._store.items() if not v.is_valid]
        for key in expired_keys:
            del self._store[key]
        return len(expired_keys)

    def xǁCacheL1Repositoryǁevict_expired__mutmut_orig(self) -> int:
        expired_keys = [k for k, v in self._store.items() if not v.is_valid]
        for key in expired_keys:
            del self._store[key]
        return len(expired_keys)

    def xǁCacheL1Repositoryǁevict_expired__mutmut_1(self) -> int:
        expired_keys = None
        for key in expired_keys:
            del self._store[key]
        return len(expired_keys)

    def xǁCacheL1Repositoryǁevict_expired__mutmut_2(self) -> int:
        expired_keys = [k for k, v in self._store.items() if v.is_valid]
        for key in expired_keys:
            del self._store[key]
        return len(expired_keys)

mutants_xǁCacheL1Repositoryǁ__init____mutmut['_mutmut_orig'] = CacheL1Repository.xǁCacheL1Repositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁ__init____mutmut['xǁCacheL1Repositoryǁ__init____mutmut_1'] = CacheL1Repository.xǁCacheL1Repositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCacheL1Repositoryǁget__mutmut['_mutmut_orig'] = CacheL1Repository.xǁCacheL1Repositoryǁget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁget__mutmut['xǁCacheL1Repositoryǁget__mutmut_1'] = CacheL1Repository.xǁCacheL1Repositoryǁget__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁget__mutmut['xǁCacheL1Repositoryǁget__mutmut_2'] = CacheL1Repository.xǁCacheL1Repositoryǁget__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁget__mutmut['xǁCacheL1Repositoryǁget__mutmut_3'] = CacheL1Repository.xǁCacheL1Repositoryǁget__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁget__mutmut['xǁCacheL1Repositoryǁget__mutmut_4'] = CacheL1Repository.xǁCacheL1Repositoryǁget__mutmut_4 # type: ignore # mutmut generated

mutants_xǁCacheL1Repositoryǁset__mutmut['_mutmut_orig'] = CacheL1Repository.xǁCacheL1Repositoryǁset__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁset__mutmut['xǁCacheL1Repositoryǁset__mutmut_1'] = CacheL1Repository.xǁCacheL1Repositoryǁset__mutmut_1 # type: ignore # mutmut generated

mutants_xǁCacheL1Repositoryǁinvalidate__mutmut['_mutmut_orig'] = CacheL1Repository.xǁCacheL1Repositoryǁinvalidate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁinvalidate__mutmut['xǁCacheL1Repositoryǁinvalidate__mutmut_1'] = CacheL1Repository.xǁCacheL1Repositoryǁinvalidate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁinvalidate__mutmut['xǁCacheL1Repositoryǁinvalidate__mutmut_2'] = CacheL1Repository.xǁCacheL1Repositoryǁinvalidate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁinvalidate__mutmut['xǁCacheL1Repositoryǁinvalidate__mutmut_3'] = CacheL1Repository.xǁCacheL1Repositoryǁinvalidate__mutmut_3 # type: ignore # mutmut generated

mutants_xǁCacheL1Repositoryǁsize__mutmut['_mutmut_orig'] = CacheL1Repository.xǁCacheL1Repositoryǁsize__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁsize__mutmut['xǁCacheL1Repositoryǁsize__mutmut_1'] = CacheL1Repository.xǁCacheL1Repositoryǁsize__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁsize__mutmut['xǁCacheL1Repositoryǁsize__mutmut_2'] = CacheL1Repository.xǁCacheL1Repositoryǁsize__mutmut_2 # type: ignore # mutmut generated

mutants_xǁCacheL1Repositoryǁevict_expired__mutmut['_mutmut_orig'] = CacheL1Repository.xǁCacheL1Repositoryǁevict_expired__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁevict_expired__mutmut['xǁCacheL1Repositoryǁevict_expired__mutmut_1'] = CacheL1Repository.xǁCacheL1Repositoryǁevict_expired__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCacheL1Repositoryǁevict_expired__mutmut['xǁCacheL1Repositoryǁevict_expired__mutmut_2'] = CacheL1Repository.xǁCacheL1Repositoryǁevict_expired__mutmut_2 # type: ignore # mutmut generated
