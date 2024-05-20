import argparse

from fronius_scraper import data_parser


def main():
    argparser = argparse.ArgumentParser(
        "fronius-parse-json-files",
        description=("Parse scraped JSON files into a usable format."),
    )

    argparser.add_argument(
        "--input-dir",
        "-i",
        default="./",
        type=str,
        # TODO Add info on filename pattern.
        help="Dir in which to search for JSON files to parse (default: %(default)s).",
    )

    argparser.add_argument(
        "--output-dir",
        "-o",
        default="./",
        type=str,
        # TODO Add info on what will be outputted.
        help="Dir to which output will be saved (default: %(default)s).",
    )

    args = argparser.parse_args()

    data_parser.parse_json_data(output_dir=args.output_dir, input_dir=args.input_dir)


if __name__ == "__main__":
    main()
