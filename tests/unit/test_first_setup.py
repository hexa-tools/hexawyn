from unittest.mock import patch

from hexawyn.infrastructure.config.first_setup import (
    PROVIDERS,
    install_selected_providers,
)


class TestProviders:
    def test_all_keys_are_providers(self):
        expected = {"aws", "azure", "gcp", "openshift", "datadog"}
        assert set(PROVIDERS.keys()) == expected

    def test_each_provider_has_description_and_package(self):
        for key, (desc, pkg) in PROVIDERS.items():
            assert isinstance(desc, str)
            assert isinstance(pkg, str)
            assert desc
            assert pkg


class TestInstallSelectedProviders:
    def test_does_nothing_when_empty(self):
        with patch("subprocess.run") as mock_run:
            install_selected_providers([])
            mock_run.assert_not_called()

    def test_does_nothing_when_none(self):
        with patch("subprocess.run") as mock_run:
            install_selected_providers(None)  # type: ignore[arg-type]
            mock_run.assert_not_called()

    def test_calls_pip_install_with_extras(self):
        with patch("subprocess.run") as mock_run:
            install_selected_providers(["aws", "datadog"])
            mock_run.assert_called_once_with(
                ["pip", "install", "hexawyn[aws,datadog]"],
                check=True,
            )
