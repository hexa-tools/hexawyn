import pytest


class TestExtendedClusterPort:
    def test_extended_cluster_port_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.extended_cluster_port import ExtendedClusterPort

        with pytest.raises(TypeError):
            ExtendedClusterPort()  # type: ignore[abstract]

    def test_concrete_implementation_works(self) -> None:
        from hexawyn.application.ports.driven.extended_cluster_port import ExtendedClusterPort

        class FakeExtendedCluster(ExtendedClusterPort):
            def list_projects(self) -> list[dict[str, str]]:
                return [{"name": "prod"}]

            def list_routes(self) -> list[dict[str, str | bool]]:
                return [{"name": "api", "tls": True}]

            def list_pipeline_runs(self) -> list[dict[str, str]]:
                return [{"name": "build", "status": "Succeeded"}]

        adapter = FakeExtendedCluster()
        assert len(adapter.list_projects()) == 1
        assert adapter.list_routes()[0]["tls"] is True
