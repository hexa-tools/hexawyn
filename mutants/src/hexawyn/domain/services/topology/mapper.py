from __future__ import annotations

from collections.abc import Iterable
from typing import TypedDict

from hexawyn.domain.models.dependency_graph import (
    DependencyEdge,
    DependencyGraph,
    InferenceSource,
    NodeType,
    ServiceNode,
)

MAX_NODES_DEFAULT = 200


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class RawServiceRecord(TypedDict):
    name: str
    namespace: str
    replicas: int
    is_external: bool


class RawEdgeRecord(TypedDict):
    caller: str
    callee: str
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut: MutantDict = {}  # type: ignore


class TopologyGraphBuilderService:
    @_mutmut_mutated(mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut)
    def build_graph(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_orig(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_1(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = None
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_2(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(None, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_3(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, None, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_4(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, None)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_5(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_6(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_7(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, )
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_8(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = None

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_9(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["XXnameXX"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_10(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["NAME"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_11(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = None

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_12(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=None, callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_13(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=None)
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_14(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_15(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], )
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_16(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["XXcallerXX"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_17(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["CALLER"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_18(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["XXcalleeXX"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_19(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["CALLEE"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_20(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names or edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_21(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["XXcallerXX"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_22(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["CALLER"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_23(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] not in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_24(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["XXcalleeXX"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_25(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["CALLEE"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_26(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] not in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_27(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = None
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_28(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(None)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_29(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = None
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_30(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(None)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_31(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = None
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_32(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(None, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_33(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, None, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_34(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, None) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_35(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_36(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_37(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, ) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_38(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = None

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_39(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(None)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_40(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=None,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_41(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=None,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_42(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=None,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_43(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=None,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_44(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=None,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_45(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=None,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_46(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_47(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_48(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_49(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_50(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            namespace_scope=namespace_scope,
        )
    def xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_51(  # noqa: PLR0913
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            )

mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['_mutmut_orig'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_1'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_2'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_3'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_4'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_5'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_6'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_7'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_8'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_9'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_10'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_11'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_12'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_13'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_14'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_15'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_16'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_17'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_18'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_19'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_20'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_21'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_22'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_23'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_24'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_25'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_26'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_27'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_28'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_29'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_30'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_31'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_32'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_33'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_34'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_35'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_36'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_37'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_38'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_39'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_40'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_41'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_42'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_43'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_44'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_45'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_46'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_47'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_48'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_48 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_49'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_49 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_50'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_50 # type: ignore # mutmut generated
mutants_xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut['xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_51'] = TopologyGraphBuilderService.xǁTopologyGraphBuilderServiceǁbuild_graph__mutmut_51 # type: ignore # mutmut generated
mutants_x__select_services__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__select_services__mutmut)
def _select_services(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_orig(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_1(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None and len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_2(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_3(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) < max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_4(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, True
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_5(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = None
    return truncated_services, True


def x__select_services__mutmut_6(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(None, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_7(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=None)[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_8(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_9(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, )[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_10(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: None)[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_11(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["XXnameXX"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_12(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["NAME"])[:max_nodes]
    return truncated_services, True


def x__select_services__mutmut_13(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, False

mutants_x__select_services__mutmut['_mutmut_orig'] = x__select_services__mutmut_orig # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_1'] = x__select_services__mutmut_1 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_2'] = x__select_services__mutmut_2 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_3'] = x__select_services__mutmut_3 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_4'] = x__select_services__mutmut_4 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_5'] = x__select_services__mutmut_5 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_6'] = x__select_services__mutmut_6 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_7'] = x__select_services__mutmut_7 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_8'] = x__select_services__mutmut_8 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_9'] = x__select_services__mutmut_9 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_10'] = x__select_services__mutmut_10 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_11'] = x__select_services__mutmut_11 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_12'] = x__select_services__mutmut_12 # type: ignore # mutmut generated
mutants_x__select_services__mutmut['x__select_services__mutmut_13'] = x__select_services__mutmut_13 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__count_degree__mutmut)
def _count_degree(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    return counts


def x__count_degree__mutmut_orig(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    return counts


def x__count_degree__mutmut_1(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = None
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    return counts


def x__count_degree__mutmut_2(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = None
    return counts


def x__count_degree__mutmut_3(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, 0) - 1
    return counts


def x__count_degree__mutmut_4(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(None, 0) + 1
    return counts


def x__count_degree__mutmut_5(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, None) + 1
    return counts


def x__count_degree__mutmut_6(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(0) + 1
    return counts


def x__count_degree__mutmut_7(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, ) + 1
    return counts


def x__count_degree__mutmut_8(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, 1) + 1
    return counts


def x__count_degree__mutmut_9(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 2
    return counts

mutants_x__count_degree__mutmut['_mutmut_orig'] = x__count_degree__mutmut_orig # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_1'] = x__count_degree__mutmut_1 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_2'] = x__count_degree__mutmut_2 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_3'] = x__count_degree__mutmut_3 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_4'] = x__count_degree__mutmut_4 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_5'] = x__count_degree__mutmut_5 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_6'] = x__count_degree__mutmut_6 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_7'] = x__count_degree__mutmut_7 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_8'] = x__count_degree__mutmut_8 # type: ignore # mutmut generated
mutants_x__count_degree__mutmut['x__count_degree__mutmut_9'] = x__count_degree__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_node__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_node__mutmut)
def _build_node(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_orig(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_1(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = None
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_2(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["XXnameXX"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_3(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["NAME"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_4(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = None
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_5(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(None, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_6(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, None)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_7(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_8(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, )
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_9(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 1)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_10(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = None

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_11(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(None, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_12(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, None)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_13(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_14(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, )

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_15(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 1)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_16(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["XXis_externalXX"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_17(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["IS_EXTERNAL"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_18(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = None
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_19(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 or node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_20(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree != 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_21(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 1 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_22(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree != 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_23(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 1:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_24(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = None
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_25(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = None

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_26(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=None,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_27(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=None,
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_28(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=None,
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_29(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=None,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_30(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=None,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_31(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=None,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_32(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=None,
    )


def x__build_node__mutmut_33(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_34(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_35(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_36(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_37(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_38(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_39(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        )


def x__build_node__mutmut_40(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["XXnamespaceXX"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_41(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["NAMESPACE"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_42(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["XXreplicasXX"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_43(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["REPLICAS"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_44(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 or node_in_degree > 0,
    )


def x__build_node__mutmut_45(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["XXreplicasXX"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_46(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["REPLICAS"] == 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_47(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] != 1 and node_in_degree > 0,
    )


def x__build_node__mutmut_48(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 2 and node_in_degree > 0,
    )


def x__build_node__mutmut_49(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree >= 0,
    )


def x__build_node__mutmut_50(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 1,
    )

mutants_x__build_node__mutmut['_mutmut_orig'] = x__build_node__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_1'] = x__build_node__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_2'] = x__build_node__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_3'] = x__build_node__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_4'] = x__build_node__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_5'] = x__build_node__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_6'] = x__build_node__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_7'] = x__build_node__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_8'] = x__build_node__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_9'] = x__build_node__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_10'] = x__build_node__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_11'] = x__build_node__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_12'] = x__build_node__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_13'] = x__build_node__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_14'] = x__build_node__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_15'] = x__build_node__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_16'] = x__build_node__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_17'] = x__build_node__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_18'] = x__build_node__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_19'] = x__build_node__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_20'] = x__build_node__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_21'] = x__build_node__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_22'] = x__build_node__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_23'] = x__build_node__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_24'] = x__build_node__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_25'] = x__build_node__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_26'] = x__build_node__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_27'] = x__build_node__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_28'] = x__build_node__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_29'] = x__build_node__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_30'] = x__build_node__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_31'] = x__build_node__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_32'] = x__build_node__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_33'] = x__build_node__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_34'] = x__build_node__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_35'] = x__build_node__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_36'] = x__build_node__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_37'] = x__build_node__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_38'] = x__build_node__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_39'] = x__build_node__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_40'] = x__build_node__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_41'] = x__build_node__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_42'] = x__build_node__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_43'] = x__build_node__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_44'] = x__build_node__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_45'] = x__build_node__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_46'] = x__build_node__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_47'] = x__build_node__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_48'] = x__build_node__mutmut_48 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_49'] = x__build_node__mutmut_49 # type: ignore # mutmut generated
mutants_x__build_node__mutmut['x__build_node__mutmut_50'] = x__build_node__mutmut_50 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_cycles__mutmut)
def _detect_cycles(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_orig(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_1(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = None
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_2(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(None)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_3(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(None, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_4(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, None).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_5(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault([]).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_6(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, ).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_7(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = None
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_8(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = None
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_9(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = None

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_10(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(None)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_11(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(None)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_12(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(None, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_13(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, None):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_14(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get([]):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_15(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, ):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_16(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor not in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_17(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = None
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_18(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(None)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_19(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.rindex(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_20(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append(None)
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_21(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_22(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(None, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_23(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, None)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_24(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_25(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, )
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_26(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(None)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_27(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(None)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_28(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start in visited:
            visit(start, [])

    return cycles


def x__detect_cycles__mutmut_29(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(None, [])

    return cycles


def x__detect_cycles__mutmut_30(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, None)

    return cycles


def x__detect_cycles__mutmut_31(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit([])

    return cycles


def x__detect_cycles__mutmut_32(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, )

    return cycles

mutants_x__detect_cycles__mutmut['_mutmut_orig'] = x__detect_cycles__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_1'] = x__detect_cycles__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_2'] = x__detect_cycles__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_3'] = x__detect_cycles__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_4'] = x__detect_cycles__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_5'] = x__detect_cycles__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_6'] = x__detect_cycles__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_7'] = x__detect_cycles__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_8'] = x__detect_cycles__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_9'] = x__detect_cycles__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_10'] = x__detect_cycles__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_11'] = x__detect_cycles__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_12'] = x__detect_cycles__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_13'] = x__detect_cycles__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_14'] = x__detect_cycles__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_15'] = x__detect_cycles__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_16'] = x__detect_cycles__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_17'] = x__detect_cycles__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_18'] = x__detect_cycles__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_19'] = x__detect_cycles__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_20'] = x__detect_cycles__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_21'] = x__detect_cycles__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_22'] = x__detect_cycles__mutmut_22 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_23'] = x__detect_cycles__mutmut_23 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_24'] = x__detect_cycles__mutmut_24 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_25'] = x__detect_cycles__mutmut_25 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_26'] = x__detect_cycles__mutmut_26 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_27'] = x__detect_cycles__mutmut_27 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_28'] = x__detect_cycles__mutmut_28 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_29'] = x__detect_cycles__mutmut_29 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_30'] = x__detect_cycles__mutmut_30 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_31'] = x__detect_cycles__mutmut_31 # type: ignore # mutmut generated
mutants_x__detect_cycles__mutmut['x__detect_cycles__mutmut_32'] = x__detect_cycles__mutmut_32 # type: ignore # mutmut generated
