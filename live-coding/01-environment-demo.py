# W1D1 Live Coding: 01-environment-demo.py

# Without programming: Manual and repetitive
print("Monday: Study 2 hours")
print("Tuesday: Study 2 hours")
print("Wednesday: Study 2 hours")
# ... imagine typing this 365 times!

# With programming: Automated and smart
def create_study_schedule(hours_per_day, days):
    total_hours = hours_per_day * days
    print(f"Study Schedule: {hours_per_day}h/day for {days} days")
    print(f"Total commitment: {total_hours} hours")
    print(f"That's {total_hours * 60} minutes of learning!")

create_study_schedule(2, 30)  # One function call replaces 30 lines!
