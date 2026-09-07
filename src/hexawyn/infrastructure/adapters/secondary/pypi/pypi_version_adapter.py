from __future__ import annotations

import logging
import os

import httpx
from hexawyn.application.ports.driven.version_check_port import VersionCheckPort
from hexawyn.infrastructure.config.config_manager import load_config, save_config

logger = logging.getLogger(__name__)

DEFAULT_PYPI_INDEX_URL = "https://pypi.org"
TEST_PYPI_INDEX_URL = "https://test.pypi.org"
_INDEX_CONFIG_KEY = "pypi_index_url"


def _pypi_json_url(index_url: str) -> str:
    """Build the JSON endpoint for a given PyPI index."""
    return f"{index_url.rstrip('/')}/pypi/hexawyn/json"


def _resolve_index_url() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def _fetch_version(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(index_url), timeout=10)
    except (httpx.HTTPError, OSError):
        return None
    if response.status_code != 200:  # noqa: PLR2004
        return None
    try:
        info = response.json().get("info", {})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


class PyPIVersionAdapter(VersionCheckPort):
    """Fetch the latest published hexawyn version from PyPI.

    When no explicit index (env var / persisted config) is configured, the
    production index is queried first and a TestPyPI fallback is attempted if
    the package is missing there. A successful fallback is persisted so later
    checks target the same index without an extra request.
    """

    def fetch_latest_version(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    @staticmethod
    def _persist_index(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, exc)
