from abc import ABC, abstractmethod


class MessagePublisherPort(ABC):
    """Port for publishing messages to a chat platform — Slack, Teams, etc."""

    @abstractmethod
    def post_message(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        """
        Post a message to a channel.
        Returns the message timestamp if delivered, None otherwise.
        Never raises — delivery failures must not crash hexawyn.
        """

    @abstractmethod
    def update_message(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        """
        Update an existing message (replace content).
        Returns the message timestamp if updated, None otherwise.
        Never raises — update failures must not crash hexawyn.
        """
