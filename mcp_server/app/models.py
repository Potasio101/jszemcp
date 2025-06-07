from pydantic import BaseModel

class Device(BaseModel):
    id: int | None = None
    name: str
    status: str | None = None
