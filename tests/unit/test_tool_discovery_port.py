from abc import ABC


class TestToolDiscoveryPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.tool_discovery_port import ToolDiscoveryPort

        assert issubclass(ToolDiscoveryPort, ABC)

    def test_declares_discover_method(self) -> None:
        from hexawyn.application.ports.driven.tool_discovery_port import ToolDiscoveryPort

        assert "discover" in ToolDiscoveryPort.__abstractmethods__
