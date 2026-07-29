"""Tests for llm_providers.py — configuration dictionary."""

from __future__ import annotations

from hexawyn.infrastructure.config.llm_providers import LLM_PROVIDERS


class TestLLMProviders:
    """Cover LLM_PROVIDERS dict (line 1)."""

    def test_has_expected_keys(self) -> None:
        expected_keys = {str(i) for i in range(9)}
        assert set(LLM_PROVIDERS.keys()) == expected_keys

    def test_each_entry_has_required_fields(self) -> None:
        for key, value in LLM_PROVIDERS.items():
            assert "name" in value
            assert "base_url" in value
            assert "env_key" in value

    def test_custom_has_empty_base_url(self) -> None:
        assert LLM_PROVIDERS["0"]["name"] == "Custom"
        assert LLM_PROVIDERS["0"]["base_url"] == ""

    def test_all_base_urls_except_custom_start_with_https(self) -> None:
        for key, value in LLM_PROVIDERS.items():
            if key != "0":
                assert value["base_url"].startswith(
                    "https://"
                ), f"Provider {key} ({value['name']}) has non-https URL"

    def test_all_env_keys_are_non_empty(self) -> None:
        for key, value in LLM_PROVIDERS.items():
            assert value["env_key"]

    def test_is_dict_of_str_str_dicts(self) -> None:
        assert isinstance(LLM_PROVIDERS, dict)
        for value in LLM_PROVIDERS.values():
            assert isinstance(value, dict)
            for field_name, field_value in value.items():
                assert isinstance(field_name, str)
                assert isinstance(field_value, str)
