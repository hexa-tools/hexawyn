_DEFAULT_WINDOW_SECONDS = 5.0


class AlertDeduplicator:
    """Suppresses repeated alerts for the same category within a time window.

    Takes `now` explicitly on each call (no internal clock) so it is
    deterministically testable and has no I/O — pure domain state.
    """

    def __init__(self, window_seconds: float = _DEFAULT_WINDOW_SECONDS) -> None:
        self.window_seconds = window_seconds
        self._last_alert_time: dict[str, float] = {}

    def should_alert(self, category: str, now: float) -> bool:
        last_seen = self._last_alert_time.get(category)
        if last_seen is not None and (now - last_seen) < self.window_seconds:
            return False
        self._last_alert_time[category] = now
        return True
