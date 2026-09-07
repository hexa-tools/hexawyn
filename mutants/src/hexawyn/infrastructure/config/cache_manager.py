import hashlib
from datetime import datetime

from hexawyn.domain.models.cache import CacheEntry
from hexawyn.infrastructure.memory.cache_l1_repository import CacheL1Repository

_repository = CacheL1Repository()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_query_hash__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_query_hash__mutmut)
def compute_query_hash(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def x_compute_query_hash__mutmut_orig(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def x_compute_query_hash__mutmut_1(query: str, cluster_name: str) -> str:
    normalized = None
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def x_compute_query_hash__mutmut_2(query: str, cluster_name: str) -> str:
    normalized = query.upper().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def x_compute_query_hash__mutmut_3(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = None
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def x_compute_query_hash__mutmut_4(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(None).hexdigest()


def x_compute_query_hash__mutmut_5(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode(None)).hexdigest()


def x_compute_query_hash__mutmut_6(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("XXutf-8XX")).hexdigest()


def x_compute_query_hash__mutmut_7(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("UTF-8")).hexdigest()

mutants_x_compute_query_hash__mutmut['_mutmut_orig'] = x_compute_query_hash__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_1'] = x_compute_query_hash__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_2'] = x_compute_query_hash__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_3'] = x_compute_query_hash__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_4'] = x_compute_query_hash__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_5'] = x_compute_query_hash__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_6'] = x_compute_query_hash__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_query_hash__mutmut['x_compute_query_hash__mutmut_7'] = x_compute_query_hash__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_l1__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_l1__mutmut)
def get_l1(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    return _repository.get(query_hash)


def x_get_l1__mutmut_orig(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    return _repository.get(query_hash)


def x_get_l1__mutmut_1(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = None
    return _repository.get(query_hash)


def x_get_l1__mutmut_2(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=None, cluster_name=cluster_name)
    return _repository.get(query_hash)


def x_get_l1__mutmut_3(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=query, cluster_name=None)
    return _repository.get(query_hash)


def x_get_l1__mutmut_4(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(cluster_name=cluster_name)
    return _repository.get(query_hash)


def x_get_l1__mutmut_5(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=query, )
    return _repository.get(query_hash)


def x_get_l1__mutmut_6(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    return _repository.get(None)

mutants_x_get_l1__mutmut['_mutmut_orig'] = x_get_l1__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_l1__mutmut['x_get_l1__mutmut_1'] = x_get_l1__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_l1__mutmut['x_get_l1__mutmut_2'] = x_get_l1__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_l1__mutmut['x_get_l1__mutmut_3'] = x_get_l1__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_l1__mutmut['x_get_l1__mutmut_4'] = x_get_l1__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_l1__mutmut['x_get_l1__mutmut_5'] = x_get_l1__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_l1__mutmut['x_get_l1__mutmut_6'] = x_get_l1__mutmut_6 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_set_l1__mutmut)
def set_l1(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_orig(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_1(query: str, cluster_name: str, result: str) -> None:
    query_hash = None
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_2(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=None, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_3(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=None)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_4(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_5(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, )
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_6(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = None
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_7(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=None,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_8(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=None,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_9(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=None,
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_10(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_11(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_12(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        )
    _repository.set(query_hash, entry)


def x_set_l1__mutmut_13(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(None, entry)


def x_set_l1__mutmut_14(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, None)


def x_set_l1__mutmut_15(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(entry)


def x_set_l1__mutmut_16(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, )

mutants_x_set_l1__mutmut['_mutmut_orig'] = x_set_l1__mutmut_orig # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_1'] = x_set_l1__mutmut_1 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_2'] = x_set_l1__mutmut_2 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_3'] = x_set_l1__mutmut_3 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_4'] = x_set_l1__mutmut_4 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_5'] = x_set_l1__mutmut_5 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_6'] = x_set_l1__mutmut_6 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_7'] = x_set_l1__mutmut_7 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_8'] = x_set_l1__mutmut_8 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_9'] = x_set_l1__mutmut_9 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_10'] = x_set_l1__mutmut_10 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_11'] = x_set_l1__mutmut_11 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_12'] = x_set_l1__mutmut_12 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_13'] = x_set_l1__mutmut_13 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_14'] = x_set_l1__mutmut_14 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_15'] = x_set_l1__mutmut_15 # type: ignore # mutmut generated
mutants_x_set_l1__mutmut['x_set_l1__mutmut_16'] = x_set_l1__mutmut_16 # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_invalidate_l1__mutmut)
def invalidate_l1(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_orig(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_1(query: str, cluster_name: str) -> None:
    query_hash = None
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_2(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=None, cluster_name=cluster_name)
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_3(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=None)
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_4(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(cluster_name=cluster_name)
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_5(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=query, )
    _repository.invalidate(query_hash)


def x_invalidate_l1__mutmut_6(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    _repository.invalidate(None)

mutants_x_invalidate_l1__mutmut['_mutmut_orig'] = x_invalidate_l1__mutmut_orig # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut['x_invalidate_l1__mutmut_1'] = x_invalidate_l1__mutmut_1 # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut['x_invalidate_l1__mutmut_2'] = x_invalidate_l1__mutmut_2 # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut['x_invalidate_l1__mutmut_3'] = x_invalidate_l1__mutmut_3 # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut['x_invalidate_l1__mutmut_4'] = x_invalidate_l1__mutmut_4 # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut['x_invalidate_l1__mutmut_5'] = x_invalidate_l1__mutmut_5 # type: ignore # mutmut generated
mutants_x_invalidate_l1__mutmut['x_invalidate_l1__mutmut_6'] = x_invalidate_l1__mutmut_6 # type: ignore # mutmut generated


def clear_l1() -> None:
    _repository.clear()


def evict_expired_l1() -> int:
    return _repository.evict_expired()
mutants_x_get_cache_stats__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_cache_stats__mutmut)
def get_cache_stats() -> dict[str, int | float]:
    return {
        "l1_size": _repository.size(),
        "l1_ttl_seconds": 300,
    }


def x_get_cache_stats__mutmut_orig() -> dict[str, int | float]:
    return {
        "l1_size": _repository.size(),
        "l1_ttl_seconds": 300,
    }


def x_get_cache_stats__mutmut_1() -> dict[str, int | float]:
    return {
        "XXl1_sizeXX": _repository.size(),
        "l1_ttl_seconds": 300,
    }


def x_get_cache_stats__mutmut_2() -> dict[str, int | float]:
    return {
        "L1_SIZE": _repository.size(),
        "l1_ttl_seconds": 300,
    }


def x_get_cache_stats__mutmut_3() -> dict[str, int | float]:
    return {
        "l1_size": _repository.size(),
        "XXl1_ttl_secondsXX": 300,
    }


def x_get_cache_stats__mutmut_4() -> dict[str, int | float]:
    return {
        "l1_size": _repository.size(),
        "L1_TTL_SECONDS": 300,
    }


def x_get_cache_stats__mutmut_5() -> dict[str, int | float]:
    return {
        "l1_size": _repository.size(),
        "l1_ttl_seconds": 301,
    }

mutants_x_get_cache_stats__mutmut['_mutmut_orig'] = x_get_cache_stats__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_cache_stats__mutmut['x_get_cache_stats__mutmut_1'] = x_get_cache_stats__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_cache_stats__mutmut['x_get_cache_stats__mutmut_2'] = x_get_cache_stats__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_cache_stats__mutmut['x_get_cache_stats__mutmut_3'] = x_get_cache_stats__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_cache_stats__mutmut['x_get_cache_stats__mutmut_4'] = x_get_cache_stats__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_cache_stats__mutmut['x_get_cache_stats__mutmut_5'] = x_get_cache_stats__mutmut_5 # type: ignore # mutmut generated
