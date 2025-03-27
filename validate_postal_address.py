"""
This module solves the validation of postal address task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import re

# Regex pattern explanation:
# ^        - Start of the string
# \d{4}   - Exactly four digits (postal code)
#  [ ]     - A single space
# [A-ZÆØÅ ]+ - One or more uppercase letters (A-Z, ÆØÅ) and spaces (place name)
# $        - End of the string
POSTAL_ADDRESS_PATTERN = r"^\d{4} [A-ZÆØÅ ]+$"


def validate_postal_address(postal_address: str) -> bool:
    """
    Validates a postal address based on the given pattern.

    Args:
        address: The postal address to validate

    Returns:
            bool: True if the address is valid, False otherwise
    """
    return bool(re.fullmatch(POSTAL_ADDRESS_PATTERN, postal_address))


# Test data
postal_addresses = [
    "1234 OSLO",  # Valid
    "5678 BERGEN",  # Valid
    "123 OSLO",  # Invalid (postal code does not have four digits)
    "12345 OSLO",  # Invalid (postal code has more than four digits)
    "1234 oslo",  # Invalid (place name is not in uppercase)
    "OSLO 1234",  # Invalid (place name comes before postal code)
    "1234 OSLO S",  # Valid (place name with space)
    "1234 OSLO SØR",  # Valid (place name with space and special characters)
]

# Test execution
for address in postal_addresses:
    if validate_postal_address(address):
        print(f"'{address}' is a valid postal address.")
    else:
        print(f"'{address}' is an invalid postal address.")
