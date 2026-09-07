from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace

from hexawyn.domain.models.helm_values_diff import (
    DiffSeverity,
    HelmValuesDiffReport,
    ValueDiff,
)
from hexawyn.domain.services.helm_values_diff.severity_matrix import (
    classify_severity,
    is_secret_key,
)
from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

_REDACTED = "[REDACTED]"
_CHRONIC_DIFF_DAYS = 7

DiffAgeProvider = Callable[[str], "int | None"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHelmValuesDiffServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut: MutantDict = {}  # type: ignore


class HelmValuesDiffService:
    """Domain service — turns two Helm values trees into a graded diff report.

    Enriches the structural diff with the authoritative severity matrix,
    redacts secret-bearing values, keeps the source→target direction explicit
    (source is the reference environment, e.g. staging), attaches
    human-readable discrepancy suggestions, and — when a diff-age provider is
    injected — flags critical differences that have persisted beyond a week.
    """

    @_mutmut_mutated(mutants_xǁHelmValuesDiffServiceǁ__init____mutmut)
    def __init__(self, diff_age_provider: DiffAgeProvider | None = None) -> None:
        self._diff_age_provider = diff_age_provider

    def xǁHelmValuesDiffServiceǁ__init____mutmut_orig(self, diff_age_provider: DiffAgeProvider | None = None) -> None:
        self._diff_age_provider = diff_age_provider

    def xǁHelmValuesDiffServiceǁ__init____mutmut_1(self, diff_age_provider: DiffAgeProvider | None = None) -> None:
        self._diff_age_provider = None

    @_mutmut_mutated(mutants_xǁHelmValuesDiffServiceǁdiff__mutmut)
    def diff(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_orig(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_1(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = None

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_2(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(None, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_3(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, None, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_4(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, None)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_5(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_6(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_7(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, )
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_8(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(None, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_9(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, None)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_10(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_11(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, )
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_12(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = None
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_13(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity != "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_14(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "XXcriticalXX"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_15(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "CRITICAL"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_16(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = None
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_17(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity != "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_18(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "XXwarningXX"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_19(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "WARNING"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_20(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = None

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_21(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity != "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_22(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "XXinformationalXX"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_23(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "INFORMATIONAL"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_24(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=None,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_25(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=None,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_26(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=None,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_27(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=None,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_28(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=None,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_29(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=None,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_30(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=None,
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_31(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=None,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_32(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_33(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_34(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_35(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_36(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_37(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_38(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            in_sync=len(enriched) == 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_39(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_40(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) != 0,
        )

    def xǁHelmValuesDiffServiceǁdiff__mutmut_41(  # noqa: PLR0913
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 1,
        )

    @_mutmut_mutated(mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut)
    def _enrich(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_orig(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_1(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = None
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_2(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(None)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_3(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = None
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_4(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(None)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_5(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = None
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_6(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret or raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_7(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = None
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_8(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret or raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_9(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = None
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_10(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(None, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_11(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, None, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_12(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, None, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_13(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, None, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_14(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, None)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_15(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_16(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_17(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_18(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_19(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, )
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_20(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            None,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_21(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=None,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_22(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=None,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_23(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=None,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_24(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=None,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_25(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=None,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_26(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_27(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_28(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_29(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            is_secret=secret,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_30(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            suggestion=suggestion,
        )

    def xǁHelmValuesDiffServiceǁ_enrich__mutmut_31(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            )

    @_mutmut_mutated(mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut)
    def _suggest(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_orig(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_1(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = None
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_2(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(None, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_3(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, None, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_4(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, None, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_5(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, None)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_6(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_7(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_8(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_9(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, )]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_10(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                None
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_11(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "XXType mismatch may cause runtime issues (e.g. a quoted number parsed as a string).XX"
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_12(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_13(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "TYPE MISMATCH MAY CAUSE RUNTIME ISSUES (E.G. A QUOTED NUMBER PARSED AS A STRING)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_14(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = None
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_15(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(None, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_16(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, None)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_17(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_18(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, )
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_19(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(None)
        return " ".join(part for part in parts if part)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_20(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(None)

    def xǁHelmValuesDiffServiceǁ_suggest__mutmut_21(  # noqa: PLR0913
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return "XX XX".join(part for part in parts if part)

    @_mutmut_mutated(mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut)
    def _base_suggestion(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_orig(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_1(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = None
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_2(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.upper()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_3(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") and key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_4(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith(None) or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_5(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("XXimage.tagXX") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_6(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("IMAGE.TAG") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_7(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith(None):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_8(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("XXimage.repositoryXX"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_9(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("IMAGE.REPOSITORY"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_10(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "XXreplicaXX" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_11(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "REPLICA" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_12(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" not in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_13(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key and "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_14(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "XXresources.limitsXX" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_15(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "RESOURCES.LIMITS" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_16(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" not in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_17(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "XXresources.requestsXX" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_18(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "RESOURCES.REQUESTS" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_19(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" not in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_20(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "XXResource sizing differs, which can change performance and OOM behaviour.XX"
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_21(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "resource sizing differs, which can change performance and oom behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_22(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "RESOURCE SIZING DIFFERS, WHICH CAN CHANGE PERFORMANCE AND OOM BEHAVIOUR."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_23(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type != "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_24(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "XXaddedXX":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_25(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "ADDED":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_26(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type != "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_27(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "XXremovedXX":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_28(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "REMOVED":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    @_mutmut_mutated(mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut)
    def _age_note(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_orig(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_1(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None and severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_2(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is not None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_3(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity == "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_4(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "XXcriticalXX":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_5(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "CRITICAL":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_6(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return "XXXX"
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_7(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = None
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_8(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(None)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_9(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None or age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_10(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_11(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days >= _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""

    def xǁHelmValuesDiffServiceǁ_age_note__mutmut_12(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return "XXXX"

mutants_xǁHelmValuesDiffServiceǁ__init____mutmut['_mutmut_orig'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ__init____mutmut['xǁHelmValuesDiffServiceǁ__init____mutmut_1'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['_mutmut_orig'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_1'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_2'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_3'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_4'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_5'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_6'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_7'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_8'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_9'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_10'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_11'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_12'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_13'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_14'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_15'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_16'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_17'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_18'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_19'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_20'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_21'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_22'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_23'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_24'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_25'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_26'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_27'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_28'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_29'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_30'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_31'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_32'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_33'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_34'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_35'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_36'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_37'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_38'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_39'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_40'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁdiff__mutmut['xǁHelmValuesDiffServiceǁdiff__mutmut_41'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁdiff__mutmut_41 # type: ignore # mutmut generated

mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['_mutmut_orig'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_1'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_2'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_3'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_4'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_5'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_6'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_7'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_8'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_9'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_10'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_11'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_12'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_13'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_14'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_15'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_16'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_17'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_18'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_19'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_20'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_21'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_22'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_23'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_24'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_25'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_26'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_27'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_28'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_29'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_30'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_enrich__mutmut['xǁHelmValuesDiffServiceǁ_enrich__mutmut_31'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_enrich__mutmut_31 # type: ignore # mutmut generated

mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['_mutmut_orig'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_1'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_2'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_3'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_4'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_5'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_6'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_7'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_8'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_9'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_10'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_11'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_12'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_13'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_14'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_15'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_16'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_17'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_18'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_19'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_20'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_suggest__mutmut['xǁHelmValuesDiffServiceǁ_suggest__mutmut_21'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_suggest__mutmut_21 # type: ignore # mutmut generated

mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['_mutmut_orig'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_1'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_2'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_3'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_4'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_5'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_6'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_7'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_8'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_9'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_10'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_11'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_12'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_13'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_14'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_15'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_16'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_17'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_18'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_19'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_20'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_21'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_22'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_23'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_24'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_25'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_26'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_27'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut['xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_28'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_base_suggestion__mutmut_28 # type: ignore # mutmut generated

mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['_mutmut_orig'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_1'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_2'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_3'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_4'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_5'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_6'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_7'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_8'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_9'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_10'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_11'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmValuesDiffServiceǁ_age_note__mutmut['xǁHelmValuesDiffServiceǁ_age_note__mutmut_12'] = HelmValuesDiffService.xǁHelmValuesDiffServiceǁ_age_note__mutmut_12 # type: ignore # mutmut generated
