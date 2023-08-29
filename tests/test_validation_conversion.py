#!/bin/usr/python3
"""
This provides the unittest for
validation_converison module
"""
import unittest
from unittest.mock import patch
from validation_conversion import validate_input


class TestValidationInput(unittest.TestCase):
    """the tests for the validation of inputs"""
    def test_validate_input(self):
        """tests the validate_input function"""
        self.assertEqual(validate_input("10.6"), None)
        self.assertEqual(validate_input("10"), None)
        self.assertEqual(validate_input(" 106 "), None)
        self.assertEqual(validate_input("99999999"), None)

    def test_validate_string_input(self):
        """tests wrong input"""
        self.assertEqual(validate_input("thanks"), "Amount must be a valid number")
        self.assertEqual(validate_input("USD"), "Amount must be a valid number")
        self.assertEqual(validate_input("10 89"), "Amount must be a valid number")

    def test_validate_dic_input(self):
        """tests if input is a dictionary"""
        self.assertEqual(validate_input({'sex': 'male'}), "Amount must be a valid number")
        self.assertEqual(validate_input({'value': '10'}), "Amount must be a valid number")

    def test_validate_list_input(self):
        """test if input is a list"""
        self.assertEqual(validate_input([10, 5]), "Amount must be a valid number")
        self.assertEqual(validate_input(["10", "5"]), "Amount must be a valid number")
        self.assertEqual(validate_input(["boy", "5"]), "Amount must be a valid number")
        self.assertEqual(validate_input(["girl", "boy"]), "Amount must be a valid number")

    def test_validate_number_lt_zero(self):
        """test if input is less than zero"""
        self.assertEqual(validate_input(-78), "Amount must be a positive number")
        self.assertEqual(validate_input(-78 ), "Amount must be a positive number")
        self.assertEqual(validate_input(-2.56), "Amount must be a positive number")
        self.assertEqual(validate_input(-0.64), "Amount must be a positive number")


if __name__ == "__main__":
    unittest.main()
