from typing import Optional, Any
from pydantic import BaseModel
from enum import Enum



class LanguageOption(Enum):
    de = 'de'
    en = 'en'
    es = 'es'


class Translation(BaseModel):
    de: Optional[str]
    en: Optional[str]
    es: Optional[str]

    def __getitem__(self, key: LanguageOption) -> Any:
        return getattr(self, key)

    def __setitem__(self, key: LanguageOption, value: Any) -> None:
        setattr(self, key, value)
