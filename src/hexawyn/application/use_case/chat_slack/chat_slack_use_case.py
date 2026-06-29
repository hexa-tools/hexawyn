from abc import ABC, abstractmethod

from hexawyn.application.use_case.chat_slack.chat_slack_command import ChatSlackCommand
from hexawyn.application.use_case.chat_slack.chat_slack_response import ChatSlackResponse


class ChatSlackUseCase(ABC):
    @abstractmethod
    def execute(self, command: ChatSlackCommand) -> ChatSlackResponse: ...
