"""Contain General Functions used for handling IO and validation."""

import csv
import re


def save_testacses_to_csv(testcases, options, filename):
    """
    Write the testcases to output csv file.

    Args:
        testcases (list): the testcases that needs to be written
        options (list): server options
        filename (str): the name of the files to write the testcases to
    """
    with open(filename, 'w') as csvfile:
        fieldnames = ["TestCase ID"]
        fieldnames += [f"Master Option For {opt}" for opt in options]
        fieldnames += [f"Client Option For {opt}" for opt in options]
        fieldnames += ["Valid TC"]
        fieldnames += [f"Expected {opt}" for opt in options]

        writer = csv.writer(csvfile)

        writer.writerow(fieldnames)

        rows = []

        for testcase in testcases:
            row = [testcase[0]]
            row += testcase[1].values()
            row += testcase[2].values()
            row.append(testcase[3])
            row += testcase[4].values()

            row = ["NA" if x is None else x for x in row]
            rows.append(row)

        writer.writerows(rows)


def contains_special_characters(str):
    """
    Check if a string has a special character in it.

    Returns:
        True if it has a special character.
    """
    return bool(re.search(r'[^a-zA-Z0-9\s]', str))


def validate_input_options(options):
    """
    Validate the input options.

    Args:
        options (list): list of options as strings

    Raises:
        ValueError
    """
    if len(options) < 2:
        raise ValueError("Options must be more than 1")
    if len(options) != len(set(options)):
        raise ValueError("Options must be unique")
    for option in options:
        if contains_special_characters(option):
            raise ValueError("Options must not include special character")
    return True


def read_input_options(filename):
    """
    Read the input options of the server from a file and validate it.

    Args:
        filename (str): name of the input file.

    Returns:
        list of options or none if there exist an invalid input.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    options = [line.strip() for line in lines]

    try:
        validate_input_options(options)
    except ValueError:
        options = None

    return options
