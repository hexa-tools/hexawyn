import os
import threading

from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.cli.presentation.formatting import format_size
from hexawyn.infrastructure.adapters.secondary.adapter_factory import build_adapters
from hexawyn.infrastructure.config.config_manager import get_llm_config
from hexawyn.infrastructure.config.kubernetes_context import FileKubernetesDiscoveryService
from hexawyn.infrastructure.config.llm_providers import LLM_PROVIDERS
from hexawyn.infrastructure.memory.duckdb_client import (
    _DB_SIZE_WARNING_THRESHOLD,
    DB_PATH,
    get_db_size_bytes,
)

_PROVIDERS = LLM_PROVIDERS


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__load_api_key_to_env__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_api_key_to_env__mutmut)
def _load_api_key_to_env() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_orig() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_1() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = None
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_2() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get(None):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_3() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("XXapi_keyXX"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_4() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("API_KEY"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_5() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = None
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_6() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["XXLLM_API_KEYXX"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_7() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["llm_api_key"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_8() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["XXapi_keyXX"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_9() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["API_KEY"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_10() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get(None):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_11() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("XXbase_urlXX"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_12() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("BASE_URL"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_13() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = None
        return True
    return False


def x__load_api_key_to_env__mutmut_14() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["XXLLM_BASE_URLXX"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_15() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["llm_base_url"] = cfg["base_url"]
        return True
    return False


def x__load_api_key_to_env__mutmut_16() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["XXbase_urlXX"]
        return True
    return False


def x__load_api_key_to_env__mutmut_17() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["BASE_URL"]
        return True
    return False


def x__load_api_key_to_env__mutmut_18() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return False
    return False


def x__load_api_key_to_env__mutmut_19() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return True

mutants_x__load_api_key_to_env__mutmut['_mutmut_orig'] = x__load_api_key_to_env__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_1'] = x__load_api_key_to_env__mutmut_1 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_2'] = x__load_api_key_to_env__mutmut_2 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_3'] = x__load_api_key_to_env__mutmut_3 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_4'] = x__load_api_key_to_env__mutmut_4 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_5'] = x__load_api_key_to_env__mutmut_5 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_6'] = x__load_api_key_to_env__mutmut_6 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_7'] = x__load_api_key_to_env__mutmut_7 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_8'] = x__load_api_key_to_env__mutmut_8 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_9'] = x__load_api_key_to_env__mutmut_9 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_10'] = x__load_api_key_to_env__mutmut_10 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_11'] = x__load_api_key_to_env__mutmut_11 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_12'] = x__load_api_key_to_env__mutmut_12 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_13'] = x__load_api_key_to_env__mutmut_13 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_14'] = x__load_api_key_to_env__mutmut_14 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_15'] = x__load_api_key_to_env__mutmut_15 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_16'] = x__load_api_key_to_env__mutmut_16 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_17'] = x__load_api_key_to_env__mutmut_17 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_18'] = x__load_api_key_to_env__mutmut_18 # type: ignore # mutmut generated
mutants_x__load_api_key_to_env__mutmut['x__load_api_key_to_env__mutmut_19'] = x__load_api_key_to_env__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynAppǁrun__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynAppǁ_run_tui__mutmut: MutantDict = {}  # type: ignore


class HexawynApp:
    @_mutmut_mutated(mutants_xǁHexawynAppǁ__init____mutmut)
    def __init__(self, expert_mode: bool = False, force_setup: bool = False) -> None:
        self.expert_mode = expert_mode
        self.force_setup = force_setup
    def xǁHexawynAppǁ__init____mutmut_orig(self, expert_mode: bool = False, force_setup: bool = False) -> None:
        self.expert_mode = expert_mode
        self.force_setup = force_setup
    def xǁHexawynAppǁ__init____mutmut_1(self, expert_mode: bool = True, force_setup: bool = False) -> None:
        self.expert_mode = expert_mode
        self.force_setup = force_setup
    def xǁHexawynAppǁ__init____mutmut_2(self, expert_mode: bool = False, force_setup: bool = True) -> None:
        self.expert_mode = expert_mode
        self.force_setup = force_setup
    def xǁHexawynAppǁ__init____mutmut_3(self, expert_mode: bool = False, force_setup: bool = False) -> None:
        self.expert_mode = None
        self.force_setup = force_setup
    def xǁHexawynAppǁ__init____mutmut_4(self, expert_mode: bool = False, force_setup: bool = False) -> None:
        self.expert_mode = expert_mode
        self.force_setup = None

    @_mutmut_mutated(mutants_xǁHexawynAppǁrun__mutmut)
    def run(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_orig(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_1(self) -> None:
        demo_mode = None
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_2(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").upper() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_3(self) -> None:
        demo_mode = os.environ.get(None, "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_4(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", None).lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_5(self) -> None:
        demo_mode = os.environ.get("false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_6(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", ).lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_7(self) -> None:
        demo_mode = os.environ.get("XXHEXAWYN_DEMO_MODEXX", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_8(self) -> None:
        demo_mode = os.environ.get("hexawyn_demo_mode", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_9(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "XXfalseXX").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_10(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "FALSE").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_11(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() != "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_12(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "XXtrueXX"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_13(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "TRUE"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_14(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_15(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup or not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_16(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_17(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=None)
            return

        self._run_tui()

    def xǁHexawynAppǁrun__mutmut_18(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=False)
            return

        self._run_tui()

    @_mutmut_mutated(mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut)
    def _auto_refresh_license(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(target=refresh_license, daemon=True).start()

    def xǁHexawynAppǁ_auto_refresh_license__mutmut_orig(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(target=refresh_license, daemon=True).start()

    def xǁHexawynAppǁ_auto_refresh_license__mutmut_1(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(target=None, daemon=True).start()

    def xǁHexawynAppǁ_auto_refresh_license__mutmut_2(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(target=refresh_license, daemon=None).start()

    def xǁHexawynAppǁ_auto_refresh_license__mutmut_3(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(daemon=True).start()

    def xǁHexawynAppǁ_auto_refresh_license__mutmut_4(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(target=refresh_license, ).start()

    def xǁHexawynAppǁ_auto_refresh_license__mutmut_5(self) -> None:
        """Refresh the license in the background so TUI startup is not blocked.

        The local license (cached) is used immediately; the network refresh runs
        in a daemon thread and does not delay opening the interface.
        """
        from hexawyn.infrastructure.license.license_reader import refresh_license

        threading.Thread(target=refresh_license, daemon=False).start()

    @_mutmut_mutated(mutants_xǁHexawynAppǁ_run_tui__mutmut)
    def _run_tui(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_orig(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_1(self, needs_setup: bool = True) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_2(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = None
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_3(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").upper() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_4(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get(None, "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_5(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", None).lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_6(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_7(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", ).lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_8(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("XXHEXAWYN_DEMO_MODEXX", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_9(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("hexawyn_demo_mode", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_10(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "XXfalseXX").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_11(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "FALSE").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_12(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() != "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_13(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "XXtrueXX"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_14(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "TRUE"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_15(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = None
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_16(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get(None, "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_17(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", None)
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_18(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_19(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", )
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_20(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("XXHEXAWYN_DEMO_SCENARIOXX", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_21(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("hexawyn_demo_scenario", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_22(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "XXaws_eksXX")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_23(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "AWS_EKS")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_24(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = None
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_25(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get(None, "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_26(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", None)
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_27(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_28(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", )
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_29(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("XXKUBECONFIG_CTXXX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_30(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("kubeconfig_ctx", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_31(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "XXunknownXX")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_32(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "UNKNOWN")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_33(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = ""

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_34(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_35(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = None
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_36(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = None
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_37(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_38(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = None

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_39(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = None
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_40(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(None)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_41(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(None)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_42(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = ""
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_43(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode or not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_44(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_45(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_46(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = None
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_47(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(None)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_48(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size >= _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_49(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = None

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_50(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(None)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_51(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = None
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_52(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=None,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_53(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=None,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_54(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=None,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_55(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=None,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_56(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=None,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_57(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=None,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_58(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=None,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_59(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=None,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_60(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=None,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_61(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_62(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_63(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_64(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_65(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_66(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_67(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_68(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            needs_setup=needs_setup,
        )
        tui.run()

    def xǁHexawynAppǁ_run_tui__mutmut_69(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")
        context_service = None

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            current = context_service.current()
            if current is not None:
                cluster_name = current.name

        adapter = build_adapters(cluster_name)
        get_runtime().set_adapter(adapter)

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            context_service=context_service,
            adapter_builder=build_adapters,
            cluster_name=cluster_name,
            )
        tui.run()

mutants_xǁHexawynAppǁ__init____mutmut['_mutmut_orig'] = HexawynApp.xǁHexawynAppǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ__init____mutmut['xǁHexawynAppǁ__init____mutmut_1'] = HexawynApp.xǁHexawynAppǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ__init____mutmut['xǁHexawynAppǁ__init____mutmut_2'] = HexawynApp.xǁHexawynAppǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ__init____mutmut['xǁHexawynAppǁ__init____mutmut_3'] = HexawynApp.xǁHexawynAppǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ__init____mutmut['xǁHexawynAppǁ__init____mutmut_4'] = HexawynApp.xǁHexawynAppǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁHexawynAppǁrun__mutmut['_mutmut_orig'] = HexawynApp.xǁHexawynAppǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_1'] = HexawynApp.xǁHexawynAppǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_2'] = HexawynApp.xǁHexawynAppǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_3'] = HexawynApp.xǁHexawynAppǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_4'] = HexawynApp.xǁHexawynAppǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_5'] = HexawynApp.xǁHexawynAppǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_6'] = HexawynApp.xǁHexawynAppǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_7'] = HexawynApp.xǁHexawynAppǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_8'] = HexawynApp.xǁHexawynAppǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_9'] = HexawynApp.xǁHexawynAppǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_10'] = HexawynApp.xǁHexawynAppǁrun__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_11'] = HexawynApp.xǁHexawynAppǁrun__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_12'] = HexawynApp.xǁHexawynAppǁrun__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_13'] = HexawynApp.xǁHexawynAppǁrun__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_14'] = HexawynApp.xǁHexawynAppǁrun__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_15'] = HexawynApp.xǁHexawynAppǁrun__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_16'] = HexawynApp.xǁHexawynAppǁrun__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_17'] = HexawynApp.xǁHexawynAppǁrun__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁrun__mutmut['xǁHexawynAppǁrun__mutmut_18'] = HexawynApp.xǁHexawynAppǁrun__mutmut_18 # type: ignore # mutmut generated

mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut['_mutmut_orig'] = HexawynApp.xǁHexawynAppǁ_auto_refresh_license__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut['xǁHexawynAppǁ_auto_refresh_license__mutmut_1'] = HexawynApp.xǁHexawynAppǁ_auto_refresh_license__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut['xǁHexawynAppǁ_auto_refresh_license__mutmut_2'] = HexawynApp.xǁHexawynAppǁ_auto_refresh_license__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut['xǁHexawynAppǁ_auto_refresh_license__mutmut_3'] = HexawynApp.xǁHexawynAppǁ_auto_refresh_license__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut['xǁHexawynAppǁ_auto_refresh_license__mutmut_4'] = HexawynApp.xǁHexawynAppǁ_auto_refresh_license__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_auto_refresh_license__mutmut['xǁHexawynAppǁ_auto_refresh_license__mutmut_5'] = HexawynApp.xǁHexawynAppǁ_auto_refresh_license__mutmut_5 # type: ignore # mutmut generated

mutants_xǁHexawynAppǁ_run_tui__mutmut['_mutmut_orig'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_1'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_2'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_3'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_4'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_5'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_6'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_7'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_8'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_9'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_10'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_11'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_12'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_13'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_14'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_15'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_16'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_17'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_18'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_19'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_20'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_21'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_22'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_23'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_24'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_25'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_26'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_27'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_28'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_29'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_30'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_31'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_32'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_33'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_34'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_35'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_36'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_37'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_38'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_39'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_40'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_41'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_42'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_43'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_44'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_45'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_46'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_47'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_48'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_49'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_50'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_51'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_52'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_53'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_54'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_55'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_56'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_57'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_58'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_59'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_60'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_61'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_62'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_63'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_64'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_65'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_66'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_67'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_67 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_68'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_68 # type: ignore # mutmut generated
mutants_xǁHexawynAppǁ_run_tui__mutmut['xǁHexawynAppǁ_run_tui__mutmut_69'] = HexawynApp.xǁHexawynAppǁ_run_tui__mutmut_69 # type: ignore # mutmut generated
