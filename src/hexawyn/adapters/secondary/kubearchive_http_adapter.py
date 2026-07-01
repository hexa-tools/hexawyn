from __future__ import annotations

from typing import cast

import httpx

from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalPodInfo,
    KubeArchivePort,
    KubeArchiveQuery,
    KubeArchiveResponse,
)
from hexawyn.domain.errors import KubeArchiveUnavailableError


class KubeArchiveHTTPAdapter(KubeArchivePort):
    def __init__(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = httpx.Client(timeout=10.0)

    def close(self) -> None:
        self._client.close()

    def query_historical_state(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise KubeArchiveUnavailableError(
                context={"endpoint": self._endpoint, "detail": str(exc)}
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )
