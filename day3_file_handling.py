# Day 3 — File Handling
# Sanjiv V | github.com/sanjiv26

# ── Read file, process data, find top student ──
try:
    with open("students.txt", "r") as students:
        score_list = []
        for student in students:
            strip_line = student.strip()
            split_line = strip_line.split(",")
            name = split_line[0]
            score = int(split_line[1])
            score_list.append({"name": name, "score": score})

        max_score = max(score_list, key=lambda s: s["score"])
        print(f"Top Student: {max_score['name']} with {max_score['score']}")

    # ── Write result to a new file ─────────────
    with open("top_student.txt", "w") as top_student:
        top_student.write(
            f"Top Student: {max_score['name']} with {max_score['score']}\n"
        )
        print("Result written to top_student.txt")

except FileNotFoundError:
    print("students.txt not found — please create the file first.")

# ── Append mode example ────────────────────────
with open("top_student.txt", "a") as log:
    log.write("Processed on: 2026-07-11\n")

# ── Reading the result file back ───────────────
print("\n── Contents of top_student.txt ──")
with open("top_student.txt", "r") as result:
    print(result.read())