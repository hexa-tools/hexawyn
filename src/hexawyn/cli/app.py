import os

from hexawyn.adapters.secondary.adapter_factory import build_adapters
from hexawyn.application.service.runtime_adapter import get_runtime
from hexawyn.infrastructure.config.config_manager import get_llm_config
from hexawyn.infrastructure.config.kubernetes_context import FileKubernetesDiscoveryService
from hexawyn.infrastructure.memory.duckdb_client import (
    _DB_SIZE_WARNING_THRESHOLD,
    DB_PATH,
    get_db_size_bytes,
)


def _format_size(size_bytes: int) -> str:
    if size_bytes < 1_048_576:
        return f"{size_bytes / 1024:.0f} KB"
    if size_bytes < 1_073_741_824:
        return f"{size_bytes / 1_048_576:.0f} MB"
    return f"{size_bytes / 1_073_741_824:.1f} GB"


_PROVIDERS: dict[str, dict[str, str]] = {
    "1": {
        "name": "DeepSeek",
        "base_url": "https://api.deepseek.com",
        "env_key": "DEEPSEEK_API_KEY",
    },
    "2": {"name": "OpenAI", "base_url": "https://api.openai.com/v1", "env_key": "OPENAI_API_KEY"},
    "3": {"name": "Groq", "base_url": "https://api.groq.com/openai/v1", "env_key": "GROQ_API_KEY"},
    "4": {
        "name": "Together AI",
        "base_url": "https://api.together.xyz/v1",
        "env_key": "TOGETHER_API_KEY",
    },
    "5": {"name": "Mistral", "base_url": "https://api.mistral.ai/v1", "env_key": "MISTRAL_API_KEY"},
    "6": {
        "name": "Google (Gemini)",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
        "env_key": "GEMINI_API_KEY",
    },
    "7": {
        "name": "OpenRouter",
        "base_url": "https://openrouter.ai/api/v1",
        "env_key": "OPENROUTER_API_KEY",
    },
    "8": {"name": "xAI (Grok)", "base_url": "https://api.x.ai/v1", "env_key": "XAI_API_KEY"},
    "0": {"name": "Custom", "base_url": "", "env_key": "LLM_API_KEY"},
}


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
        has_key = _load_api_key_to_env()

        if self.force_setup and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        if not has_key and not demo_mode:
            self._run_tui(needs_setup=True)
            return

        self._run_tui()

    def _run_tui(self, needs_setup: bool = False) -> None:
        from hexawyn.cli.tui import HexawynTUI

        demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        startup_status = None
        context_service = None
        cluster_name = os.environ.get("KUBECONFIG_CTX", "unknown")

        if not demo_mode:
            context_service = FileKubernetesDiscoveryService()
            startup_status = context_service.startup_status()
            if startup_status.current_context is not None:
                cluster_name = startup_status.current_context.name

        adapter = build_adapters(cluster_name)

        run_startup_scan = False
        if startup_status is not None and startup_status.connected and not needs_setup:
            get_runtime().set_adapter(adapter)
            run_startup_scan = True

        extra_chip = None
        if not self.expert_mode and not demo_mode:
            db_size = get_db_size_bytes(DB_PATH)
            if db_size > _DB_SIZE_WARNING_THRESHOLD:
                extra_chip = f"DB: {_format_size(db_size)} — run 'hexa db purge' to clean old data"

        tui = HexawynTUI(
            adapter=adapter,
            expert_mode=self.expert_mode,
            demo_mode=demo_mode,
            scenario=scenario,
            extra_chip=extra_chip,
            startup_status=startup_status,
            context_service=context_service,
            adapter_builder=build_adapters,
            run_startup_scan=run_startup_scan,
            cluster_name=cluster_name,
            needs_setup=needs_setup,
        )
        tui.run()
