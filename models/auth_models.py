from __future__ import annotations

from pydantic import BaseModel


class AuthModel(BaseModel):
    token: str
