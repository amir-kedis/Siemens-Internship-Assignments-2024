import unittest

from src.utils import validate_input_options


class TestValidateInputOptions(unittest.TestCase):
    def test_invalid_logic(self):
        self.assertRaises(ValueError, validate_input_options,
                          ["test"])
        self.assertRaises(ValueError, validate_input_options,
                          ["test", "test"])

    def test_invalid_input(self):
        self.assertRaises(ValueError, validate_input_options,
                          ["$test1", "test2"])

    def test_valid_input(self):
        self.assertTrue(validate_input_options(["testa", "testb"]))
        self.assertTrue(validate_input_options(["testa", "testb", "testc"]))
