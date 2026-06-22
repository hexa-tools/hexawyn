from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from uuid import UUID, uuid4


class InvestigationStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    ERROR = "error"
    DEGRADED = "degraded"  # UNVERIFIED — checker failed


class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class InvestigationResult:
    query: str
    answer: str
    status: InvestigationStatus
    id: UUID = field(default_factory=uuid4)
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    tool_name: str = ""
    cause: str = ""
    solution: str = ""
    severity: Severity = Severity.LOW
    suggestions: list[str] = field(default_factory=list)  # suggestion chips
    embedding: list[float] = field(default_factory=list)
    verified: bool = False
