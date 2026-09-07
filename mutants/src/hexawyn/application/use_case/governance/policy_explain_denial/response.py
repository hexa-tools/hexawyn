from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class PolicyExplainDenialResponse:
    policy_name: str = ""
    rule_name: str = ""
    raw_message: str = ""
    human_explanation: str = ""
    fix_suggestion: str = ""
    error: str | None = None
