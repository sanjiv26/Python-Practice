# Day 2 — Error Handling
# Sanjiv V | github.com/sanjiv26

# ── Basic try/except ───────────────────────────
def safe_divide(a, b):
    try:
        value = a / b
        return value
    except TypeError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Can't divide by zero!")

print("── safe_divide tests ──")
print(safe_divide(10, 2))   # 5.0
safe_divide(10, 0)           # Can't divide by zero!
safe_divide(10, "x")         # Invalid input!

# ── finally — always runs ──────────────────────
print("\n── finally example ──")
try:
    age = int("hello")       # this will fail
except ValueError:
    print("Invalid value caught!")
finally:
    print("This always runs, error or not.")

# ── Real-world pattern: retry until valid input ─
def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

print("\n── retry until valid input ──")
a = get_valid_number("Enter first number: ")
b = get_valid_number("Enter second number: ")
result = safe_divide(a, b)
if result is not None:
    print(f"{a} / {b} = {result}")