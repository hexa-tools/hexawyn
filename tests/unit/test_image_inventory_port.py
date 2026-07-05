from __future__ import annotations

from abc import ABC

import pytest


class TestImageInventoryPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort

        assert issubclass(ImageInventoryPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort

        with pytest.raises(TypeError):
            ImageInventoryPort()  # type: ignore[abstract]
