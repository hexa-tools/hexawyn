from __future__ import annotations

from typing import cast

from hexawyn.domain.models.schedule import CronCheck
from hexawyn.infrastructure.config.config_manager import load_config, save_config


class YamlScheduleSource:
    """Charge/persiste les CronCheck depuis ~/.hexawyn/schedule.yaml."""

    def load_checks(self) -> list[CronCheck]:
        config = load_config()
        schedule_section = config.get("schedule")
        if not isinstance(schedule_section, dict):
            return []

        checks: list[CronCheck] = []
        for name, entry in schedule_section.items():
            if not isinstance(entry, dict):
                continue
            checks.append(
                CronCheck(
                    name=str(name),
                    schedule=str(entry.get("schedule", "0 0 * * *")),
                    use_case=str(entry.get("use_case", "")),
                    params=cast(dict[str, str], entry.get("params"))
                    if isinstance(entry.get("params"), dict)
                    else {},
                    enabled=bool(entry.get("enabled", True)),
                    notify_policy=str(entry.get("notify_policy", "on_change")),
                    destinations=(
                        list(entry.get("destinations", ["slack"]))
                        if isinstance(entry.get("destinations"), list)
                        else ["slack"]
                    ),
                    timeout_seconds=int(entry.get("timeout_seconds", 300)),
                )
            )
        return checks

    def save_checks(self, checks: list[CronCheck]) -> None:
        config = load_config()
        schedule_section: dict[str, dict[str, object]] = {}
        for check in checks:
            schedule_section[check.name] = {
                "schedule": check.schedule,
                "use_case": check.use_case,
                "params": check.params,
                "enabled": check.enabled,
                "notify_policy": check.notify_policy,
                "destinations": check.destinations,
                "timeout_seconds": check.timeout_seconds,
            }
        config["schedule"] = schedule_section
        save_config(config)
