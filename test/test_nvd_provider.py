from src.nvd_provider import NVDProvider


def test_nvd_provider():
    nvd = NVDProvider("")

    foo = nvd.get_vuln_info_for_cpe("cpe:2.3:o:microsoft:windows_10:1607:*:*:*:*:*:*:*")

    assert foo is not None
