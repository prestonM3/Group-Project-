from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SystemDocumentationBase(BaseModel):
    title: str
    category: str
    content: str


class SystemDocumentationCreate(SystemDocumentationBase):
    pass


class SystemDocumentationResponse(SystemDocumentationBase):
    id: int
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)

class SystemDocumentationUpdate(BaseModel):
    title: str | None = None
    category: str | None = None
    content: str | None = None