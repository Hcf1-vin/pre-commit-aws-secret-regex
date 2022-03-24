from __future__ import annotations

import argparse
import re
from typing import NamedTuple
from typing import Sequence

class BadFile(NamedTuple):
    filename: str
    key: str


def check_file_for_aws_keys(filenames: Sequence[str],keys: set[bytes],) -> list[BadFile]:

    bad_files = []

    for filename in filenames:
        with open(filename, 'rb') as content:
            text_body = content.read()
            for key in keys:
                if re.search(key, text_body):
                    bad_files.append(BadFile(filename, 'aws access key or secret found'))
    return bad_files


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+', help='Filenames to run')

    args = parser.parse_args(argv)

    regex_secrets =[
        '([aA][wW][sS]*.*=\s?[a-zA-Z0-9+/]{20})',
        '([aA][wW][sS]*.*=\s?[a-zA-Z0-9+/]{40})',
    ]

    regex_secrets = {regex_secret.encode() for regex_secret in regex_secrets}

    bad_filenames = check_file_for_aws_keys(args.filenames, regex_secrets)
    if bad_filenames:
        for bad_file in bad_filenames:
            print(f'AWS secret found in {bad_file.filename}: {bad_file.key}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
