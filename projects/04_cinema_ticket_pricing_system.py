"""
Day 4 Mini Project – Cinema Ticket Pricing System
==================================================
Demonstrates: if/elif/else, logical operators, set membership,
nested if, ternary expression, and f-strings.
"""

BASE_PRICE    = 500.00   
WEEKDAYS      = {"monday", "tuesday", "wednesday", "thursday", "friday"}

print("=" * 52)
print("        CINEMA TICKET PRICING SYSTEM")
print("=" * 52)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number. Try again.")

age       = get_int("Enter your age                : ")
day       = input("Enter day of the week         : ").strip().lower()
answer    = input("Are you a member? (yes/no)    : ").strip().lower()
is_member = answer == "yes"                              


if age < 5:
    category       = "Child (Under 5)"
    price          = 0.00
    age_discount   = 100
elif age < 18:
    category       = "Minor (5–17)"
    price          = BASE_PRICE * 0.50
    age_discount   = 50
elif age >= 60:
    category       = "Senior (60+)"
    price          = BASE_PRICE * 0.70
    age_discount   = 30
else:
    category       = "Adult"
    price          = BASE_PRICE
    age_discount   = 0


is_weekday        = day in WEEKDAYS                      
member_discount   = is_member and is_weekday             

if member_discount:
    price = price * 0.90                                 

if is_member:
    if is_weekday:
        popcorn = "Large popcorn — FREE!"
    else:
        popcorn = "Small popcorn — FREE!"
else:
    popcorn = "No popcorn offer."

message = "Free entry — enjoy the show!" if price == 0 else "Enjoy the show!"


W = 52

print()
print("=" * W)
print("             TICKET SUMMARY")
print("=" * W)
print(f"  Customer Category : {category}")
print(f"  Day               : {day.title()}")
print(f"  Member            : {'Yes' if is_member else 'No'}")
print("-" * W)
print(f"  Base Price        : NPR {BASE_PRICE:.2f}")
print(f"  Age Discount      : {age_discount}%")
print(f"  Member + Weekday  : {'10% off' if member_discount else 'Not applicable'}")
print("-" * W)
print(f"  Final Price       : NPR {price:.2f}")
print(f"  Popcorn Offer     : {popcorn}")
print("-" * W)
print(f"  {message}")
print("=" * W)