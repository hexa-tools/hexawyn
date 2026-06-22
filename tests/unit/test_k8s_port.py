from abc import ABC

import pytest

from hexawyn.application.ports.driven.k8s_port import K8sPort


class TestK8sPort:
    def test_is_abstract(self):
        assert issubclass(K8sPort, ABC)

    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            K8sPort()
