# Name: Smrity Thapa
# Approach: Base class BankAccount with private __balance; SavingsAccount adds
# interest via a protected helper; CurrentAccount overrides withdraw for overdraft.
 
"""
Assignment 1 — Bank Account System
====================================
Week 3 · Dlytica Data and AI Foundations Track
Topics: Encapsulation, Inheritance, super(), Validation
"""

class BankAccount:
    def __init__(self, owner, opening_balance=0):
        self.owner     = owner
        self.__balance = opening_balance          

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            print("  ⚠  Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f" Deposited Rs {amount}. New balance: Rs {self.__balance}")

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance exists."""
        if amount <= 0:
            print("  Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print(f"  Not enough balance! Available: Rs {self.__balance}")
            return
        self.__balance -= amount
        print(f" Withdrawn Rs {amount}. New balance: Rs {self.__balance}")

    def get_balance(self):
        """Getter — read-only access to private balance."""
        return self.__balance

    def _update_balance(self, amount):
        """Protected helper for child classes to modify balance safely."""
        self.__balance += amount

    def __str__(self):
        return f"{self.__class__.__name__}(owner={self.owner}, balance=Rs {self.__balance})"


class SavingsAccount(BankAccount):
    def __init__(self, owner, opening_balance=0):
        super().__init__(owner, opening_balance)

    def add_interest(self, rate):
        """Add interest at given rate (%) to the balance."""
        interest = self.get_balance() * rate / 100
        self._update_balance(interest)
        print(f"  Interest of {rate}% added (Rs {interest:.2f}). New balance: Rs {self.get_balance():.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, owner, opening_balance=0, overdraft_limit=0):
        super().__init__(owner, opening_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Override withdraw to allow overdraft up to overdraft_limit."""
        if amount <= 0:
            print("  Withdrawal amount must be positive.")
            return
        if self.get_balance() - amount < -self.overdraft_limit:
            print(f"  Overdraft limit reached! Limit: Rs {self.overdraft_limit}")
            return
        self._update_balance(-amount)
        print(f" Withdrawn Rs {amount}. New balance: Rs {self.get_balance()}")


print("=" * 50)
print("         BANK ACCOUNT SYSTEM — TEST RUN")
print("=" * 50)

print("\n-- Savings Account --")
s = SavingsAccount("Asha", 1000)
s.deposit(500)
s.add_interest(10)                  
print(f"  Balance: Rs {s.get_balance()}")
s.withdraw(5000)                    

print("\n-- Current Account --")
c = CurrentAccount("Bibek", 200, overdraft_limit=500)
c.withdraw(600)                     
print(f"  Balance: Rs {c.get_balance()}")
c.withdraw(200)                     
print("\n-- Encapsulation Test --")
try:
    print(s.__balance)              
except AttributeError as e:
    print(f" Direct access blocked: {e}")

print("\n-- __str__ --")
print(f"  {s}")
print(f"  {c}")
print("=" * 50)