from abc import ABC, abstractmethod
from typing import TypedDict


class AlertMessage(TypedDict):
    text: str
    title: str | None
    severity: str
    remediation: str | None
    cluster_name: str
    score: int
    is_pro: bool


class AlertNotificationPort(ABC):
    @abstractmethod
    def send_alert(self, message: AlertMessage) -> bool:
        """
        Send an alert message to the notification platform.
        Returns True if sent successfully, False otherwise.
        Never raises on delivery failures.
        Raises QuotaExceededError if monthly limit is reached.
        """

    @abstractmethod
    def format_finding_alert(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        """
        Format a cluster finding into a generic AlertMessage.
        Each adapter renders it in the platform's native format (Slack blocks, Teams cards, etc.).
        """
