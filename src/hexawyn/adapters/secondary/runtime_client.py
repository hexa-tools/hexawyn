import time

import httpx

DEFAULT_TIMEOUT = 60.0
DEFAULT_POLL_INTERVAL = 1.0


class RuntimeClient:
    def __init__(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = httpx.Client(timeout=30.0)

    def close(self) -> None:
        self._client.close()

    def post_tools(self, tools_payload: list[dict[str, object]]) -> None:
        response = self._client.post(
            f"{self._endpoint}/api/v1/tools/sync",
            json={"tools": tools_payload},
        )
        response.raise_for_status()

    def check_quota(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota")
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def increment_quota(self) -> None:
        response = self._client.post(f"{self._endpoint}/api/v1/quota/increment")
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
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def get_investigation(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
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
            if current_status in ("completed", "failed", "complete"):
                return status_response
            time.sleep(interval)
        return status_response
