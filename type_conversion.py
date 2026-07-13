# Type Conversion Practice
# Sanjiv V | github.com/sanjiv26

# ── String to number ───────────────────────────────
year = input("Enter birth year: ")
age = 2026 - int(year)
print(f"Your age is {age}")

# ── int() truncates, doesn't round ────────────────
print(int(3.9))    # 3 not 4
print(int(-3.9))   # -3 not -4
print(round(3.9))  # 4 — use round() if you want rounding

# ── bool() on empty containers ────────────────────
print(bool([]))    # False — empty list
print(bool([1]))   # True  — non-empty list
print(bool(""))    # False — empty string
print(bool("hi"))  # True  — non-empty string

# ── Converting between types ──────────────────────
lst = [3, 1, 2, 1, 3]
unique_sorted = sorted(set(lst))    # remove dupes + sort
print(unique_sorted)                 # [1, 2, 3]

# ── dict to list (keys only!) ─────────────────────
d = {"name": "Sanjiv", "age": 25}
print(list(d))           # ['name', 'age'] — keys only
print(list(d.values()))  # ['Sanjiv', 25]  — values
print(list(d.items()))   # [('name','Sanjiv'), ('age',25)]

# ── List comprehensions ────────────────────────────
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in nums if n % 2 == 0]
squares = [n ** 2 for n in nums]
even_squares = [n ** 2 for n in nums if n % 2 == 0]

print(evens)        # [2, 4, 6, 8, 10]
print(squares)      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(even_squares) # [4, 16, 36, 64, 100]