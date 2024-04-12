from typing import Optional
from model.Translation import Translation
from model.Image import Image
from model.PreviewAuthor import PreviewAuthor


class Author(PreviewAuthor):
    about: Optional[Translation]
    image: Optional[Image]
    hidden: Optional[bool]
