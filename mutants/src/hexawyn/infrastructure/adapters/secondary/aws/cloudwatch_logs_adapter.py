from __future__ import annotations

import json
from typing import Protocol, TypedDict

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_MINUTES_TO_MILLIS = 60 * 1000
_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_ACCESS_DENIED_CODE = "AccessDeniedException"
_NOT_FOUND_CODE = "ResourceNotFoundException"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _LogEvent(TypedDict, total=False):
    message: str


class _FilterLogEventsResponse(TypedDict, total=False):
    events: list[_LogEvent]
    nextToken: str


class LogsClient(Protocol):
    """Minimal contract for the boto3 CloudWatch Logs client used here."""

    def filter_log_events(self, **kwargs: object) -> _FilterLogEventsResponse:
        """Return log events matching a filter within a time window."""
mutants_xǁCloudWatchLogsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class CloudWatchLogsAdapter(LogSearchPort):
    """LogSearchPort backed by CloudWatch Logs (Container Insights).

    Reads pod/container logs from the Container Insights `application` log
    group — no `kubectl logs` needed on EKS.
    """

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁ__init____mutmut)
    def __init__(
        self, cluster_name: str, region: str | None, logs_client: LogsClient | None = None
    ) -> None:
        self._cluster_name = cluster_name
        self._region = region
        self._logs_client = logs_client

    def xǁCloudWatchLogsAdapterǁ__init____mutmut_orig(
        self, cluster_name: str, region: str | None, logs_client: LogsClient | None = None
    ) -> None:
        self._cluster_name = cluster_name
        self._region = region
        self._logs_client = logs_client

    def xǁCloudWatchLogsAdapterǁ__init____mutmut_1(
        self, cluster_name: str, region: str | None, logs_client: LogsClient | None = None
    ) -> None:
        self._cluster_name = None
        self._region = region
        self._logs_client = logs_client

    def xǁCloudWatchLogsAdapterǁ__init____mutmut_2(
        self, cluster_name: str, region: str | None, logs_client: LogsClient | None = None
    ) -> None:
        self._cluster_name = cluster_name
        self._region = None
        self._logs_client = logs_client

    def xǁCloudWatchLogsAdapterǁ__init____mutmut_3(
        self, cluster_name: str, region: str | None, logs_client: LogsClient | None = None
    ) -> None:
        self._cluster_name = cluster_name
        self._region = region
        self._logs_client = None

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut)
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_orig(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_1(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = None
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_2(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(None)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_3(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() / 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_4(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1001)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_5(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = None
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_6(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms + time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_7(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes / _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_8(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = None
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_9(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(None, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_10(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, None, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_11(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, None, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_12(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, None)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_13(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_14(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, start_ms, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_15(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, end_ms)
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_16(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, )
        return self._group_by_container(messages)

    def xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_17(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(None)

    def _log_group(self) -> str:
        return f"/aws/containerinsights/{self._cluster_name}/application"

    def _filter_pattern(self, pod_name: str, namespace: str) -> str:
        return (
            f'{{ $.kubernetes.pod_name = "{pod_name}" '
            f'&& $.kubernetes.namespace_name = "{namespace}" }}'
        )

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut)
    def _filter_events(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_orig(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_1(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = None
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_2(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = None
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_3(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = ""
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_4(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while False:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_5(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = None
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_6(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    None, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_7(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, None, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_8(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, None, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_9(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, None, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_10(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, None, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_11(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, None
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_12(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_13(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_14(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_15(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_16(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_17(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_18(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    None
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_19(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["XXmessageXX"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_20(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["MESSAGE"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_21(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get(None, []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_22(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", None) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_23(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get([]) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_24(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", ) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_25(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("XXeventsXX", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_26(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("EVENTS", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_27(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get(None)
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_28(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("XXmessageXX")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_29(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("MESSAGE")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_30(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = None
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_31(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get(None)
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_32(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("XXnextTokenXX")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_33(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nexttoken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_34(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("NEXTTOKEN")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_35(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_36(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    return
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_37(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                None,
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_38(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context=None,
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_39(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_40(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_41(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "XXAWS credentials not found. Run 'aws configure' or attach an IAM role.XX",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_42(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "aws credentials not found. run 'aws configure' or attach an iam role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_43(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS CREDENTIALS NOT FOUND. RUN 'AWS CONFIGURE' OR ATTACH AN IAM ROLE.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_44(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"XXclusterXX": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_45(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"CLUSTER": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_46(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "XXregionXX": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_47(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "REGION": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_48(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region and "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_49(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "XXunknownXX"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_50(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "UNKNOWN"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_51(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(None)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_52(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                None,
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_53(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context=None,
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_54(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_55(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_56(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "XXUnable to reach CloudWatch Logs.XX",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_57(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "unable to reach cloudwatch logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_58(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "UNABLE TO REACH CLOUDWATCH LOGS.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_59(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"XXregionXX": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_60(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"REGION": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_61(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region and "unknown", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_62(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "XXunknownXX", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_63(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "UNKNOWN", "error": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_64(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "XXerrorXX": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_65(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "ERROR": str(exc)},
            ) from exc
        return messages

    def xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_66(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(None)},
            ) from exc
        return messages

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut)
    def _filter_page(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_orig(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_1(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = None
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_2(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "XXlogGroupNameXX": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_3(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "loggroupname": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_4(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "LOGGROUPNAME": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_5(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "XXfilterPatternXX": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_6(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterpattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_7(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "FILTERPATTERN": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_8(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(None, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_9(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, None),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_10(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_11(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, ),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_12(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "XXstartTimeXX": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_13(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "starttime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_14(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "STARTTIME": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_15(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "XXendTimeXX": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_16(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endtime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_17(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "ENDTIME": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_18(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = None
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_19(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["XXnextTokenXX"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_20(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nexttoken"] = page_cursor
        return client.filter_log_events(**request)

    def xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_21(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["NEXTTOKEN"] = page_cursor
        return client.filter_log_events(**request)

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut)
    def _handle_client_error(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_orig(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_1(self, exc: Exception) -> list[str]:
        code = None
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_2(self, exc: Exception) -> list[str]:
        code = _error_code(None)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_3(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code != _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_4(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code != _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_5(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                None,
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_6(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context=None,
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_7(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_8(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_9(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "XXAccess denied reading CloudWatch Logs.XX",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_10(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "access denied reading cloudwatch logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_11(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "ACCESS DENIED READING CLOUDWATCH LOGS.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_12(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"XXclusterXX": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_13(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"CLUSTER": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_14(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "XXregionXX": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_15(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "REGION": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_16(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region and "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_17(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "XXunknownXX"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_18(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "UNKNOWN"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_19(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            None,
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_20(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context=None,
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_21(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_22(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_23(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "XXCloudWatch Logs query failed.XX",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_24(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "cloudwatch logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_25(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CLOUDWATCH LOGS QUERY FAILED.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_26(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "XXclusterXX": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_27(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "CLUSTER": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_28(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "XXregionXX": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_29(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "REGION": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_30(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region and "unknown",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_31(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "XXunknownXX",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_32(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "UNKNOWN",
                "error": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_33(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "XXerrorXX": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_34(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "ERROR": str(exc),
            },
        ) from exc

    def xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_35(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(None),
            },
        ) from exc

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut)
    def _group_by_container(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_orig(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_1(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = None
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_2(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = None
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_3(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = None
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_4(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(None)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_5(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = None
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_6(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(None, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_7(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, None)
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_8(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault([])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_9(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, )
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_10(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) > _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_11(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(None)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_12(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                break
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_13(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(None)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_14(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=None,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_15(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=None,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_16(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=None,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_17(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_18(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_19(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                )
            for container, lines in lines_by_container.items()
        ]

    def xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_20(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container not in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    @_mutmut_mutated(mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("logs", region_name=self._region)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_orig(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("logs", region_name=self._region)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_1(self) -> LogsClient:
        if self._logs_client is not None:
            import boto3

            self._logs_client = boto3.client("logs", region_name=self._region)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_2(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = None
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_3(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client(None, region_name=self._region)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_4(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("logs", region_name=None)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_5(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client(region_name=self._region)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_6(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("logs", )
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_7(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("XXlogsXX", region_name=self._region)
        return self._logs_client

    def xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_8(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("LOGS", region_name=self._region)
        return self._logs_client

mutants_xǁCloudWatchLogsAdapterǁ__init____mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ__init____mutmut['xǁCloudWatchLogsAdapterǁ__init____mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ__init____mutmut['xǁCloudWatchLogsAdapterǁ__init____mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ__init____mutmut['xǁCloudWatchLogsAdapterǁ__init____mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_4'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_5'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_6'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_7'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_8'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_9'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_10'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_11'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_12'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_13'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_14'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_15'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_16'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut['xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_17'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁfetch_pod_container_logs__mutmut_17 # type: ignore # mutmut generated

mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_4'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_5'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_6'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_7'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_8'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_9'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_10'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_11'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_12'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_13'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_14'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_15'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_16'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_17'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_18'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_19'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_20'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_21'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_22'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_23'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_24'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_25'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_26'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_27'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_28'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_29'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_30'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_31'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_32'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_33'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_34'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_35'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_36'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_37'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_38'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_39'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_40'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_41'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_42'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_43'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_44'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_45'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_46'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_47'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_48'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_49'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_50'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_51'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_51 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_52'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_52 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_53'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_53 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_54'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_54 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_55'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_55 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_56'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_56 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_57'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_57 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_58'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_58 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_59'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_59 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_60'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_60 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_61'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_61 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_62'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_62 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_63'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_63 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_64'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_64 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_65'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_65 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_events__mutmut['xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_66'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_events__mutmut_66 # type: ignore # mutmut generated

mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_4'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_5'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_6'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_7'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_8'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_9'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_10'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_11'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_12'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_13'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_14'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_15'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_16'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_17'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_18'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_19'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_20'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_filter_page__mutmut['xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_21'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_filter_page__mutmut_21 # type: ignore # mutmut generated

mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_4'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_5'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_6'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_7'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_8'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_9'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_10'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_11'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_12'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_13'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_14'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_15'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_16'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_17'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_18'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_19'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_20'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_21'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_22'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_23'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_24'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_25'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_26'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_27'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_28'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_29'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_30'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_31'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_32'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_33'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_34'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut['xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_35'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_handle_client_error__mutmut_35 # type: ignore # mutmut generated

mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_4'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_5'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_6'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_7'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_8'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_9'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_10'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_11'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_12'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_13'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_14'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_15'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_16'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_17'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_18'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_19'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut['xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_20'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_group_by_container__mutmut_20 # type: ignore # mutmut generated

mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_1'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_2'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_3'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_4'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_5'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_6'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_7'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut['xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_8'] = CloudWatchLogsAdapter.xǁCloudWatchLogsAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated
mutants_x__error_code__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__error_code__mutmut)
def _error_code(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_orig(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_1(exc: Exception) -> str:
    response = None
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_2(exc: Exception) -> str:
    response = getattr(None, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_3(exc: Exception) -> str:
    response = getattr(exc, None, None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_4(exc: Exception) -> str:
    response = getattr("response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_5(exc: Exception) -> str:
    response = getattr(exc, None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_6(exc: Exception) -> str:
    response = getattr(exc, "response", )
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_7(exc: Exception) -> str:
    response = getattr(exc, "XXresponseXX", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_8(exc: Exception) -> str:
    response = getattr(exc, "RESPONSE", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_9(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = None
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_10(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get(None, {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_11(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", None)
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_12(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get({})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_13(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", )
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_14(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("XXErrorXX", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_15(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_16(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("ERROR", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def x__error_code__mutmut_17(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(None)
    return ""


def x__error_code__mutmut_18(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get(None, ""))
    return ""


def x__error_code__mutmut_19(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", None))
    return ""


def x__error_code__mutmut_20(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get(""))
    return ""


def x__error_code__mutmut_21(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ))
    return ""


def x__error_code__mutmut_22(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("XXCodeXX", ""))
    return ""


def x__error_code__mutmut_23(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("code", ""))
    return ""


def x__error_code__mutmut_24(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("CODE", ""))
    return ""


def x__error_code__mutmut_25(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", "XXXX"))
    return ""


def x__error_code__mutmut_26(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return "XXXX"

mutants_x__error_code__mutmut['_mutmut_orig'] = x__error_code__mutmut_orig # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_1'] = x__error_code__mutmut_1 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_2'] = x__error_code__mutmut_2 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_3'] = x__error_code__mutmut_3 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_4'] = x__error_code__mutmut_4 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_5'] = x__error_code__mutmut_5 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_6'] = x__error_code__mutmut_6 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_7'] = x__error_code__mutmut_7 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_8'] = x__error_code__mutmut_8 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_9'] = x__error_code__mutmut_9 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_10'] = x__error_code__mutmut_10 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_11'] = x__error_code__mutmut_11 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_12'] = x__error_code__mutmut_12 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_13'] = x__error_code__mutmut_13 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_14'] = x__error_code__mutmut_14 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_15'] = x__error_code__mutmut_15 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_16'] = x__error_code__mutmut_16 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_17'] = x__error_code__mutmut_17 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_18'] = x__error_code__mutmut_18 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_19'] = x__error_code__mutmut_19 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_20'] = x__error_code__mutmut_20 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_21'] = x__error_code__mutmut_21 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_22'] = x__error_code__mutmut_22 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_23'] = x__error_code__mutmut_23 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_24'] = x__error_code__mutmut_24 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_25'] = x__error_code__mutmut_25 # type: ignore # mutmut generated
mutants_x__error_code__mutmut['x__error_code__mutmut_26'] = x__error_code__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_message__mutmut)
def _parse_message(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_orig(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_1(message: str) -> tuple[str, str]:
    try:
        parsed = None
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_2(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(None)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_3(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_4(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = None
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_5(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get(None, {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_6(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", None)
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_7(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get({})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_8(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", )
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_9(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("XXkubernetesXX", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_10(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("KUBERNETES", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_11(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = None
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_12(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = None
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_13(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(None)
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_14(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get(None, _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_15(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", None))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_16(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get(_UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_17(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", ))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_18(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("XXcontainer_nameXX", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_19(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("CONTAINER_NAME", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line


def x__parse_message__mutmut_20(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = None
    return container, line


def x__parse_message__mutmut_21(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(None)
    return container, line


def x__parse_message__mutmut_22(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get(None, message))
    return container, line


def x__parse_message__mutmut_23(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", None))
    return container, line


def x__parse_message__mutmut_24(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get(message))
    return container, line


def x__parse_message__mutmut_25(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", ))
    return container, line


def x__parse_message__mutmut_26(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("XXlogXX", message))
    return container, line


def x__parse_message__mutmut_27(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("LOG", message))
    return container, line

mutants_x__parse_message__mutmut['_mutmut_orig'] = x__parse_message__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_1'] = x__parse_message__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_2'] = x__parse_message__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_3'] = x__parse_message__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_4'] = x__parse_message__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_5'] = x__parse_message__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_6'] = x__parse_message__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_7'] = x__parse_message__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_8'] = x__parse_message__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_9'] = x__parse_message__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_10'] = x__parse_message__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_11'] = x__parse_message__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_12'] = x__parse_message__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_13'] = x__parse_message__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_14'] = x__parse_message__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_15'] = x__parse_message__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_16'] = x__parse_message__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_17'] = x__parse_message__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_18'] = x__parse_message__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_19'] = x__parse_message__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_20'] = x__parse_message__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_21'] = x__parse_message__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_22'] = x__parse_message__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_23'] = x__parse_message__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_24'] = x__parse_message__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_25'] = x__parse_message__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_26'] = x__parse_message__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_27'] = x__parse_message__mutmut_27 # type: ignore # mutmut generated
