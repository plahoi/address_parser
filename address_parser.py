import re
import json
import typing
import argparse
import constants


"""
Assumptions: 
 - Street numbers can't be negative
 - We can't rely on commas to separate street and number 
    because there are a lot street names with commas in the middle
 - There are no addreses with range of house numbers like "31 - 32"
"""


def pprint(*args, **kwargs):
    print(constants.DATETIME_LOG_STR, *args, **kwargs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-s',
        type=str,
        help='String of address'
    )

    args = parser.parse_args()

    return args


def splitter(address_str: str) -> typing.List[str]:
    # remove special characters and signs like in "Calle Aduana, 29" or "Boulevard Porfirio Díaz #58"
    address_str = re.sub(constants.SPECIAL_CHARACTERS_TO_AVOID, constants.ADDRESS_SEP, address_str)
    # Split address line to separate chunks
    return [address_part.strip() for address_part in address_str.split()]


def has_num(var: str) -> bool:
    """
    Check whether the provided variable contains digits or not
    :return: True if value contains digits

    Example: has_num("123B") -> True, has_num("Boulevard") -> False
    """
    return any(i.isdigit() for i in var)


def construct_json(street: str, house_number: str) -> str:
    return json.dumps(
        {
            constants.STREET: street,
            constants.HOUSE_NUMBER: house_number
        }
    )


def extract_parts(address_str) -> typing.Tuple[str, str]:
    """
    3 different approaches to extract the corresponding address components.\
    They are evaluated one at a time. When the parser matches with one of the cases for the input address line,
    it's not necessary to continue with others.

    :param: address_str -> The given address string

    1. Regex for No/nr notion
    2. Checking for the trailing house number
    3. Checking for the leading house number
    4. Checking for the house number in between the characters

    """
    splitted_address = splitter(address_str)

    # Cases with No/Nr/№ are handled differently
    match = re.match(constants.PATTERN_NONR, address_str)
    if match is not None:
        street = match.group(constants.STREET)
        house_number = match.group(constants.HOUSE_NUMBER)
        return street, house_number
    elif has_num(splitted_address[-1]):  # if the number in the end
        house_number = splitted_address[-1]
        street = constants.ADDRESS_SEP.join(splitted_address[:-1])
        return street, house_number
    elif has_num(splitted_address[0]):  # if the number in the beginning
        house_number = splitted_address[0]
        street = constants.ADDRESS_SEP.join(splitted_address[1:])
        return street, house_number

    # if the number is not on the ends, then let's check in reverse until the number is found
    for ix in reversed(range(len(splitted_address))):
        part = constants.ADDRESS_SEP.join(splitted_address[ix:])
        if not has_num(part):
            continue
        house_number = part
        street = constants.ADDRESS_SEP.join(splitted_address[:ix])
        return street, house_number

    return constants.NOT_AVAILABLE_VALUE, constants.NOT_AVAILABLE_VALUE


def parse(address_str):
    street, house_number = extract_parts(address_str)
    return construct_json(street, house_number)
