from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SecurityAudit:
    cluster_name: str
    severity: str
    findings: dict[str, object] = field(default_factory=dict)

    @property
    def is_critical(self) -> bool:
        return self.severity == "critical"

    @property
    def total_issues(self) -> int:
        total = 0
        for category, content in self.findings.items():
            if isinstance(content, dict):
                for value in content.values():
                    if isinstance(value, int | float):
                        total += int(value)
        return total

    @property
    def category_summary(self) -> dict[str, int]:
        summary: dict[str, int] = {}
        for category, content in self.findings.items():
            if isinstance(content, dict):
                count = 0
                for value in content.values():
                    if isinstance(value, int | float):
                        count += int(value)
                summary[str(category)] = count
        return summary

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> SecurityAudit:
        raw_findings = data.get("findings", {})
        if isinstance(raw_findings, dict):
            findings: dict[str, object] = raw_findings
        else:
            findings = {}
        return cls(
            cluster_name=str(data.get("cluster_name", "")),
            severity=str(data.get("severity", "low")),
            findings=findings,
        )
