from pydantic import BaseModel


class Translation(BaseModel):
    de: str
    en: str
    es: str
