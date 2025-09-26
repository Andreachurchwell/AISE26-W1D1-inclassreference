# W1D1 Breakout 2: Personal Python Toolkit - Example Solution

from typing import Union, List, Tuple, Optional
import datetime

def calculate_compound_interest(
    principal: float, 
    rate: float, 
    time: int, 
    frequency: int = 12
) -> tuple[float, float]:
    """
    Calculate compound interest with industry standards.
    
    Args:
        principal: Initial investment amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Investment period in years
        frequency: Compounding frequency (default monthly)
    
    Returns:
        tuple: (final_amount, interest_earned)
    
    Raises:
        ValueError: If any inputs are negative
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 2)
        (1104.94, 104.94)
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("All inputs must be non-negative")
    
    final_amount = principal * (1 + rate/frequency) ** (frequency * time)
    interest_earned = final_amount - principal
    
    return round(final_amount, 2), round(interest_earned, 2)

def main() -> None:
    """
    Main function to demonstrate the compound interest calculator.
    """
    print("\n--- Compound Interest Calculator ---")
    try:
        final_amount, interest_earned = calculate_compound_interest(1000, 0.05, 2)
        print(f"Initial investment: $1000.00")
        print(f"Annual interest rate: 5%")
        print(f"Investment period: 2 years")
        print(f"Final amount: ${final_amount:.2f}")
        print(f"Interest earned: ${interest_earned:.2f}")

        final_amount_2, interest_earned_2 = calculate_compound_interest(5000, 0.03, 5, 4) # Quarterly compounding
        print(f"\nInitial investment: $5000.00")
        print(f"Annual interest rate: 3%")
        print(f"Investment period: 5 years")
        print(f"Compounding frequency: Quarterly")
        print(f"Final amount: ${final_amount_2:.2f}")
        print(f"Interest earned: ${interest_earned_2:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
