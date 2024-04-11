from typing import Optional
from pydantic import BaseModel


class Translation(BaseModel):
    de: Optional[str]
    en: Optional[str]
    es: Optional[str]
