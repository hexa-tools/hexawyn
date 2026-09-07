_DEFAULT_WINDOW_SECONDS = 5.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAlertDeduplicatorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut: MutantDict = {}  # type: ignore


class AlertDeduplicator:
    """Suppresses repeated alerts for the same category within a time window.

    Takes `now` explicitly on each call (no internal clock) so it is
    deterministically testable and has no I/O — pure domain state.
    """

    @_mutmut_mutated(mutants_xǁAlertDeduplicatorǁ__init____mutmut)
    def __init__(self, window_seconds: float = _DEFAULT_WINDOW_SECONDS) -> None:
        self.window_seconds = window_seconds
        self._last_alert_time: dict[str, float] = {}

    def xǁAlertDeduplicatorǁ__init____mutmut_orig(self, window_seconds: float = _DEFAULT_WINDOW_SECONDS) -> None:
        self.window_seconds = window_seconds
        self._last_alert_time: dict[str, float] = {}

    def xǁAlertDeduplicatorǁ__init____mutmut_1(self, window_seconds: float = _DEFAULT_WINDOW_SECONDS) -> None:
        self.window_seconds = None
        self._last_alert_time: dict[str, float] = {}

    def xǁAlertDeduplicatorǁ__init____mutmut_2(self, window_seconds: float = _DEFAULT_WINDOW_SECONDS) -> None:
        self.window_seconds = window_seconds
        self._last_alert_time: dict[str, float] = None

    @_mutmut_mutated(mutants_xǁAlertDeduplicatorǁshould_alert__mutmut)
    def should_alert(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_orig(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_1(self, category: str, now: float) -> bool:
        last_seen = None
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_2(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(None)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_3(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None or (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_4(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_5(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now + last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_6(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) <= self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_7(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return True
        self._last_alert_time[category] = now
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_8(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = None
        return True

    def xǁAlertDeduplicatorǁshould_alert__mutmut_9(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return False

mutants_xǁAlertDeduplicatorǁ__init____mutmut['_mutmut_orig'] = AlertDeduplicator.xǁAlertDeduplicatorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁ__init____mutmut['xǁAlertDeduplicatorǁ__init____mutmut_1'] = AlertDeduplicator.xǁAlertDeduplicatorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁ__init____mutmut['xǁAlertDeduplicatorǁ__init____mutmut_2'] = AlertDeduplicator.xǁAlertDeduplicatorǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['_mutmut_orig'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_1'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_2'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_3'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_4'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_5'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_6'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_7'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_8'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAlertDeduplicatorǁshould_alert__mutmut['xǁAlertDeduplicatorǁshould_alert__mutmut_9'] = AlertDeduplicator.xǁAlertDeduplicatorǁshould_alert__mutmut_9 # type: ignore # mutmut generated
