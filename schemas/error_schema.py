from pydantic import BaseModel


class ErrorSchema(BaseModel):
    error_msg: str