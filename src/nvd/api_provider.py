import json

import requests

from ..types.component import Component
from ..types.vulnerability import Vulnerability


class APIProvider:
    def __init__(self, nvd_api_token: str):
        self.nvd_api_token = nvd_api_token
        self.base_url = "https://services.nvd.nist.gov/rest/json/"

    def get_cpe_for_component(self, component: Component):
        url = f"{self.base_url}cpes/2.0?cpeMatchString=cpe:2.3:{component.part}:{component.vendor}:{component.product}:{component.version}"
        payload = {}
        headers = {"x-api-key": self.nvd_api_token}

        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != 200:
            raise Exception(
                f"Error finding cpe information for {component.package_url}:\n\tcode: {response.status_code}\n\ttext: {response.text}\n\response headers: {response.headers}"
            )

        return response

    def get_vuln_info_for_cpe(self, cpe: str) -> list[Vulnerability]:
        url = f"{self.base_url}cves/2.0?cpeName={cpe}"
        payload = {}
        headers = {"x-api-key": self.nvd_api_token}

        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != 200:
            raise Exception(
                f"Error getting vulnerability information for {cpe}:\n\tcode: {response.status_code}\n\ttext: {response.text}\n\response headers: {response.headers}"
            )

        vulns: Vulnerability = []

        for i in range(0, 10):
            vulns.append(
                Vulnerability(data=json.loads(response.text)["vulnerabilities"][i])
            )

        return vulns
