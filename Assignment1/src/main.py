"""Tests server, client components for a certain set of options."""

import itertools
import csv

from client import Client
from server import Server


def generate_test_cases(options):
    """
    Generate the testcases for given set of options and gets you the expected value and if it's valid or not.

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


if __name__ == "__main__":
    options = ["BufferData", "Timeout"]

    testcases = generate_test_cases(options)

    save_testacses_to_csv(testcases, options, "output.csv")
