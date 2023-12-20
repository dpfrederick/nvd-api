from pydantic import BaseModel, Field


class Dependency(BaseModel):
    ref: str
    depends_on: list = Field(..., alias="dependsOn")
