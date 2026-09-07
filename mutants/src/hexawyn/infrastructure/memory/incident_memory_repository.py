from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.incident_memory_port import IncidentMemoryPort
from hexawyn.domain.models.incident_memory import IncidentMemoryRecord

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
mutants_xǁIncidentMemoryRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut: MutantDict = {}  # type: ignore


class IncidentMemoryRepository(IncidentMemoryPort):
    """Persists completed investigations in DuckDB for similarity retrieval.

    Best-effort: storage failures are swallowed — memory persistence must
    never block the caller's investigation response. Records without an
    embedding (or missing cluster/tool) are skipped, since they cannot be
    retrieved by the VSS search path.
    """

    @_mutmut_mutated(mutants_xǁIncidentMemoryRepositoryǁ__init____mutmut)
    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁIncidentMemoryRepositoryǁ__init____mutmut_orig(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁIncidentMemoryRepositoryǁ__init____mutmut_1(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = None

    @_mutmut_mutated(mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut)
    def store_incident(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("insert_incident.sql"),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_orig(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("insert_incident.sql"),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_1(self, record: IncidentMemoryRecord) -> None:
        if record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("insert_incident.sql"),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_2(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                None,
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_3(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("insert_incident.sql"),
                None,
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_4(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_5(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("insert_incident.sql"),
                )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_6(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql(None),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_7(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("XXinsert_incident.sqlXX"),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

    def xǁIncidentMemoryRepositoryǁstore_incident__mutmut_8(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("INSERT_INCIDENT.SQL"),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass

mutants_xǁIncidentMemoryRepositoryǁ__init____mutmut['_mutmut_orig'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁ__init____mutmut['xǁIncidentMemoryRepositoryǁ__init____mutmut_1'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['_mutmut_orig'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_1'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_2'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_3'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_4'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_5'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_6'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_7'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIncidentMemoryRepositoryǁstore_incident__mutmut['xǁIncidentMemoryRepositoryǁstore_incident__mutmut_8'] = IncidentMemoryRepository.xǁIncidentMemoryRepositoryǁstore_incident__mutmut_8 # type: ignore # mutmut generated
