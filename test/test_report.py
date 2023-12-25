from src.types import Report


def test__bom():
    report = Report(
        "/Users/dpfrederick/code/tools/nvd-api/bom.json",
        "f8ca11b7-157e-479a-824c-d34dc5b642c4",
    )

    bom = report.bom
    assert bom is not None
