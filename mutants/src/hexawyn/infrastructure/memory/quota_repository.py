from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.quota_port import QuotaStorePort
from hexawyn.domain.models.quota import UNLIMITED, LicenseTier, SlackQuota, UsageQuota

SQL_DIR = Path(__file__).parent / "sql"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__load_sql__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_sql__mutmut)
def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_orig(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_1(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding=None)


def x__load_sql__mutmut_2(filename: str) -> str:
    return (SQL_DIR * filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_3(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="XXutf-8XX")


def x__load_sql__mutmut_4(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="UTF-8")

mutants_x__load_sql__mutmut['_mutmut_orig'] = x__load_sql__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_1'] = x__load_sql__mutmut_1 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_2'] = x__load_sql__mutmut_2 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_3'] = x__load_sql__mutmut_3 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_4'] = x__load_sql__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut: MutantDict = {}  # type: ignore
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut: MutantDict = {}  # type: ignore
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut: MutantDict = {}  # type: ignore
mutants_xǁQuotaRepositoryǁreset__mutmut: MutantDict = {}  # type: ignore


class QuotaRepository(QuotaStorePort):
    """Repository for usage quota in DuckDB.

    Handles both investigation quota and Slack alert quota. Limits are not
    hardcoded here: they stream from the control plane / cache, defaulting to
    ``UNLIMITED`` (neutral) when unknown.
    """

    @_mutmut_mutated(mutants_xǁQuotaRepositoryǁ__init____mutmut)
    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁQuotaRepositoryǁ__init____mutmut_orig(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁQuotaRepositoryǁ__init____mutmut_1(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = None

    @_mutmut_mutated(mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut)
    def get_investigation_quota(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_orig(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_1(self, month: str) -> UsageQuota:
        row = None

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_2(self, month: str) -> UsageQuota:
        row = self._conn.execute(None, [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_3(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), None).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_4(self, month: str) -> UsageQuota:
        row = self._conn.execute([month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_5(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), ).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_6(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql(None), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_7(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("XXget_quota.sqlXX"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_8(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("GET_QUOTA.SQL"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_9(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is not None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_10(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=None, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_11(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=None, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_12(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=None)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_13(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_14(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_15(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, )

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_16(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=1, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_17(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=None,
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_18(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=None,
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_19(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=None,
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_20(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_21(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_22(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_23(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(None),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_24(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[2]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_25(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(None),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_26(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[4]),
            limit=int(row[4]),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_27(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(None),
        )

    def xǁQuotaRepositoryǁget_investigation_quota__mutmut_28(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=UNLIMITED)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[5]),
        )

    @_mutmut_mutated(mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut)
    def get_slack_quota(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_orig(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_1(self, month: str) -> SlackQuota:
        row = None

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_2(self, month: str) -> SlackQuota:
        row = self._conn.execute(None, [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_3(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), None).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_4(self, month: str) -> SlackQuota:
        row = self._conn.execute([month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_5(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), ).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_6(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql(None), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_7(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("XXget_quota.sqlXX"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_8(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("GET_QUOTA.SQL"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_9(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is not None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_10(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=None, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_11(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=None, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_12(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=None)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_13(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_14(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_15(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, )

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_16(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=1, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_17(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=None,
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_18(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=None,
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_19(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=None,
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_20(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_21(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_22(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_23(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(None),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_24(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[2]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_25(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(None),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_26(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[6]),
            limit=int(row[6]),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_27(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(None),
        )

    def xǁQuotaRepositoryǁget_slack_quota__mutmut_28(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=UNLIMITED)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[7]),
        )

    @_mutmut_mutated(mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut)
    def increment_investigation(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_investigation_quota.sql"),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_orig(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_investigation_quota.sql"),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_1(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            None,
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_2(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_investigation_quota.sql"),
            None,
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_3(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_4(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_investigation_quota.sql"),
            )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_5(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql(None),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_6(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("XXupsert_investigation_quota.sqlXX"),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_investigation__mutmut_7(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("UPSERT_INVESTIGATION_QUOTA.SQL"),
            [month, tier.value, limit],
        )

    @_mutmut_mutated(mutants_xǁQuotaRepositoryǁincrement_slack__mutmut)
    def increment_slack(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_slack_quota.sql"),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_orig(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_slack_quota.sql"),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_1(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            None,
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_2(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_slack_quota.sql"),
            None,
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_3(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_4(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_slack_quota.sql"),
            )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_5(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql(None),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_6(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("XXupsert_slack_quota.sqlXX"),
            [month, tier.value, limit],
        )

    def xǁQuotaRepositoryǁincrement_slack__mutmut_7(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("UPSERT_SLACK_QUOTA.SQL"),
            [month, tier.value, limit],
        )

    @_mutmut_mutated(mutants_xǁQuotaRepositoryǁreset__mutmut)
    def reset(self, month: str) -> None:
        self._conn.execute(_load_sql("reset_quota.sql"), [month])

    def xǁQuotaRepositoryǁreset__mutmut_orig(self, month: str) -> None:
        self._conn.execute(_load_sql("reset_quota.sql"), [month])

    def xǁQuotaRepositoryǁreset__mutmut_1(self, month: str) -> None:
        self._conn.execute(None, [month])

    def xǁQuotaRepositoryǁreset__mutmut_2(self, month: str) -> None:
        self._conn.execute(_load_sql("reset_quota.sql"), None)

    def xǁQuotaRepositoryǁreset__mutmut_3(self, month: str) -> None:
        self._conn.execute([month])

    def xǁQuotaRepositoryǁreset__mutmut_4(self, month: str) -> None:
        self._conn.execute(_load_sql("reset_quota.sql"), )

    def xǁQuotaRepositoryǁreset__mutmut_5(self, month: str) -> None:
        self._conn.execute(_load_sql(None), [month])

    def xǁQuotaRepositoryǁreset__mutmut_6(self, month: str) -> None:
        self._conn.execute(_load_sql("XXreset_quota.sqlXX"), [month])

    def xǁQuotaRepositoryǁreset__mutmut_7(self, month: str) -> None:
        self._conn.execute(_load_sql("RESET_QUOTA.SQL"), [month])

mutants_xǁQuotaRepositoryǁ__init____mutmut['_mutmut_orig'] = QuotaRepository.xǁQuotaRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁ__init____mutmut['xǁQuotaRepositoryǁ__init____mutmut_1'] = QuotaRepository.xǁQuotaRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['_mutmut_orig'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_1'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_2'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_3'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_4'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_5'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_6'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_7'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_7 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_8'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_8 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_9'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_9 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_10'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_10 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_11'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_11 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_12'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_12 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_13'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_13 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_14'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_14 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_15'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_15 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_16'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_16 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_17'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_17 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_18'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_18 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_19'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_19 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_20'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_20 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_21'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_21 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_22'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_22 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_23'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_23 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_24'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_24 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_25'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_25 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_26'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_26 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_27'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_27 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_investigation_quota__mutmut['xǁQuotaRepositoryǁget_investigation_quota__mutmut_28'] = QuotaRepository.xǁQuotaRepositoryǁget_investigation_quota__mutmut_28 # type: ignore # mutmut generated

mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['_mutmut_orig'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_1'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_2'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_3'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_4'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_5'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_6'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_7'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_7 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_8'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_8 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_9'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_9 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_10'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_10 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_11'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_11 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_12'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_12 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_13'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_13 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_14'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_14 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_15'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_15 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_16'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_16 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_17'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_17 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_18'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_18 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_19'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_19 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_20'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_20 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_21'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_21 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_22'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_22 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_23'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_23 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_24'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_24 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_25'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_25 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_26'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_26 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_27'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_27 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁget_slack_quota__mutmut['xǁQuotaRepositoryǁget_slack_quota__mutmut_28'] = QuotaRepository.xǁQuotaRepositoryǁget_slack_quota__mutmut_28 # type: ignore # mutmut generated

mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['_mutmut_orig'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_1'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_2'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_3'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_4'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_5'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_6'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_investigation__mutmut['xǁQuotaRepositoryǁincrement_investigation__mutmut_7'] = QuotaRepository.xǁQuotaRepositoryǁincrement_investigation__mutmut_7 # type: ignore # mutmut generated

mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['_mutmut_orig'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_1'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_2'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_3'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_4'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_5'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_6'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁincrement_slack__mutmut['xǁQuotaRepositoryǁincrement_slack__mutmut_7'] = QuotaRepository.xǁQuotaRepositoryǁincrement_slack__mutmut_7 # type: ignore # mutmut generated

mutants_xǁQuotaRepositoryǁreset__mutmut['_mutmut_orig'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_1'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_2'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_3'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_4'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_5'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_6'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQuotaRepositoryǁreset__mutmut['xǁQuotaRepositoryǁreset__mutmut_7'] = QuotaRepository.xǁQuotaRepositoryǁreset__mutmut_7 # type: ignore # mutmut generated
