import json
from dataclasses import dataclass
from datetime import datetime

from .types import Bom, Dependency


@dataclass
class BomAnalyzer:
    def __init__(self, bom_path, nvd_api_token):
        self.nvd_api_token = nvd_api_token
        self.bom_path = bom_path

    @property
    def bom(self) -> Bom:
        with open(self.bom_path, "r") as bom_file:
            bom_json = json.load(bom_file)

        timestamp = datetime.fromisoformat(bom_json["metadata"]["timestamp"])
        component_name = bom_json["metadata"]["component"]["name"]
        dependencies = [Dependency(**dep) for dep in bom_json.get("dependencies", [])]

        return Bom(timestamp, component_name, dependencies)
