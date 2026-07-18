from pathlib import Path


class TestStackViewRefactored:
    def test_no_provider_imports_at_module_level(self) -> None:
        source = Path("src/hexawyn/cli/presentation/stack_view.py").read_text()
        lines = source.split("\n")
        adapter_imports = [
            line.strip()
            for line in lines[:15]
            if "import" in line
            and line.strip().startswith("from")
            and (
                "aws_eks_provider" in line
                or "azure_aks_provider" in line
                or "gcp_gke_provider" in line
            )
        ]
        assert (
            not adapter_imports
        ), f"Provider imports should be deferred inside functions: {adapter_imports}"
