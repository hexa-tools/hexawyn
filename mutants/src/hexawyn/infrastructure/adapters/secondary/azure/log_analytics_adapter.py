from __future__ import annotations

from collections.abc import Iterable, Sequence
from datetime import timedelta
from typing import Protocol, cast

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_FORBIDDEN_STATUS = 403
_CREDENTIALS_HINT = "Run 'az login' or attach a managed identity, then retry."
_CONTAINER_LOG_TABLE = "ContainerLogV2"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _LogsTable(Protocol):
    columns: Sequence[str]
    rows: Iterable[Sequence[object]]


class _LogsResult(Protocol):
    status: object
    tables: Sequence[_LogsTable]


class LogsClient(Protocol):
    """Minimal contract for the azure-monitor-query LogsQueryClient used here."""

    def query_workspace(
        self, workspace_id: str, query: str, *, timespan: timedelta
    ) -> _LogsResult: ...
mutants_xǁAzureLogAnalyticsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class AzureLogAnalyticsAdapter(LogSearchPort):
    """LogSearchPort backed by Azure Log Analytics (ContainerLogV2) via KQL.

    Reads pod/container logs from the Log Analytics workspace — no
    `kubectl logs` needed on AKS.
    """

    @_mutmut_mutated(mutants_xǁAzureLogAnalyticsAdapterǁ__init____mutmut)
    def __init__(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = logs_client

    def xǁAzureLogAnalyticsAdapterǁ__init____mutmut_orig(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = logs_client

    def xǁAzureLogAnalyticsAdapterǁ__init____mutmut_1(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = None
        self._logs_client = logs_client

    def xǁAzureLogAnalyticsAdapterǁ__init____mutmut_2(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = None

    @_mutmut_mutated(mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut)
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_orig(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_1(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = None
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_2(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(None, time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_3(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), None)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_4(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_5(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), )
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_6(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(None, namespace), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_7(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, None), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_8(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(namespace), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_9(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, ), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_10(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), time_window_minutes)
        if table is not None:
            return []
        return self._group_by_container(table)

    def xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_11(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(None)

    @_mutmut_mutated(mutants_xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut)
    def _logs_kql(self, pod_name: str, namespace: str) -> str:
        return (
            f"{_CONTAINER_LOG_TABLE} "
            f'| where PodName == "{pod_name}" and PodNamespace == "{namespace}" '
            f"| project ContainerName, LogMessage "
            f"| take {_MAX_LINES_PER_CONTAINER * 4}"
        )

    def xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_orig(self, pod_name: str, namespace: str) -> str:
        return (
            f"{_CONTAINER_LOG_TABLE} "
            f'| where PodName == "{pod_name}" and PodNamespace == "{namespace}" '
            f"| project ContainerName, LogMessage "
            f"| take {_MAX_LINES_PER_CONTAINER * 4}"
        )

    def xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_1(self, pod_name: str, namespace: str) -> str:
        return (
            f"{_CONTAINER_LOG_TABLE} "
            f'| where PodName == "{pod_name}" and PodNamespace == "{namespace}" '
            f"| project ContainerName, LogMessage "
            f"| take {_MAX_LINES_PER_CONTAINER / 4}"
        )

    def xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_2(self, pod_name: str, namespace: str) -> str:
        return (
            f"{_CONTAINER_LOG_TABLE} "
            f'| where PodName == "{pod_name}" and PodNamespace == "{namespace}" '
            f"| project ContainerName, LogMessage "
            f"| take {_MAX_LINES_PER_CONTAINER * 5}"
        )

    @_mutmut_mutated(mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut)
    def _query(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_orig(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_1(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = None
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_2(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                None, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_3(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, None, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_4(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=None
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_5(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_6(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_7(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_8(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=None)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_9(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                None,
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_10(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context=None,
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_11(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_12(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_13(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"XXworkspaceXX": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_14(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"WORKSPACE": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_15(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(None, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_16(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, None, None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_17(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr("status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_18(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_19(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", ) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_20(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "XXstatus_codeXX", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_21(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "STATUS_CODE", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_22(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) != _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_23(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    None,
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_24(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context=None,
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_25(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_26(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_27(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "XXAccess denied reading Azure Log Analytics.XX",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_28(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "access denied reading azure log analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_29(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "ACCESS DENIED READING AZURE LOG ANALYTICS.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_30(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"XXworkspaceXX": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_31(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"WORKSPACE": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_32(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                None,
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_33(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context=None,
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_34(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_35(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_36(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "XXUnable to query Azure Log Analytics.XX",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_37(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "unable to query azure log analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_38(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "UNABLE TO QUERY AZURE LOG ANALYTICS.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_39(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"XXworkspaceXX": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_40(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"WORKSPACE": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_41(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "XXerrorXX": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_42(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "ERROR": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_43(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(None)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_44(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(None, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_45(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, None, None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_46(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr("status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_47(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_48(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", ) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_49(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "XXstatusXX", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_50(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "STATUS", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_51(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) != LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_52(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                None,
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_53(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context=None,
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_54(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_55(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_56(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "XXAzure Log Analytics query failed.XX",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_57(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "azure log analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_58(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "AZURE LOG ANALYTICS QUERY FAILED.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_59(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"XXworkspaceXX": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_60(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"WORKSPACE": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_61(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = None
        return tables[0] if tables else None

    def xǁAzureLogAnalyticsAdapterǁ_query__mutmut_62(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[1] if tables else None

    @_mutmut_mutated(mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut)
    def _group_by_container(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_orig(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_1(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = None
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_2(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = None
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_3(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = None
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_4(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(None)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_5(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = None
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_6(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(None)
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_7(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(None, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_8(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, None, strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_9(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=None))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_10(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip([row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_11(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_12(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], ))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_13(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(None)], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_14(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=True))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_15(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = None
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_16(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(None)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_17(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get(None, _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_18(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", None))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_19(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get(_UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_20(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", ))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_21(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("XXContainerNameXX", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_22(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("containername", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_23(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("CONTAINERNAME", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_24(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = None
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_25(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(None, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_26(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, None)
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_27(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault([])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_28(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, )
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_29(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) > _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_30(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(None)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_31(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                break
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_32(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(None).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_33(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get(None, "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_34(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", None)).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_35(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_36(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", )).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_37(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("XXLogMessageXX", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_38(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("logmessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_39(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LOGMESSAGE", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_40(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "XXXX")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_41(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = None
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_42(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(None)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_43(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=None,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_44(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=None,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_45(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=None,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_46(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_47(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_48(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                )
            for container, lines in lines_by_container.items()
        ]

    def xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_49(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container not in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    @_mutmut_mutated(mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_orig(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_1(self) -> LogsClient:
        client = None
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_2(self) -> LogsClient:
        client = self._logs_client
        if client is not None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_3(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = None
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_4(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(None, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_5(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, None)
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_6(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_7(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, )
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_8(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(None))
            self._logs_client = client
        return client

    def xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_9(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = None
        return client

mutants_xǁAzureLogAnalyticsAdapterǁ__init____mutmut['_mutmut_orig'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ__init____mutmut['xǁAzureLogAnalyticsAdapterǁ__init____mutmut_1'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ__init____mutmut['xǁAzureLogAnalyticsAdapterǁ__init____mutmut_2'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['_mutmut_orig'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_1'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_2'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_3'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_4'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_5'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_6'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_7'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_8'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_9'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_10'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut['xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_11'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁfetch_pod_container_logs__mutmut_11 # type: ignore # mutmut generated

mutants_xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut['_mutmut_orig'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut['xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_1'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut['xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_2'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_logs_kql__mutmut_2 # type: ignore # mutmut generated

mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['_mutmut_orig'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_1'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_2'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_3'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_4'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_5'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_6'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_7'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_8'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_9'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_10'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_11'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_12'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_13'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_14'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_15'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_16'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_17'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_18'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_19'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_20'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_21'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_22'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_23'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_24'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_25'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_26'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_27'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_28'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_29'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_30'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_31'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_32'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_33'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_34'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_35'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_36'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_37'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_38'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_39'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_40'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_41'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_42'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_43'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_44'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_45'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_46'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_47'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_48'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_49'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_50'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_51'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_52'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_53'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_54'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_55'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_56'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_57'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_58'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_59'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_60'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_61'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_query__mutmut['xǁAzureLogAnalyticsAdapterǁ_query__mutmut_62'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_query__mutmut_62 # type: ignore # mutmut generated

mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['_mutmut_orig'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_1'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_2'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_3'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_4'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_5'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_6'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_7'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_8'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_9'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_10'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_11'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_12'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_13'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_14'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_15'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_16'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_17'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_18'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_19'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_20'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_21'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_22'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_23'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_24'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_25'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_26'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_27'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_28'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_29'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_30'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_31'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_32'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_33'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_34'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_35'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_36'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_37'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_38'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_39'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_40'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_41'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_42'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_43'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_44'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_45'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_46'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_47'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_48'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut['xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_49'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_group_by_container__mutmut_49 # type: ignore # mutmut generated

mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_1'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_2'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_3'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_4'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_5'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_6'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_7'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_8'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut['xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_9'] = AzureLogAnalyticsAdapter.xǁAzureLogAnalyticsAdapterǁ_client_or_create__mutmut_9 # type: ignore # mutmut generated
