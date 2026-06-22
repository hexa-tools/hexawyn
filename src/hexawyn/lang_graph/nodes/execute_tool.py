from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import ExecuteToolOutput


def run(state: AgentState) -> ExecuteToolOutput:
    """
    Execute the selected MCP tool against the cluster.
    Stub: returns empty tool output.
    """
    return ExecuteToolOutput(tool_output={})
