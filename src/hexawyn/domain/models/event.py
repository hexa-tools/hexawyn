from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventSeverity(Enum):
    """Severity level of a Kubernetes event."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class EventCategory(Enum):
    """Functional category of a Kubernetes event."""

    FAILURE = "failure"
    SCHEDULING = "scheduling"
    NETWORKING = "networking"
    STORAGE = "storage"
    SCALING = "scaling"
    LIFECYCLE = "lifecycle"
    HEALTH = "health"
    SECURITY = "security"
    CONFIGURATION = "configuration"
    RESOURCE = "resource"
    IMAGE = "image"
    OTHER = "other"


@dataclass
class ClassifiedEvent:
    """A Kubernetes event with severity and category classification."""

    event_type: str
    reason: str
    message: str
    severity: EventSeverity
    category: EventCategory
    namespace: str
    involved_object: str
    count: int = 1
    first_timestamp: datetime | None = None
    last_timestamp: datetime | None = None
    source_component: str = ""
    source_host: str = ""
