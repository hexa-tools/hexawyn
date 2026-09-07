from pathlib import Path


class TestAppRefactored:
    def test_no_format_size_in_app(self) -> None:
        source = Path("src/hexawyn/cli/app.py").read_text()
        assert (
            "def _format_size" not in source
        ), "_format_size should be imported from presentation/formatting.py"

    def test_no_providers_dict_in_app(self) -> None:
        source = Path("src/hexawyn/cli/app.py").read_text()
        assert (
            "_PROVIDERS" not in source or "from hexawyn" in source
        ), "_PROVIDERS should be imported from a shared config module"

    def test_format_size_in_formatting(self) -> None:
        source = Path("src/hexawyn/cli/presentation/formatting.py").read_text()
        assert (
            "def _format_size" in source or "def format_size" in source
        ), "format_size should live in presentation/formatting.py"

    def test_providers_in_shared_module(self) -> None:
        provider_file = Path("src/hexawyn/infrastructure/config/llm_providers.py")
        assert (
            provider_file.exists()
        ), "LLM providers should be in infrastructure/config/llm_providers.py"
