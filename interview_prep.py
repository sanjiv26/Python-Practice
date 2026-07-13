# Interview Prep — Data Structures & Problem Solving
# Sanjiv V | github.com/sanjiv26

# ── Problem 1: Find duplicates in a list ──────────
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

print(find_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5]))   # {1, 5}

# ── Problem 2: Highest paid in a department ───────
employees = [
    {"name": "Sanjiv",  "salary": 85000, "dept": "Engineering"},
    {"name": "Priya",   "salary": 92000, "dept": "Marketing"},
    {"name": "Ravi",    "salary": 78000, "dept": "Engineering"},
    {"name": "Ashwi",   "salary": 95000, "dept": "Marketing"},
    {"name": "Meena",   "salary": 72000, "dept": "Engineering"}
]

def highest_in_dept(employees, dept):
    filtered = [e for e in employees if e["dept"] == dept]
    return max(filtered, key=lambda e: e["salary"])

result = highest_in_dept(employees, "Engineering")
print(f"Highest in Engineering: {result['name']} — ₹{result['salary']:,}")

# ── Problem 3: Group by department + average salary
def group_by_dept(employees):
    groups = {}
    for emp in employees:
        dept = emp["dept"]
        if dept not in groups:
            groups[dept] = []
        groups[dept].append(emp["salary"])

    averages = {}
    for dept, salaries in groups.items():
        averages[dept] = sum(salaries) // len(salaries)
    return averages

print(group_by_dept(employees))

# ── Problem 4: Remove duplicates preserving order ─
def remove_dupes(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

print(remove_dupes([3, 1, 3, 2, 1, 4]))   # [3, 1, 2, 4]

# ── Problem 5: Most frequent element ──────────────
def most_frequent(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=lambda k: counts[k])

print(most_frequent([1, 2, 2, 3, 3, 3]))   # 3