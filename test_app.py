import unittest
from app import converter


class TestConversion(unittest.TestCase):
    def test_converter(self):
        input_str = "3000 INR to USD".split(" ")
        result = converter(input_str)
        self.assertAlmostEqual(result, 36.13, delta=1)

    def test_converter_for_unsupported_currency(self):
        input_str = "3000 INR to qwe".split(" ")
        result = converter(input_str)
        self.assertEqual(result, "Unsupported Currency")

    def test_converted_for_malformed_query(self):
        input_str = "3000 INR farzi".split(" ")
        result = converter(input_str)
        self.assertEqual(
            result, "Malformed Query. e.g. query \n/convert 3000 inr to usd"
        )
