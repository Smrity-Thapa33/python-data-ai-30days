# Name: Smrity Thapa
# Approach: Abstract base class Employee enforces calculate_pay() contract;
# three child classes implement it differently — polymorphism handles the loop.

"""
Assignment 3 — Employee Payroll System
========================================
Week 3 · Dlytica Data and AI Foundations Track
Topics: Abstraction, abc.ABC, Inheritance, Polymorphism
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        """Every child must implement this — abstract contract."""
        pass

    def payslip(self):
        """Normal method — calls child's calculate_pay() via polymorphism."""
        print(f"  {self.name:<10} | Pay: Rs {self.calculate_pay()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"FullTimeEmployee({self.name})"


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate   = hourly_rate
        self.hours_worked  = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"PartTimeEmployee({self.name})"


class Contractor(Employee):
    def __init__(self, name, project_fee, projects):
        super().__init__(name)
        self.project_fee = project_fee
        self.projects    = projects

    def calculate_pay(self):
        return self.project_fee * self.projects

    def __str__(self):
        return f"Contractor({self.name})"


print("=" * 50)
print("       EMPLOYEE PAYROLL SYSTEM — TEST RUN")
print("=" * 50)

staff = [
    FullTimeEmployee("Asha",  monthly_salary=60000),
    PartTimeEmployee("Bibek", hourly_rate=500, hours_worked=80),
    Contractor("Chen",        project_fee=15000, projects=3),
]

print("\n-- Payslips --")
for emp in staff:
    emp.payslip()                              

total = sum(e.calculate_pay() for e in staff)
print(f"\n  Total Payroll : Rs {total}")

print("\n-- __str__ --")
for emp in staff:
    print(f"  {emp}")

print("\n-- Abstraction Test (Employee cannot be instantiated) --")
try:
    Employee("Test")
except TypeError as e:
    print(f" Caught: {e}")

print("=" * 50)