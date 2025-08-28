"""
Implement a function to check whether a given string is a valid mathematical expression (only digits, + ,- ,* , / , and parentheses) and whether the parentheses are balanced.
"""


def valid_expression(n: str):
    valid_string = "0123456789+-*/()"
    if n not in valid_string:
        print("Invalid input")
