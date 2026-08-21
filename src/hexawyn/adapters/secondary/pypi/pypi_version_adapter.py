from __future__ import annotations

import httpx
from hexawyn.application.ports.driven.version_check_port import VersionCheckPort

PYPI_JSON_URL = "https://pypi.org/pypi/hexawyn/json"


class PyPIVersionAdapter(VersionCheckPort):
    """Fetch the latest published hexawyn version from PyPI."""

    def fetch_latest_version(self) -> str:
        try:
            response = httpx.get(PYPI_JSON_URL, timeout=10)
        except (httpx.HTTPError, OSError):
            return ""
        if response.status_code != 200:  # noqa: PLR2004
            return ""
        try:
            info = response.json().get("info", {})
        except ValueError:
            return ""
        return str(info.get("version", "")) if isinstance(info, dict) else ""
