from src.bom_analyzer import BomAnalyzer


def test__bom():
    bom_analyzer = BomAnalyzer(
        "/Users/dpfrederick/code/tools/nvd-api/bom.json", "foobar"
    )

    bom = bom_analyzer.bom
    assert bom is not None
