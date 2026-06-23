import pytest


class TestOpenshiftPortABC:
    def test_openshift_port_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.openshift_port import OpenshiftPort

        with pytest.raises(TypeError):
            OpenshiftPort()  # type: ignore[abstract]

    def test_concrete_implementation_works(self) -> None:
        from hexawyn.application.ports.driven.openshift_port import OpenshiftPort

        class FakeOpenshift(OpenshiftPort):
            def list_projects(self) -> list[dict[str, str]]:
                return [{"name": "prod"}]

            def list_routes(self) -> list[dict[str, str | bool]]:
                return [{"name": "api", "tls": True}]

            def list_pipeline_runs(self) -> list[dict[str, str]]:
                return [{"name": "build", "status": "Succeeded"}]

        adapter = FakeOpenshift()
        assert len(adapter.list_projects()) == 1
        assert adapter.list_routes()[0]["tls"] is True
