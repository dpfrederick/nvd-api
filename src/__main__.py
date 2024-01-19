import argparse
import os

from dotenv import load_dotenv

# from . import NVDProvider
from .types.report import Report

# def create_report(cpe: str):
#     nvd_provider = NVDProvider(os.environ.get("NVD_API_TOKEN"))
#     vulns = nvd_provider.get_vuln_info_for_cpe(cpe)
#     print(vulns[0])


def main():
    load_dotenv(".env")
    nvd_api_token = os.environ.get("NVD_API_KEY")

    parser = argparse.ArgumentParser(
        description="A CLI tool for analyzing dependencies or creating reports."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-b", "--bom", type=str, help="Path to the BOM file for dependency analysis."
    )
    group.add_argument(
        "-c", "--cpe", type=str, help="CPE for which to create a report."
    )

    args = parser.parse_args()

    if args.bom:
        if os.path.exists(args.bom):
            report = Report(args.bom, nvd_api_token)
            print(report.bom)
        else:
            print(f"Error: BOM file not found at {args.bom}")

    elif args.cpe:
        create_report(args.cpe)


if __name__ == "__main__":
    main()
