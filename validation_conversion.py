#!/usr/bin/python3
"""
This module holds the functions that
validates the inputs
"""


def validate_input(amount_str):
    """Validates user input"""
    try:
        amount = float(amount_str)
        if amount <= 0:
            text = "Amount must be a positive number"
        else:
            text = None
    except (ValueError, TypeError):
        text = "Amount must be a valid number"
        return text
    return text
currency_values = ("AED", "AFN", "ALL", "AMD", "ANG", "AOA",
                   "ARS", "AUD", "AWG", "AZN", "BAM", "BBD",
                   "BDT", "BHD", "BIF", "BMD", "BND", "BOB",
                   "BRL", "BSD", "BTC", "BTN", "BWP", "BYN",
                   "BYR", "BZD", "CAD", "CDF", "CHF", "CLF",
                   "CLP", "CNY", "COP", "CRC", "CUC", "CUP",
                   "CVE", "CZK", "DJF", "DKK", "DOP", "DZD",
                   "EGP", "ETB", "EUR", "FJD", "GBP", "GEL",
                   "GHS", "GMD", "GNF", "GTQ", "GYD", "HKD",
                   "HNL", "HRK", "HTG", "HUF", "IDR", "ILS",
                   "INR", "IQD", "IRR", "ISK", "JMD", "JOD",
                   "JPY", "KES", "KGS", "KHR", "KMF", "KRW",
                   "KWD", "KYD", "KZT", "LAK", "LBP", "LKR",
                   "LRD", "LSL", "LTL", "LVL", "LYD", "MAD",
                   "MDL", "MGA", "MKD", "MMK", "MOP", "MRO",
                   "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
                   "NAD", "NGN", "NIO", "NOK", "NPR", "NZD",
                   "OMR", "PAB", "PEN", "PGK", "PHP", "PKR",
                   "PLN", "PYG", "QAR", "RON", "RSD", "RUB",
                   "RWF", "SAR", "SBD", "SCR", "SDG", "SEK",
                   "SGD", "SHP", "SLL", "SOS", "SRD", "STD",
                   "SVC", "SZL", "THB", "TJS", "TMT", "TND",
                   "TOP", "TRY", "TTD", "TWD", "TZS", "UAH",
                   "UGX", "USD", "UYU", "UZS", "VND", "XAF",
                   "XCD", "XDR", "XOF", "XPF", "YER", "ZAR",
                   "ZMK", "ZMW", "ZWL")