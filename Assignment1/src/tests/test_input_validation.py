import unittest

from src.utils import validate_input_options


class TestValidateInputOptions(unittest.TestCase):

    def test_invalid_logic_no_input(self):
        self.assertRaises(ValueError, validate_input_options,
                          [])

    def test_invalid_logic_duplicate(self):
        self.assertRaises(ValueError, validate_input_options,
                          ["test", "test"])

    def test_invalid_input(self):
        self.assertRaises(ValueError, validate_input_options,
                          ["$test1", "test2"])

    def test_valid_input_1(self):
        self.assertTrue(validate_input_options(["testa"]))

    def test_valid_input_2(self):
        self.assertTrue(validate_input_options(["testa", "testb"]))

    def test_valid_input_3(self):
        self.assertTrue(validate_input_options(["testa", "testb", "testc"]))
