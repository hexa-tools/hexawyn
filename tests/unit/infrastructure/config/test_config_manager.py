import os
from unittest.mock import patch

from hexawyn.infrastructure.config.config_manager import (
    get_api_key,
    get_llm_config,
    load_config,
    save_config,
    save_llm_config,
)


class TestLoadConfig:
    def test_returns_empty_dict_when_no_file(self, tmp_path):
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            assert load_config() == {}

    def test_loads_existing_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-test-key\nlog_level: INFO\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            config = load_config()
            assert config == {"api_key": "sk-test-key", "log_level": "INFO"}


class TestSaveConfig:
    def test_creates_file_and_directory(self, tmp_path):
        config_path = tmp_path / ".hexawyn" / "config.yaml"
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_path):
            save_config({"api_key": "sk-new"})
            assert config_path.exists()
            data = load_config()
            assert data["api_key"] == "sk-new"


class TestGetApiKey:
    def test_prefers_llm_api_key_env_var(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-from-file\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {"LLM_API_KEY": "sk-from-env"}, clear=True):
                assert get_api_key() == "sk-from-env"

    def test_falls_back_to_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-from-file\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {}, clear=True):
                assert get_api_key() == "sk-from-file"

    def test_returns_none_when_no_key(self, tmp_path):
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(os.environ, {}, clear=True):
                assert get_api_key() is None


class TestSaveLLMConfig:
    def test_persists_provider_url_and_key(self, tmp_path):
        config_path = tmp_path / "config.yaml"
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_path):
            save_llm_config("DeepSeek", "https://api.deepseek.com", "sk-saved-key")
            data = load_config()
            assert data["api_key"] == "sk-saved-key"
            assert data["llm_provider"] == "DeepSeek"
            assert data["llm_base_url"] == "https://api.deepseek.com"


class TestRuntimeMode:
    def test_defaults_to_remote(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(os.environ, {}, clear=True):
                from hexawyn.infrastructure.config.config_manager import get_runtime_mode

                assert get_runtime_mode() == "remote"

    def test_reads_configured_mode(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        config_file = tmp_path / "config.yaml"
        config_file.write_text("runtime:\n  mode: remote\n  endpoint: http://localhost:8000\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            from hexawyn.infrastructure.config.config_manager import get_runtime_mode

            assert get_runtime_mode() == "remote"

    def test_invalid_value_falls_back_to_remote(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        config_file = tmp_path / "config.yaml"
        config_file.write_text("runtime:\n  mode: invalid\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {}, clear=True):
                from hexawyn.infrastructure.config.config_manager import get_runtime_mode

                assert get_runtime_mode() == "remote"

    def test_remote_mode_with_endpoint(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        config_file = tmp_path / "config.yaml"
        config_file.write_text("runtime:\n  mode: remote\n  endpoint: http://localhost:8000\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {}, clear=True):
                from hexawyn.infrastructure.config.config_manager import (
                    get_runtime_endpoint,
                )

                assert get_runtime_endpoint() == "http://localhost:8000"

    def test_runtime_endpoint_prefers_env_var(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        config_file = tmp_path / "config.yaml"
        config_file.write_text("runtime:\n  mode: remote\n  endpoint: http://localhost:8000\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(
                os.environ, {"HEXAWYN_RUNTIME_ENDPOINT": "http://172.18.0.4:30080"}, clear=True
            ):
                from hexawyn.infrastructure.config.config_manager import (
                    get_runtime_endpoint,
                )

                assert get_runtime_endpoint() == "http://172.18.0.4:30080"

    def test_runtime_endpoint_env_var_enables_remote_mode(self, tmp_path) -> None:  # type: ignore[no-untyped-def]
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(
                os.environ, {"HEXAWYN_RUNTIME_ENDPOINT": "http://172.18.0.4:30080"}, clear=True
            ):
                from hexawyn.infrastructure.config.config_manager import get_runtime_mode

                assert get_runtime_mode() == "remote"


class TestGetLLMConfig:
    def test_returns_provider_and_url(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text(
            "api_key: sk-xxx\nllm_provider: OpenAI\nllm_base_url: https://api.openai.com/v1\n"
        )
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {}, clear=True):
                cfg = get_llm_config()
                assert cfg["provider"] == "OpenAI"
                assert cfg["base_url"] == "https://api.openai.com/v1"
                assert cfg["api_key"] == "sk-xxx"

    def test_returns_empty_dict_when_no_config(self, tmp_path):
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(os.environ, {}, clear=True):
                assert get_llm_config() == {}


class TestConfigManagerEdgeCases:
    def test_get_api_key_falls_through_empty_env_to_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-from-file\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {"LLM_API_KEY": ""}, clear=True):
                assert get_api_key() == "sk-from-file"

    def test_save_config_overwrites_existing(self, tmp_path):
        config_path = tmp_path / ".hexawyn" / "config.yaml"
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text("api_key: old-key\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_path):
            save_config({"api_key": "new-key"})
            data = load_config()
            assert data["api_key"] == "new-key"

    def test_config_with_nested_keys(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text(
            "api_key: sk-xxx\nruntime:\n  mode: remote\n  endpoint: http://localhost:8000\n"
        )
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            config = load_config()
            assert "runtime" in config
            assert config["runtime"]["mode"] == "remote"

    def test_load_config_non_dict_yaml_returns_empty_dict(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("- item1\n- item2\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            assert load_config() == {}

    def test_get_runtime_endpoint_default(self, tmp_path):
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(os.environ, {}, clear=True):
                from hexawyn.infrastructure.config.config_manager import (
                    get_runtime_endpoint,
                )

                assert get_runtime_endpoint() == "https://api.hexawyn.com"

    def test_get_runtime_mode_embedded(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("runtime:\n  mode: embedded\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {}, clear=True):
                from hexawyn.infrastructure.config.config_manager import get_runtime_mode

                assert get_runtime_mode() == "embedded"


class TestGetRuntimeMode:
    def test_runtime_mode_env_overrides_to_embedded(self, tmp_path) -> None:
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(os.environ, {"HEXAWYN_RUNTIME_MODE": "embedded"}, clear=True):
                from hexawyn.infrastructure.config.config_manager import get_runtime_mode

                assert get_runtime_mode() == "embedded"

    def test_runtime_mode_env_overrides_to_remote(self, tmp_path) -> None:
        with patch(
            "hexawyn.infrastructure.config.config_manager.CONFIG_PATH",
            tmp_path / "nonexistent.yaml",
        ):
            with patch.dict(os.environ, {"HEXAWYN_RUNTIME_MODE": "remote"}, clear=True):
                from hexawyn.infrastructure.config.config_manager import get_runtime_mode

                assert get_runtime_mode() == "remote"
