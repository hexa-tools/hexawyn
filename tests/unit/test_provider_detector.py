import pytest

from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


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
        # boto3, azure, etc. are not installed in dev venv
        assert providers["aws"] is False
        assert providers["azure"] is False
        assert providers["gcp"] is False
