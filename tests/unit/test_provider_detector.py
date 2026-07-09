import importlib.util

import pytest
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


def _is_importable(module_name: str) -> bool:
    try:
        return importlib.util.find_spec(module_name) is not None
    except ModuleNotFoundError:
        return False


class TestDetectInstalledProviders:
    def test_vanilla_always_true(self):
        providers = detect_installed_providers()
        assert providers["vanilla"] is True

    def test_returns_dict_with_all_keys(self):
        providers = detect_installed_providers()
        expected_keys = {"vanilla", "aws", "azure", "gcp", "openshift", "datadog"}
        assert set(providers.keys()) == expected_keys

    def test_all_values_are_booleans(self):
        providers = detect_installed_providers()
        for key, value in providers.items():
            assert isinstance(value, bool), f"{key} is not bool: {type(value)}"

    def test_never_raises(self):
        try:
            detect_installed_providers()
        except Exception as e:
            pytest.fail(f"detect_installed_providers raised {e}")

    def test_unknown_providers_false(self):
        providers = detect_installed_providers()
        # Detection must reflect the real import availability in the current
        # environment (extras may or may not be installed), never a hardcoded
        # assumption.
        assert providers["aws"] is _is_importable("boto3")
        assert providers["azure"] is _is_importable("azure.identity")
        assert providers["gcp"] is _is_importable("google.cloud.container")
