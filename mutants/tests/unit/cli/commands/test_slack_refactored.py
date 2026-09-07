class TestSlackRefactored:
    def test_no_bot_token_duplication(self) -> None:
        from pathlib import Path

        source = Path("src/hexawyn/cli/commands/slack_command.py").read_text()
        occurrences = source.count("SLACK_BOT_TOKEN not set")
        assert (
            occurrences <= 1
        ), f"'SLACK_BOT_TOKEN not set' appears {occurrences} times, should be extracted"

    def test_no_app_token_duplication(self) -> None:
        from pathlib import Path

        source = Path("src/hexawyn/cli/commands/slack_command.py").read_text()
        occurrences = source.count("SLACK_APP_TOKEN not set")
        assert occurrences <= 1, f"'SLACK_APP_TOKEN not set' appears {occurrences} times"
