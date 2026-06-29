from abc import ABC, abstractmethod

from hexawyn.application.use_case.chat_cli.chat_cli_command import ChatCliCommand
from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse


class ChatCliUseCase(ABC):
    @abstractmethod
    def execute(self, command: ChatCliCommand) -> ChatCliResponse: ...
