# W1D1 Live Coding: 02-decomposition-example.py

# Professional Decomposition Principles
"""
1. One function = One clear purpose
2. Descriptive names tell the story
3. Functions should be testable independently
4. Parameters make functions flexible
5. Return values enable function chaining
"""

# Example of good decomposition
def calculate_tax(income, tax_rate=0.2):
    """Single purpose: calculate tax"""
    return income * tax_rate

def calculate_net_income(gross_income, tax_rate=0.2):
    """Builds on other functions"""
    tax = calculate_tax(gross_income, tax_rate)
    return gross_income - tax
