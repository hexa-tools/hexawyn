

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_context_command__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_is_context_command__mutmut)
def is_context_command(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_orig(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_1(text: str) -> bool:
    command_name = None
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_2(text: str) -> bool:
    command_name = text.split(maxsplit=None)[0] if text else ""
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_3(text: str) -> bool:
    command_name = text.rsplit(maxsplit=1)[0] if text else ""
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_4(text: str) -> bool:
    command_name = text.split(maxsplit=2)[0] if text else ""
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_5(text: str) -> bool:
    command_name = text.split(maxsplit=1)[1] if text else ""
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_6(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else "XXXX"
    return command_name in {"/context", "/ctx"}
def x_is_context_command__mutmut_7(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name not in {"/context", "/ctx"}
def x_is_context_command__mutmut_8(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"XX/contextXX", "/ctx"}
def x_is_context_command__mutmut_9(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"/CONTEXT", "/ctx"}
def x_is_context_command__mutmut_10(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"/context", "XX/ctxXX"}
def x_is_context_command__mutmut_11(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"/context", "/CTX"}

mutants_x_is_context_command__mutmut['_mutmut_orig'] = x_is_context_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_1'] = x_is_context_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_2'] = x_is_context_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_3'] = x_is_context_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_4'] = x_is_context_command__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_5'] = x_is_context_command__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_6'] = x_is_context_command__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_7'] = x_is_context_command__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_8'] = x_is_context_command__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_9'] = x_is_context_command__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_10'] = x_is_context_command__mutmut_10 # type: ignore # mutmut generated
mutants_x_is_context_command__mutmut['x_is_context_command__mutmut_11'] = x_is_context_command__mutmut_11 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_token_command__mutmut)
def is_token_command(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/token"


def x_is_token_command__mutmut_orig(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/token"


def x_is_token_command__mutmut_1(text: str) -> bool:
    command_name = None
    return command_name == "/token"


def x_is_token_command__mutmut_2(text: str) -> bool:
    command_name = text.split(maxsplit=None)[0] if text else ""
    return command_name == "/token"


def x_is_token_command__mutmut_3(text: str) -> bool:
    command_name = text.rsplit(maxsplit=1)[0] if text else ""
    return command_name == "/token"


def x_is_token_command__mutmut_4(text: str) -> bool:
    command_name = text.split(maxsplit=2)[0] if text else ""
    return command_name == "/token"


def x_is_token_command__mutmut_5(text: str) -> bool:
    command_name = text.split(maxsplit=1)[1] if text else ""
    return command_name == "/token"


def x_is_token_command__mutmut_6(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else "XXXX"
    return command_name == "/token"


def x_is_token_command__mutmut_7(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name != "/token"


def x_is_token_command__mutmut_8(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "XX/tokenXX"


def x_is_token_command__mutmut_9(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/TOKEN"

mutants_x_is_token_command__mutmut['_mutmut_orig'] = x_is_token_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_1'] = x_is_token_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_2'] = x_is_token_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_3'] = x_is_token_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_4'] = x_is_token_command__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_5'] = x_is_token_command__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_6'] = x_is_token_command__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_7'] = x_is_token_command__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_8'] = x_is_token_command__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_token_command__mutmut['x_is_token_command__mutmut_9'] = x_is_token_command__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_stack_command__mutmut)
def is_stack_command(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/stack"


def x_is_stack_command__mutmut_orig(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/stack"


def x_is_stack_command__mutmut_1(text: str) -> bool:
    command_name = None
    return command_name == "/stack"


def x_is_stack_command__mutmut_2(text: str) -> bool:
    command_name = text.split(maxsplit=None)[0] if text else ""
    return command_name == "/stack"


def x_is_stack_command__mutmut_3(text: str) -> bool:
    command_name = text.rsplit(maxsplit=1)[0] if text else ""
    return command_name == "/stack"


def x_is_stack_command__mutmut_4(text: str) -> bool:
    command_name = text.split(maxsplit=2)[0] if text else ""
    return command_name == "/stack"


def x_is_stack_command__mutmut_5(text: str) -> bool:
    command_name = text.split(maxsplit=1)[1] if text else ""
    return command_name == "/stack"


def x_is_stack_command__mutmut_6(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else "XXXX"
    return command_name == "/stack"


def x_is_stack_command__mutmut_7(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name != "/stack"


def x_is_stack_command__mutmut_8(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "XX/stackXX"


def x_is_stack_command__mutmut_9(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/STACK"

mutants_x_is_stack_command__mutmut['_mutmut_orig'] = x_is_stack_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_1'] = x_is_stack_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_2'] = x_is_stack_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_3'] = x_is_stack_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_4'] = x_is_stack_command__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_5'] = x_is_stack_command__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_6'] = x_is_stack_command__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_7'] = x_is_stack_command__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_8'] = x_is_stack_command__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_stack_command__mutmut['x_is_stack_command__mutmut_9'] = x_is_stack_command__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_refresh_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_refresh_command__mutmut)
def is_refresh_command(text: str) -> bool:
    return text.strip() == "/refresh"


def x_is_refresh_command__mutmut_orig(text: str) -> bool:
    return text.strip() == "/refresh"


def x_is_refresh_command__mutmut_1(text: str) -> bool:
    return text.strip() != "/refresh"


def x_is_refresh_command__mutmut_2(text: str) -> bool:
    return text.strip() == "XX/refreshXX"


def x_is_refresh_command__mutmut_3(text: str) -> bool:
    return text.strip() == "/REFRESH"

mutants_x_is_refresh_command__mutmut['_mutmut_orig'] = x_is_refresh_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_refresh_command__mutmut['x_is_refresh_command__mutmut_1'] = x_is_refresh_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_refresh_command__mutmut['x_is_refresh_command__mutmut_2'] = x_is_refresh_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_refresh_command__mutmut['x_is_refresh_command__mutmut_3'] = x_is_refresh_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_cloud_providers_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_cloud_providers_command__mutmut)
def is_cloud_providers_command(text: str) -> bool:
    return text.strip() == "/providers"


def x_is_cloud_providers_command__mutmut_orig(text: str) -> bool:
    return text.strip() == "/providers"


def x_is_cloud_providers_command__mutmut_1(text: str) -> bool:
    return text.strip() != "/providers"


def x_is_cloud_providers_command__mutmut_2(text: str) -> bool:
    return text.strip() == "XX/providersXX"


def x_is_cloud_providers_command__mutmut_3(text: str) -> bool:
    return text.strip() == "/PROVIDERS"

mutants_x_is_cloud_providers_command__mutmut['_mutmut_orig'] = x_is_cloud_providers_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_cloud_providers_command__mutmut['x_is_cloud_providers_command__mutmut_1'] = x_is_cloud_providers_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_cloud_providers_command__mutmut['x_is_cloud_providers_command__mutmut_2'] = x_is_cloud_providers_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_cloud_providers_command__mutmut['x_is_cloud_providers_command__mutmut_3'] = x_is_cloud_providers_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_setup_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_setup_command__mutmut)
def is_setup_command(text: str) -> bool:
    return text.strip() == "/setup"


def x_is_setup_command__mutmut_orig(text: str) -> bool:
    return text.strip() == "/setup"


def x_is_setup_command__mutmut_1(text: str) -> bool:
    return text.strip() != "/setup"


def x_is_setup_command__mutmut_2(text: str) -> bool:
    return text.strip() == "XX/setupXX"


def x_is_setup_command__mutmut_3(text: str) -> bool:
    return text.strip() == "/SETUP"

mutants_x_is_setup_command__mutmut['_mutmut_orig'] = x_is_setup_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_setup_command__mutmut['x_is_setup_command__mutmut_1'] = x_is_setup_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_setup_command__mutmut['x_is_setup_command__mutmut_2'] = x_is_setup_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_setup_command__mutmut['x_is_setup_command__mutmut_3'] = x_is_setup_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_extract_requested_context__mutmut)
def extract_requested_context(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_orig(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_1(text: str) -> str | None:
    if text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_2(text: str) -> str | None:
    if not text.strip():
        return None
    parts = None
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_3(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=None)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_4(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().rsplit(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_5(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=2)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_6(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) <= 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_7(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 3:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_8(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = None
    return requested_name if requested_name else None


def x_extract_requested_context__mutmut_9(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[2].strip()
    return requested_name if requested_name else None

mutants_x_extract_requested_context__mutmut['_mutmut_orig'] = x_extract_requested_context__mutmut_orig # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_1'] = x_extract_requested_context__mutmut_1 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_2'] = x_extract_requested_context__mutmut_2 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_3'] = x_extract_requested_context__mutmut_3 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_4'] = x_extract_requested_context__mutmut_4 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_5'] = x_extract_requested_context__mutmut_5 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_6'] = x_extract_requested_context__mutmut_6 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_7'] = x_extract_requested_context__mutmut_7 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_8'] = x_extract_requested_context__mutmut_8 # type: ignore # mutmut generated
mutants_x_extract_requested_context__mutmut['x_extract_requested_context__mutmut_9'] = x_extract_requested_context__mutmut_9 # type: ignore # mutmut generated
