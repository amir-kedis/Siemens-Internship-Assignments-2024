import itertools

from client import Client
from server import Server


def generate_test_cases(options):
    input_combinatinos = list(itertools.product(
        [True, False, None], repeat=len(options)*2))
    return input_combinatinos


if __name__ == "__main__":
    options = ["BufferData", "Timeout"]
    testcases = generate_test_cases(options)
    server = Server(options)
    master_client = Client(server, is_master=True)
    slave_client = Client(server)
    print(master_client.configure_server(
        {"BufferData": None, "Timeout": None}))
    print(slave_client.configure_server(
        {"BufferData": False, "Timeout": True}))
    print(server.get_options())
    # for i in testcases:
    #     print(i)
    # print(len(testcases))
    # print(server.get_options())
