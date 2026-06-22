import os
from unittest.mock import patch

import pytest

from hexawyn.infrastructure.config.config_manager import (
    get_api_key,
    load_config,
    save_api_key,
    save_config,
)


class TestLoadConfig:
    def test_returns_empty_dict_when_no_file(self, tmp_path):
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", tmp_path / "nonexistent.yaml"):
            assert load_config() == {}

    def test_loads_existing_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-ant-test-key\nlog_level: INFO\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            config = load_config()
            assert config == {"api_key": "sk-ant-test-key", "log_level": "INFO"}


class TestSaveConfig:
    def test_creates_file_and_directory(self, tmp_path):
        config_path = tmp_path / ".hexawyn" / "config.yaml"
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_path):
            save_config({"api_key": "sk-ant-new"})
            assert config_path.exists()
            data = load_config()
            assert data["api_key"] == "sk-ant-new"


class TestGetApiKey:
    def test_prefers_env_var_over_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-ant-from-file\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-from-env"}):
                assert get_api_key() == "sk-ant-from-env"

    def test_falls_back_to_config(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("api_key: sk-ant-from-file\n")
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_file):
            with patch.dict(os.environ, {}, clear=True):
                assert get_api_key() == "sk-ant-from-file"

    def test_returns_none_when_no_key(self, tmp_path):
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", tmp_path / "nonexistent.yaml"):
            with patch.dict(os.environ, {}, clear=True):
                assert get_api_key() is None


class TestSaveApiKey:
    def test_persists_key_to_config(self, tmp_path):
        config_path = tmp_path / "config.yaml"
        with patch("hexawyn.infrastructure.config.config_manager.CONFIG_PATH", config_path):
            save_api_key("sk-ant-saved-key")
            data = load_config()
            assert data["api_key"] == "sk-ant-saved-key"
