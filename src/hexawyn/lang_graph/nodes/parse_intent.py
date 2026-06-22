from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import ParseIntentOutput


def run(state: AgentState) -> ParseIntentOutput:
    """
    Parse the user query and extract intent + tool name.
    Stub: returns default values. Full implementation in subsequent tickets.
    """
    return ParseIntentOutput(
        intent="diagnose",
        tool_name="describe_pod",
        tool_args={},
        retry_count=0,
    )
