from src.nvd.api_provider import APIProvider


def test__nvd_provider():
    nvd = APIProvider("")

    cpes = [
        "cpe:2.3:o:microsoft:windows_10:1607:*:*:*:*:*:*:*",
        "cpe:2.3:pkg:npm:graphql.web:1.0.4:*:*:*:*:*:*:*",
    ]

    for cpe in cpes:
        foo = nvd.get_vuln_info_for_cpe(cpe)

        assert foo is not None
