from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_provides_ingress_restriction__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_provides_ingress_restriction__mutmut)
def provides_ingress_restriction(ingress_rule_count: int) -> bool:
    return ingress_rule_count > 0


def x_provides_ingress_restriction__mutmut_orig(ingress_rule_count: int) -> bool:
    return ingress_rule_count > 0


def x_provides_ingress_restriction__mutmut_1(ingress_rule_count: int) -> bool:
    return ingress_rule_count >= 0


def x_provides_ingress_restriction__mutmut_2(ingress_rule_count: int) -> bool:
    return ingress_rule_count > 1

mutants_x_provides_ingress_restriction__mutmut['_mutmut_orig'] = x_provides_ingress_restriction__mutmut_orig # type: ignore # mutmut generated
mutants_x_provides_ingress_restriction__mutmut['x_provides_ingress_restriction__mutmut_1'] = x_provides_ingress_restriction__mutmut_1 # type: ignore # mutmut generated
mutants_x_provides_ingress_restriction__mutmut['x_provides_ingress_restriction__mutmut_2'] = x_provides_ingress_restriction__mutmut_2 # type: ignore # mutmut generated
mutants_x_provides_egress_restriction__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_provides_egress_restriction__mutmut)
def provides_egress_restriction(egress_rule_count: int) -> bool:
    return egress_rule_count > 0


def x_provides_egress_restriction__mutmut_orig(egress_rule_count: int) -> bool:
    return egress_rule_count > 0


def x_provides_egress_restriction__mutmut_1(egress_rule_count: int) -> bool:
    return egress_rule_count >= 0


def x_provides_egress_restriction__mutmut_2(egress_rule_count: int) -> bool:
    return egress_rule_count > 1

mutants_x_provides_egress_restriction__mutmut['_mutmut_orig'] = x_provides_egress_restriction__mutmut_orig # type: ignore # mutmut generated
mutants_x_provides_egress_restriction__mutmut['x_provides_egress_restriction__mutmut_1'] = x_provides_egress_restriction__mutmut_1 # type: ignore # mutmut generated
mutants_x_provides_egress_restriction__mutmut['x_provides_egress_restriction__mutmut_2'] = x_provides_egress_restriction__mutmut_2 # type: ignore # mutmut generated
