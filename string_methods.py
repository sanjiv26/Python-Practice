# String Methods Practice
# Sanjiv V | github.com/sanjiv26

s = "  Senior Python Automation Engineer  "

# ── Cleaning ───────────────────────────────────────
print(s.strip())          # removes spaces
print(s.strip().upper())  # chain methods
print(s.strip().lower())  # lowercase
print(s.strip().title())  # Title Case

# ── Searching ──────────────────────────────────────
print(s.find("Python"))   # index where Python starts
print("Python" in s)      # True — fastest check
print(s.count("e"))       # how many 'e' characters

# ── Splitting & joining ────────────────────────────
words = s.strip().split(" ")
print(words)
print(" | ".join(words))   # join with custom separator

# ── Real use case: parse CSV line ─────────────────
csv_line = "Sanjiv,25,Bangalore,Python"
parts = csv_line.split(",")
name, age, city, skill = parts   # unpacking
print(f"{name} is {age} years old from {city}, skilled in {skill}")

# ── Check content type ─────────────────────────────
print("12345".isdigit())    # True
print("Sanjiv".isalpha())   # True
print("abc123".isalnum())   # True
print("  ".isspace())       # True

# ── f-string formatting ────────────────────────────
salary = 2300000
print(f"Salary: ₹{salary:,}")       # ₹2,300,000
print(f"PI: {3.14159:.2f}")          # PI: 3.14
print(f"{'Sanjiv':>10}")             # right-align in 10 chars
print(f"{'Sanjiv':<10}|")           # left-align in 10 chars