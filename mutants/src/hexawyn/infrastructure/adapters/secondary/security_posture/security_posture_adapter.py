from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.security_posture_port import (  # type: ignore
    SecurityPosturePort,
    WorkloadComplianceRaw,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ComplianceCategoryProvider(Protocol):
    """One security-audit category normalized into posture records.

    Each provider wraps an existing audit (TLS, RBAC, Pod Security, image
    scanning, secret rotation) and returns its results as WorkloadComplianceRaw.
    """

    def category(self) -> str: ...

    def fetch(self) -> list[WorkloadComplianceRaw]: ...
mutants_xǁSecurityPostureAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut: MutantDict = {}  # type: ignore


class SecurityPostureAdapter(SecurityPosturePort):
    """Facade over the individual security audits.

    Fans out to each injected category provider, normalizing heterogeneous
    audit results into a single uniform contract for the domain. A provider
    that fails (e.g. times out on a large cluster) is skipped and its category
    is left undefined, marking the overall scan partial — the report degrades
    gracefully instead of crashing.
    """

    @_mutmut_mutated(mutants_xǁSecurityPostureAdapterǁ__init____mutmut)
    def __init__(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = providers
        self._defined_categories: list[str] = []
        self._partial = False

    def xǁSecurityPostureAdapterǁ__init____mutmut_orig(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = providers
        self._defined_categories: list[str] = []
        self._partial = False

    def xǁSecurityPostureAdapterǁ__init____mutmut_1(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = None
        self._defined_categories: list[str] = []
        self._partial = False

    def xǁSecurityPostureAdapterǁ__init____mutmut_2(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = providers
        self._defined_categories: list[str] = None
        self._partial = False

    def xǁSecurityPostureAdapterǁ__init____mutmut_3(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = providers
        self._defined_categories: list[str] = []
        self._partial = None

    def xǁSecurityPostureAdapterǁ__init____mutmut_4(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = providers
        self._defined_categories: list[str] = []
        self._partial = True

    @_mutmut_mutated(mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut)
    def list_workload_compliance(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_orig(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_1(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = None
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_2(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = None
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_3(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = None
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_4(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = True
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_5(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = None
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_6(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = None
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_7(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = False
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_8(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                break
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_9(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(None)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_10(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(None)
        self._defined_categories = defined
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_11(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = None
        self._partial = partial
        return records

    def xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_12(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = None
        return records

    def get_defined_categories(self) -> list[str]:
        return self._defined_categories

    def is_partial(self) -> bool:
        return self._partial

mutants_xǁSecurityPostureAdapterǁ__init____mutmut['_mutmut_orig'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁ__init____mutmut['xǁSecurityPostureAdapterǁ__init____mutmut_1'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁ__init____mutmut['xǁSecurityPostureAdapterǁ__init____mutmut_2'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁ__init____mutmut['xǁSecurityPostureAdapterǁ__init____mutmut_3'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁ__init____mutmut['xǁSecurityPostureAdapterǁ__init____mutmut_4'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['_mutmut_orig'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_1'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_2'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_3'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_4'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_5'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_6'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_7'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_8'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_9'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_10'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_11'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut['xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_12'] = SecurityPostureAdapter.xǁSecurityPostureAdapterǁlist_workload_compliance__mutmut_12 # type: ignore # mutmut generated
