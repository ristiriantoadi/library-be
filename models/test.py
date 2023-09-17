from pydantic import BaseModel


class TestInput(BaseModel):
    something: str
