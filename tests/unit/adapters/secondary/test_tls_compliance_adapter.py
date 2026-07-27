from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.tls_compliance_adapter import TLSComplianceAdapter
from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort

_CFG = "kubernetes.config.load_kube_config"
_API = "kubernetes.client.CoreV1Api"


class TestTLSComplianceAdapter:
    def test_implements_port(self) -> None:
        adapter = TLSComplianceAdapter()
        assert isinstance(adapter, TLSCompliancePort)

    def test_scan_services_with_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()

            secret = MagicMock()
            sec_meta = MagicMock()
            sec_meta.name = "app-tls"
            sec_meta.namespace = "default"
            secret.metadata = sec_meta
            secret.type = "kubernetes.io/tls"
            mock_v1.list_secret_for_all_namespaces.return_value = MagicMock(items=[secret])

            svc = MagicMock()
            svc_meta = MagicMock()
            svc_meta.name = "app-tls"
            svc_meta.namespace = "default"
            svc.metadata = svc_meta
            svc.spec = MagicMock()
            svc.spec.selector = {"app": "myapp"}
            svc.spec.ports = [MagicMock(name="https", port=443)]  # type: ignore[assignment]
            mock_v1.list_service_for_all_namespaces.return_value = MagicMock(items=[svc])
            mock_api.return_value = mock_v1

            adapter = TLSComplianceAdapter()
            result = adapter.scan_services()

            assert len(result) >= 1
            assert result[0]["name"] == "app-tls"

    def test_scan_services_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):  # noqa: E501
            adapter = TLSComplianceAdapter()
            result = adapter.scan_services()
            assert result == []

    def test_scan_services_no_tls_secrets(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_secret_for_all_namespaces.return_value = MagicMock(items=[])
            mock_v1.list_service_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            adapter = TLSComplianceAdapter()
            result = adapter.scan_services()
            assert result == []

    def test_scan_services_missing_metadata(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            secret_no_meta = MagicMock()
            secret_no_meta.metadata = None
            mock_v1.list_secret_for_all_namespaces.return_value = MagicMock(items=[secret_no_meta])
            mock_v1.list_service_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            adapter = TLSComplianceAdapter()
            result = adapter.scan_services()
            assert result == []
