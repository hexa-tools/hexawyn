from collections.abc import Callable
from typing import Any, Protocol

from textual.app import App
from textual.binding import Binding

from hexawyn.cli.presentation.asides import (
    failed_pod_count,
    pending_pod_count,
    running_pod_count,
    safe_pods,
)
from hexawyn.infrastructure.adapters.secondary.adapter_factory import build_adapters
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
    KubernetesStartupStatus,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ContextService(Protocol):
    def discover(self) -> list[KubernetesClusterContext]:
        """Return available Kubernetes contexts."""

    def switch_context(self, context_name: str) -> KubernetesContextSwitchResult:
        """Switch Hexawyn runtime context."""
mutants_xǁHexawynTUIǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynTUIǁon_mount__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut: MutantDict = {}  # type: ignore


class HexawynTUI(App[None]):
    ALLOW_SELECT = True

    CSS = """
    Header {
        display: none;
    }

    Screen {
        background: #05070d;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "clear_input", "Cancel", show=False),
        Binding("ctrl+q", "quit", "Quit", show=False),
    ]

    @_mutmut_mutated(mutants_xǁHexawynTUIǁ__init____mutmut)
    def __init__(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_orig(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_1(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = True,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_2(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = True,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_3(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "XXaws_eksXX",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_4(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "AWS_EKS",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_5(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = True,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_6(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "XXunknownXX",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_7(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "UNKNOWN",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_8(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = True,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_9(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = None
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_10(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = None
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_11(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = None
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_12(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = None
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_13(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = None
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_14(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = None
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_15(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = None
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_16(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = None
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_17(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = None
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_18(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = None
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_19(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = ""
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_20(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = None
        self.ai_suggestion: str | None = None

    def xǁHexawynTUIǁ__init____mutmut_21(  # noqa: PLR0913
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup
        self.ai_suggestion: str | None = ""

    @_mutmut_mutated(mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut)
    def _generate_ai_suggestion(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_orig(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_1(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = None
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_2(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = None
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_3(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(None)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_4(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = None
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_5(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "XXnameXX": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_6(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "NAME": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_7(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(None),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_8(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get(None, "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_9(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", None)),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_10(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_11(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", )),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_12(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("XXnameXX", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_13(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("NAME", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_14(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "XXXX")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_15(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "XXnamespaceXX": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_16(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "NAMESPACE": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_17(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(None),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_18(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get(None, "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_19(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", None)),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_20(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_21(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", )),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_22(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("XXnamespaceXX", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_23(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("NAMESPACE", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_24(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "XXXX")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_25(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "XXstatusXX": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_26(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "STATUS": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_27(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(None),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_28(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get(None, "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_29(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", None)),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_30(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_31(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", )),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_32(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("XXstatusXX", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_33(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("STATUS", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_34(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "XXXX")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_35(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "XXrestartsXX": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_36(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "RESTARTS": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_37(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(None),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_38(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(None)),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_39(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get(None, 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_40(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", None))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_41(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get(0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_42(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", ))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_43(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("XXrestartsXX", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_44(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("RESTARTS", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_45(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 1))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_46(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = None
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_47(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(None, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_48(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=None)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_49(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_50(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, )
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_51(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = None

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_52(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get(None, "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_53(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", None)

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_54(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_55(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", )

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_56(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[1].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_57(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("XXvalueXX", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_58(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("VALUE", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_59(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "XXXX")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_60(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 or scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_61(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion or scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_62(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_63(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score >= 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_64(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 1 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_65(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_66(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(None):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_67(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = None

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_68(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_69(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = None

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(_refresh)
        except Exception:
            pass

    def xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_70(self) -> None:
        try:
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()
            pods = safe_pods(self.adapter)
            pod_dicts: list[dict[str, object]] = [
                {
                    "name": str(p.get("name", "")),
                    "namespace": str(p.get("namespace", "")),
                    "status": str(p.get("status", "")),
                    "restarts": int(str(p.get("restarts", 0))),
                }
                for p in pods
            ]
            scan = runtime.run_startup_scan(self.cluster_name, pods=pod_dicts)
            if scan.suggestions:
                self.ai_suggestion = scan.suggestions[0].get("value", "")

            if not self.ai_suggestion and scan.health_score > 0 and scan.narrative_summary:
                from hexawyn.application.service.startup_scan_service import is_error_narrative

                if not is_error_narrative(scan.narrative_summary):
                    self.ai_suggestion = scan.narrative_summary

            if not self.ai_suggestion:
                self.ai_suggestion = self._fallback_suggestion()

            if self.ai_suggestion:

                def _refresh() -> None:
                    from hexawyn.cli.screens.session import SessionScreen

                    if isinstance(self.screen, SessionScreen):
                        self.screen._refresh_aside()

                self.call_from_thread(None)
        except Exception:
            pass

    @_mutmut_mutated(mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut)
    def _fallback_suggestion(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_orig(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_1(self) -> str | None:
        try:
            pods = None
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_2(self) -> str | None:
        try:
            pods = safe_pods(None)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_3(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = None
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_4(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = None
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_5(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(None)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_6(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = None
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_7(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(None)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_8(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = None

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_9(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(None)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_10(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total != 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_11(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 1:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_12(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed >= 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_13(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 1:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_14(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending >= 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_15(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 1:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_16(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running != total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_17(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = None
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_18(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending + failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_19(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running + pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_20(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total + running - pending - failed
            if other > 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_21(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other >= 0:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    def xǁHexawynTUIǁ_fallback_suggestion__mutmut_22(self) -> str | None:
        try:
            pods = safe_pods(self.adapter)
            total = len(pods)
            running = running_pod_count(pods)
            pending = pending_pod_count(pods)
            failed = failed_pod_count(pods)

            if total == 0:
                return None
            if failed > 0:
                return f"{failed} pod(s) in failed state — run a health check to investigate"
            if pending > 0:
                return f"{pending} pod(s) pending — check resource quotas or node capacity"
            if running == total:
                return f"All {total} pods healthy — no issues detected"
            other = total - running - pending - failed
            if other > 1:
                return f"{running}/{total} pods running — {other} finished or in transition"
            return None
        except Exception:
            return None

    @_mutmut_mutated(mutants_xǁHexawynTUIǁon_mount__mutmut)
    def on_mount(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_orig(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_1(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(None)
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_2(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(None)
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_3(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(None)
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_4(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(None, thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_5(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=None)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_6(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(thread=True)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_7(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, )
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_8(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=False)
        self.run_worker(self._connect_and_scan, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_9(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(None, thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_10(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=None)

    def xǁHexawynTUIǁon_mount__mutmut_11(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(thread=True)

    def xǁHexawynTUIǁon_mount__mutmut_12(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, )

    def xǁHexawynTUIǁon_mount__mutmut_13(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())
        self.run_worker(self._generate_ai_suggestion, thread=True)
        self.run_worker(self._connect_and_scan, thread=False)

    @_mutmut_mutated(mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut)
    def _connect_and_scan(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_orig(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_1(self) -> None:
        if self.demo_mode and self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_2(self) -> None:
        if self.demo_mode or self.context_service is not None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_3(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = None  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_4(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = None
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_5(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = None
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_6(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = False
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_7(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(None)
            self.call_from_thread(self._refresh_aside_after_connect)
        except Exception:
            pass

    def xǁHexawynTUIǁ_connect_and_scan__mutmut_8(self) -> None:
        if self.demo_mode or self.context_service is None:
            return
        try:
            status = self.context_service.startup_status()  # type: ignore[attr-defined]
            self.startup_status = status
            if status.connected:
                self.run_startup_scan = True
                from hexawyn.application.service.runtime_adapter import get_runtime

                get_runtime().set_adapter(self.adapter)
            self.call_from_thread(None)
        except Exception:
            pass

    @_mutmut_mutated(mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut)
    def _refresh_aside_after_connect(self) -> None:
        try:
            if hasattr(self.screen, "_refresh_aside"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_orig(self) -> None:
        try:
            if hasattr(self.screen, "_refresh_aside"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_1(self) -> None:
        try:
            if hasattr(None, "_refresh_aside"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_2(self) -> None:
        try:
            if hasattr(self.screen, None):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_3(self) -> None:
        try:
            if hasattr("_refresh_aside"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_4(self) -> None:
        try:
            if hasattr(self.screen, ):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_5(self) -> None:
        try:
            if hasattr(self.screen, "XX_refresh_asideXX"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_6(self) -> None:
        try:
            if hasattr(self.screen, "_REFRESH_ASIDE"):
                self.screen._refresh_aside()
        except Exception:
            pass

    def action_clear_input(self) -> None:
        if isinstance(self.screen, WelcomeScreen | SessionScreen):
            self.screen.action_clear_input()

mutants_xǁHexawynTUIǁ__init____mutmut['_mutmut_orig'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_1'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_2'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_3'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_4'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_5'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_6'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_7'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_8'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_9'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_10'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_11'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_12'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_13'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_14'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_15'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_16'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_17'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_18'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_19'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_20'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ__init____mutmut['xǁHexawynTUIǁ__init____mutmut_21'] = HexawynTUI.xǁHexawynTUIǁ__init____mutmut_21 # type: ignore # mutmut generated

mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['_mutmut_orig'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_1'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_2'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_3'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_4'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_5'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_6'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_7'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_8'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_9'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_10'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_11'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_12'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_13'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_14'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_15'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_16'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_17'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_18'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_19'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_20'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_21'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_22'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_23'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_24'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_25'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_26'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_27'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_28'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_29'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_30'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_31'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_32'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_33'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_34'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_35'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_36'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_37'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_38'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_39'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_40'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_41'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_42'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_43'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_44'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_45'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_46'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_47'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_48'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_49'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_50'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_51'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_52'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_53'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_54'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_55'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_56'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_57'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_58'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_59'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_60'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_61'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_62'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_63'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_64'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_65'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_66'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_67'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_67 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_68'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_68 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_69'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_69 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_generate_ai_suggestion__mutmut['xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_70'] = HexawynTUI.xǁHexawynTUIǁ_generate_ai_suggestion__mutmut_70 # type: ignore # mutmut generated

mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['_mutmut_orig'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_1'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_2'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_3'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_4'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_5'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_6'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_7'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_8'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_9'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_10'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_11'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_12'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_13'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_14'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_15'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_16'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_17'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_18'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_19'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_20'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_21'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_fallback_suggestion__mutmut['xǁHexawynTUIǁ_fallback_suggestion__mutmut_22'] = HexawynTUI.xǁHexawynTUIǁ_fallback_suggestion__mutmut_22 # type: ignore # mutmut generated

mutants_xǁHexawynTUIǁon_mount__mutmut['_mutmut_orig'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_1'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_2'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_3'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_4'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_5'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_6'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_7'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_8'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_9'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_10'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_11'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_12'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁon_mount__mutmut['xǁHexawynTUIǁon_mount__mutmut_13'] = HexawynTUI.xǁHexawynTUIǁon_mount__mutmut_13 # type: ignore # mutmut generated

mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['_mutmut_orig'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_1'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_2'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_3'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_4'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_5'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_6'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_7'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_connect_and_scan__mutmut['xǁHexawynTUIǁ_connect_and_scan__mutmut_8'] = HexawynTUI.xǁHexawynTUIǁ_connect_and_scan__mutmut_8 # type: ignore # mutmut generated

mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['_mutmut_orig'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_1'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_2'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_3'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_4'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_5'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut['xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_6'] = HexawynTUI.xǁHexawynTUIǁ_refresh_aside_after_connect__mutmut_6 # type: ignore # mutmut generated


# ── Backwards-compatible re-exports ──────────────────────────────────────────
# Preserved so existing imports from hexawyn.cli.tui continue to work.
# ruff: noqa: F401, E402
from hexawyn.cli.presentation.asides import (
    crashloop_finding_count as _crashloop_finding_count,
)
from hexawyn.cli.presentation.asides import (
    failed_pod_count as _failed_pod_count,
)
from hexawyn.cli.presentation.asides import (
    finding_message as _finding_message,
)
from hexawyn.cli.presentation.asides import (
    issue_name as _issue_name,
)
from hexawyn.cli.presentation.asides import (
    issue_reason as _issue_reason,
)
from hexawyn.cli.presentation.asides import (
    kubectl_current_context as _kubectl_current_context,
)
from hexawyn.cli.presentation.asides import (
    mapping_int as _mapping_int,
)
from hexawyn.cli.presentation.asides import (
    mapping_text as _mapping_text,
)
from hexawyn.cli.presentation.asides import (
    namespace_count as _namespace_count,
)
from hexawyn.cli.presentation.asides import (
    pending_pod_count as _pending_pod_count,
)
from hexawyn.cli.presentation.asides import (
    restarting_finding_count as _restarting_finding_count,
)
from hexawyn.cli.presentation.asides import (
    running_pod_count as _running_pod_count,
)
from hexawyn.cli.presentation.asides import (
    safe_findings as _safe_findings,
)
from hexawyn.cli.presentation.asides import (
    safe_health_score as _safe_health_score,
)
from hexawyn.cli.presentation.asides import (
    safe_metrics as _safe_metrics,
)
from hexawyn.cli.presentation.asides import (
    safe_pods as _safe_pods,
)
from hexawyn.cli.presentation.asides import (
    safe_suggestions as _safe_suggestions,
)
from hexawyn.cli.presentation.constants import (
    _LOGO_BANNER,
    _POD_STATUS_COLORS,
)
from hexawyn.cli.presentation.formatting import (
    app_version as _app_version,
)
from hexawyn.cli.presentation.formatting import (
    compact_project_directory as _compact_project_directory,
)
from hexawyn.cli.presentation.formatting import (
    connection_line as _connection_line,
)
from hexawyn.cli.presentation.formatting import (
    context_line as _context_line,
)
from hexawyn.cli.presentation.formatting import (
    context_list_lines as _context_list_lines,
)
from hexawyn.cli.presentation.formatting import (
    current_context_from as _current_context_from,
)
from hexawyn.cli.presentation.formatting import (
    missing_context_lines as _missing_context_lines,
)
from hexawyn.cli.presentation.formatting import (
    startup_lines as _startup_lines,
)
from hexawyn.cli.presentation.formatting import (
    startup_status_from_switch as _startup_status_from_switch,
)
from hexawyn.cli.screens.context_picker import ContextPickerScreen
from hexawyn.cli.screens.provider_setup import ProviderSetupScreen
from hexawyn.cli.screens.session import SessionScreen
from hexawyn.cli.screens.welcome import WelcomeScreen
