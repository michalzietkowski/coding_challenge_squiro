from pydantic import BaseModel


class InputData(BaseModel):
    prompt: str
    context: str
