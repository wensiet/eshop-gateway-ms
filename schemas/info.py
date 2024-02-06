from pydantic import BaseModel


class InfoResponse(BaseModel):
    message: str
