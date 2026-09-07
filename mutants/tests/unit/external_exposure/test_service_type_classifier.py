"""Unit tests for is_externally_exposed_type — the ticket's explicitly-named
"service type classification" domain logic."""

from __future__ import annotations


class TestIsExternallyExposedType:
    def test_load_balancer_is_externally_exposed(self) -> None:
        from hexawyn.domain.services.external_exposure.service_type_classifier import (
            is_externally_exposed_type,
        )

        assert is_externally_exposed_type("LoadBalancer") is True

    def test_node_port_is_externally_exposed(self) -> None:
        from hexawyn.domain.services.external_exposure.service_type_classifier import (
            is_externally_exposed_type,
        )

        assert is_externally_exposed_type("NodePort") is True

    def test_cluster_ip_is_not_externally_exposed(self) -> None:
        from hexawyn.domain.services.external_exposure.service_type_classifier import (
            is_externally_exposed_type,
        )

        assert is_externally_exposed_type("ClusterIP") is False

    def test_external_name_is_not_externally_exposed(self) -> None:
        from hexawyn.domain.services.external_exposure.service_type_classifier import (
            is_externally_exposed_type,
        )

        assert is_externally_exposed_type("ExternalName") is False
