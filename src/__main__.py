import argparse
import os

from dotenv import load_dotenv


def main():
    load_dotenv(".env")
    nvd_api_token = os.environ.get("NVD_API_TOKEN")

    parser = argparse.ArgumentParser(
        prog="nvd-api", description="Starter Python CLI", epilog="foobar"
    )
    parser.add_argument("-b", "--bom", help="The path to the bom.json file to parse.")
    args = parser.parse_args()

    bom_analyzer = BomAnalyzer(args.bom, nvd_api_token)


if __name__ == "__main__":
    main()
