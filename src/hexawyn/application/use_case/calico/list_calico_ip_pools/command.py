from dataclasses import dataclass


@dataclass(frozen=True)
class ListCalicoIpPoolsCommand:
    """Empty command — Calico IPPools are cluster-scoped."""

    pass
