# Day 4 — JSON
# Sanjiv V | github.com/sanjiv26

import json

# ── Part 1: Create and save profile to JSON file ──
profile = {
    "name": "Sanjiv",
    "role": "Senior Python Automation Engineer",
    "skills": ["Python", "Pytest", "Selenium", "Docker"],
    "experience_years": 4,
    "fav_sport": "Cricket"
}

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=4)

print("profile.json created!")

# ── Part 2: Read it back and print ────────────────
with open("profile.json", "r") as f:
    profile_data = json.load(f)

print(profile_data["name"])

for skill in profile_data["skills"]:
    print(skill)

print(f"Favourite sport: {profile_data['fav_sport']}")

# ── Part 3: Add new key and save back ─────────────
profile_data["available"] = True

with open("profile.json", "w") as f:
    json.dump(profile_data, f, indent=4)

print("\nUpdated profile.json with available: True")

# ── Bonus: json.loads and json.dumps (string versions) ──
api_response = '''
[
    {"name": "Sanjiv", "role": "Automation Engineer", "salary": 85000},
    {"name": "Priya", "role": "Data Engineer", "salary": 92000},
    {"name": "Ravi", "role": "DevOps Engineer", "salary": 78000}
]
'''

employees = json.loads(api_response)

print("\n── API Response Parsed ──")
for emp in employees:
    print(f"{emp['name']} — {emp['role']} — ₹{emp['salary']:,}")