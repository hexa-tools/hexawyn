import logging
import os

from hexawyn.adapters.secondary.adapter_factory import build_adapters
from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.cli.presentation.formatting import format_size
from hexawyn.infrastructure.config.config_manager import get_llm_config
from hexawyn.infrastructure.config.kubernetes_context import FileKubernetesDiscoveryService
from hexawyn.infrastructure.config.llm_providers import LLM_PROVIDERS
from hexawyn.infrastructure.memory.duckdb_client import (
    _DB_SIZE_WARNING_THRESHOLD,
    DB_PATH,
    get_db_size_bytes,
)

logger = logging.getLogger(__name__)

_PROVIDERS = LLM_PROVIDERS


def _load_api_key_to_env() -> bool:
    """Load saved API key + base_url into env vars. Returns True if configured."""
    cfg = get_llm_config()
    if cfg.get("api_key"):
        os.environ["LLM_API_KEY"] = cfg["api_key"]
        if cfg.get("base_url"):
            os.environ["LLM_BASE_URL"] = cfg["base_url"]
        return True
    return False


class HexawynApp:
    def __init__(self, expert_mode: bool = False, force_setup: bool = False) -> None:
        self.expert_mode = expert_mode
        self.force_setup = force_setup

    def run(self) -> None:
        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        _load_api_key_to_env()

        if not demo_mode:
            self._auto_refresh_license()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def _auto_refresh_license(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        refresh_license()

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
