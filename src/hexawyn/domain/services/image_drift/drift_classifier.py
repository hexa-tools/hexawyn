from __future__ import annotations

from hexawyn.domain.models.image_drift import DriftType, ImageReference

_DIGEST_ALGORITHM_MARKER = ":sha256:"


def classify_drift(
    running: ImageReference, declared: ImageReference, running_image_id: str | None
) -> DriftType | None:
    running_digest = _effective_digest(running, running_image_id)
    if declared.digest is not None and running_digest is not None:
        return None if running_digest == declared.digest else "digest_mismatch"
    return None if running.tag == declared.tag else "tag_mismatch"


def _effective_digest(ref: ImageReference, image_id: str | None) -> str | None:
    if ref.digest is not None:
        return ref.digest
    return _extract_digest_from_image_id(image_id)


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
