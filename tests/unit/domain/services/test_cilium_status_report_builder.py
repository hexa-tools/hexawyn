from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumAgentHealth,
    CiliumStatusResult,
)
from hexawyn.domain.services.cilium.status_report_builder import (
    build_status_result,
    crds_only_result,
    not_installed_result,
)


def _ready_agent(node: str, restart: int = 0) -> CiliumAgentHealth:
    return CiliumAgentHealth(
        node=node,
        pod_name=f"cilium-{node}",
        namespace="kube-system",
        ready=True,
        phase="Running",
        restart_count=restart,
        message=None,
    )


def _down_agent(node: str) -> CiliumAgentHealth:
    return CiliumAgentHealth(
        node=node,
        pod_name=f"cilium-{node}",
        namespace="kube-system",
        ready=False,
        phase="Running",
        restart_count=0,
        message="agent not ready",
    )


class TestBuildStatusResult:
    def test_healthy_when_all_ready(self) -> None:
        result = build_status_result([_ready_agent("node-1"), _ready_agent("node-2")])
        assert result.status == "healthy"
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.total_agents == 2  # noqa: PLR2004
        assert result.degraded_summary is None
        assert result.controller_errors == 0
        assert result.connectivity == "ok"

    def test_healthy_exact_result(self) -> None:
        nodes = [_ready_agent("node-1"), _ready_agent("node-2")]

        result = build_status_result(nodes, note="seen")

        assert result == CiliumStatusResult(
            installed=True,
            status="healthy",
            ready_agents=2,  # noqa: PLR2004
            total_agents=2,  # noqa: PLR2004
            degraded_summary=None,
            controller_errors=0,
            connectivity="ok",
            nodes=nodes,
            note="seen",
        )

    def test_degraded_when_some_down(self) -> None:
        result = build_status_result([_ready_agent("node-1"), _down_agent("node-2")])
        assert result.status == "degraded"
        assert result.ready_agents == 1  # noqa: PLR2004
        assert result.total_agents == 2  # noqa: PLR2004
        assert result.degraded_summary == "1/2 agents ready"
        assert result.controller_errors == 1  # noqa: PLR2004
        assert result.connectivity == "degraded"

    def test_degraded_exact_result(self) -> None:
        nodes = [_ready_agent("node-1"), _down_agent("node-2")]

        result = build_status_result(nodes)

        assert result == CiliumStatusResult(
            installed=True,
            status="degraded",
            ready_agents=1,  # noqa: PLR2004
            total_agents=2,  # noqa: PLR2004
            degraded_summary="1/2 agents ready",
            controller_errors=1,  # noqa: PLR2004
            connectivity="degraded",
            nodes=nodes,
            note=None,
        )

    def test_unknown_when_no_nodes(self) -> None:
        result = build_status_result([])
        assert result.status == "unknown"
        assert result.total_agents == 0
        assert result.connectivity is None
        assert result.degraded_summary is None

    def test_unknown_exact_result(self) -> None:
        result = build_status_result([], note="none seen")

        assert result == CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=[],
            note="none seen",
        )

    def test_controller_errors_counts_restarted_agents(self) -> None:
        result = build_status_result([_ready_agent("node-1", restart=3)])  # noqa: PLR2004
        assert result.status == "healthy"
        assert result.controller_errors == 1  # noqa: PLR2004

    def test_restart_count_of_one_still_counts_as_error(self) -> None:
        result = build_status_result([_ready_agent("node-1", restart=1)])

        assert result.controller_errors == 1  # noqa: PLR2004

    def test_note_is_forwarded(self) -> None:
        result = build_status_result([_ready_agent("node-1")], note="observed")
        assert result.note == "observed"


class TestNotInstalledResult:
    def test_returns_not_installed_marker(self) -> None:
        result = not_installed_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.nodes == []
        assert result.ready_agents == 0
        assert result.note is not None

    def test_exact_dataclass(self) -> None:
        result = not_installed_result()

        assert result == CiliumStatusResult(
            installed=False,
            status="not_installed",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=[],
            note="Cilium is not installed in this cluster",
        )


class TestCrdsOnlyResult:
    def test_returns_unknown_with_note(self) -> None:
        result = crds_only_result(note="CRDs present, no DaemonSet")
        assert result.installed is True
        assert result.status == "unknown"
        assert result.nodes == []
        assert result.note == "CRDs present, no DaemonSet"

    def test_exact_dataclass(self) -> None:
        result = crds_only_result()

        assert result == CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=[],
            note=None,
        )
