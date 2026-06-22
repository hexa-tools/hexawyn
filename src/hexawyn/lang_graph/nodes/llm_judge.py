from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import LLMJudgeOutput


def run(state: AgentState) -> LLMJudgeOutput:
    """
    LLM-based judge: verify factual accuracy of the response.
    Stub: returns None result (goes to format_response).
    """
    return LLMJudgeOutput(judge_result=None)
