from __future__ import annotations

from hexawyn.domain.models.image_drift import ImageReference

_DIGEST_ALGORITHM_MARKER = ":sha256:"


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


def is_mutable_tag(tag: str | None) -> bool:
    return tag is None or tag == "latest"
