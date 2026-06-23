import os

from hexawyn.infrastructure.config.quota_manager import check_quota
from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import ParseIntentOutput


def run(state: AgentState) -> ParseIntentOutput:
    """
    Parse the user query and extract intent + tool name.

    IMPORTANT: checks quota BEFORE starting the investigation.
    Demo mode skips quota check — demo scenarios never count against quota.

    Raises:
        QuotaExceededError: if Free tier monthly limit is reached.
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if not demo_mode:
        check_quota()

    return ParseIntentOutput(
        intent="diagnose",
        tool_name="describe_pod",
        tool_args={},
        retry_count=0,
    )
