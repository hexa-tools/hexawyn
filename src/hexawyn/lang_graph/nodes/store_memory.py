from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import StoreMemoryOutput


def run(state: AgentState) -> StoreMemoryOutput:
    """
    Store investigation result in DuckDB with embedding.
    Stub: no-op.
    """
    return StoreMemoryOutput()
