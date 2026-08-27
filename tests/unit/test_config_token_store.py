"""Unit tests for the config-backed token store."""

from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.auth.config_token_store import ConfigTokenStore


class TestGetToken:
    def test_env_token_takes_precedence(self, monkeypatch) -> None:
        monkeypatch.setenv("HEXAWYN_TOKEN", "hxw_env")
        with patch(
            "hexawyn.adapters.secondary.auth.config_token_store.load_config",
            return_value={"hexawyn_token": "hxw_file"},
        ):
            assert ConfigTokenStore().get_token() == "hxw_env"

    def test_falls_back_to_config(self, monkeypatch) -> None:
        monkeypatch.delenv("HEXAWYN_TOKEN", raising=False)
        with patch(
            "hexawyn.adapters.secondary.auth.config_token_store.load_config",
            return_value={"hexawyn_token": "hxw_file"},
        ):
            assert ConfigTokenStore().get_token() == "hxw_file"

    def test_returns_none_when_absent(self, monkeypatch) -> None:
        monkeypatch.delenv("HEXAWYN_TOKEN", raising=False)
        with patch(
            "hexawyn.adapters.secondary.auth.config_token_store.load_config", return_value={}
        ):
            assert ConfigTokenStore().get_token() is None

    def test_ignores_non_string_config(self, monkeypatch) -> None:
        monkeypatch.delenv("HEXAWYN_TOKEN", raising=False)
        with patch(
            "hexawyn.adapters.secondary.auth.config_token_store.load_config",
            return_value={"hexawyn_token": 42},
        ):
            assert ConfigTokenStore().get_token() is None


class TestSaveToken:
    def test_saves_token_to_config(self, monkeypatch) -> None:
        monkeypatch.delenv("HEXAWYN_TOKEN", raising=False)
        saved: dict[str, object] = {}

        def fake_load() -> dict[str, object]:
            return dict(saved)

        def fake_save(config: dict[str, object]) -> None:
            saved.clear()
            saved.update(config)

        with (
            patch(
                "hexawyn.adapters.secondary.auth.config_token_store.load_config",
                side_effect=fake_load,
            ),
            patch(
                "hexawyn.adapters.secondary.auth.config_token_store.save_config",
                side_effect=fake_save,
            ),
        ):
            ConfigTokenStore().save_token("hxw_new")
            assert saved["hexawyn_token"] == "hxw_new"

    def test_preserves_existing_keys(self, monkeypatch) -> None:
        monkeypatch.delenv("HEXAWYN_TOKEN", raising=False)
        base = {"llm_provider": "ollama", "hexawyn_token": "hxw_old"}
        saved: dict[str, object] = dict(base)

        def fake_load() -> dict[str, object]:
            return dict(saved)

        def fake_save(config: dict[str, object]) -> None:
            saved.clear()
            saved.update(config)

        with (
            patch(
                "hexawyn.adapters.secondary.auth.config_token_store.load_config",
                side_effect=fake_load,
            ),
            patch(
                "hexawyn.adapters.secondary.auth.config_token_store.save_config",
                side_effect=fake_save,
            ),
        ):
            ConfigTokenStore().save_token("hxw_new")
            assert saved["llm_provider"] == "ollama"
            assert saved["hexawyn_token"] == "hxw_new"
