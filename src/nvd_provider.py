import json

import requests

from .types import Vulnerability


class NVDProvider:
    def __init__(self, nvd_api_token: str):
        self.nvd_api_token = nvd_api_token
        self.base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    def get_vuln_info_for_cpe(self, cpe: str):
        url = f"{self.base_url}?cpeName={cpe}"
        payload = {}
        headers = {"x-api-key": self.nvd_api_token}

        response = requests.request("GET", url, headers=headers, data=payload)
        return Vulnerability(json.loads(response.text)["vulnerabilities"])
