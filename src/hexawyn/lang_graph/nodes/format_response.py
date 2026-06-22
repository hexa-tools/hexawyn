from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import FormatResponseOutput


def run(state: AgentState) -> FormatResponseOutput:
    """
    Format the final InvestigationResult for the MCP client.
    Stub: marks status as COMPLETE.
    """
    return FormatResponseOutput()
