from __future__ import annotations

import os

from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomSimulationPort,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort
from hexawyn.application.ports.driven.ingress_port import IngressPort
from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driven.kubernetes_topology_port import (
    KubernetesTopologyPort,
)
from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
from hexawyn.application.ports.driven.pod_metrics_port import PodMetricsPort
from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig
from hexawyn.infrastructure.memory.duckdb_client import get_connection
from hexawyn.mcp.providers.detector import (
    _current_cluster_context,
    _is_aws_eks_context,
    _is_datadog_enabled,
    context_name,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_k8s_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_k8s_adapter__mutmut)
def build_k8s_adapter() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_k8s_adapter__mutmut_orig() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_k8s_adapter__mutmut_1() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_k8s_adapter__mutmut_2() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_k8s_adapter__mutmut_3() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_k8s_adapter__mutmut_4() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_k8s_adapter__mutmut_5() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_k8s_adapter__mutmut_6() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_k8s_adapter__mutmut_7() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_k8s_adapter__mutmut_8() -> K8sPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_k8s_adapter__mutmut['_mutmut_orig'] = x_build_k8s_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_1'] = x_build_k8s_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_2'] = x_build_k8s_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_3'] = x_build_k8s_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_4'] = x_build_k8s_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_5'] = x_build_k8s_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_6'] = x_build_k8s_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_7'] = x_build_k8s_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_k8s_adapter__mutmut['x_build_k8s_adapter__mutmut_8'] = x_build_k8s_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_ingress_adapter__mutmut)
def build_ingress_adapter() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_ingress_adapter__mutmut_orig() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_ingress_adapter__mutmut_1() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_ingress_adapter__mutmut_2() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_ingress_adapter__mutmut_3() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_ingress_adapter__mutmut_4() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_ingress_adapter__mutmut_5() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_ingress_adapter__mutmut_6() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_ingress_adapter__mutmut_7() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_ingress_adapter__mutmut_8() -> IngressPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_ingress_adapter__mutmut['_mutmut_orig'] = x_build_ingress_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_1'] = x_build_ingress_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_2'] = x_build_ingress_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_3'] = x_build_ingress_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_4'] = x_build_ingress_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_5'] = x_build_ingress_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_6'] = x_build_ingress_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_7'] = x_build_ingress_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_ingress_adapter__mutmut['x_build_ingress_adapter__mutmut_8'] = x_build_ingress_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_tekton_adapter__mutmut)
def build_tekton_adapter() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_orig() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_1() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_2() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name == "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_3() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "XXunknownXX" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_4() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "UNKNOWN" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_5() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = None
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_6() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=None)
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_7() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context and "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_8() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "XXdefaultXX")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_9() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "DEFAULT")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_10() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = None
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_11() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=None)
    return TektonHistoryWriter(tekton_port=vanilla, history_port=history)


def x_build_tekton_adapter__mutmut_12() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=None, history_port=history)


def x_build_tekton_adapter__mutmut_13() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, history_port=None)


def x_build_tekton_adapter__mutmut_14() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(history_port=history)


def x_build_tekton_adapter__mutmut_15() -> TektonPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_history_writer import (
        TektonHistoryWriter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
    from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
        PipelineRunHistoryRepository,
    )

    context = context_name if context_name != "unknown" else None
    vanilla = VanillaAdapter(cluster_name=context or "default")
    history = PipelineRunHistoryRepository(conn=get_connection())
    return TektonHistoryWriter(tekton_port=vanilla, )

mutants_x_build_tekton_adapter__mutmut['_mutmut_orig'] = x_build_tekton_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_1'] = x_build_tekton_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_2'] = x_build_tekton_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_3'] = x_build_tekton_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_4'] = x_build_tekton_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_5'] = x_build_tekton_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_6'] = x_build_tekton_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_7'] = x_build_tekton_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_8'] = x_build_tekton_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_9'] = x_build_tekton_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_10'] = x_build_tekton_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_11'] = x_build_tekton_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_12'] = x_build_tekton_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_13'] = x_build_tekton_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_14'] = x_build_tekton_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_tekton_adapter__mutmut['x_build_tekton_adapter__mutmut_15'] = x_build_tekton_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_rightsizing_adapter__mutmut)
def build_rightsizing_adapter() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_rightsizing_adapter__mutmut_orig() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_rightsizing_adapter__mutmut_1() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_rightsizing_adapter__mutmut_2() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_rightsizing_adapter__mutmut_3() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_rightsizing_adapter__mutmut_4() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_rightsizing_adapter__mutmut_5() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_rightsizing_adapter__mutmut_6() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_rightsizing_adapter__mutmut_7() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_rightsizing_adapter__mutmut_8() -> RightsizingPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_rightsizing_adapter__mutmut['_mutmut_orig'] = x_build_rightsizing_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_1'] = x_build_rightsizing_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_2'] = x_build_rightsizing_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_3'] = x_build_rightsizing_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_4'] = x_build_rightsizing_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_5'] = x_build_rightsizing_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_6'] = x_build_rightsizing_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_7'] = x_build_rightsizing_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_rightsizing_adapter__mutmut['x_build_rightsizing_adapter__mutmut_8'] = x_build_rightsizing_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_what_if_simulation_adapter__mutmut)
def build_what_if_simulation_adapter() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_what_if_simulation_adapter__mutmut_orig() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_what_if_simulation_adapter__mutmut_1() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_what_if_simulation_adapter__mutmut_2() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_what_if_simulation_adapter__mutmut_3() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_what_if_simulation_adapter__mutmut_4() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_what_if_simulation_adapter__mutmut_5() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_what_if_simulation_adapter__mutmut_6() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_what_if_simulation_adapter__mutmut_7() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_what_if_simulation_adapter__mutmut_8() -> WhatIfSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_what_if_simulation_adapter__mutmut['_mutmut_orig'] = x_build_what_if_simulation_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_1'] = x_build_what_if_simulation_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_2'] = x_build_what_if_simulation_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_3'] = x_build_what_if_simulation_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_4'] = x_build_what_if_simulation_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_5'] = x_build_what_if_simulation_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_6'] = x_build_what_if_simulation_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_7'] = x_build_what_if_simulation_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_what_if_simulation_adapter__mutmut['x_build_what_if_simulation_adapter__mutmut_8'] = x_build_what_if_simulation_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_waste_adapter__mutmut)
def build_waste_adapter() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_orig() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_1() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_2() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_3() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_4() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_5() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = None
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_6() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get(None, "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_7() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", None)
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_8() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_9() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", )
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_10() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("XXPROMETHEUS_URLXX", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_11() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("prometheus_url", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_12() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "XXXX")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_13() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=None, prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_14() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=None)


def x_build_waste_adapter__mutmut_15() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_16() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", )


def x_build_waste_adapter__mutmut_17() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context and "default", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_18() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "XXdefaultXX", prometheus_url=prometheus_url)


def x_build_waste_adapter__mutmut_19() -> NamespaceWasteAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "DEFAULT", prometheus_url=prometheus_url)

mutants_x_build_waste_adapter__mutmut['_mutmut_orig'] = x_build_waste_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_1'] = x_build_waste_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_2'] = x_build_waste_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_3'] = x_build_waste_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_4'] = x_build_waste_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_5'] = x_build_waste_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_6'] = x_build_waste_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_7'] = x_build_waste_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_8'] = x_build_waste_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_9'] = x_build_waste_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_10'] = x_build_waste_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_11'] = x_build_waste_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_12'] = x_build_waste_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_13'] = x_build_waste_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_14'] = x_build_waste_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_15'] = x_build_waste_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_16'] = x_build_waste_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_17'] = x_build_waste_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_18'] = x_build_waste_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_waste_adapter__mutmut['x_build_waste_adapter__mutmut_19'] = x_build_waste_adapter__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_zombie_detection_adapter__mutmut)
def build_zombie_detection_adapter() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_zombie_detection_adapter__mutmut_orig() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_zombie_detection_adapter__mutmut_1() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_zombie_detection_adapter__mutmut_2() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_zombie_detection_adapter__mutmut_3() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_zombie_detection_adapter__mutmut_4() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_zombie_detection_adapter__mutmut_5() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_zombie_detection_adapter__mutmut_6() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_zombie_detection_adapter__mutmut_7() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_zombie_detection_adapter__mutmut_8() -> ZombieDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_zombie_detection_adapter__mutmut['_mutmut_orig'] = x_build_zombie_detection_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_1'] = x_build_zombie_detection_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_2'] = x_build_zombie_detection_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_3'] = x_build_zombie_detection_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_4'] = x_build_zombie_detection_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_5'] = x_build_zombie_detection_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_6'] = x_build_zombie_detection_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_7'] = x_build_zombie_detection_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_zombie_detection_adapter__mutmut['x_build_zombie_detection_adapter__mutmut_8'] = x_build_zombie_detection_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_fleet_health_adapter__mutmut)
def build_fleet_health_adapter() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_orig() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_1() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = None
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_2() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get(None, "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_3() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", None)
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_4() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_5() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", )
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_6() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("XXPROMETHEUS_URLXX", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_7() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("prometheus_url", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_8() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "XXXX")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def x_build_fleet_health_adapter__mutmut_9() -> FleetHealthPort:
    from hexawyn.infrastructure.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return FleetHealthAdapter(prometheus_url=None)

mutants_x_build_fleet_health_adapter__mutmut['_mutmut_orig'] = x_build_fleet_health_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_1'] = x_build_fleet_health_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_2'] = x_build_fleet_health_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_3'] = x_build_fleet_health_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_4'] = x_build_fleet_health_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_5'] = x_build_fleet_health_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_6'] = x_build_fleet_health_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_7'] = x_build_fleet_health_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_8'] = x_build_fleet_health_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_fleet_health_adapter__mutmut['x_build_fleet_health_adapter__mutmut_9'] = x_build_fleet_health_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_cluster_certificate_health_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cluster_certificate_health_adapter__mutmut)
def build_cluster_certificate_health_adapter() -> ClusterCertificateHealthPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )

    api = load_kubeconfig()
    return KubernetesClusterCertificateAdapter(api=api)


def x_build_cluster_certificate_health_adapter__mutmut_orig() -> ClusterCertificateHealthPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )

    api = load_kubeconfig()
    return KubernetesClusterCertificateAdapter(api=api)


def x_build_cluster_certificate_health_adapter__mutmut_1() -> ClusterCertificateHealthPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )

    api = None
    return KubernetesClusterCertificateAdapter(api=api)


def x_build_cluster_certificate_health_adapter__mutmut_2() -> ClusterCertificateHealthPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )

    api = load_kubeconfig()
    return KubernetesClusterCertificateAdapter(api=None)

mutants_x_build_cluster_certificate_health_adapter__mutmut['_mutmut_orig'] = x_build_cluster_certificate_health_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cluster_certificate_health_adapter__mutmut['x_build_cluster_certificate_health_adapter__mutmut_1'] = x_build_cluster_certificate_health_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cluster_certificate_health_adapter__mutmut['x_build_cluster_certificate_health_adapter__mutmut_2'] = x_build_cluster_certificate_health_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_kubernetes_topology_adapter__mutmut)
def build_kubernetes_topology_adapter() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def x_build_kubernetes_topology_adapter__mutmut_orig() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def x_build_kubernetes_topology_adapter__mutmut_1() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def x_build_kubernetes_topology_adapter__mutmut_2() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name == "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def x_build_kubernetes_topology_adapter__mutmut_3() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "XXunknownXX" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def x_build_kubernetes_topology_adapter__mutmut_4() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "UNKNOWN" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def x_build_kubernetes_topology_adapter__mutmut_5() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=None)


def x_build_kubernetes_topology_adapter__mutmut_6() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context and "default")


def x_build_kubernetes_topology_adapter__mutmut_7() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "XXdefaultXX")


def x_build_kubernetes_topology_adapter__mutmut_8() -> KubernetesTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_kubernetes_topology_adapter__mutmut['_mutmut_orig'] = x_build_kubernetes_topology_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_1'] = x_build_kubernetes_topology_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_2'] = x_build_kubernetes_topology_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_3'] = x_build_kubernetes_topology_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_4'] = x_build_kubernetes_topology_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_5'] = x_build_kubernetes_topology_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_6'] = x_build_kubernetes_topology_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_7'] = x_build_kubernetes_topology_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_kubernetes_topology_adapter__mutmut['x_build_kubernetes_topology_adapter__mutmut_8'] = x_build_kubernetes_topology_adapter__mutmut_8 # type: ignore # mutmut generated


def build_istio_topology_adapter() -> IstioTopologyPort:
    from hexawyn.infrastructure.adapters.secondary.istio_topology_adapter import (
        IstioTopologyAdapter,
    )

    return IstioTopologyAdapter()
mutants_x_build_topology_snapshot_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_topology_snapshot_adapter__mutmut)
def build_topology_snapshot_adapter() -> TopologySnapshotPort:
    from hexawyn.infrastructure.memory.topology_snapshot_repository import (
        TopologySnapshotRepository,
    )

    return TopologySnapshotRepository(conn=get_connection())


def x_build_topology_snapshot_adapter__mutmut_orig() -> TopologySnapshotPort:
    from hexawyn.infrastructure.memory.topology_snapshot_repository import (
        TopologySnapshotRepository,
    )

    return TopologySnapshotRepository(conn=get_connection())


def x_build_topology_snapshot_adapter__mutmut_1() -> TopologySnapshotPort:
    from hexawyn.infrastructure.memory.topology_snapshot_repository import (
        TopologySnapshotRepository,
    )

    return TopologySnapshotRepository(conn=None)

mutants_x_build_topology_snapshot_adapter__mutmut['_mutmut_orig'] = x_build_topology_snapshot_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_topology_snapshot_adapter__mutmut['x_build_topology_snapshot_adapter__mutmut_1'] = x_build_topology_snapshot_adapter__mutmut_1 # type: ignore # mutmut generated


def build_rollouts_adapter() -> RolloutsPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.argo_rollouts_detector import (
        ArgoRolloutsDetector,
    )

    return ArgoRolloutsDetector()


def build_policy_adapter() -> PolicyPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.policy_detector import PolicyDetector

    return PolicyDetector()
mutants_x_build_cert_manager_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cert_manager_adapter__mutmut)
def build_cert_manager_adapter() -> CertManagerPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(VanillaAdapter(cluster_name="default"))


def x_build_cert_manager_adapter__mutmut_orig() -> CertManagerPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(VanillaAdapter(cluster_name="default"))


def x_build_cert_manager_adapter__mutmut_1() -> CertManagerPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(None)


def x_build_cert_manager_adapter__mutmut_2() -> CertManagerPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(VanillaAdapter(cluster_name=None))


def x_build_cert_manager_adapter__mutmut_3() -> CertManagerPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(VanillaAdapter(cluster_name="XXdefaultXX"))


def x_build_cert_manager_adapter__mutmut_4() -> CertManagerPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cert_manager_adapter import (
        CertManagerAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CertManagerAdapter(VanillaAdapter(cluster_name="DEFAULT"))

mutants_x_build_cert_manager_adapter__mutmut['_mutmut_orig'] = x_build_cert_manager_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cert_manager_adapter__mutmut['x_build_cert_manager_adapter__mutmut_1'] = x_build_cert_manager_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cert_manager_adapter__mutmut['x_build_cert_manager_adapter__mutmut_2'] = x_build_cert_manager_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cert_manager_adapter__mutmut['x_build_cert_manager_adapter__mutmut_3'] = x_build_cert_manager_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cert_manager_adapter__mutmut['x_build_cert_manager_adapter__mutmut_4'] = x_build_cert_manager_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_keda_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_keda_adapter__mutmut)
def build_keda_adapter() -> KedaPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(VanillaAdapter(cluster_name="default"))


def x_build_keda_adapter__mutmut_orig() -> KedaPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(VanillaAdapter(cluster_name="default"))


def x_build_keda_adapter__mutmut_1() -> KedaPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(None)


def x_build_keda_adapter__mutmut_2() -> KedaPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(VanillaAdapter(cluster_name=None))


def x_build_keda_adapter__mutmut_3() -> KedaPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(VanillaAdapter(cluster_name="XXdefaultXX"))


def x_build_keda_adapter__mutmut_4() -> KedaPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.keda_adapter import KedaAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return KedaAdapter(VanillaAdapter(cluster_name="DEFAULT"))

mutants_x_build_keda_adapter__mutmut['_mutmut_orig'] = x_build_keda_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_keda_adapter__mutmut['x_build_keda_adapter__mutmut_1'] = x_build_keda_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_keda_adapter__mutmut['x_build_keda_adapter__mutmut_2'] = x_build_keda_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_keda_adapter__mutmut['x_build_keda_adapter__mutmut_3'] = x_build_keda_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_keda_adapter__mutmut['x_build_keda_adapter__mutmut_4'] = x_build_keda_adapter__mutmut_4 # type: ignore # mutmut generated


def build_canary_comparison_adapter() -> CanaryComparisonPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_canary_comparison_adapter import (
        OTelCanaryComparisonAdapter,
    )

    return OTelCanaryComparisonAdapter()


def build_memory_saturation_adapter() -> MemorySaturationPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_memory_adapter import (
        PrometheusMemoryAdapter,
    )

    return PrometheusMemoryAdapter()


def build_capacity_forecast_adapter() -> CapacityForecastPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (  # noqa: E501
        KubernetesCapacityForecastAdapter,
    )

    return KubernetesCapacityForecastAdapter()


def build_headroom_simulation_adapter() -> HeadroomSimulationPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (  # noqa: E501
        KubernetesHeadroomSimulationAdapter,
    )

    return KubernetesHeadroomSimulationAdapter()
mutants_x_build_spike_provisioning_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_spike_provisioning_adapter__mutmut)
def build_spike_provisioning_adapter() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_orig() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_1() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=None,
        current_cpu_used_cores=0.0,
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_2() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=None,
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_3() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        current_memory_used_gb=None,
    )


def x_build_spike_provisioning_adapter__mutmut_4() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        current_cpu_used_cores=0.0,
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_5() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_6() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        )


def x_build_spike_provisioning_adapter__mutmut_7() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=1.0,
        current_memory_used_gb=0.0,
    )


def x_build_spike_provisioning_adapter__mutmut_8() -> SpikeProvisioningPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        current_memory_used_gb=1.0,
    )

mutants_x_build_spike_provisioning_adapter__mutmut['_mutmut_orig'] = x_build_spike_provisioning_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_1'] = x_build_spike_provisioning_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_2'] = x_build_spike_provisioning_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_3'] = x_build_spike_provisioning_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_4'] = x_build_spike_provisioning_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_5'] = x_build_spike_provisioning_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_6'] = x_build_spike_provisioning_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_7'] = x_build_spike_provisioning_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_spike_provisioning_adapter__mutmut['x_build_spike_provisioning_adapter__mutmut_8'] = x_build_spike_provisioning_adapter__mutmut_8 # type: ignore # mutmut generated


def build_node_analysis_adapter() -> HotNodeAnalysisPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
        KubernetesNodeAnalysisAdapter,
    )

    return KubernetesNodeAnalysisAdapter()
mutants_x_build_cluster_resource_metrics_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cluster_resource_metrics_adapter__mutmut)
def build_cluster_resource_metrics_adapter() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_orig() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_1() -> ClusterResourceMetricsPort:
    context = None
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_2() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(None):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_3() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = None
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_4() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=None, app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_5() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=None, site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_6() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=None
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_7() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_8() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_9() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_10() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["XXkeyXX"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_11() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["KEY"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_12() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["XXapp_keyXX"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_13() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["APP_KEY"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_14() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["XXsiteXX"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_15() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["SITE"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_16() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(None):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_17() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=None, region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_18() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=None
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_19() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_20() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_21() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["XXnameXX"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_22() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["NAME"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_23() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(None).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_cluster_resource_metrics_adapter__mutmut_24() -> ClusterResourceMetricsPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (  # noqa: E501
        PrometheusClusterResourceMetricsAdapter,
    )
    from hexawyn.mcp.server import build_metrics_query_adapter

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=None)

mutants_x_build_cluster_resource_metrics_adapter__mutmut['_mutmut_orig'] = x_build_cluster_resource_metrics_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_1'] = x_build_cluster_resource_metrics_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_2'] = x_build_cluster_resource_metrics_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_3'] = x_build_cluster_resource_metrics_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_4'] = x_build_cluster_resource_metrics_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_5'] = x_build_cluster_resource_metrics_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_6'] = x_build_cluster_resource_metrics_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_7'] = x_build_cluster_resource_metrics_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_8'] = x_build_cluster_resource_metrics_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_9'] = x_build_cluster_resource_metrics_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_10'] = x_build_cluster_resource_metrics_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_11'] = x_build_cluster_resource_metrics_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_12'] = x_build_cluster_resource_metrics_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_13'] = x_build_cluster_resource_metrics_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_14'] = x_build_cluster_resource_metrics_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_15'] = x_build_cluster_resource_metrics_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_16'] = x_build_cluster_resource_metrics_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_17'] = x_build_cluster_resource_metrics_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_18'] = x_build_cluster_resource_metrics_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_19'] = x_build_cluster_resource_metrics_adapter__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_20'] = x_build_cluster_resource_metrics_adapter__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_21'] = x_build_cluster_resource_metrics_adapter__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_22'] = x_build_cluster_resource_metrics_adapter__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_23'] = x_build_cluster_resource_metrics_adapter__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_cluster_resource_metrics_adapter__mutmut['x_build_cluster_resource_metrics_adapter__mutmut_24'] = x_build_cluster_resource_metrics_adapter__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_cluster_diff_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cluster_diff_adapter__mutmut)
def build_cluster_diff_adapter() -> ClusterDiffPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cluster_diff_adapter import (
        ClusterDiffAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.cluster_diff_source import (
        EmptyClusterInventorySource,
    )

    return ClusterDiffAdapter(source=EmptyClusterInventorySource())


def x_build_cluster_diff_adapter__mutmut_orig() -> ClusterDiffPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cluster_diff_adapter import (
        ClusterDiffAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.cluster_diff_source import (
        EmptyClusterInventorySource,
    )

    return ClusterDiffAdapter(source=EmptyClusterInventorySource())


def x_build_cluster_diff_adapter__mutmut_1() -> ClusterDiffPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cluster_diff_adapter import (
        ClusterDiffAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.cluster_diff_source import (
        EmptyClusterInventorySource,
    )

    return ClusterDiffAdapter(source=None)

mutants_x_build_cluster_diff_adapter__mutmut['_mutmut_orig'] = x_build_cluster_diff_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cluster_diff_adapter__mutmut['x_build_cluster_diff_adapter__mutmut_1'] = x_build_cluster_diff_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_pod_metrics_adapter__mutmut)
def build_pod_metrics_adapter() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_pod_metrics_adapter__mutmut_orig() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_pod_metrics_adapter__mutmut_1() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_pod_metrics_adapter__mutmut_2() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_pod_metrics_adapter__mutmut_3() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_pod_metrics_adapter__mutmut_4() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_pod_metrics_adapter__mutmut_5() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_pod_metrics_adapter__mutmut_6() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_pod_metrics_adapter__mutmut_7() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_pod_metrics_adapter__mutmut_8() -> PodMetricsPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_pod_metrics_adapter__mutmut['_mutmut_orig'] = x_build_pod_metrics_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_1'] = x_build_pod_metrics_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_2'] = x_build_pod_metrics_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_3'] = x_build_pod_metrics_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_4'] = x_build_pod_metrics_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_5'] = x_build_pod_metrics_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_6'] = x_build_pod_metrics_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_7'] = x_build_pod_metrics_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_adapter__mutmut['x_build_pod_metrics_adapter__mutmut_8'] = x_build_pod_metrics_adapter__mutmut_8 # type: ignore # mutmut generated
