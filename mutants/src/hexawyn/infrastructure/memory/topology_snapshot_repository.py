import json
from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.domain.services.topology.exporter import DependencyGraphExport

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
mutants_xǁTopologySnapshotRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut: MutantDict = {}  # type: ignore


class TopologySnapshotRepository(TopologySnapshotPort):
    """Persists topology graph snapshots in DuckDB for historical comparison.

    Best-effort: storage failures are swallowed — history persistence must
    never block the caller's topology mapping response.
    """

    @_mutmut_mutated(mutants_xǁTopologySnapshotRepositoryǁ__init____mutmut)
    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁTopologySnapshotRepositoryǁ__init____mutmut_orig(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def xǁTopologySnapshotRepositoryǁ__init____mutmut_1(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = None

    @_mutmut_mutated(mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut)
    def save_snapshot(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_topology_snapshot.sql"),
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_orig(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_topology_snapshot.sql"),
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_1(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                None,
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_2(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_topology_snapshot.sql"),
                None,
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_3(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_4(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_topology_snapshot.sql"),
                )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_5(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql(None),
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_6(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("XXinsert_topology_snapshot.sqlXX"),
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_7(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("INSERT_TOPOLOGY_SNAPSHOT.SQL"),
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass

    def xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_8(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_topology_snapshot.sql"),
                [cluster_name, json.dumps(None)],
            )
        except Exception:
            pass

mutants_xǁTopologySnapshotRepositoryǁ__init____mutmut['_mutmut_orig'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁ__init____mutmut['xǁTopologySnapshotRepositoryǁ__init____mutmut_1'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['_mutmut_orig'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_1'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_2'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_3'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_4'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_5'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_6'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_7'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut['xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_8'] = TopologySnapshotRepository.xǁTopologySnapshotRepositoryǁsave_snapshot__mutmut_8 # type: ignore # mutmut generated
