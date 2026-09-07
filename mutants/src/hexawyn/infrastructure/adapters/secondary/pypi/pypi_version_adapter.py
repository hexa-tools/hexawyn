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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__pypi_json_url__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pypi_json_url__mutmut)
def _pypi_json_url(index_url: str) -> str:
    """Build the JSON endpoint for a given PyPI index."""
    return f"{index_url.rstrip('/')}/pypi/hexawyn/json"


def x__pypi_json_url__mutmut_orig(index_url: str) -> str:
    """Build the JSON endpoint for a given PyPI index."""
    return f"{index_url.rstrip('/')}/pypi/hexawyn/json"


def x__pypi_json_url__mutmut_1(index_url: str) -> str:
    """Build the JSON endpoint for a given PyPI index."""
    return f"{index_url.rstrip(None)}/pypi/hexawyn/json"


def x__pypi_json_url__mutmut_2(index_url: str) -> str:
    """Build the JSON endpoint for a given PyPI index."""
    return f"{index_url.lstrip('/')}/pypi/hexawyn/json"


def x__pypi_json_url__mutmut_3(index_url: str) -> str:
    """Build the JSON endpoint for a given PyPI index."""
    return f"{index_url.rstrip('XX/XX')}/pypi/hexawyn/json"

mutants_x__pypi_json_url__mutmut['_mutmut_orig'] = x__pypi_json_url__mutmut_orig # type: ignore # mutmut generated
mutants_x__pypi_json_url__mutmut['x__pypi_json_url__mutmut_1'] = x__pypi_json_url__mutmut_1 # type: ignore # mutmut generated
mutants_x__pypi_json_url__mutmut['x__pypi_json_url__mutmut_2'] = x__pypi_json_url__mutmut_2 # type: ignore # mutmut generated
mutants_x__pypi_json_url__mutmut['x__pypi_json_url__mutmut_3'] = x__pypi_json_url__mutmut_3 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__resolve_index_url__mutmut)
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


def x__resolve_index_url__mutmut_orig() -> str:
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


def x__resolve_index_url__mutmut_1() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = None
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_2() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get(None)
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_3() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("XXHEXAWYN_PYPI_INDEX_URLXX")
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_4() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("hexawyn_pypi_index_url")
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_5() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.rstrip(None)

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_6() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.lstrip("/")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_7() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.rstrip("XX/XX")

    config = load_config()
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_8() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.rstrip("/")

    config = None
    config_index = config.get(_INDEX_CONFIG_KEY)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_9() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = None
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_10() -> str:
    """Resolve the PyPI index in priority order.

    1. ``HEXAWYN_PYPI_INDEX_URL`` env var (explicit override, e.g. TestPyPI dev).
    2. A previously persisted ``pypi_index_url`` in ~/.hexawyn/config.yaml.
    3. The default production index (https://pypi.org).
    """
    env_index = os.environ.get("HEXAWYN_PYPI_INDEX_URL")
    if env_index:
        return env_index.rstrip("/")

    config = load_config()
    config_index = config.get(None)
    if isinstance(config_index, str) and config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_11() -> str:
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
    if isinstance(config_index, str) or config_index:
        return config_index.rstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_12() -> str:
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
        return config_index.rstrip(None)

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_13() -> str:
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
        return config_index.lstrip("/")

    return DEFAULT_PYPI_INDEX_URL


def x__resolve_index_url__mutmut_14() -> str:
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
        return config_index.rstrip("XX/XX")

    return DEFAULT_PYPI_INDEX_URL

mutants_x__resolve_index_url__mutmut['_mutmut_orig'] = x__resolve_index_url__mutmut_orig # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_1'] = x__resolve_index_url__mutmut_1 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_2'] = x__resolve_index_url__mutmut_2 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_3'] = x__resolve_index_url__mutmut_3 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_4'] = x__resolve_index_url__mutmut_4 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_5'] = x__resolve_index_url__mutmut_5 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_6'] = x__resolve_index_url__mutmut_6 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_7'] = x__resolve_index_url__mutmut_7 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_8'] = x__resolve_index_url__mutmut_8 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_9'] = x__resolve_index_url__mutmut_9 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_10'] = x__resolve_index_url__mutmut_10 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_11'] = x__resolve_index_url__mutmut_11 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_12'] = x__resolve_index_url__mutmut_12 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_13'] = x__resolve_index_url__mutmut_13 # type: ignore # mutmut generated
mutants_x__resolve_index_url__mutmut['x__resolve_index_url__mutmut_14'] = x__resolve_index_url__mutmut_14 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__fetch_version__mutmut)
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


def x__fetch_version__mutmut_orig(index_url: str) -> str | None:
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


def x__fetch_version__mutmut_1(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = None
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


def x__fetch_version__mutmut_2(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(None, timeout=10)
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


def x__fetch_version__mutmut_3(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(index_url), timeout=None)
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


def x__fetch_version__mutmut_4(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(timeout=10)
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


def x__fetch_version__mutmut_5(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(index_url), )
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


def x__fetch_version__mutmut_6(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(None), timeout=10)
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


def x__fetch_version__mutmut_7(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(index_url), timeout=11)
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


def x__fetch_version__mutmut_8(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(index_url), timeout=10)
    except (httpx.HTTPError, OSError):
        return None
    if response.status_code == 200:  # noqa: PLR2004
        return None
    try:
        info = response.json().get("info", {})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_9(index_url: str) -> str | None:
    """Fetch the latest version from a single index.

    Returns the version string, or None when the index cannot be reached,
    does not host the package, or returns malformed data.
    """
    try:
        response = httpx.get(_pypi_json_url(index_url), timeout=10)
    except (httpx.HTTPError, OSError):
        return None
    if response.status_code != 201:  # noqa: PLR2004
        return None
    try:
        info = response.json().get("info", {})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_10(index_url: str) -> str | None:
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
        info = None
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_11(index_url: str) -> str | None:
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
        info = response.json().get(None, {})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_12(index_url: str) -> str | None:
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
        info = response.json().get("info", None)
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_13(index_url: str) -> str | None:
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
        info = response.json().get({})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_14(index_url: str) -> str | None:
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
        info = response.json().get("info", )
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_15(index_url: str) -> str | None:
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
        info = response.json().get("XXinfoXX", {})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_16(index_url: str) -> str | None:
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
        info = response.json().get("INFO", {})
    except ValueError:
        return None
    if not isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_17(index_url: str) -> str | None:
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
    if isinstance(info, dict):
        return None
    version = info.get("version")
    return str(version) if version else None


def x__fetch_version__mutmut_18(index_url: str) -> str | None:
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
    version = None
    return str(version) if version else None


def x__fetch_version__mutmut_19(index_url: str) -> str | None:
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
    version = info.get(None)
    return str(version) if version else None


def x__fetch_version__mutmut_20(index_url: str) -> str | None:
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
    version = info.get("XXversionXX")
    return str(version) if version else None


def x__fetch_version__mutmut_21(index_url: str) -> str | None:
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
    version = info.get("VERSION")
    return str(version) if version else None


def x__fetch_version__mutmut_22(index_url: str) -> str | None:
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
    return str(None) if version else None

mutants_x__fetch_version__mutmut['_mutmut_orig'] = x__fetch_version__mutmut_orig # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_1'] = x__fetch_version__mutmut_1 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_2'] = x__fetch_version__mutmut_2 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_3'] = x__fetch_version__mutmut_3 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_4'] = x__fetch_version__mutmut_4 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_5'] = x__fetch_version__mutmut_5 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_6'] = x__fetch_version__mutmut_6 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_7'] = x__fetch_version__mutmut_7 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_8'] = x__fetch_version__mutmut_8 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_9'] = x__fetch_version__mutmut_9 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_10'] = x__fetch_version__mutmut_10 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_11'] = x__fetch_version__mutmut_11 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_12'] = x__fetch_version__mutmut_12 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_13'] = x__fetch_version__mutmut_13 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_14'] = x__fetch_version__mutmut_14 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_15'] = x__fetch_version__mutmut_15 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_16'] = x__fetch_version__mutmut_16 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_17'] = x__fetch_version__mutmut_17 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_18'] = x__fetch_version__mutmut_18 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_19'] = x__fetch_version__mutmut_19 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_20'] = x__fetch_version__mutmut_20 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_21'] = x__fetch_version__mutmut_21 # type: ignore # mutmut generated
mutants_x__fetch_version__mutmut['x__fetch_version__mutmut_22'] = x__fetch_version__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut: MutantDict = {}  # type: ignore


class PyPIVersionAdapter(VersionCheckPort):
    """Fetch the latest published hexawyn version from PyPI.

    When no explicit index (env var / persisted config) is configured, the
    production index is queried first and a TestPyPI fallback is attempted if
    the package is missing there. A successful fallback is persisted so later
    checks target the same index without an extra request.
    """

    @_mutmut_mutated(mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut)
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

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_orig(self) -> str:
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

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_1(self) -> str:
        index_url = None
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

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_2(self) -> str:
        index_url = _resolve_index_url()
        version = None
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

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_3(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(None)
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

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_4(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_5(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = None
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_6(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") and load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_7(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get(None) or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_8(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("XXHEXAWYN_PYPI_INDEX_URLXX") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_9(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("hexawyn_pypi_index_url") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_10(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(None)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_11(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit or index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_12(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_13(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url != DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_14(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = None
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_15(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(None)
            if fallback_version is not None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_16(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is None:
                self._persist_index(TEST_PYPI_INDEX_URL)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_17(self) -> str:
        index_url = _resolve_index_url()
        version = _fetch_version(index_url)
        if version is not None:
            return version

        # Only fall back to TestPyPI when no explicit index was configured.
        explicit = os.environ.get("HEXAWYN_PYPI_INDEX_URL") or load_config().get(_INDEX_CONFIG_KEY)
        if not explicit and index_url == DEFAULT_PYPI_INDEX_URL:
            fallback_version = _fetch_version(TEST_PYPI_INDEX_URL)
            if fallback_version is not None:
                self._persist_index(None)
                return fallback_version

        return ""

    def xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_18(self) -> str:
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

        return "XXXX"

    @staticmethod
    @_mutmut_mutated(mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut)
    def _persist_index(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_orig(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_1(index_url: str) -> None:
        try:
            config = None
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_2(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = None
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_3(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(None)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_4(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning(None, index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_5(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", None, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_6(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, None)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_7(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning(index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_8(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_9(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not persist PyPI index %s: %s", index_url, )

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_10(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("XXCould not persist PyPI index %s: %sXX", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_11(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("could not persist pypi index %s: %s", index_url, exc)

    @staticmethod
    def xǁPyPIVersionAdapterǁ_persist_index__mutmut_12(index_url: str) -> None:
        try:
            config = load_config()
            config[_INDEX_CONFIG_KEY] = index_url
            save_config(config)
        except Exception as exc:  # noqa: BLE001
            logger.warning("COULD NOT PERSIST PYPI INDEX %S: %S", index_url, exc)

mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['_mutmut_orig'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_1'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_2'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_3'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_4'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_5'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_6'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_7'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_8'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_9'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_10'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_11'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_12'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_13'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_14'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_15'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_16'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_17'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁfetch_latest_version__mutmut['xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_18'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁfetch_latest_version__mutmut_18 # type: ignore # mutmut generated

mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['_mutmut_orig'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_1'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_2'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_3'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_4'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_5'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_6'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_7'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_8'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_9'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_10'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_11'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPyPIVersionAdapterǁ_persist_index__mutmut['xǁPyPIVersionAdapterǁ_persist_index__mutmut_12'] = PyPIVersionAdapter.xǁPyPIVersionAdapterǁ_persist_index__mutmut_12 # type: ignore # mutmut generated
