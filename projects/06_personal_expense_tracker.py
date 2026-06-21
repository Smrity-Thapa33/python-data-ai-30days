"""
Assignment 2 — Personal Expense Tracker
=========================================
Week 2 · Dlytica Data and AI Foundations Track
Topics: File Handling, Dictionaries, List Comprehensions, Error Handling
"""

import os

def load_expenses(filename):
    """Read expenses from file. Return list of (category, amount) tuples.
    Returns empty list if file does not exist."""
    try:
        expenses = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    category, amount = line.split(",")
                    expenses.append((category.strip(), float(amount.strip())))
        return expenses
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty list.")
        return []


def add_expense(filename, category, amount):
    """Append a new expense to the file. Raise ValueError if amount <= 0."""
    if amount <= 0:
        raise ValueError(f"Amount must be a positive number. Got: {amount}")
    with open(filename, "a") as f:
        f.write(f"{category},{amount}\n")
    print(f"Added: {category} → ${amount:.2f}")


def category_totals(expenses):
    """Group and sum spending per category. Print totals and grand total."""
    totals = {}
    for cat, amount in expenses:
        totals[cat] = totals.get(cat, 0) + amount

    grand_total = sum(totals.values())

    W = 40
    print("\n" + "=" * W)
    print(f"  {'Category':<16} {'Total':>10}")
    print("─" * W)
    for cat, total in totals.items():
        print(f"  {cat:<16} : ${total:>8.2f}")
    print("─" * W)
    print(f"  {'Grand Total':<16} : ${grand_total:>8.2f}")
    print("=" * W)

    return totals


def above_threshold(expenses, limit):
    """Return all (category, amount) tuples where amount exceeds limit."""
    return [(c, a) for c, a in expenses if a > limit]   

FILENAME = "expenses.txt"

if not os.path.exists(FILENAME):
    sample = "Food,150\nTransport,60\nFood,200\nEntertainment,120\nUtilities,300\nTransport,45\n"
    with open(FILENAME, "w") as f:
        f.write(sample)
    print(f"Created sample '{FILENAME}'")

expenses = load_expenses(FILENAME)
category_totals(expenses)

LIMIT = 100
above = above_threshold(expenses, LIMIT)
print(f"\n  Expenses above ${LIMIT}:")
for cat, amt in above:
    print(f"    {cat:<14} → ${amt:.2f}")

print("\n--- Adding a new expense ---")
try:
    add_expense(FILENAME, "Food", 85)
    add_expense(FILENAME, "Gym", -50)    
except ValueError as e:
    print(f"Error caught gracefully: {e}")

print("\n--- Updated totals after adding new expense ---")
expenses = load_expenses(FILENAME)
category_totals(expenses)