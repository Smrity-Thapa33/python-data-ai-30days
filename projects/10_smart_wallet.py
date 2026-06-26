# Name: Smrity Thapa
# Approach: Money class with dunder methods for arithmetic and comparison;
# Wallet holds a list of Money objects and uses __len__ and a total() method.

"""
Assignment 2 — Smart Wallet with Money Objects
================================================
Week 3 · Dlytica Data and AI Foundations Track
Topics: Dunder methods, Operator overloading, __str__ / __repr__, Sorting
"""

class Money:
    def __init__(self, amount, currency="Rs"):
        self.amount   = amount
        self.currency = currency

    def __str__(self):
        """Human-readable: Rs 500"""
        return f"{self.currency} {self.amount}"

    def __repr__(self):
        """Developer-readable: Money(500, 'Rs')"""
        return f"Money({self.amount}, '{self.currency}')"

    def __add__(self, other):
        """Return a new Money with combined amounts (assumes same currency)."""
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        """True if amounts are equal."""
        return self.amount == other.amount

    def __lt__(self, other):
        """True if this amount is less than the other — enables sorted()."""
        return self.amount < other.amount


class Wallet:
    def __init__(self, notes):
        self.notes = notes             

    def __len__(self):
        """Return number of notes in the wallet."""
        return len(self.notes)

    def total(self):
        """Return total value as a Money object."""
        result = Money(0, self.notes[0].currency if self.notes else "Rs")
        for note in self.notes:
            result = result + note
        return result


print("=" * 50)
print("       SMART WALLET — TEST RUN")
print("=" * 50)

a = Money(500)
b = Money(300)

print(f"\n  a = {a}")
print(f"  b = {b}")

print(f"\n  a + b        : {a + b}")           
print(f"  a == Money(500): {a == Money(500)}") 
print(f"  b < a        : {b < a}")             
print(f"  repr(a)      : {repr(a)}")           

print("\n-- Sorting --")
notes = [Money(100), Money(500), Money(50)]
print(f"  Unsorted : {[str(n) for n in notes]}")
print(f"  Sorted   : {[str(n) for n in sorted(notes)]}")

print("\n-- Wallet --")
w = Wallet(notes)
print(f"  Notes in wallet : {len(w)}")         
print(f"  Total           : {w.total()}")       

print("=" * 50)