from __future__ import annotations


def provides_ingress_restriction(ingress_rule_count: int) -> bool:
    return ingress_rule_count > 0


def provides_egress_restriction(egress_rule_count: int) -> bool:
    return egress_rule_count > 0
