from pydantic import BaseModel


class Error(BaseModel):
    short_message: str
    message: str
    help: str

    class Config:
        orm_mode = True
        allow_mutation = False
