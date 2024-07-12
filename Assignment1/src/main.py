"""Tests server, client components for a certain set of options."""

import itertools
import csv
import re

from client import Client
from server import Server


def generate_test_cases(options):
    """
    Generate testcases for given set of options with expected values.

    Args:
        options (list): list of strings of options
    """
    testcases = []
    testcase_id = 1

    input_combinatinos = list(itertools.product(
        [True, False, None], repeat=len(options)*2))

    for config in input_combinatinos:
        server = Server(options)
        master_client = Client(server, is_master=True)
        slave_client = Client(server)

        master_options = dict(zip(options, config[0:len(options)]))
        slave_options = dict(
            zip(options, config[len(options):len(options)*2]))

        master_client.configure_server(master_options)
        result = slave_client.configure_server(slave_options)

        valid_testcase = "YES" if "Error" not in result else "NO"

        expected_options = {}

        # NOTE: here I assumed that if the testcase is invalid
        #       the expected options should be none
        if valid_testcase == "YES":
            expected_options = server.get_options()
        else:
            expected_options = {option: None for option in options}

        testcases.append([
            testcase_id,
            master_options,
            slave_options,
            valid_testcase,
            expected_options
        ])

        testcase_id += 1

    return testcases


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

    if len(options) < 2:
        return None
    if len(options) != len(set(options)):
        return None
    for option in options:
        if contains_special_characters(option):
            return None

    return options


if __name__ == "__main__":
    options = read_input_options("input.txt")

    if options is None:
        print("Please check the input")
    else:
        testcases = generate_test_cases(options)
        save_testacses_to_csv(testcases, options, "output.csv")
