"""Unit tests for KubernetesExternalExposureAdapter — mocks the K8s API
client to exercise Service->ServiceRaw mapping and error translation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest


def _mock_service_item(
    name: str = "test-svc",
    namespace: str = "default",
    service_type: str = "LoadBalancer",
    ports: list[int] | None = None,
    node_port: int | None = None,
    external_ip: str | None = None,
    external_hostname: str | None = None,
    source_ranges: list[str] | None = None,
    annotations: dict[str, str] | None = None,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.annotations = annotations
    item.spec.type = service_type
    item.spec.load_balancer_source_ranges = source_ranges

    port_objs = []
    if ports:
        for i, port_num in enumerate(ports):
            p = MagicMock()
            p.port = port_num
            p.node_port = node_port if i == 0 else None
            port_objs.append(p)
    item.spec.ports = port_objs or None

    status = MagicMock()
    if external_ip or external_hostname:
        ingress = MagicMock()
        ingress.ip = external_ip
        ingress.hostname = external_hostname
        status.load_balancer.ingress = [ingress]
    else:
        status.load_balancer.ingress = None
    item.status = status

    return item


class TestKubernetesExternalExposureAdapter:
    def test_list_services_maps_loadbalancer_with_external_ip(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        mock_item = _mock_service_item(
            name="api-gateway",
            namespace="production",
            service_type="LoadBalancer",
            ports=[443],
            external_ip="203.0.113.1",
            annotations={"service.beta.kubernetes.io/aws-load-balancer-internal": "true"},
        )
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = [mock_item]

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert len(result) == 1
        svc = result[0]
        assert svc["name"] == "api-gateway"
        assert svc["namespace"] == "production"
        assert svc["service_type"] == "LoadBalancer"
        assert svc["ports"] == [443]
        assert svc["external_ip"] == "203.0.113.1"
        assert svc["external_hostname"] is None
        assert svc["node_port"] is None
        assert svc["annotations"] == {
            "service.beta.kubernetes.io/aws-load-balancer-internal": "true"
        }

    def test_list_services_maps_nodeport(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        mock_item = _mock_service_item(
            name="redis-cache",
            namespace="staging",
            service_type="NodePort",
            ports=[6379],
            node_port=31234,
        )

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = [mock_item]

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert len(result) == 1
        svc = result[0]
        assert svc["name"] == "redis-cache"
        assert svc["service_type"] == "NodePort"
        assert svc["node_port"] == 31234
        assert svc["external_ip"] is None

    def test_list_services_detects_source_ranges(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        mock_item = _mock_service_item(
            name="restricted-svc",
            namespace="production",
            service_type="LoadBalancer",
            ports=[5432],
            external_ip="203.0.113.5",
            source_ranges=["10.0.0.0/8"],
        )

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = [mock_item]

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert result[0]["has_source_ranges"] is True

    def test_list_services_maps_multiple_services(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        items = [
            _mock_service_item(name=f"svc-{i}", service_type="LoadBalancer", ports=[80 + i])
            for i in range(3)
        ]

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = items

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert len(result) == 3
        assert {s["name"] for s in result} == {"svc-0", "svc-1", "svc-2"}

    def test_list_services_returns_empty_list_when_no_services(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = []

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert result == []

    def test_list_services_with_external_hostname(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        mock_item = _mock_service_item(
            name="hostname-svc",
            namespace="production",
            service_type="LoadBalancer",
            ports=[443],
            external_hostname="abc123.elb.amazonaws.com",
        )

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = [mock_item]

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert result[0]["external_hostname"] == "abc123.elb.amazonaws.com"

    def test_list_services_pending_loadbalancer_has_no_ip(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        mock_item = _mock_service_item(
            name="pending-svc",
            namespace="production",
            service_type="LoadBalancer",
            ports=[5432],
            external_ip=None,
            external_hostname=None,
        )

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = [mock_item]

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert result[0]["external_ip"] is None
        assert result[0]["external_hostname"] is None

    def test_list_services_defaults_service_type_to_cluster_ip(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )

        mock_item = _mock_service_item(name="default-type-svc", service_type="ClusterIP")
        mock_item.spec.type = None

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value.items = [mock_item]

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()
            result = adapter.list_external_services()

        assert result[0]["service_type"] == "ClusterIP"

    def test_403_error_translates_to_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )
        from hexawyn.domain.errors import InsufficientPermissionsError

        core_api = MagicMock()
        forbidden = Exception("Forbidden")
        forbidden.status = 403  # type: ignore[attr-defined]
        core_api.list_service_for_all_namespaces.side_effect = forbidden

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_external_services()

    def test_connection_error_translates_to_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
            KubernetesExternalExposureAdapter,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.side_effect = Exception("Connection refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesExternalExposureAdapter()

            with pytest.raises(ClusterUnreachableError):
                adapter.list_external_services()
