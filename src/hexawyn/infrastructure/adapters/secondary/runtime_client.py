import json
import time
from collections.abc import Generator

import httpx

DEFAULT_TIMEOUT = 300.0
DEFAULT_POLL_INTERVAL = 1.0


class RuntimeClient:
    def __init__(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)

    def close(self) -> None:
        self._client.close()

    def check_quota(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota", headers=self._headers)
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def increment_quota(self) -> None:
        response = self._client.post(
            f"{self._endpoint}/api/v1/quota/increment", headers=self._headers
        )
        response.raise_for_status()

    def post_investigation(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def get_investigation(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def poll_investigation(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def stream_investigation(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def list_custom_tools(self) -> list[dict[str, object]]:
        response = self._client.get(f"{self._endpoint}/api/v1/custom-tools", headers=self._headers)
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def describe_custom_tool(self, name: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/custom-tools/{name}", headers=self._headers
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def run_custom_tool(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=params,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def startup_scan(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data
