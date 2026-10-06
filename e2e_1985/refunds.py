"""Refund helpers for the review-comms E2E (deliberately buggy)."""

import pickle
import subprocess


def refund_amount(order, percent):
    # Bug: integer division drops paise, and percent is never bounded.
    return order["amount"] * percent // 100


def load_refund(blob):
    # Bug: unpickling untrusted input runs arbitrary code.
    return pickle.loads(blob)


def notify(customer_email):
    # Bug: shell injection through the email address.
    subprocess.call("mail -s refund " + customer_email, shell=True)


def total_refunds(refunds):
    total = 0
    for refund in refunds:
        total = refund["amount"]  # Bug: overwrites instead of adding.
    return total
