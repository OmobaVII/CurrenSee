#!/bin/bash/python3
"""
This module has the currency
converter function
"""
import requests


def convert_currency(amount, base_currency, target_currency):
    """A function that converts the currency based on its exchange rates"""
    api_key = "cur_live_btz3n36rhcueNURyIk1YycbXmpvQEQDAFCXM1bnN"
    url = f"https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies={target_currency}&base_currency={base_currency}"
    response = requests.get(url, timeout=60)

    if response.status_code == 200:
        data = response.json()
        update_at = data["meta"]["last_updated_at"]
        conversion_rate = data["data"][target_currency]["value"]
        converted_currency = amount * conversion_rate
        return converted_currency, update_at
    else:
        return response.status_code