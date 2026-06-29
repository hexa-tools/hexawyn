from abc import ABC

import pytest
from hexawyn.application.ports.driven.k8s_port import K8sPort, NamespaceInfo


class TestNamespaceInfo:
    def test_creates_namespace_info_with_all_fields(self) -> None:
        ns = NamespaceInfo(name="default", status="Active", age="30d")
        assert ns["name"] == "default"
        assert ns["status"] == "Active"
        assert ns["age"] == "30d"

    def test_field_keys_are_exact(self) -> None:
        ns = NamespaceInfo(name="ns", status="Active", age="1h")
        assert set(ns.keys()) == {"name", "status", "age"}


class TestK8sPort:
    def test_is_abstract(self):
        assert issubclass(K8sPort, ABC)

    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            K8sPort()

    def test_list_namespaces_is_abstract(self) -> None:
        assert getattr(K8sPort.list_namespaces, "__isabstractmethod__", False)
