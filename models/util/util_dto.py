from pydantic import BaseModel


class OutputTotalCount(BaseModel):
    count: int
