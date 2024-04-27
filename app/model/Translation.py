from typing import Optional
from pydantic import BaseModel
from enum import Enum


class Translation(BaseModel):
    de: Optional[str]
    en: Optional[str]
    es: Optional[str]


class LanguageOption(Enum):
    de = 'de'
    en = 'en'
    es = 'es'
