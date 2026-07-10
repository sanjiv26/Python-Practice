# Day 1 — Python Fundamentals Practice
# Sanjiv V | github.com/sanjiv26

# ── Variables & f-strings ──────────────────────
name = "Sanjiv"
age = 25
city = "Bangalore"
is_working = True
print(f"{name} is {age} years old, lives in {city}, and it is {is_working} that he is working")

# ── Functions ──────────────────────────────────
def calculate_age(birth_year):
    age = 2026 - int(birth_year)
    return age

current_age = calculate_age(input("Enter your birth year: "))
print(f"Your age is {current_age}")

# ── Lists & loops ──────────────────────────────
students = [
    ["Sanjiv", 85, ["Math", "Science"]],
    ["Priya", 92, ["English", "Art", "Music"]],
    ["Ravi", 78, ["History"]]
]

for student in students:
    name = student[0]
    subjects = student[2]
    print(f"{name} studies: {', '.join(subjects)}")

# ── Sorting ────────────────────────────────────
employees = [
    {"name": "Sanjiv", "dept": "Engineering", "salary": 85000},
    {"name": "Priya",  "dept": "Marketing",   "salary": 92000},
    {"name": "Ravi",   "dept": "Engineering",  "salary": 78000},
    {"name": "Ashwi",  "dept": "Marketing",    "salary": 95000}
]

sorted_employees = sorted(employees, key=lambda e: e["salary"], reverse=True)
print("\nEmployees by salary (highest first):")
for emp in sorted_employees:
    print(f"  {emp['name']} — ₹{emp['salary']}")

# ── Sets ───────────────────────────────────────
words = ["apple", "banana", "apple", "mango", "banana", "banana"]
seen = set()
duplicates = set()

for word in words:
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)

print(f"\nDuplicates found: {duplicates}")

# ── Bubble sort (optimized) ────────────────────
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

print(f"\nBubble sort: {bubble_sort([5, 1, 4, 2, 8])}")