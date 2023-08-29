#!/bin/usr/python3
"""
This provides the unittest for
currency_convert.py file
"""
import unittest
from unittest.mock import patch
from currency_convert import convert_currency


class TestCurrencyConverter(unittest.TestCase):
    """Unittest for currency converter logic"""
    @patch("currency_convert.requests.get")
    def test_convert_currency_success(self, test_get):
        """test the convert_currency function"""
        test_response = test_get.return_value
        test_response.status_code = 200
        test_response.json.return_value = {
            "meta": {
                "last_updated_at": "2023-08-01T12:00:00Z"
            },
            "data": {
                "USD": {
                    "value": 0.9
                }
            }
        }
        
        result = convert_currency(10, "EUR", "USD")
        self.assertEqual(result[0], 9.0)
        self.assertEqual(result[1], "2023-08-01T12:00:00Z")

    @patch("currency_convert.requests.get")
    def test_convert_currency_failure(self, test_get):
        """test if the convert_currency function fails"""
        test_response = test_get.return_value
        test_response.status_code = 404
        
        result = convert_currency(10, "EUR", "USD")
        self.assertEqual(result, 404)

if __name__ == "__main__":
    unittest.main()