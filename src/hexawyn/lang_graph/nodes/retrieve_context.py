from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import RetrieveContextOutput


def run(state: AgentState) -> RetrieveContextOutput:
    """
    Retrieve k8s context: namespace, node status, topology.
    Stub: returns empty context.
    """
    return RetrieveContextOutput(tool_output={})
