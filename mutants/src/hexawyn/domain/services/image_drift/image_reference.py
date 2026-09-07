from __future__ import annotations

from hexawyn.domain.models.image_drift import ImageReference

_DIGEST_ALGORITHM_MARKER = ":sha256:"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_parse_image_reference__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_image_reference__mutmut)
def parse_image_reference(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_orig(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_1(image: str) -> ImageReference:
    if "XX@XX" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_2(image: str) -> ImageReference:
    if "@" not in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_3(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = None
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_4(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split(None, 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_5(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", None)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_6(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split(1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_7(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", )
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_8(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.rsplit("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_9(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("XX@XX", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_10(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 2)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_11(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=None, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_12(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=None)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_13(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_14(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_15(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, )
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_16(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER not in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_17(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = None
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_18(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(None)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_19(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.rindex(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_20(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=None, tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_21(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=None)
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_22(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_23(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_24(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, )
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_25(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index - 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_26(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 2 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_27(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = None
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_28(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind(None)
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_29(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.find("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_30(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("XX/XX")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_31(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = None
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_32(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(None)
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_33(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.find(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_34(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind("XX:XX")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_35(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon >= last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_36(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=None, tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_37(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=None, digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_38(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_39(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_40(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_41(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon - 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_42(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 2 :], digest=None
        )
    return ImageReference(repository=image, tag=None, digest=None)


def x_parse_image_reference__mutmut_43(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=None, tag=None, digest=None)


def x_parse_image_reference__mutmut_44(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(tag=None, digest=None)


def x_parse_image_reference__mutmut_45(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, digest=None)


def x_parse_image_reference__mutmut_46(image: str) -> ImageReference:
    if "@" in image:
        repository, digest = image.split("@", 1)
        return ImageReference(repository=repository, tag=None, digest=digest)
    if _DIGEST_ALGORITHM_MARKER in image:
        index = image.index(_DIGEST_ALGORITHM_MARKER)
        return ImageReference(repository=image[:index], tag=None, digest=image[index + 1 :])
    last_slash = image.rfind("/")
    last_colon = image.rfind(":")
    if last_colon > last_slash:
        return ImageReference(
            repository=image[:last_colon], tag=image[last_colon + 1 :], digest=None
        )
    return ImageReference(repository=image, tag=None, )

mutants_x_parse_image_reference__mutmut['_mutmut_orig'] = x_parse_image_reference__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_1'] = x_parse_image_reference__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_2'] = x_parse_image_reference__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_3'] = x_parse_image_reference__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_4'] = x_parse_image_reference__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_5'] = x_parse_image_reference__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_6'] = x_parse_image_reference__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_7'] = x_parse_image_reference__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_8'] = x_parse_image_reference__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_9'] = x_parse_image_reference__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_10'] = x_parse_image_reference__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_11'] = x_parse_image_reference__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_12'] = x_parse_image_reference__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_13'] = x_parse_image_reference__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_14'] = x_parse_image_reference__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_15'] = x_parse_image_reference__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_16'] = x_parse_image_reference__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_17'] = x_parse_image_reference__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_18'] = x_parse_image_reference__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_19'] = x_parse_image_reference__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_20'] = x_parse_image_reference__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_21'] = x_parse_image_reference__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_22'] = x_parse_image_reference__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_23'] = x_parse_image_reference__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_24'] = x_parse_image_reference__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_25'] = x_parse_image_reference__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_26'] = x_parse_image_reference__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_27'] = x_parse_image_reference__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_28'] = x_parse_image_reference__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_29'] = x_parse_image_reference__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_30'] = x_parse_image_reference__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_31'] = x_parse_image_reference__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_32'] = x_parse_image_reference__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_33'] = x_parse_image_reference__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_34'] = x_parse_image_reference__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_35'] = x_parse_image_reference__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_36'] = x_parse_image_reference__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_37'] = x_parse_image_reference__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_38'] = x_parse_image_reference__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_39'] = x_parse_image_reference__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_40'] = x_parse_image_reference__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_41'] = x_parse_image_reference__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_42'] = x_parse_image_reference__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_43'] = x_parse_image_reference__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_44'] = x_parse_image_reference__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_45'] = x_parse_image_reference__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_image_reference__mutmut['x_parse_image_reference__mutmut_46'] = x_parse_image_reference__mutmut_46 # type: ignore # mutmut generated
mutants_x_is_mutable_tag__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_mutable_tag__mutmut)
def is_mutable_tag(tag: str | None) -> bool:
    return tag is None or tag == "latest"


def x_is_mutable_tag__mutmut_orig(tag: str | None) -> bool:
    return tag is None or tag == "latest"


def x_is_mutable_tag__mutmut_1(tag: str | None) -> bool:
    return tag is None and tag == "latest"


def x_is_mutable_tag__mutmut_2(tag: str | None) -> bool:
    return tag is not None or tag == "latest"


def x_is_mutable_tag__mutmut_3(tag: str | None) -> bool:
    return tag is None or tag != "latest"


def x_is_mutable_tag__mutmut_4(tag: str | None) -> bool:
    return tag is None or tag == "XXlatestXX"


def x_is_mutable_tag__mutmut_5(tag: str | None) -> bool:
    return tag is None or tag == "LATEST"

mutants_x_is_mutable_tag__mutmut['_mutmut_orig'] = x_is_mutable_tag__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_mutable_tag__mutmut['x_is_mutable_tag__mutmut_1'] = x_is_mutable_tag__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_mutable_tag__mutmut['x_is_mutable_tag__mutmut_2'] = x_is_mutable_tag__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_mutable_tag__mutmut['x_is_mutable_tag__mutmut_3'] = x_is_mutable_tag__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_mutable_tag__mutmut['x_is_mutable_tag__mutmut_4'] = x_is_mutable_tag__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_mutable_tag__mutmut['x_is_mutable_tag__mutmut_5'] = x_is_mutable_tag__mutmut_5 # type: ignore # mutmut generated
