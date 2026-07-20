class TestScheduleRegistry:
    def test_build_registry_returns_callables(self) -> None:
        from hexawyn.infrastructure.config.schedule_registry import build_registry

        registry = build_registry()
        assert "certs_list" in registry
        assert "global_health_check" in registry
        assert callable(registry["certs_list"])
        assert callable(registry["global_health_check"])

    def test_certs_list_wrapper_returns_dict(self) -> None:
        from hexawyn.infrastructure.config.schedule_registry import (
            _certs_list,
            _global_health,
        )

        result = _certs_list({})
        assert isinstance(result, dict)

        result = _global_health({})
        assert isinstance(result, dict)
