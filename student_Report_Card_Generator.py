# STUDENT REPORT CARD GENERATOR USING PYTHON tuple

# 📄 Report Card for Alice (Roll No: 101)
# - Scores: Math: 85, Science: 90, English: 78
# - Average: 84.33
# - Hobbies: painting, reading

# -----------------------------------

# Class Topper: Charlie (92.00 average)

max_avg = 0
topper = ""

students = [
    ("Alice", (85, 90, 78), 101, "painting", "reading"),
    ("Bob", (72, 88, 91), 102, "chess"),
    ("Charlie", (95, 92, 89), 103, "football", "gaming")
]

# Accessing each item of tuple using loops
for name, scores, enroll, *hobbies in students:
    print(f"\n📄 Repost Card for {name} (Roll No: {enroll})")

    # unpacking scores (tuple)
    math, sci, eng = scores
    print(f"- Scores : Math : {math}, Science: {sci}, English : {eng}")

    # calculation of average. to get maximum average score
    avg = sum(scores) / len(scores)
    if avg >= max_avg:
        # update maximum average and name of student
        max_avg = avg
        topper = name
    print(f"- Average {avg:.2f}")
    print(f"- Hobbies : {', '.join(hobbies)}")

