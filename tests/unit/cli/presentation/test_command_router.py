from __future__ import annotations

from hexawyn.cli.presentation.command_router import (
    extract_requested_context,
    is_context_command,
    is_refresh_command,
    is_setup_command,
    is_stack_command,
    is_token_command,
)


class TestIsContextCommand:
    def test_context_command_recognized(self) -> None:
        assert is_context_command("/context prod-eu") is True

    def test_ctx_alias_recognized(self) -> None:
        assert is_context_command("/ctx staging") is True

    def test_context_without_args_recognized(self) -> None:
        assert is_context_command("/context") is True

    def test_other_commands_not_context(self) -> None:
        assert is_context_command("/help") is False

    def test_empty_string_not_context(self) -> None:
        assert is_context_command("") is False

    def test_plain_text_not_context(self) -> None:
        assert is_context_command("show me pods") is False


class TestIsTokenCommand:
    def test_token_recognized(self) -> None:
        assert is_token_command("/token") is True

    def test_token_with_args(self) -> None:
        assert is_token_command("/token abc123") is True

    def test_not_token(self) -> None:
        assert is_token_command("/context") is False

    def test_empty_string(self) -> None:
        assert is_token_command("") is False


class TestIsStackCommand:
    def test_stack_recognized(self) -> None:
        assert is_stack_command("/stack") is True

    def test_stack_with_args(self) -> None:
        assert is_stack_command("/stack payments-api") is True

    def test_not_stack(self) -> None:
        assert is_stack_command("/context") is False


class TestIsRefreshCommand:
    def test_exact_refresh(self) -> None:
        assert is_refresh_command("/refresh") is True

    def test_refresh_with_spaces(self) -> None:
        assert is_refresh_command("  /refresh  ") is True

    def test_refresh_with_extra_args_not_matched(self) -> None:
        assert is_refresh_command("/refresh now") is False

    def test_not_refresh(self) -> None:
        assert is_refresh_command("/setup") is False


class TestIsSetupCommand:
    def test_exact_setup(self) -> None:
        assert is_setup_command("/setup") is True

    def test_setup_with_spaces(self) -> None:
        assert is_setup_command("  /setup  ") is True

    def test_setup_with_extra_not_matched(self) -> None:
        assert is_setup_command("/setup wizard") is False

    def test_not_setup(self) -> None:
        assert is_setup_command("/refresh") is False


class TestExtractRequestedContext:
    def test_extracts_second_word(self) -> None:
        assert extract_requested_context("/context prod-eu") == "prod-eu"

    def test_no_args_returns_none(self) -> None:
        assert extract_requested_context("/context") is None

    def test_multiple_words_returns_rest(self) -> None:
        assert (
            extract_requested_context("/context prod-eu namespace default")
            == "prod-eu namespace default"
        )

    def test_only_whitespace_after_command_returns_none(self) -> None:
        assert extract_requested_context("/context   ") is None
