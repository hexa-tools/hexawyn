import ast
from pathlib import Path


class TestAuthCommandNoDuplicateJwt:
    def test_no_inline_jwt_split_decode(self) -> None:
        source = Path("src/hexawyn/cli/commands/auth_command.py").read_text()
        tree = ast.parse(source)

        jwt_patterns = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                body_text = ast.unparse(node)
                if '.split(".")' in body_text and "base64" in body_text:
                    jwt_patterns += 1

        assert jwt_patterns <= 1, (
            f"auth_command.py has {jwt_patterns} places doing manual JWT split+decode. "
            "Use read_license_state() from license_reader.py instead."
        )

    def test_no_is_jwt_expired_function(self) -> None:
        source = Path("src/hexawyn/cli/commands/auth_command.py").read_text()
        assert (
            "_is_jwt_expired" not in source
        ), "Remove _is_jwt_expired. Use LicenseState from read_license_state() instead."

    def test_no_decode_jwt_payload_function(self) -> None:
        source = Path("src/hexawyn/cli/commands/auth_command.py").read_text()
        assert (
            "_decode_jwt_payload" not in source
        ), "Remove _decode_jwt_payload. Use read_license_state() from license_reader.py."

    def test_no_read_license_key_function(self) -> None:
        source = Path("src/hexawyn/cli/commands/auth_command.py").read_text()
        assert (
            "def _read_license_key" not in source
        ), "Remove _read_license_key — duplicated in license_reader.py."

    def test_no_format_expiry_from_timestamp(self) -> None:
        source = Path("src/hexawyn/cli/commands/auth_command.py").read_text()
        assert (
            "_format_expiry_from_timestamp" not in source
        ), "Remove _format_expiry_from_timestamp. Use LicenseState.expiry_date."

    def test_status_uses_read_license_state(self) -> None:
        source = Path("src/hexawyn/cli/commands/auth_command.py").read_text()
        assert (
            "read_license_state" in source
        ), "status() command should use read_license_state() instead of manual JWT parsing."
