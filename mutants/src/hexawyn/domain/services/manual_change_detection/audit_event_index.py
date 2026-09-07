from __future__ import annotations

from hexawyn.application.ports.driven.gitops_drift_audit_port import AuditEventRaw


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_index_audit_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_audit_events__mutmut)
def index_audit_events(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_orig(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_1(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["XXkindXX"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_2(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["KIND"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_3(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["XXnameXX"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_4(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["NAME"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_5(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["XXnamespaceXX"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_6(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["NAMESPACE"], event["timestamp"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_7(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["XXtimestampXX"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_8(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["TIMESTAMP"]): event["actor"]
        for event in events
    }


def x_index_audit_events__mutmut_9(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["XXactorXX"]
        for event in events
    }


def x_index_audit_events__mutmut_10(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["ACTOR"]
        for event in events
    }

mutants_x_index_audit_events__mutmut['_mutmut_orig'] = x_index_audit_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_1'] = x_index_audit_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_2'] = x_index_audit_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_3'] = x_index_audit_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_4'] = x_index_audit_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_5'] = x_index_audit_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_6'] = x_index_audit_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_7'] = x_index_audit_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_8'] = x_index_audit_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_9'] = x_index_audit_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_index_audit_events__mutmut['x_index_audit_events__mutmut_10'] = x_index_audit_events__mutmut_10 # type: ignore # mutmut generated
