from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.detect_privileged_pods.command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.security.detect_privileged_pods.detect_privileged_pods_use_case import (  # noqa: E501
    DetectPrivilegedPodsUseCase,
)
from hexawyn.application.use_case.security.detect_privileged_pods.response import (  # noqa: E501
    DetectPrivilegedPodsResponse,
)


def _secure_pod(name: str = "secure-nginx", namespace: str = "default") -> dict[str, object]:
    return {
        "pod_name": name,
        "namespace": namespace,
        "owner_kind": "Deployment",
        "pod_run_as_non_root": True,
        "host_pid": False,
        "host_network": False,
        "host_ipc": False,
        "containers": [
            {
                "container_name": "nginx",
                "container_kind": "container",
                "privileged": False,
                "allow_privilege_escalation": False,
                "run_as_non_root": True,
                "added_capabilities": [],
            }
        ],
    }


class TestDetectPrivilegedPodsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = []
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = DetectPrivilegedPodsUseCase(port=port)
        result = use_case.execute(DetectPrivilegedPodsCommand())

        assert isinstance(result, DetectPrivilegedPodsResponse)
        assert result.total_pods_checked == 0

    def test_execute_detects_privileged_pod(self) -> None:
        privileged = {
            "pod_name": "priv-pod",
            "namespace": "default",
            "owner_kind": "Pod",
            "pod_run_as_non_root": False,
            "host_pid": True,
            "host_network": False,
            "host_ipc": False,
            "containers": [
                {
                    "container_name": "app",
                    "container_kind": "container",
                    "privileged": True,
                    "allow_privilege_escalation": True,
                    "run_as_non_root": False,
                    "added_capabilities": ["SYS_ADMIN"],
                }
            ],
        }
        port = MagicMock()
        port.list_pod_security_specs.return_value = [privileged]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = DetectPrivilegedPodsUseCase(port=port)
        result = use_case.execute(DetectPrivilegedPodsCommand())

        assert result.total_pods_checked == 1
        assert result.compliant_pod_count == 0

    def test_execute_secure_pod_counted_compliant(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [_secure_pod()]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = DetectPrivilegedPodsUseCase(port=port)
        result = use_case.execute(DetectPrivilegedPodsCommand())

        assert result.compliant_pod_count == 1

    def test_execute_filters_by_namespaces(self) -> None:
        pod = _secure_pod(namespace="production")
        port = MagicMock()
        port.list_pod_security_specs.return_value = [pod]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = DetectPrivilegedPodsUseCase(port=port)
        result = use_case.execute(DetectPrivilegedPodsCommand(namespaces=["staging"]))

        assert result.total_pods_checked == 1
        assert result.compliant_pod_count == 0

    def test_execute_all_privileged_no_compliant(self) -> None:
        priv = {
            "pod_name": "priv",
            "namespace": "default",
            "owner_kind": "Pod",
            "pod_run_as_non_root": False,
            "host_pid": True,
            "host_network": True,
            "host_ipc": True,
            "containers": [
                {
                    "container_name": "app",
                    "container_kind": "container",
                    "privileged": True,
                    "allow_privilege_escalation": True,
                    "run_as_non_root": False,
                    "added_capabilities": ["SYS_ADMIN"],
                }
            ],
        }
        port = MagicMock()
        port.list_pod_security_specs.return_value = [priv]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = DetectPrivilegedPodsUseCase(port=port)
        result = use_case.execute(DetectPrivilegedPodsCommand())

        assert result.compliant_pod_count == 0
