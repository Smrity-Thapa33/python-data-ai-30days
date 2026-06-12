"""
Day 2 Mini Project – Student Report Card Generator
===================================================
Task: Build a program that reads a student's marks and produces a
formatted report card, applying arithmetic, logical, and conditional logic.

Program requirements:
1. Read student name, roll number, and marks in 3 subjects using input() + float()
2. Store student details in a dictionary
3. Calculate total and percentage using arithmetic operators
4. Decide pass/fail using logical operators (every subject >= 40 to pass)
5. Assign letter grade (A+, A, B, C, D, F) using if/elif/else chain
6. Use nested if + set membership test to award distinction remark
7. Set PASS/FAIL status using a ternary expression
8. Print neatly formatted report card using f-strings and separator lines
"""

print("=" * 50)
print("       STUDENT REPORT CARD GENERATOR")
print("=" * 50)

name       = input("Enter student name      : ")
roll       = input("Enter roll number       : ")
marks_math = float(input("Enter marks in Math     : "))
marks_sci  = float(input("Enter marks in Science  : "))
marks_eng  = float(input("Enter marks in English  : "))


student = {
    "name"        : name,
    "roll"        : roll,
    "Math"        : marks_math,
    "Science"     : marks_sci,
    "English"     : marks_eng,
}

TOTAL_MARKS = 300                                         
PASS_MARK   = 40                                          

total      = student["Math"] + student["Science"] + student["English"]
percentage = (total / TOTAL_MARKS) * 100


passed_all = (student["Math"]    >= PASS_MARK and
              student["Science"] >= PASS_MARK and
              student["English"] >= PASS_MARK)


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


if passed_all:
    if grade in {"A+", "A"}:                              
        remark = "Distinction — Outstanding Performance!"
    elif grade in {"B", "C"}:
        remark = "Merit — Good Performance!"
    else:
        remark = "Satisfactory Performance."
else:
    remark = "Did not meet minimum requirements."


status = "PASS" if passed_all else "FAIL"


print()
print("=" * 50)
print("            REPORT CARD")
print("=" * 50)
print(f"  Name        : {student['name']}")
print(f"  Roll Number : {student['roll']}")
print("-" * 50)
print(f"  {'Subject':<12}  {'Marks':>6}  {'Out Of':>6}  {'Status':>6}")
print("-" * 50)

for subject in ["Math", "Science", "English"]:
    sub_status = "Pass" if student[subject] >= PASS_MARK else "Fail"
    print(f"  {subject:<12}  {student[subject]:>6.1f}  {'100':>6}  {sub_status:>6}")

print("-" * 50)
print(f"  {'Total':<12}  {total:>6.1f}  {'300':>6}")
print(f"  {'Percentage':<12}  {percentage:>5.2f}%")
print("-" * 50)
print(f"  Grade       : {grade}")
print(f"  Status      : {status}")
print(f"  Remark      : {remark}")
print("=" * 50)