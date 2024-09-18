from __future__ import annotations

from typing import TYPE_CHECKING, Final

from . import metadata


if TYPE_CHECKING:
    from fastapi import APIRouter


routers_list: Final[tuple[APIRouter]] = (metadata.router,)
