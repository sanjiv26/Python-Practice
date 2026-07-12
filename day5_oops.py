# Day 5 — OOP (Object Oriented Programming)
# Sanjiv V | github.com/sanjiv26

# ── Base class ─────────────────────────────────
class AutomationEngineer:
    def __init__(self, name, company, skills):
        self.name = name
        self.company = company
        self.skills = skills

    def introduce(self):
        print(f"I am {self.name}, working at {self.company}, skilled in {', '.join(self.skills)}")

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"Skill added: {skill}")

    def is_senior(self):
        return len(self.skills) > 3

# ── Inherited class ────────────────────────────
class SeniorEngineer(AutomationEngineer):
    def __init__(self, name, company, skills, team_size):
        super().__init__(name, company, skills)   # run parent __init__ first
        self.team_size = team_size                 # then add new attribute

    def mentor(self):
        print(f"{self.name} is mentoring a team of {self.team_size} engineers")

# ── Test base class ────────────────────────────
print("── AutomationEngineer ──")
eng = AutomationEngineer("Priya", "TCS", ["Python", "Selenium"])
eng.introduce()
print(eng.is_senior())       # False — only 2 skills
eng.add_skill("Docker")
eng.add_skill("Pytest")
print(eng.is_senior())       # True — now 4 skills

# ── Test inherited class ───────────────────────
print("\n── SeniorEngineer ──")
senior = SeniorEngineer("Sanjiv", "Sony", ["Python", "Pytest", "Docker", "RAG"], 5)
senior.introduce()
senior.mentor()
print(senior.is_senior())    # True — 4 skills
senior.add_skill("Agents")
senior.introduce()