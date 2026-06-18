"""
Day 3 Mini Project – Personal Bio-Data Card
============================================
Demonstrates deliberate use of: str, int, float, bool,
tuple, list, set, and dict — one per kind of information.
"""

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number. Try again.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number. Try again.")


print("=" * 52)
print("          PERSONAL BIO-DATA CARD")
print("=" * 52)

name   = input("Full name          : ").strip().title()   
city   = input("City               : ").strip().title()   
age    = get_int("Age                : ")                 
height = get_float("Height (in cm)     : ")               


answer    = input("Are you a student? (yes/no): ").strip().lower()
is_student = answer == "yes"                              


print("\n  -- Date of Birth --")
birth_day   = get_int("  Day              : ")
birth_month = get_int("  Month            : ")
birth_year  = get_int("  Year             : ")

dob = (birth_day, birth_month, birth_year)                


print("\n  -- Hobbies (enter 3) --")
hobbies = []                                               
for i in range(1, 4):
    hobby = input(f"  Hobby {i}           : ").strip().title()
    hobbies.append(hobby)


print("\n  -- Languages (enter 3; duplicates will be dropped) --")
languages = set()                                          
for i in range(1, 4):
    lang = input(f"  Language {i}        : ").strip().title()
    languages.add(lang)


profile = {
    "name"       : name,
    "city"       : city,
    "age"        : age,
    "height_cm"  : height,
    "is_student" : is_student,
    "dob"        : dob,
    "hobbies"    : hobbies,
    "languages"  : languages,
}


first_letter    = profile["name"][0]                       
hobby_count     = len(profile["hobbies"])                  
language_count  = len(profile["languages"])               


W = 52

print()
print("=" * W)
print("             BIO-DATA CARD")
print("=" * W)
print(f"  Name          : {profile['name']}")
print(f"  Initial       : {first_letter}  ← name[0] (string indexing)")
print(f"  City          : {profile['city']}")
print("-" * W)
print(f"  Age           : {profile['age']}  \t{type(profile['age'])}")
print(f"  Height        : {profile['height_cm']} cm  \t{type(profile['height_cm'])}")
print(f"  Student       : {profile['is_student']}  \t{type(profile['is_student'])}")
print("-" * W)

dob_d, dob_m, dob_y = profile["dob"]
print(f"  Date of Birth : {dob_d:02d}/{dob_m:02d}/{dob_y}  \t{type(profile['dob'])}")
print("-" * W)

print(f"  Hobbies ({hobby_count})    : {type(profile['hobbies'])}")
for h in profile["hobbies"]:
    print(f"    • {h}")

print("-" * W)

print(f"  Languages ({language_count})  : {type(profile['languages'])}")
if language_count < 3:
    print(f"Duplicate detected — set kept only {language_count} unique value(s).")
for lang in profile["languages"]:
    print(f"    • {lang}")

print("-" * W)
print(f"  Profile type  : {type(profile)}")
print("=" * W)