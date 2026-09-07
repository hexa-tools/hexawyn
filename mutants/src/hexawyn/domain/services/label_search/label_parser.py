from __future__ import annotations

from hexawyn.domain.errors import LabelSelectorError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_parse_label_selector__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_label_selector__mutmut)
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


def x_parse_label_selector__mutmut_orig(selector: str) -> list[tuple[str, str]]:
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


def x_parse_label_selector__mutmut_1(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if selector.strip():
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


def x_parse_label_selector__mutmut_2(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(None, "selector is empty")

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


def x_parse_label_selector__mutmut_3(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, None)

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


def x_parse_label_selector__mutmut_4(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError("selector is empty")

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


def x_parse_label_selector__mutmut_5(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, )

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


def x_parse_label_selector__mutmut_6(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "XXselector is emptyXX")

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


def x_parse_label_selector__mutmut_7(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "SELECTOR IS EMPTY")

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


def x_parse_label_selector__mutmut_8(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "selector is empty")

    pairs: list[tuple[str, str]] = None
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


def x_parse_label_selector__mutmut_9(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "selector is empty")

    pairs: list[tuple[str, str]] = []
    for raw_pair in selector.split(None):
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


def x_parse_label_selector__mutmut_10(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "selector is empty")

    pairs: list[tuple[str, str]] = []
    for raw_pair in selector.split("XX,XX"):
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


def x_parse_label_selector__mutmut_11(selector: str) -> list[tuple[str, str]]:
    """Parses a K8s-style label selector ("app=payment,env=production") into
    key/value pairs. Splits each pair on the *first* '=' only — label values
    never contain '=' in Kubernetes, and keys may contain exactly one '/'
    (domain-prefixed keys, e.g. "app.kubernetes.io/name").
    """
    if not selector.strip():
        raise LabelSelectorError(selector, "selector is empty")

    pairs: list[tuple[str, str]] = []
    for raw_pair in selector.split(","):
        pair = None
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


def x_parse_label_selector__mutmut_12(selector: str) -> list[tuple[str, str]]:
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
        if "XX=XX" not in pair:
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


def x_parse_label_selector__mutmut_13(selector: str) -> list[tuple[str, str]]:
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
        if "=" in pair:
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


def x_parse_label_selector__mutmut_14(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(None, f"missing '=' in pair '{pair}'")

        key, _, value = pair.partition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_15(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(selector, None)

        key, _, value = pair.partition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_16(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(f"missing '=' in pair '{pair}'")

        key, _, value = pair.partition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_17(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(selector, )

        key, _, value = pair.partition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_18(selector: str) -> list[tuple[str, str]]:
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

        key, _, value = None
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_19(selector: str) -> list[tuple[str, str]]:
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

        key, _, value = pair.partition(None)
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_20(selector: str) -> list[tuple[str, str]]:
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

        key, _, value = pair.rpartition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_21(selector: str) -> list[tuple[str, str]]:
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

        key, _, value = pair.partition("XX=XX")
        key = key.strip()
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_22(selector: str) -> list[tuple[str, str]]:
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
        key = None
        value = value.strip()
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_23(selector: str) -> list[tuple[str, str]]:
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
        value = None
        if not key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_24(selector: str) -> list[tuple[str, str]]:
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
        if key:
            raise LabelSelectorError(selector, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_25(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(None, f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_26(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(selector, None)
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_27(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(f"empty key in pair '{pair}'")
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_28(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(selector, )
        if not value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_29(selector: str) -> list[tuple[str, str]]:
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
        if value:
            raise LabelSelectorError(selector, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_30(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(None, f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_31(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(selector, None)

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_32(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(f"empty value in pair '{pair}'")

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_33(selector: str) -> list[tuple[str, str]]:
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
            raise LabelSelectorError(selector, )

        pairs.append((key, value))

    return pairs


def x_parse_label_selector__mutmut_34(selector: str) -> list[tuple[str, str]]:
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

        pairs.append(None)

    return pairs

mutants_x_parse_label_selector__mutmut['_mutmut_orig'] = x_parse_label_selector__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_1'] = x_parse_label_selector__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_2'] = x_parse_label_selector__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_3'] = x_parse_label_selector__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_4'] = x_parse_label_selector__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_5'] = x_parse_label_selector__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_6'] = x_parse_label_selector__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_7'] = x_parse_label_selector__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_8'] = x_parse_label_selector__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_9'] = x_parse_label_selector__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_10'] = x_parse_label_selector__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_11'] = x_parse_label_selector__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_12'] = x_parse_label_selector__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_13'] = x_parse_label_selector__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_14'] = x_parse_label_selector__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_15'] = x_parse_label_selector__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_16'] = x_parse_label_selector__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_17'] = x_parse_label_selector__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_18'] = x_parse_label_selector__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_19'] = x_parse_label_selector__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_20'] = x_parse_label_selector__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_21'] = x_parse_label_selector__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_22'] = x_parse_label_selector__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_23'] = x_parse_label_selector__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_24'] = x_parse_label_selector__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_25'] = x_parse_label_selector__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_26'] = x_parse_label_selector__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_27'] = x_parse_label_selector__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_28'] = x_parse_label_selector__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_29'] = x_parse_label_selector__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_30'] = x_parse_label_selector__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_31'] = x_parse_label_selector__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_32'] = x_parse_label_selector__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_33'] = x_parse_label_selector__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_label_selector__mutmut['x_parse_label_selector__mutmut_34'] = x_parse_label_selector__mutmut_34 # type: ignore # mutmut generated
