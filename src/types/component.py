from pydantic import BaseModel, Field

from .vulnerability import Vulnerability


class Component(BaseModel):
    part: str = Field(default="pkg")
    vendor: str = Field(default="npm")
    product: str = Field(required=True, alias="name")
    version: str
    package_url: str = Field(required=True, alias="purl")
    vulnerabilities: list[Vulnerability]

    @property
    def cpe(self) -> str:
        return f"cpe:2.3:{self.part}:{self.vendor}:{self.product}:{self.version}"
