"""DuckDB adapter for memory consolidation."""

from pathlib import Path
from typing import Any

import duckdb

from hexawyn.application.ports.driven.consolidation_port import (
    ConsolidationConfig,
    ConsolidationPort,
)

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
mutants_xǁDuckDBConsolidationRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut: MutantDict = {}  # type: ignore


class DuckDBConsolidationRepository(ConsolidationPort):
    @_mutmut_mutated(mutants_xǁDuckDBConsolidationRepositoryǁ__init____mutmut)
    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn
    def xǁDuckDBConsolidationRepositoryǁ__init____mutmut_orig(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn
    def xǁDuckDBConsolidationRepositoryǁ__init____mutmut_1(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = None

    @_mutmut_mutated(mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut)
    def find_incident_groups(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_orig(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_1(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = None
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_2(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            None,
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_3(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            None,
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_4(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_5(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_6(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql(None),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_7(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("XXfind_groups.sqlXX"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_8(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("FIND_GROUPS.SQL"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_9(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["XXmax_age_daysXX"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_10(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["MAX_AGE_DAYS"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_11(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["XXmin_occurrencesXX"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_12(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["MIN_OCCURRENCES"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_13(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(None), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_14(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] and ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_15(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[1] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_16(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or "XXXX"), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_17(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(None), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_18(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] and ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_19(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[2] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_20(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or "XXXX"), str(r[2] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_21(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(None), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_22(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] and ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_23(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[3] or ""), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_24(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or "XXXX"), int(r[3])) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_25(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(None)) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_26(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[4])) for r in rows]

    @_mutmut_mutated(mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut)
    def get_incidents_for_group(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_orig(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_1(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = None
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_2(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            None,
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_3(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            None,
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_4(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_5(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_6(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql(None),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_7(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("XXget_group_incidents.sqlXX"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_8(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("GET_GROUP_INCIDENTS.SQL"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_9(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(None) for r in rows]

    def xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_10(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[1]) for r in rows]

    @_mutmut_mutated(mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut)
    def store_knowledge(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_orig(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_1(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "XXXX",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_2(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "XXXX",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_3(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 2.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_4(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 1.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_5(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                None,
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_6(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                None,
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_7(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_8(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_9(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql(None),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_10(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("XXinsert_consolidated.sqlXX"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_11(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("INSERT_CONSOLIDATED.SQL"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_12(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids and [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_13(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding and [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    @_mutmut_mutated(mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut)
    def mark_consolidated(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("mark_consolidated.sql"),
            [knowledge_id, incident_ids],
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_orig(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("mark_consolidated.sql"),
            [knowledge_id, incident_ids],
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_1(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            None,
            [knowledge_id, incident_ids],
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_2(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("mark_consolidated.sql"),
            None,
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_3(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            [knowledge_id, incident_ids],
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_4(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("mark_consolidated.sql"),
            )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_5(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql(None),
            [knowledge_id, incident_ids],
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_6(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("XXmark_consolidated.sqlXX"),
            [knowledge_id, incident_ids],
        )

    def xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_7(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("MARK_CONSOLIDATED.SQL"),
            [knowledge_id, incident_ids],
        )

    @_mutmut_mutated(mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut)
    def search_consolidated(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("search_consolidated.sql"),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_orig(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("search_consolidated.sql"),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_1(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = None
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_2(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            None,
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_3(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("search_consolidated.sql"),
            None,
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_4(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_5(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("search_consolidated.sql"),
            ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_6(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql(None),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_7(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("XXsearch_consolidated.sqlXX"),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_8(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("SEARCH_CONSOLIDATED.SQL"),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)

    def xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_9(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("search_consolidated.sql"),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(None)

mutants_xǁDuckDBConsolidationRepositoryǁ__init____mutmut['_mutmut_orig'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁ__init____mutmut['xǁDuckDBConsolidationRepositoryǁ__init____mutmut_1'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['_mutmut_orig'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_1'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_2'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_3'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_4'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_5'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_6'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_7'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_8'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_9'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_10'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_11'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_12'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_13'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_14'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_15'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_16'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_17'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_18'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_19'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_20'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_21'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_22'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_23'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_24'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_25'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut['xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_26'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁfind_incident_groups__mutmut_26 # type: ignore # mutmut generated

mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['_mutmut_orig'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_1'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_2'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_3'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_4'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_5'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_6'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_7'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_8'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_9'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut['xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_10'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁget_incidents_for_group__mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['_mutmut_orig'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_1'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_2'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_3'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_4'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_5'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_6'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_7'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_8'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_9'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_10'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_11'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_12'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut['xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_13'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁstore_knowledge__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['_mutmut_orig'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_1'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_2'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_3'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_4'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_5'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_6'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_7'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁmark_consolidated__mutmut_7 # type: ignore # mutmut generated

mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['_mutmut_orig'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_1'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_2'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_3'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_4'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_5'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_6'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_7'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_8'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut['xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_9'] = DuckDBConsolidationRepository.xǁDuckDBConsolidationRepositoryǁsearch_consolidated__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_consolidated_rows__mutmut)
def _parse_consolidated_rows(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_orig(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_1(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = None
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_2(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            None
        )
    return results


def x__parse_consolidated_rows__mutmut_3(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "XXidXX": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_4(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "ID": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_5(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(None),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_6(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[1]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_7(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "XXpatternXX": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_8(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "PATTERN": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_9(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(None),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_10(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[2]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_11(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "XXresource_nameXX": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_12(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "RESOURCE_NAME": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_13(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(None) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_14(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[3]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_15(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[3] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_16(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "XXresource_kindXX": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_17(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "RESOURCE_KIND": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_18(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(None) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_19(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[4]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_20(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[4] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_21(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "XXnamespaceXX": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_22(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "NAMESPACE": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_23(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(None) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_24(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[5]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_25(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[5] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_26(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "XXtool_nameXX": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_27(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "TOOL_NAME": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_28(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(None),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_29(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[6]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_30(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "XXoccurrence_countXX": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_31(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "OCCURRENCE_COUNT": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_32(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(None),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_33(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[7]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_34(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "XXfirst_seenXX": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_35(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "FIRST_SEEN": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_36(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(None),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_37(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[8]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_38(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "XXlast_seenXX": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_39(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "LAST_SEEN": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_40(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(None),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_41(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[9]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_42(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "XXweightXX": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_43(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "WEIGHT": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_44(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(None),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_45(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[10]),
                "confidence": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_46(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "XXconfidenceXX": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_47(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "CONFIDENCE": float(r[10]),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_48(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(None),
            }
        )
    return results


def x__parse_consolidated_rows__mutmut_49(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[11]),
            }
        )
    return results

mutants_x__parse_consolidated_rows__mutmut['_mutmut_orig'] = x__parse_consolidated_rows__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_1'] = x__parse_consolidated_rows__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_2'] = x__parse_consolidated_rows__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_3'] = x__parse_consolidated_rows__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_4'] = x__parse_consolidated_rows__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_5'] = x__parse_consolidated_rows__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_6'] = x__parse_consolidated_rows__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_7'] = x__parse_consolidated_rows__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_8'] = x__parse_consolidated_rows__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_9'] = x__parse_consolidated_rows__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_10'] = x__parse_consolidated_rows__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_11'] = x__parse_consolidated_rows__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_12'] = x__parse_consolidated_rows__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_13'] = x__parse_consolidated_rows__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_14'] = x__parse_consolidated_rows__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_15'] = x__parse_consolidated_rows__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_16'] = x__parse_consolidated_rows__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_17'] = x__parse_consolidated_rows__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_18'] = x__parse_consolidated_rows__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_19'] = x__parse_consolidated_rows__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_20'] = x__parse_consolidated_rows__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_21'] = x__parse_consolidated_rows__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_22'] = x__parse_consolidated_rows__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_23'] = x__parse_consolidated_rows__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_24'] = x__parse_consolidated_rows__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_25'] = x__parse_consolidated_rows__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_26'] = x__parse_consolidated_rows__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_27'] = x__parse_consolidated_rows__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_28'] = x__parse_consolidated_rows__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_29'] = x__parse_consolidated_rows__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_30'] = x__parse_consolidated_rows__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_31'] = x__parse_consolidated_rows__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_32'] = x__parse_consolidated_rows__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_33'] = x__parse_consolidated_rows__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_34'] = x__parse_consolidated_rows__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_35'] = x__parse_consolidated_rows__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_36'] = x__parse_consolidated_rows__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_37'] = x__parse_consolidated_rows__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_38'] = x__parse_consolidated_rows__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_39'] = x__parse_consolidated_rows__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_40'] = x__parse_consolidated_rows__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_41'] = x__parse_consolidated_rows__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_42'] = x__parse_consolidated_rows__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_43'] = x__parse_consolidated_rows__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_44'] = x__parse_consolidated_rows__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_45'] = x__parse_consolidated_rows__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_46'] = x__parse_consolidated_rows__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_47'] = x__parse_consolidated_rows__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_48'] = x__parse_consolidated_rows__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_consolidated_rows__mutmut['x__parse_consolidated_rows__mutmut_49'] = x__parse_consolidated_rows__mutmut_49 # type: ignore # mutmut generated
