from __future__ import annotations

from typing import TypedDict

from hexawyn.domain.models.dependency_graph import DependencyGraph


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ServiceNodeExport(TypedDict):
    name: str
    namespace: str
    replicas: int
    type: str
    is_spof: bool


class DependencyEdgeExport(TypedDict):
    caller: str
    callee: str


class DependencyGraphExport(TypedDict):
    nodes: list[ServiceNodeExport]
    edges: list[DependencyEdgeExport]
    single_points_of_failure: list[str]
    orphan_nodes: list[str]
    cycles: list[list[str]]
    inference_source: str
    truncated: bool
    namespace_scope: str | None
mutants_x_to_structured_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_structured_dict__mutmut)
def to_structured_dict(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_orig(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_1(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=None,
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_2(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=None,
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_3(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=None,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_4(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=None,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_5(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=None,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_6(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=None,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_7(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=None,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_8(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=None,
    )


def x_to_structured_dict__mutmut_9(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_10(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_11(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_12(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_13(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_14(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_15(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_16(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        )


def x_to_structured_dict__mutmut_17(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=None,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_18(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=None,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_19(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=None,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_20(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=None,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_21(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=None,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_22(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_23(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_24(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_25(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_26(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_27(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=None, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_28(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=None) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_29(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def x_to_structured_dict__mutmut_30(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, ) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )

mutants_x_to_structured_dict__mutmut['_mutmut_orig'] = x_to_structured_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_1'] = x_to_structured_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_2'] = x_to_structured_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_3'] = x_to_structured_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_4'] = x_to_structured_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_5'] = x_to_structured_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_6'] = x_to_structured_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_7'] = x_to_structured_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_8'] = x_to_structured_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_9'] = x_to_structured_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_10'] = x_to_structured_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_11'] = x_to_structured_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_12'] = x_to_structured_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_13'] = x_to_structured_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_14'] = x_to_structured_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_15'] = x_to_structured_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_16'] = x_to_structured_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_17'] = x_to_structured_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_18'] = x_to_structured_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_19'] = x_to_structured_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_20'] = x_to_structured_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_21'] = x_to_structured_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_22'] = x_to_structured_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_23'] = x_to_structured_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_24'] = x_to_structured_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_25'] = x_to_structured_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_26'] = x_to_structured_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_27'] = x_to_structured_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_28'] = x_to_structured_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_29'] = x_to_structured_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x_to_structured_dict__mutmut['x_to_structured_dict__mutmut_30'] = x_to_structured_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_mermaid__mutmut)
def to_mermaid(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_orig(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_1(graph: DependencyGraph) -> str:
    lines = None

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_2(graph: DependencyGraph) -> str:
    lines = ["XXgraph TDXX"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_3(graph: DependencyGraph) -> str:
    lines = ["graph td"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_4(graph: DependencyGraph) -> str:
    lines = ["GRAPH TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_5(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(None)

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_6(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(None)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_7(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(None)

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_8(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(None)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_9(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(None)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_10(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append(None)
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_11(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("XX    classDef spof fill:#f96,stroke:#900,stroke-width:2pxXX")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_12(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classdef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_13(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    CLASSDEF SPOF FILL:#F96,STROKE:#900,STROKE-WIDTH:2PX")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_14(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = None
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_15(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(None)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_16(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = "XX,XX".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_17(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(None) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def x_to_mermaid__mutmut_18(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(None)

    return "\n".join(lines)


def x_to_mermaid__mutmut_19(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(None)


def x_to_mermaid__mutmut_20(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "XX\nXX".join(lines)

mutants_x_to_mermaid__mutmut['_mutmut_orig'] = x_to_mermaid__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_1'] = x_to_mermaid__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_2'] = x_to_mermaid__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_3'] = x_to_mermaid__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_4'] = x_to_mermaid__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_5'] = x_to_mermaid__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_6'] = x_to_mermaid__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_7'] = x_to_mermaid__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_8'] = x_to_mermaid__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_9'] = x_to_mermaid__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_10'] = x_to_mermaid__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_11'] = x_to_mermaid__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_12'] = x_to_mermaid__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_13'] = x_to_mermaid__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_14'] = x_to_mermaid__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_15'] = x_to_mermaid__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_16'] = x_to_mermaid__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_17'] = x_to_mermaid__mutmut_17 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_18'] = x_to_mermaid__mutmut_18 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_19'] = x_to_mermaid__mutmut_19 # type: ignore # mutmut generated
mutants_x_to_mermaid__mutmut['x_to_mermaid__mutmut_20'] = x_to_mermaid__mutmut_20 # type: ignore # mutmut generated
mutants_x__safe_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__safe_id__mutmut)
def _safe_id(name: str) -> str:
    return name.replace("-", "_")


def x__safe_id__mutmut_orig(name: str) -> str:
    return name.replace("-", "_")


def x__safe_id__mutmut_1(name: str) -> str:
    return name.replace(None, "_")


def x__safe_id__mutmut_2(name: str) -> str:
    return name.replace("-", None)


def x__safe_id__mutmut_3(name: str) -> str:
    return name.replace("_")


def x__safe_id__mutmut_4(name: str) -> str:
    return name.replace("-", )


def x__safe_id__mutmut_5(name: str) -> str:
    return name.replace("XX-XX", "_")


def x__safe_id__mutmut_6(name: str) -> str:
    return name.replace("-", "XX_XX")

mutants_x__safe_id__mutmut['_mutmut_orig'] = x__safe_id__mutmut_orig # type: ignore # mutmut generated
mutants_x__safe_id__mutmut['x__safe_id__mutmut_1'] = x__safe_id__mutmut_1 # type: ignore # mutmut generated
mutants_x__safe_id__mutmut['x__safe_id__mutmut_2'] = x__safe_id__mutmut_2 # type: ignore # mutmut generated
mutants_x__safe_id__mutmut['x__safe_id__mutmut_3'] = x__safe_id__mutmut_3 # type: ignore # mutmut generated
mutants_x__safe_id__mutmut['x__safe_id__mutmut_4'] = x__safe_id__mutmut_4 # type: ignore # mutmut generated
mutants_x__safe_id__mutmut['x__safe_id__mutmut_5'] = x__safe_id__mutmut_5 # type: ignore # mutmut generated
mutants_x__safe_id__mutmut['x__safe_id__mutmut_6'] = x__safe_id__mutmut_6 # type: ignore # mutmut generated
