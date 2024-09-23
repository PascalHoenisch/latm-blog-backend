from pydantic import BaseModel

from model.Image import Image
from model.Translation import Translation
from typing import Optional, List, Union


class Content(BaseModel):
    md: Optional[Translation]
    # the html field is an array of either a Translation Object or a Image Object
    html: List[Union[Translation, Image]]
