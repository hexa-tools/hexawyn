import ast
from pathlib import Path


class TestDbCommandNoInlineSql:
    def test_no_select_count_from_incidents_inline(self) -> None:
        source = Path("src/hexawyn/cli/commands/db_command.py").read_text()
        tree = ast.parse(source)

        sql_strings: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if "SELECT" in node.value.upper() and "FROM" in node.value.upper():
                    sql_strings.append(node.value.strip()[:60])

        assert (
            not sql_strings
        ), f"db_command.py contains {len(sql_strings)} inline SQL string(s): {sql_strings}"

    def test_purge_uses_load_sql(self) -> None:
        source = Path("src/hexawyn/cli/commands/db_command.py").read_text()
        assert (
            "_load_sql" in source or "purge_expired_incidents" in source
        ), "db_command.py should use _load_sql() or purge_*() helpers instead of inline SQL"
