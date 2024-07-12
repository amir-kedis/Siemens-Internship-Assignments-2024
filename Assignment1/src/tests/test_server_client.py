import unittest

from src.server import Server
from src.client import Client


class TestServerClientFunctionality(unittest.TestCase):

    def test_master_none_client_none(self):
        server = Server(["BufferData", "TimeOut"])
        master_client = Client(server, is_master=True)
        slave_client = Client(server)

        master_client.configure_server({"BufferData": None, "TimeOut": None})
        result = slave_client.configure_server(
            {"BufferData": None, "TimeOut": None})

        self.assertEqual(result, "Server configured successfully")
        self.assertEqual(server.get_options(), {
                         "BufferData": True, "TimeOut": True})

    def test_master_True_slave_none(self):
        server = Server(["BufferData", "TimeOut"])
        master_client = Client(server, is_master=True)
        slave_client = Client(server)

        master_client.configure_server({"BufferData": True, "TimeOut": True})
        result = slave_client.configure_server(
            {"BufferData": None, "TimeOut": None})

        self.assertEqual(result, "Server configured successfully")
        self.assertEqual(server.get_options(), {
                         "BufferData": True, "TimeOut": True})

    def test_master_none_slave_True(self):
        server = Server(["BufferData", "TimeOut"])
        master_client = Client(server, is_master=True)
        slave_client = Client(server)

        master_client.configure_server({"BufferData": None, "TimeOut": None})
        result = slave_client.configure_server(
            {"BufferData": True, "TimeOut": True})

        self.assertEqual(result, "Server configured successfully")
        self.assertEqual(server.get_options(), {
                         "BufferData": True, "TimeOut": True})

    def test_master_True_slave_False(self):
        server = Server(["BufferData", "TimeOut"])
        master_client = Client(server, is_master=True)
        slave_client = Client(server)

        master_client.configure_server({"BufferData": True, "TimeOut": True})
        result = slave_client.configure_server(
            {"BufferData": False, "TimeOut": True})

        self.assertEqual(result, "Error: Cannot change BufferData")

    def test_master_mixed_slave_follows(self):
        server = Server(["BufferData", "TimeOut"])
        master_client = Client(server, is_master=True)
        slave_client = Client(server)

        master_client.configure_server({"BufferData": True, "TimeOut": False})
        result = slave_client.configure_server(
            {"BufferData": None, "TimeOut": False})

        self.assertEqual(result, "Server configured successfully")
        self.assertEqual(server.get_options(), {
                         "BufferData": True, "TimeOut": False})
