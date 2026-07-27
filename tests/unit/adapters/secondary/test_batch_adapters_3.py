from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
    _cpu_to_cores,
)
from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
    _match_labels,
    _matches_selector,
)
from hexawyn.adapters.secondary.openshift.openshift_logs_adapter import (
    OpenShiftLogsAdapter,
)


class TestMatchLabels:
    def test_with_labels(self) -> None:
        dep = Mock()
        dep.spec.selector.match_labels = {"app": "web"}
        assert _match_labels(dep) == {"app": "web"}

    def test_no_selector(self) -> None:
        dep = Mock()
        dep.spec.selector = None
        assert _match_labels(dep) == {}


class TestMatchesSelector:
    def test_all_match(self) -> None:
        assert _matches_selector({"app": "web", "env": "prod"}, {"app": "web"}) is True

    def test_partial_fail(self) -> None:
        assert _matches_selector({"app": "web"}, {"app": "web", "env": "prod"}) is False

    def test_empty_selector(self) -> None:
        assert _matches_selector({"app": "web"}, {}) is True


class TestCpuToCores:
    def test_millicores(self) -> None:
        assert _cpu_to_cores("500m") == 0.5  # noqa: PLR2004

    def test_nanocores(self) -> None:
        assert _cpu_to_cores("500000000n") == 0.5  # noqa: PLR2004

    def test_microcores(self) -> None:
        assert _cpu_to_cores("500000u") == 0.5  # noqa: PLR2004

    def test_plain_cores(self) -> None:
        assert _cpu_to_cores("2") == 2.0  # noqa: PLR2004

    def test_zero(self) -> None:
        assert _cpu_to_cores("0") == 0.0


class TestOpenShiftLogsAdapter:
    def test_implements_port(self) -> None:
        from hexawyn.application.ports.driven.log_search_port import LogSearchPort

        assert isinstance(OpenShiftLogsAdapter(), LogSearchPort)

    def test_list_pipelines_delegates(self) -> None:
        delegate = Mock()
        delegate.fetch_pod_container_logs.return_value = []
        adapter = OpenShiftLogsAdapter(delegate=delegate)
        assert adapter.fetch_pod_container_logs("p", "ns", 60) == []
