import logging


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_logger__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_logger__mutmut)
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_orig(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_1(name: str) -> logging.Logger:
    logger = None

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_2(name: str) -> logging.Logger:
    logger = logging.getLogger(None)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_3(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_4(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = None
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_5(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = None
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_6(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(None)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_7(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("XX%(asctime)s | %(levelname)s | %(name)s | %(message)sXX")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_8(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(ASCTIME)S | %(LEVELNAME)S | %(NAME)S | %(MESSAGE)S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_9(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(None)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_10(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(None)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_11(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(None)
        logger.propagate = False

    return logger


def x_get_logger__mutmut_12(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = None

    return logger


def x_get_logger__mutmut_13(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = True

    return logger

mutants_x_get_logger__mutmut['_mutmut_orig'] = x_get_logger__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_1'] = x_get_logger__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_2'] = x_get_logger__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_3'] = x_get_logger__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_4'] = x_get_logger__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_5'] = x_get_logger__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_6'] = x_get_logger__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_7'] = x_get_logger__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_8'] = x_get_logger__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_9'] = x_get_logger__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_10'] = x_get_logger__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_11'] = x_get_logger__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_12'] = x_get_logger__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_13'] = x_get_logger__mutmut_13 # type: ignore # mutmut generated
