from pydantic import BaseModel
from typing import Union

class ModelTestRequest(BaseModel):
    text: Union[str, None] = None