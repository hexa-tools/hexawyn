from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import SemanticCheckerOutput


def run(state: AgentState) -> SemanticCheckerOutput:
    """
    Deterministic checker: validate LLM output against tool output.
    Stub: returns None result (goes to format_response).
    """
    return SemanticCheckerOutput(checker_result=None)
