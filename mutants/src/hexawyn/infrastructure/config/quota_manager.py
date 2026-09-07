from datetime import UTC, datetime

from hexawyn.application.ports.driven.quota_port import QuotaStorePort
from hexawyn.domain.errors import QuotaExceededError, SlackQuotaExceededError
from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    SlackQuota,
    UsageQuota,
)
from hexawyn.infrastructure.config import quota_cache

_store: QuotaStorePort | None = None


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__get_store__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_store__mutmut)
def _get_store() -> QuotaStorePort:
    """Lazily initialize the quota store (defaults to DuckDB-backed QuotaRepository)."""
    global _store
    if _store is None:
        from hexawyn.infrastructure.memory.duckdb_client import get_connection
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        _store = QuotaRepository(conn=get_connection())
    return _store


def x__get_store__mutmut_orig() -> QuotaStorePort:
    """Lazily initialize the quota store (defaults to DuckDB-backed QuotaRepository)."""
    global _store
    if _store is None:
        from hexawyn.infrastructure.memory.duckdb_client import get_connection
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        _store = QuotaRepository(conn=get_connection())
    return _store


def x__get_store__mutmut_1() -> QuotaStorePort:
    """Lazily initialize the quota store (defaults to DuckDB-backed QuotaRepository)."""
    global _store
    if _store is not None:
        from hexawyn.infrastructure.memory.duckdb_client import get_connection
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        _store = QuotaRepository(conn=get_connection())
    return _store


def x__get_store__mutmut_2() -> QuotaStorePort:
    """Lazily initialize the quota store (defaults to DuckDB-backed QuotaRepository)."""
    global _store
    if _store is None:
        from hexawyn.infrastructure.memory.duckdb_client import get_connection
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        _store = None
    return _store


def x__get_store__mutmut_3() -> QuotaStorePort:
    """Lazily initialize the quota store (defaults to DuckDB-backed QuotaRepository)."""
    global _store
    if _store is None:
        from hexawyn.infrastructure.memory.duckdb_client import get_connection
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        _store = QuotaRepository(conn=None)
    return _store

mutants_x__get_store__mutmut['_mutmut_orig'] = x__get_store__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_store__mutmut['x__get_store__mutmut_1'] = x__get_store__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_store__mutmut['x__get_store__mutmut_2'] = x__get_store__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_store__mutmut['x__get_store__mutmut_3'] = x__get_store__mutmut_3 # type: ignore # mutmut generated
mutants_x_inject_quota_store__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_inject_quota_store__mutmut)
def inject_quota_store(store: QuotaStorePort) -> None:
    """Inject a custom QuotaStorePort implementation (for testing)."""
    global _store
    _store = store


def x_inject_quota_store__mutmut_orig(store: QuotaStorePort) -> None:
    """Inject a custom QuotaStorePort implementation (for testing)."""
    global _store
    _store = store


def x_inject_quota_store__mutmut_1(store: QuotaStorePort) -> None:
    """Inject a custom QuotaStorePort implementation (for testing)."""
    global _store
    _store = None

mutants_x_inject_quota_store__mutmut['_mutmut_orig'] = x_inject_quota_store__mutmut_orig # type: ignore # mutmut generated
mutants_x_inject_quota_store__mutmut['x_inject_quota_store__mutmut_1'] = x_inject_quota_store__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_current_month__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_current_month__mutmut)
def _get_current_month() -> str:
    return datetime.now(UTC).strftime("%Y-%m")


def x__get_current_month__mutmut_orig() -> str:
    return datetime.now(UTC).strftime("%Y-%m")


def x__get_current_month__mutmut_1() -> str:
    return datetime.now(UTC).strftime(None)


def x__get_current_month__mutmut_2() -> str:
    return datetime.now(None).strftime("%Y-%m")


def x__get_current_month__mutmut_3() -> str:
    return datetime.now(UTC).strftime("XX%Y-%mXX")


def x__get_current_month__mutmut_4() -> str:
    return datetime.now(UTC).strftime("%y-%m")


def x__get_current_month__mutmut_5() -> str:
    return datetime.now(UTC).strftime("%Y-%M")

mutants_x__get_current_month__mutmut['_mutmut_orig'] = x__get_current_month__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_current_month__mutmut['x__get_current_month__mutmut_1'] = x__get_current_month__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_current_month__mutmut['x__get_current_month__mutmut_2'] = x__get_current_month__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_current_month__mutmut['x__get_current_month__mutmut_3'] = x__get_current_month__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_current_month__mutmut['x__get_current_month__mutmut_4'] = x__get_current_month__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_current_month__mutmut['x__get_current_month__mutmut_5'] = x__get_current_month__mutmut_5 # type: ignore # mutmut generated


def _get_current_tier() -> LicenseTier:
    """
    Get current license tier from license_manager.
    Returns LicenseTier.STARTER if no valid license found.
    Import is deferred to avoid circular dependency with license_manager.
    """
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        return get_license_tier()
    except ImportError:
        return LicenseTier.STARTER
mutants_x__local_investigation_limit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__local_investigation_limit__mutmut)
def _local_investigation_limit() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is not None:
        return int(cached["limit"])
    return UNLIMITED


def x__local_investigation_limit__mutmut_orig() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is not None:
        return int(cached["limit"])
    return UNLIMITED


def x__local_investigation_limit__mutmut_1() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = None
    if cached is not None:
        return int(cached["limit"])
    return UNLIMITED


def x__local_investigation_limit__mutmut_2() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is None:
        return int(cached["limit"])
    return UNLIMITED


def x__local_investigation_limit__mutmut_3() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is not None:
        return int(None)
    return UNLIMITED


def x__local_investigation_limit__mutmut_4() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is not None:
        return int(cached["XXlimitXX"])
    return UNLIMITED


def x__local_investigation_limit__mutmut_5() -> int:
    """Investigation limit from the encrypted CP cache, else neutral (UNLIMITED)."""
    cached = quota_cache.load_quota()
    if cached is not None:
        return int(cached["LIMIT"])
    return UNLIMITED

mutants_x__local_investigation_limit__mutmut['_mutmut_orig'] = x__local_investigation_limit__mutmut_orig # type: ignore # mutmut generated
mutants_x__local_investigation_limit__mutmut['x__local_investigation_limit__mutmut_1'] = x__local_investigation_limit__mutmut_1 # type: ignore # mutmut generated
mutants_x__local_investigation_limit__mutmut['x__local_investigation_limit__mutmut_2'] = x__local_investigation_limit__mutmut_2 # type: ignore # mutmut generated
mutants_x__local_investigation_limit__mutmut['x__local_investigation_limit__mutmut_3'] = x__local_investigation_limit__mutmut_3 # type: ignore # mutmut generated
mutants_x__local_investigation_limit__mutmut['x__local_investigation_limit__mutmut_4'] = x__local_investigation_limit__mutmut_4 # type: ignore # mutmut generated
mutants_x__local_investigation_limit__mutmut['x__local_investigation_limit__mutmut_5'] = x__local_investigation_limit__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_current_investigation_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_current_investigation_quota__mutmut)
def _get_current_investigation_quota() -> UsageQuota:
    return _get_store().get_investigation_quota(month=_get_current_month())


def x__get_current_investigation_quota__mutmut_orig() -> UsageQuota:
    return _get_store().get_investigation_quota(month=_get_current_month())


def x__get_current_investigation_quota__mutmut_1() -> UsageQuota:
    return _get_store().get_investigation_quota(month=None)

mutants_x__get_current_investigation_quota__mutmut['_mutmut_orig'] = x__get_current_investigation_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_current_investigation_quota__mutmut['x__get_current_investigation_quota__mutmut_1'] = x__get_current_investigation_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_current_slack_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_current_slack_quota__mutmut)
def _get_current_slack_quota() -> SlackQuota:
    return _get_store().get_slack_quota(month=_get_current_month())


def x__get_current_slack_quota__mutmut_orig() -> SlackQuota:
    return _get_store().get_slack_quota(month=_get_current_month())


def x__get_current_slack_quota__mutmut_1() -> SlackQuota:
    return _get_store().get_slack_quota(month=None)

mutants_x__get_current_slack_quota__mutmut['_mutmut_orig'] = x__get_current_slack_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_current_slack_quota__mutmut['x__get_current_slack_quota__mutmut_1'] = x__get_current_slack_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__increment_investigation__mutmut)
def _increment_investigation() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def x__increment_investigation__mutmut_orig() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def x__increment_investigation__mutmut_1() -> None:
    tier = None
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def x__increment_investigation__mutmut_2() -> None:
    tier = _get_current_tier()
    limit = None
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=limit,
    )


def x__increment_investigation__mutmut_3() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=None,
        tier=tier,
        limit=limit,
    )


def x__increment_investigation__mutmut_4() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=None,
        limit=limit,
    )


def x__increment_investigation__mutmut_5() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        limit=None,
    )


def x__increment_investigation__mutmut_6() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        tier=tier,
        limit=limit,
    )


def x__increment_investigation__mutmut_7() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        limit=limit,
    )


def x__increment_investigation__mutmut_8() -> None:
    tier = _get_current_tier()
    limit = _local_investigation_limit()
    _get_store().increment_investigation(
        month=_get_current_month(),
        tier=tier,
        )

mutants_x__increment_investigation__mutmut['_mutmut_orig'] = x__increment_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_1'] = x__increment_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_2'] = x__increment_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_3'] = x__increment_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_4'] = x__increment_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_5'] = x__increment_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_6'] = x__increment_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_7'] = x__increment_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_x__increment_investigation__mutmut['x__increment_investigation__mutmut_8'] = x__increment_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__increment_slack__mutmut)
def _increment_slack() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=tier,
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_orig() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=tier,
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_1() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = None
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=tier,
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_2() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=None,
        tier=tier,
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_3() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=None,
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_4() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=tier,
        limit=None,
    )


def x__increment_slack__mutmut_5() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        tier=tier,
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_6() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        limit=UNLIMITED,
    )


def x__increment_slack__mutmut_7() -> None:
    # (ii) Slack is counted-but-unlimited locally; real limit is a CP follow-up.
    tier = _get_current_tier()
    _get_store().increment_slack(
        month=_get_current_month(),
        tier=tier,
        )

mutants_x__increment_slack__mutmut['_mutmut_orig'] = x__increment_slack__mutmut_orig # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_1'] = x__increment_slack__mutmut_1 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_2'] = x__increment_slack__mutmut_2 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_3'] = x__increment_slack__mutmut_3 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_4'] = x__increment_slack__mutmut_4 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_5'] = x__increment_slack__mutmut_5 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_6'] = x__increment_slack__mutmut_6 # type: ignore # mutmut generated
mutants_x__increment_slack__mutmut['x__increment_slack__mutmut_7'] = x__increment_slack__mutmut_7 # type: ignore # mutmut generated
mutants_x_check_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_quota__mutmut)
def check_quota() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=quota.limit)


def x_check_quota__mutmut_orig() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=quota.limit)


def x_check_quota__mutmut_1() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = None
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=quota.limit)


def x_check_quota__mutmut_2() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=None, limit=quota.limit)


def x_check_quota__mutmut_3() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, limit=None)


def x_check_quota__mutmut_4() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(limit=quota.limit)


def x_check_quota__mutmut_5() -> None:
    """Check investigation quota before starting LangGraph pipeline.

    The limit is streamed from the control plane (or its cache). When unknown
    (neutral), the quota is not locally constrained and this does not block —
    the control plane re-enforces on the next sync. Demo mode: caller must
    skip this.
    """
    quota = _get_current_investigation_quota()
    if quota.is_exceeded:
        raise QuotaExceededError(used=quota.count, )

mutants_x_check_quota__mutmut['_mutmut_orig'] = x_check_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_quota__mutmut['x_check_quota__mutmut_1'] = x_check_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_quota__mutmut['x_check_quota__mutmut_2'] = x_check_quota__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_quota__mutmut['x_check_quota__mutmut_3'] = x_check_quota__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_quota__mutmut['x_check_quota__mutmut_4'] = x_check_quota__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_quota__mutmut['x_check_quota__mutmut_5'] = x_check_quota__mutmut_5 # type: ignore # mutmut generated
mutants_x_check_slack_quota__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_slack_quota__mutmut)
def check_slack_quota() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, limit=quota.limit)


def x_check_slack_quota__mutmut_orig() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, limit=quota.limit)


def x_check_slack_quota__mutmut_1() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = None
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, limit=quota.limit)


def x_check_slack_quota__mutmut_2() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=None, limit=quota.limit)


def x_check_slack_quota__mutmut_3() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, limit=None)


def x_check_slack_quota__mutmut_4() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(limit=quota.limit)


def x_check_slack_quota__mutmut_5() -> None:
    """Check Slack alert quota before sending.

    Slack is counted-but-unlimited locally until the control plane exposes a
    real limit, so this does not block on a fabricated number.
    """
    quota = _get_current_slack_quota()
    if quota.is_exceeded:
        raise SlackQuotaExceededError(used=quota.count, )

mutants_x_check_slack_quota__mutmut['_mutmut_orig'] = x_check_slack_quota__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_slack_quota__mutmut['x_check_slack_quota__mutmut_1'] = x_check_slack_quota__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_slack_quota__mutmut['x_check_slack_quota__mutmut_2'] = x_check_slack_quota__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_slack_quota__mutmut['x_check_slack_quota__mutmut_3'] = x_check_slack_quota__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_slack_quota__mutmut['x_check_slack_quota__mutmut_4'] = x_check_slack_quota__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_slack_quota__mutmut['x_check_slack_quota__mutmut_5'] = x_check_slack_quota__mutmut_5 # type: ignore # mutmut generated


def increment_quota() -> None:
    """Increment investigation count after successful investigation.
    Demo mode: caller must skip."""
    _increment_investigation()


def increment_slack_quota() -> None:
    """Increment Slack alert count after sending."""
    _increment_slack()


def get_history_days() -> int:
    """
    DuckDB history window for VSS search.

    Neutral by design: no hardcoded tiered figure. When the control plane does
    not supply a retention window, the client does not fabricate one — it keeps
    the full window (unlimited).
    """
    return UNLIMITED
mutants_x_get_quota_display__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_quota_display__mutmut)
def get_quota_display() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_orig() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_1() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = None
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_2() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = None

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_3() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = None
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_4() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "XXStarterXX",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_5() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_6() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "STARTER",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_7() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "XXTeamXX",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_8() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_9() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "TEAM",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_10() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "XXScale-upXX",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_11() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_12() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "SCALE-UP",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_13() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = None

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_14() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(None, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_15() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, None)

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_16() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get("Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_17() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, )

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_18() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "XXStarterXX")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_19() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_20() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "STARTER")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_21() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = None  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_22() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = "XX \u26a0\ufe0fXX" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_23() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26A0\uFE0F" if quota.remaining <= 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_24() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining < 5 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_25() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 6 else ""  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )


def x_get_quota_display__mutmut_26() -> str:
    """
    Display string shown in CLI after each investigation.

    When the quota is neutral (UNKNOWN / unlimited locally) this reports the
    plan label without fabricating a numeric usage figure.
    """
    tier = _get_current_tier()
    quota = _get_current_investigation_quota()

    tier_labels: dict[LicenseTier, str] = {
        LicenseTier.STARTER: "Starter",
        LicenseTier.TEAM: "Team",
        LicenseTier.SCALE_UP: "Scale-up",
    }
    label = tier_labels.get(tier, "Starter")

    if quota.is_unlimited:
        return f"[\u2b50 {label} \u2014 unlimited investigations]"

    warning = " \u26a0\ufe0f" if quota.remaining <= 5 else "XXXX"  # noqa: PLR2004
    return (
        f"[{quota.count}/{quota.limit} {label} investigations"
        f" \u00b7 {quota.remaining} remaining{warning}]"
    )

mutants_x_get_quota_display__mutmut['_mutmut_orig'] = x_get_quota_display__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_1'] = x_get_quota_display__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_2'] = x_get_quota_display__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_3'] = x_get_quota_display__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_4'] = x_get_quota_display__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_5'] = x_get_quota_display__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_6'] = x_get_quota_display__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_7'] = x_get_quota_display__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_8'] = x_get_quota_display__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_9'] = x_get_quota_display__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_10'] = x_get_quota_display__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_11'] = x_get_quota_display__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_12'] = x_get_quota_display__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_13'] = x_get_quota_display__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_14'] = x_get_quota_display__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_15'] = x_get_quota_display__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_16'] = x_get_quota_display__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_17'] = x_get_quota_display__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_18'] = x_get_quota_display__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_19'] = x_get_quota_display__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_20'] = x_get_quota_display__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_21'] = x_get_quota_display__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_22'] = x_get_quota_display__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_23'] = x_get_quota_display__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_24'] = x_get_quota_display__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_25'] = x_get_quota_display__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_quota_display__mutmut['x_get_quota_display__mutmut_26'] = x_get_quota_display__mutmut_26 # type: ignore # mutmut generated
