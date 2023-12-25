import argparse
import os

from dotenv import load_dotenv

from .types import Report


def main():
    load_dotenv(".env")
    nvd_api_token = os.environ.get("NVD_API_TOKEN")

    parser = argparse.ArgumentParser(
        prog="nvd-api", description="Starter Python CLI", epilog="foobar"
    )
    parser.add_argument(
        "-b",
        "--bom",
        required=True,
        help="The relative path to a bom.json file to ingest.",
    )
    args = parser.parse_args()

    report = Report(args.bom, nvd_api_token)

    print(report.bom)


if __name__ == "__main__":
    main()
