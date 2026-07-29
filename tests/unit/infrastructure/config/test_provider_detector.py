from __future__ import annotations

from unittest.mock import patch

from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


class TestDetectInstalledProviders:
    def test_vanilla_always_available(self) -> None:
        providers = detect_installed_providers()
        assert providers["vanilla"] is True

    def test_returns_dict_with_all_provider_keys(self) -> None:
        providers = detect_installed_providers()
        for key in ("vanilla", "aws", "azure", "gcp", "openshift", "datadog"):
            assert key in providers
            assert isinstance(providers[key], bool)

    def test_import_failures_are_caught(self) -> None:
        with patch("builtins.__import__", side_effect=ImportError("no module")):
            providers = detect_installed_providers()
            assert providers["vanilla"] is True
            assert providers["aws"] is False
            assert providers["azure"] is False
            assert providers["gcp"] is False
            assert providers["openshift"] is False
            assert providers["datadog"] is False
