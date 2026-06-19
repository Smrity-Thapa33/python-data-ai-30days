"""
Assignment 1 — Student Grade Analyser
======================================
Week 2 · Dlytica Data and AI Foundations Track
Topics: Loops, Dictionaries, Functions, Error Handling
"""

def letter_grade(score):
    """Return a letter grade for a score (0–100). Raise ValueError if out of range."""
    if not (0 <= score <= 100):
        raise ValueError(f"Invalid score: {score}. Must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def analyse(students):
    """
    Accept {name: score} and return {name: {"score": ..., "grade": ...}}.
    Calls letter_grade() for each student.
    """
    results = {}
    for name, score in students.items():
        grade = letter_grade(score)
        results[name] = {"score": score, "grade": grade}
    return results


def summary(results):
    """Print class statistics: average, highest, lowest, grade counts."""
    scores      = {name: results[name]["score"] for name in results}
    total       = sum(scores.values())
    average     = total / len(scores)

    highest     = max(results, key=lambda k: results[k]["score"])
    lowest      = min(results, key=lambda k: results[k]["score"])

    counts = {}
    for data in results.values():
        g = data["grade"]
        counts[g] = counts.get(g, 0) + 1

    W = 45
    print("=" * W)
    print("           STUDENT GRADE REPORT")
    print("=" * W)
    for name in sorted(results):
        s = results[name]["score"]
        g = results[name]["grade"]
        print(f"  {name:<10} : {s:>3} → {g}")

    print("-" * W)
    print(f"  Class Average : {average:.2f}")
    print(f"  Highest Score : {highest} ({results[highest]['score']})")
    print(f"  Lowest Score  : {lowest} ({results[lowest]['score']})")
    print("-" * W)

    grade_line = "  Grade Counts  : " + "  ".join(
        f"{g}={counts.get(g, 0)}" for g in ["A", "B", "C", "D", "F"]
    )
    print(grade_line)
    print("=" * W)


students = {
    "Alice": 92, "Bob": 78, "Carol": 85,
    "Dave": 61, "Eve": 55, "Frank": 99
}

try:
    results = analyse(students)
    summary(results)
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Testing invalid score (110) ---")
students_invalid = {
    "Alice": 92, "Bob": 110  
}

try:
    results = analyse(students_invalid)
    summary(results)
except ValueError as e:
    print(f"Error caught gracefully: {e}")