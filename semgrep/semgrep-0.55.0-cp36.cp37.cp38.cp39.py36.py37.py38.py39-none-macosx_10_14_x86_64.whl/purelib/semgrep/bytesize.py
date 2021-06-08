#
# Parse command-line arguments representing a number of bytes, such as
# '5 mb' or '3.2GiB'.
#
# Maybe we could use an external package for this, such as
# https://pypi.org/project/datasize/ (documentation?)
# or https://github.com/xolox/python-humanfriendly
#
import re

UNITS = {
    "": 1,
    "B": 1,
    "KIB": 2 ** 10,
    "MIB": 2 ** 20,
    "GIB": 2 ** 30,
    "TIB": 2 ** 40,
    "KB": 10 ** 3,
    "MB": 10 ** 6,
    "GB": 10 ** 9,
    "TB": 10 ** 12,
}


def parse_size(input: str) -> int:
    s = input.upper()
    # note that '1e6' is a valid float and should not become '1 e6'.
    s = re.sub(r"([BKMGT][A-Z]*)", r" \1", s)
    tokens = [sub.strip() for sub in s.split()]
    n = len(tokens)
    if n == 1:
        number = tokens[0]
        unit = ""
    elif n == 2:
        number, unit = tokens
    else:
        raise ValueError(f"Invalid representation for a number of bytes: '{input}'")
    if unit in UNITS:
        return int(float(number) * UNITS[unit])
    else:
        raise ValueError(f"Invalid representation for a number of bytes: '{input}'")
