"""Memory consolidation domain service."""

import logging
import uuid
from datetime import UTC, datetime

from hexawyn.application.ports.driven.consolidation_port import (
    ConsolidationConfig,
    ConsolidationPort,
)
from hexawyn.domain.models.consolidation import (
    ConsolidatedKnowledge,
)
from hexawyn.domain.models.consolidation import (
    ConsolidationConfig as DomainConfig,
)

logger = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConsolidationJobǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConsolidationJobǁrun__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConsolidationJobǁ_build_pattern__mutmut: MutantDict = {}  # type: ignore


class ConsolidationJob:
    @_mutmut_mutated(mutants_xǁConsolidationJobǁ__init____mutmut)
    def __init__(
        self,
        port: ConsolidationPort,
        config: DomainConfig | None = None,
    ) -> None:
        self._port = port
        self._config = config or DomainConfig()
    def xǁConsolidationJobǁ__init____mutmut_orig(
        self,
        port: ConsolidationPort,
        config: DomainConfig | None = None,
    ) -> None:
        self._port = port
        self._config = config or DomainConfig()
    def xǁConsolidationJobǁ__init____mutmut_1(
        self,
        port: ConsolidationPort,
        config: DomainConfig | None = None,
    ) -> None:
        self._port = None
        self._config = config or DomainConfig()
    def xǁConsolidationJobǁ__init____mutmut_2(
        self,
        port: ConsolidationPort,
        config: DomainConfig | None = None,
    ) -> None:
        self._port = port
        self._config = None
    def xǁConsolidationJobǁ__init____mutmut_3(
        self,
        port: ConsolidationPort,
        config: DomainConfig | None = None,
    ) -> None:
        self._port = port
        self._config = config and DomainConfig()

    @_mutmut_mutated(mutants_xǁConsolidationJobǁrun__mutmut)
    def run(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_orig(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_1(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = None

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_2(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "XXmin_occurrencesXX": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_3(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "MIN_OCCURRENCES": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_4(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "XXsimilarity_thresholdXX": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_5(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "SIMILARITY_THRESHOLD": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_6(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "XXmax_age_daysXX": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_7(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "MAX_AGE_DAYS": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_8(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = None

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_9(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=None, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_10(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=None)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_11(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_12(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, )

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_13(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = None
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_14(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count <= self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_15(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                break

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_16(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = None
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_17(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=None,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_18(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=None,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_19(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=None,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_20(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=None,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_21(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=None,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_22(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_23(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_24(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_25(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_26(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                )
            if knowledge is not None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_27(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is None:
                results.append(knowledge)

        return results

    def xǁConsolidationJobǁrun__mutmut_28(self, cluster_name: str) -> list[ConsolidatedKnowledge]:
        api_config: ConsolidationConfig = {
            "min_occurrences": self._config.min_occurrences,
            "similarity_threshold": self._config.similarity_threshold,
            "max_age_days": self._config.max_age_days,
        }

        groups = self._port.find_incident_groups(config=api_config, cluster_name=cluster_name)

        results: list[ConsolidatedKnowledge] = []
        for namespace, resource_name, tool_name, occurrence_count in groups:
            if occurrence_count < self._config.min_occurrences:
                continue

            knowledge = self._consolidate_group(
                namespace=namespace,
                resource_name=resource_name,
                tool_name=tool_name,
                cluster_name=cluster_name,
                occurrence_count=occurrence_count,
            )
            if knowledge is not None:
                results.append(None)

        return results

    @_mutmut_mutated(mutants_xǁConsolidationJobǁ_consolidate_group__mutmut)
    def _consolidate_group(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_orig(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_1(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = None

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_2(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=None,
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_3(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_4(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=None,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_5(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=None,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_6(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=None,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_7(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_8(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_9(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_10(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_11(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_12(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace and "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_13(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "XX_null_XX",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_14(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_NULL_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_15(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name and "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_16(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "XX_null_XX",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_17(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_NULL_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_18(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) <= self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_19(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = None

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_20(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=None,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_21(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_22(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=None,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_23(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=None,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_24(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_25(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_26(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_27(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_28(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = None
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_29(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(None)
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_30(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = None

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_31(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(None).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_32(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=None,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_33(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=None,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_34(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_35(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_36(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=None,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_37(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=None,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_38(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=None,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_39(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=None,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_40(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=None,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_41(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=None,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_42(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=None,
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_43(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=None,
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_44(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_45(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_46(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_47(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_48(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_49(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_50(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_51(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_52(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_53(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_54(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_55(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_56(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name and None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_57(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace and None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_58(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(None, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_59(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, None),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_60(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_61(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, ),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_62(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(6.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_63(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 - (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_64(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 2.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_65(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) / 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_66(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count + 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_67(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 2) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_68(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 1.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_69(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(None, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_70(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, None),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_71(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_72(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, ),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_73(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(2.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_74(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 - occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_75(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 1.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_76(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count / 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_77(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 1.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_78(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=None,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_79(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=None,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_80(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_81(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_82(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=None,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_83(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=None,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_84(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_85(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_86(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=None,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_87(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=None,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_88(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=None,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_89(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=None,
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_90(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=None,
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_91(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_92(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_93(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_94(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_95(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_96(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_97(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_98(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_99(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_100(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name and None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_101(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace and None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_102(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(None, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_103(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, None),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_104(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_105(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, ),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_106(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(6.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_107(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 - (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_108(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 2.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_109(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) / 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_110(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count + 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_111(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 2) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_112(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 1.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_113(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(None, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_114(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, None),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_115(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_116(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, ),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_117(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(2.0, 0.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_118(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 - occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_119(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 1.5 + occurrence_count * 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_120(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count / 0.1),
        )

    def xǁConsolidationJobǁ_consolidate_group__mutmut_121(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
    ) -> ConsolidatedKnowledge | None:
        incident_ids = self._port.get_incidents_for_group(
            namespace=namespace or "_null_",
            resource_name=resource_name or "_null_",
            tool_name=tool_name,
            cluster_name=cluster_name,
            max_age_days=self._config.max_age_days,
        )

        if len(incident_ids) < self._config.min_occurrences:
            return None

        pattern = self._build_pattern(
            namespace=namespace,
            resource_name=resource_name,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
        )

        knowledge_id = str(uuid.uuid4())
        now = datetime.now(UTC).isoformat()

        self._port.store_knowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            cluster_name=cluster_name,
            occurrence_count=occurrence_count,
            first_seen=now,
            last_seen=now,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 0.1),
        )

        self._port.mark_consolidated(
            incident_ids=incident_ids,
            knowledge_id=knowledge_id,
        )

        return ConsolidatedKnowledge(
            id=knowledge_id,
            pattern=pattern,
            resource_name=resource_name or None,
            namespace=namespace or None,
            tool_name=tool_name,
            occurrence_count=occurrence_count,
            source_incident_ids=incident_ids,
            weight=min(5.0, 1.0 + (occurrence_count - 1) * 0.5),
            confidence=min(1.0, 0.5 + occurrence_count * 1.1),
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁConsolidationJobǁ_build_pattern__mutmut)
    def _build_pattern(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "unknown resource"
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_orig(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "unknown resource"
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_1(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = None
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_2(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name and "unknown resource"
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_3(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "XXunknown resourceXX"
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_4(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "UNKNOWN RESOURCE"
        ns = f" in {namespace}" if namespace else ""
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_5(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "unknown resource"
        ns = None
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

    @staticmethod
    def xǁConsolidationJobǁ_build_pattern__mutmut_6(
        namespace: str,
        resource_name: str,
        tool_name: str,
        occurrence_count: int,
    ) -> str:
        resource = resource_name or "unknown resource"
        ns = f" in {namespace}" if namespace else "XXXX"
        return (
            f"{resource}{ns} has been investigated {occurrence_count} times "
            f"via {tool_name} — review past causes and solutions before investigating again."
        )

mutants_xǁConsolidationJobǁ__init____mutmut['_mutmut_orig'] = ConsolidationJob.xǁConsolidationJobǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ__init____mutmut['xǁConsolidationJobǁ__init____mutmut_1'] = ConsolidationJob.xǁConsolidationJobǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ__init____mutmut['xǁConsolidationJobǁ__init____mutmut_2'] = ConsolidationJob.xǁConsolidationJobǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ__init____mutmut['xǁConsolidationJobǁ__init____mutmut_3'] = ConsolidationJob.xǁConsolidationJobǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁConsolidationJobǁrun__mutmut['_mutmut_orig'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_1'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_2'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_3'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_4'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_5'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_6'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_7'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_8'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_9'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_10'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_11'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_12'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_13'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_14'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_15'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_16'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_17'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_18'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_18 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_19'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_19 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_20'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_20 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_21'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_21 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_22'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_22 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_23'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_23 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_24'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_24 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_25'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_25 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_26'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_26 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_27'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_27 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁrun__mutmut['xǁConsolidationJobǁrun__mutmut_28'] = ConsolidationJob.xǁConsolidationJobǁrun__mutmut_28 # type: ignore # mutmut generated

mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['_mutmut_orig'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_1'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_2'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_3'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_4'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_5'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_6'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_7'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_8'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_9'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_10'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_11'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_12'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_13'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_14'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_15'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_16'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_17'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_18'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_18 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_19'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_19 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_20'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_20 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_21'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_21 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_22'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_22 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_23'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_23 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_24'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_24 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_25'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_25 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_26'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_26 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_27'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_27 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_28'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_28 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_29'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_29 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_30'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_30 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_31'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_31 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_32'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_32 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_33'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_33 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_34'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_34 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_35'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_35 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_36'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_36 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_37'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_37 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_38'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_38 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_39'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_39 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_40'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_40 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_41'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_41 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_42'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_42 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_43'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_43 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_44'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_44 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_45'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_45 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_46'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_46 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_47'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_47 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_48'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_48 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_49'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_49 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_50'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_50 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_51'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_51 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_52'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_52 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_53'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_53 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_54'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_54 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_55'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_55 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_56'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_56 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_57'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_57 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_58'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_58 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_59'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_59 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_60'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_60 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_61'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_61 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_62'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_62 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_63'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_63 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_64'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_64 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_65'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_65 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_66'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_66 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_67'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_67 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_68'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_68 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_69'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_69 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_70'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_70 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_71'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_71 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_72'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_72 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_73'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_73 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_74'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_74 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_75'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_75 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_76'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_76 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_77'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_77 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_78'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_78 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_79'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_79 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_80'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_80 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_81'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_81 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_82'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_82 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_83'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_83 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_84'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_84 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_85'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_85 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_86'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_86 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_87'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_87 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_88'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_88 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_89'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_89 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_90'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_90 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_91'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_91 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_92'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_92 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_93'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_93 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_94'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_94 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_95'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_95 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_96'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_96 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_97'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_97 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_98'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_98 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_99'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_99 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_100'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_100 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_101'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_101 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_102'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_102 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_103'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_103 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_104'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_104 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_105'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_105 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_106'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_106 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_107'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_107 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_108'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_108 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_109'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_109 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_110'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_110 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_111'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_111 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_112'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_112 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_113'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_113 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_114'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_114 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_115'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_115 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_116'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_116 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_117'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_117 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_118'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_118 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_119'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_119 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_120'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_120 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_consolidate_group__mutmut['xǁConsolidationJobǁ_consolidate_group__mutmut_121'] = ConsolidationJob.xǁConsolidationJobǁ_consolidate_group__mutmut_121 # type: ignore # mutmut generated

mutants_xǁConsolidationJobǁ_build_pattern__mutmut['_mutmut_orig'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_build_pattern__mutmut['xǁConsolidationJobǁ_build_pattern__mutmut_1'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_build_pattern__mutmut['xǁConsolidationJobǁ_build_pattern__mutmut_2'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_build_pattern__mutmut['xǁConsolidationJobǁ_build_pattern__mutmut_3'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_build_pattern__mutmut['xǁConsolidationJobǁ_build_pattern__mutmut_4'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_build_pattern__mutmut['xǁConsolidationJobǁ_build_pattern__mutmut_5'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConsolidationJobǁ_build_pattern__mutmut['xǁConsolidationJobǁ_build_pattern__mutmut_6'] = ConsolidationJob.xǁConsolidationJobǁ_build_pattern__mutmut_6 # type: ignore # mutmut generated
