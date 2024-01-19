import json
from dataclasses import dataclass
from datetime import datetime

from ..nvd.api_provider import APIProvider
from .bom import Bom
from .component import Component
from .dependency import Dependency


@dataclass
class Report:
    def __init__(self, bom_path, nvd_api_token):
        self.nvd_api_token = nvd_api_token
        self.bom_path = bom_path
        self.nvd = APIProvider(nvd_api_token)

    @property
    def bom(self) -> Bom:
        with open(self.bom_path, "r") as bom_file:
            bom_json = json.load(bom_file)

        timestamp = datetime.fromisoformat(bom_json["metadata"]["timestamp"])
        component_name = bom_json["metadata"]["component"]["name"]

        components = [Component(**comp) for comp in bom_json.get("components", [])]
        for comp in components:
            comp.cpe = self.nvd.get_cpe_for_component(comp)
            comp.vulnerabilities = self.nvd.get_vuln_info_for_cpe(comp.cpe)

        dependencies = [Dependency(**dep) for dep in bom_json.get("dependencies", [])]

        return Bom(
            bom_format=bom_json["bomFormat"],
            spec_version=bom_json["specVersion"],
            timestamp=timestamp,
            component_name=component_name,
            components=components,
            dependencies=dependencies,
        )
