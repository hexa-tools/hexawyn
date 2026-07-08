from __future__ import annotations

from hexawyn.domain.errors import LabelSelectorError


def parse_label_selector(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "selector is empty")

    pairs: list[tuple[str, str]] = []
    for raw_pair in selector.split(","):
        pair = raw_pair.strip()
        if "=" not in pair:
            raise LabelSelectorError(selector, f"missing '=' in pair '{pair}'")

        key, _, value = pair.partition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs
