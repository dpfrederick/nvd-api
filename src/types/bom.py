from dataclasses import dataclass
from datetime import datetime
from typing import Final, final

from .dependency import Dependency


@dataclass
@final
class Bom:
    timestamp: Final[datetime]
    component_name: Final[str]
    dependencies: Final[list[Dependency]]
