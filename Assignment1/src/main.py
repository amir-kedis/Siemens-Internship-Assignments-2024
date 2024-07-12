"""Tests server, client components for a certain set of options."""

import itertools
import os
import sys


from colorama import Fore, init

from client import Client
from server import Server
from utils import read_input_options, save_testacses_to_csv


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


def main(input_filename, output_filename):
    """
    Run the testcase generator for a certain input.

    Args:
        input_filename (str): input file name
        output_filename (str): output file name
    """
    options = read_input_options(input_filename)

    if options is None:
        print("Invalid Input.")
    else:
        testcases = generate_test_cases(options)
        save_testacses_to_csv(testcases, options, output_filename)
        print("output file created successfully")


def run_tests():
    """
    Run the main program against custom already made testcases.

    Testcases are located in tests/inputs directory and output files
    are stored in the tests/output directory.
    """
    init()

    print(Fore.GREEN)
    print("==================================================================")
    print("            RUNNING the program with different inputs             ")
    print("==================================================================")

    input_files = os.listdir("./src/tests/inputs")

    for input_file in input_files:
        print(Fore.MAGENTA)
        print("Running " + input_file)

        print(Fore.GREEN, end="")
        output_file = os.path.splitext(input_file)[0] + "_out.csv"
        main("./src/tests/inputs/" + input_file,
             "./src/tests/outputs/" + output_file)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main("input.txt", "output.csv")
