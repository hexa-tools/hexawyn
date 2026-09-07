from __future__ import annotations

from hexawyn.domain.models.image_drift import DriftType, ImageReference

_DIGEST_ALGORITHM_MARKER = ":sha256:"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_drift__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_drift__mutmut)
def classify_drift(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_orig(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_1(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = None
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_2(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(None, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_3(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, None)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_4(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_5(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, )
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_6(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None or running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_7(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_8(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_9(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest != declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_10(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "XXdigest_mismatchXX"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_11(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "DIGEST_MISMATCH"
    return None if running.tag == declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_12(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag != declared.tag else "tag_mismatch"


def x_classify_drift__mutmut_13(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "XXtag_mismatchXX"


def x_classify_drift__mutmut_14(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "TAG_MISMATCH"

mutants_x_classify_drift__mutmut['_mutmut_orig'] = x_classify_drift__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_1'] = x_classify_drift__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_2'] = x_classify_drift__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_3'] = x_classify_drift__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_4'] = x_classify_drift__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_5'] = x_classify_drift__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_6'] = x_classify_drift__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_7'] = x_classify_drift__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_8'] = x_classify_drift__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_9'] = x_classify_drift__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_10'] = x_classify_drift__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_11'] = x_classify_drift__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_12'] = x_classify_drift__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_13'] = x_classify_drift__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_drift__mutmut['x_classify_drift__mutmut_14'] = x_classify_drift__mutmut_14 # type: ignore # mutmut generated
mutants_x__effective_digest__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__effective_digest__mutmut)
def _effective_digest(ref: ImageReference, image_id: str | None) -> str | None:
    if ref.digest is not None:
        return ref.digest
    return _extract_digest_from_image_id(image_id)


def x__effective_digest__mutmut_orig(ref: ImageReference, image_id: str | None) -> str | None:
    if ref.digest is not None:
        return ref.digest
    return _extract_digest_from_image_id(image_id)


def x__effective_digest__mutmut_1(ref: ImageReference, image_id: str | None) -> str | None:
    if ref.digest is None:
        return ref.digest
    return _extract_digest_from_image_id(image_id)


def x__effective_digest__mutmut_2(ref: ImageReference, image_id: str | None) -> str | None:
    if ref.digest is not None:
        return ref.digest
    return _extract_digest_from_image_id(None)

mutants_x__effective_digest__mutmut['_mutmut_orig'] = x__effective_digest__mutmut_orig # type: ignore # mutmut generated
mutants_x__effective_digest__mutmut['x__effective_digest__mutmut_1'] = x__effective_digest__mutmut_1 # type: ignore # mutmut generated
mutants_x__effective_digest__mutmut['x__effective_digest__mutmut_2'] = x__effective_digest__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_digest_from_image_id__mutmut)
def _extract_digest_from_image_id(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_orig(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_1(image_id: str | None) -> str | None:
    if image_id is not None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_2(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = None
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_3(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split(None, 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_4(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", None)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_5(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split(1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_6(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", )[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_7(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.rsplit("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_8(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("XX://XX", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_9(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 2)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_10(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[2] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_11(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "XX://XX" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_12(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" not in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_13(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "XX@XX" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_14(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" not in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_15(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split(None, 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_16(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", None)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_17(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split(1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_18(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", )[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_19(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.rsplit("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_20(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("XX@XX", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_21(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 2)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_22(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[2]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_23(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER not in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_24(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = None
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_25(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(None)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_26(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.rindex(_DIGEST_ALGORITHM_MARKER)
        return value[index + 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_27(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index - 1 :]
    return None


def x__extract_digest_from_image_id__mutmut_28(image_id: str | None) -> str | None:
    if image_id is None:
        return None
    value = image_id.split("://", 1)[1] if "://" in image_id else image_id
    if "@" in value:
        return value.split("@", 1)[1]
    if _DIGEST_ALGORITHM_MARKER in value:
        index = value.index(_DIGEST_ALGORITHM_MARKER)
        return value[index + 2 :]
    return None

mutants_x__extract_digest_from_image_id__mutmut['_mutmut_orig'] = x__extract_digest_from_image_id__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_1'] = x__extract_digest_from_image_id__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_2'] = x__extract_digest_from_image_id__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_3'] = x__extract_digest_from_image_id__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_4'] = x__extract_digest_from_image_id__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_5'] = x__extract_digest_from_image_id__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_6'] = x__extract_digest_from_image_id__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_7'] = x__extract_digest_from_image_id__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_8'] = x__extract_digest_from_image_id__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_9'] = x__extract_digest_from_image_id__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_10'] = x__extract_digest_from_image_id__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_11'] = x__extract_digest_from_image_id__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_12'] = x__extract_digest_from_image_id__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_13'] = x__extract_digest_from_image_id__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_14'] = x__extract_digest_from_image_id__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_15'] = x__extract_digest_from_image_id__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_16'] = x__extract_digest_from_image_id__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_17'] = x__extract_digest_from_image_id__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_18'] = x__extract_digest_from_image_id__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_19'] = x__extract_digest_from_image_id__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_20'] = x__extract_digest_from_image_id__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_21'] = x__extract_digest_from_image_id__mutmut_21 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_22'] = x__extract_digest_from_image_id__mutmut_22 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_23'] = x__extract_digest_from_image_id__mutmut_23 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_24'] = x__extract_digest_from_image_id__mutmut_24 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_25'] = x__extract_digest_from_image_id__mutmut_25 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_26'] = x__extract_digest_from_image_id__mutmut_26 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_27'] = x__extract_digest_from_image_id__mutmut_27 # type: ignore # mutmut generated
mutants_x__extract_digest_from_image_id__mutmut['x__extract_digest_from_image_id__mutmut_28'] = x__extract_digest_from_image_id__mutmut_28 # type: ignore # mutmut generated
