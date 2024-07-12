"""Tests server, client components for a certain set of options."""

import itertools

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


if __name__ == "__main__":
    options = ["BufferData", "Timeout"]
    testcases = generate_test_cases(options)

    for testcase in testcases:
        print(testcase)

    # server = Server(options)
    # master_client = Client(server, is_master=True)
    # slave_client = Client(server)
    # print(server.get_options())
    # for i in testcases:
    #     print(i)
    # print(len(testcases))
    # print(server.get_options())
