# W1D1 Breakout 2: Personal Python Toolkit - Starter Template

## Overview
**Time:** 20 minutes  
**Goal:** Create a personalized Python toolkit with 3+ functions that solve real problems in your daily life

## Your Mission
Transform repetitive calculations or decision-making processes from your daily routine into reusable Python functions. Think about what you calculate on paper, in your head, or wish you had a quick tool for!

## Instructions

### Step 1: Brainstorm (3 minutes)
Think about calculations you do regularly:
- **Fitness:** BMI, protein needs, running pace, workout splits
- **Finance:** Bill splitting, investment growth, loan payments
- **Academic:** Grade needed on final exam, study hours per credit
- **Food:** Recipe scaling, meal prep portions, nutrition tracking
- **Time:** Commute optimization, meeting scheduler, timezone converter
- **Hobbies:** Gaming statistics, crafting materials, collection value

### Step 2: Build Your Functions (12 minutes)
1. Replace the `your_function_1/2/3` placeholders with meaningful names
2. Write clear docstrings explaining:
   - What problem it solves
   - Parameters needed
   - What it returns
3. Keep functions focused - each should do ONE thing well
4. Add input validation if time permits

### Step 3: Test & Demonstrate (5 minutes)
1. Update the `main()` function to showcase each function
2. Use realistic examples
3. Format output clearly
4. Be ready to share one function with the group!

## Example Functions to Inspire You

```python
def calculate_grade_needed(current_grade, target_grade, final_weight):
    """
    Calculate grade needed on final exam to achieve target grade
    
    Args:
        current_grade: Current grade percentage (0-100)
        target_grade: Desired final grade (0-100)  
        final_weight: Weight of final exam as decimal (e.g., 0.3 for 30%)
    
    Returns:
        float: Grade needed on final exam
    """
    grade_needed = (target_grade - current_grade * (1 - final_weight)) / final_weight
    return min(grade_needed, 100)  # Can't score above 100%


def split_bill_with_tip(total, people, tip_percent=20):
    """
    Calculate bill split including tip
    
    Args:
        total: Bill total before tip
        people: Number of people splitting
        tip_percent: Tip percentage (default 20%)
    
    Returns:
        tuple: (per_person_amount, total_with_tip)
    """
    tip_amount = total * (tip_percent / 100)
    total_with_tip = total + tip_amount
    per_person = total_with_tip / people
    return per_person, total_with_tip


def workout_pace_calculator(distance_miles, time_minutes):
    """
    Calculate running/cycling pace
    
    Args:
        distance_miles: Distance covered in miles
        time_minutes: Total time in minutes
    
    Returns:
        str: Pace in MM:SS per mile format
    """
    pace = time_minutes / distance_miles
    minutes = int(pace)
    seconds = int((pace - minutes) * 60)
    return f"{minutes}:{seconds:02d} per mile"
```

## Tips for Success
- **Start simple:** Get a basic version working first, then enhance
- **Use meaningful names:** `calculate_macros()` not `func1()`
- **Think about edge cases:** What if someone enters 0 or negative values?
- **Make it personal:** The best functions solve YOUR actual problems
- **Comments help:** Add brief comments for complex calculations

## Sharing Format
When we reconvene, be ready to share:
1. **Function name & purpose** (15 seconds)
2. **Problem it solves** (15 seconds)
3. **Quick demo** (30 seconds)