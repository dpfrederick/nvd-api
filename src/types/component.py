from typing import Iterable, Optional

from pydantic import BaseModel, Field

from .vulnerability import Vulnerability


class Component(BaseModel):
    part: str = Field(default="pkg")
    vendor: str = Field(default="npm")
    product: str = Field(alias="name")
    version: str
    package_url: str = Field(alias="purl")
    vulnerabilities: Optional[Iterable[Vulnerability]] = None
    cpe: str = Field(default=None)

    # @property
    # def cpe(self) -> str:
    #     return f"cpe:2.3:{self.part}:{self.vendor}:{self.product}:{self.version}"

    # TODO: Add validation
    # @cpe.setter
    # def cpe(self, value: str):
    #     parts = value.split(":")
    #     self.part = parts[3]
    #     self.vendor = parts[4]
    #     self.product = parts[5]
    #     self.version = parts[6]
