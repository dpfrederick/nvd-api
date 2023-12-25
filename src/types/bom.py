from datetime import datetime

from pydantic import BaseModel

from .component import Component
from .dependency import Dependency


class Bom(BaseModel):
    bom_format: str
    spec_version: str
    timestamp: datetime
    component_name: str
    components: list[Component]
    dependencies: list[Dependency]

    def __str__(self):
        return f"timestamp: {self.timestamp},\nproject name: {self.component_name},\nnumber of dependencies={self.dependencies.count})"
