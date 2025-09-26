# W1D1 Live Coding: 03-functions-solution.py

# Functions as Building Blocks

# Version 1: Hardcoded
def greet_alice():
    print("Hello, Alice!")

# Version 2: Parameterized  
def greet_person(name):
    print(f"Hello, {name}!")

# Version 3: Flexible and reusable
def create_greeting(name, time_of_day="day"):
    greetings = {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
        "day": "Hello"
    }
    return f"{greetings.get(time_of_day, 'Hello')}, {name}!"

# Version 4: Production-ready
def create_personalized_message(name, context="greeting", **kwargs):
    """
    Create contextual messages for various situations
    
    Args:
        name: Person's name
        context: Type of message ('greeting', 'farewell', 'reminder')
        **kwargs: Additional context-specific parameters
    """
    templates = {
        "greeting": "Hello, {name}! {extra}",
        "farewell": "Goodbye, {name}. {extra}",
        "reminder": "Hi {name}, remember to {extra}"
    }
    
    template = templates.get(context, "Hi {name}")
    extra_msg = kwargs.get('extra', '')
    
    return template.format(name=name, extra=extra_msg)

# Usage showing evolution
message = create_personalized_message(
    "Alice", 
    "reminder", 
    extra="submit your Python toolkit"
)
print(message)


# Common Pitfalls & Solutions

# Pitfall 1: Forgetting return
def calculate_bad(x, y):
    result = x + y  # Calculates but doesn't return!
    
def calculate_good(x, y):
    return x + y    # Returns the value

# Pitfall 2: Scope confusion
total = 0  # Global - avoid when possible

def update_total_bad():
    total = 100  # Creates local variable, doesn't update global

def update_total_good(current_total, amount):
    return current_total + amount  # Explicit and clear

# Pitfall 3: Mutable default arguments
def add_item_bad(item, list=[]):  # DON'T DO THIS
    list.append(item)
    return list

def add_item_good(item, list=None):  # DO THIS
    if list is None:
        list = []
    list.append(item)
    return list
