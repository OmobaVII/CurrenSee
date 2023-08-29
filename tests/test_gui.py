#!/bin/usr/python3
"""
This provides the unittest for
gui.py file
"""
import unittest
from unittest.mock import patch
import gui
from tkinter import Tk


class TestGUI(unittest.TestCase):
    """Unnittest for the GUI"""

    def setUp(self):
        """used to setup the test"""
        self.root = Tk()

    def tearDown(self):
        """used to destroy the test"""
        self.root.destroy()

    @patch("gui.convert_currency")
    def test_perform_conversion(self, fake_convert_currency):
        """testing the perform converion function"""
        gui.entry_amount = gui.Entry(self.root)
        gui.dropdown_base_currency = gui.AutocompleteCombobox(self.root)
        gui.dropdown_target_currency = gui.AutocompleteCombobox(self.root)
        gui.label_result = gui.Label(self.root, text="")
        gui.label_date = gui.Label(self.root, text="")

        gui.entry_amount.insert(0, "10")
        gui.dropdown_base_currency.set("USD")
        gui.dropdown_target_currency.set("EUR")

        fake_convert_currency.return_value = (20.0, "2023-08-01T12:00:00Z")

        gui.perform_conversion()

        self.assertEqual(gui.label_result["text"], "20.00 EUR")
    
    def test_amount_entry(self):
        """tests the function amount_entry"""
        gui.entry_amount = gui.Entry(self.root)
        
        gui.entry_amount.insert(0, "Enter Amount")
        gui.amount_entry(None)

        self.assertEqual(gui.entry_amount.get(), "")
        self.assertEqual(gui.entry_amount["foreground"], "black")

    def test_amount_leave(self):
        """tests the function amount_leave"""
        gui.entry_amount = gui.Entry(self.root)
        
        gui.entry_amount.insert(0, "")
        gui.amount_leave(None)

        self.assertEqual(gui.entry_amount.get(), "Enter Amount")
        self.assertEqual(gui.entry_amount["foreground"], "grey")

if __name__ == "__main__":
    unittest.main()