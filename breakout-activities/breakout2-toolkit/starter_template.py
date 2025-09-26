# W1D1 Breakout 2: Personal Python Toolkit - Starter Template

"""
Breakout 2: Personal Python Toolkit
Time: 20 minutes
Goal: Create 3+ useful functions for your daily life

Ideas:
- Fitness: Calculate calories, track workouts, pace calculations
- Finance: Tip calculator, budget tracker, savings estimator  
- Academic: GPA calculator, study time planner, deadline tracker
- Productivity: Pomodoro timer math, task prioritizer
- Hobbies: Game score tracker, recipe converter, collection organizer
"""

import datetime

def professional_header():
    """Every toolkit needs proper documentation"""
    return f"""
    ================================
    Personal Python Toolkit
    Author: [Your Name]
    Created: {datetime.date.today()}
    Purpose: Automate daily calculations
    ================================
    """

# Example starter function
def calculate_coffee_budget(cups_per_day, price_per_cup, days=30):
    """
    Calculate monthly coffee spending and potential savings
    
    Args:
        cups_per_day: Average daily coffee consumption
        price_per_cup: Cost per cup (in dollars)
        days: Number of days to calculate (default 30)
    
    Returns:
        tuple: (total_cost, homemade_savings)
    """
    total_cost = cups_per_day * price_per_cup * days
    homemade_cost = cups_per_day * 0.50 * days  # Assume $0.50 at home
    savings = total_cost - homemade_cost
    
    return total_cost, savings

# TODO: Create 3 more functions that solve YOUR problems

def your_function_1():
    """What problem does this solve?"""
    pass

def your_function_2():
    """What calculation do you do repeatedly?"""
    pass

def your_function_3():
    """What would make your life easier?"""
    pass

def main():
    """Demonstrate all toolkit functions"""
    print(professional_header())
    
    # Example usage
    cost, saved = calculate_coffee_budget(2, 4.50)
    print(f"Monthly coffee cost: ${cost:.2f}")
    print(f"Potential savings: ${saved:.2f}")
    
    # TODO: Demonstrate your functions
    
if __name__ == "__main__":
    main()
