import argparse
import os

from dotenv import load_dotenv


def main():
    load_dotenv(".env")
    foo = os.environ.get("FOO")
    parser = argparse.ArgumentParser(description="Starter Python CLI")
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()

    print(f"Hello {args.name}! The value of FOO is {foo}")


if __name__ == "__main__":
    main()
