# STUDENT REPORT CARD GENERATOR USING PYTHON tuple


print("\n----------- STUDENTS REPORT CARD OF CLASS 'XTH' -----------")
max_avg = 0
topper = ""

students = [
    ("Nandini", (85, 90, 78), 101, "painting", "reading"),
    ("Isha", (72, 88, 91), 102, "chess"),
    ("Anant", (100,99,96), 105, "chess", "reading"),
    ("Naina", (95, 92, 89), 103, "football", "gaming"),
    ("Arnish", (56,85,96), 104, "dancing", "swimming", "gaming")
]

# Accessing each item of tuple using loops
for name, scores, enroll, *hobbies in students:
    print(f"\n📄 Report Card for {name} (Roll No: {enroll})")

    # unpacking scores (tuple)
    math, sci, eng = scores
    print(f"- Scores : Math : {math}, Science: {sci}, English : {eng}")

    # calculation of average. to get maximum average score
    avg = sum(scores) / len(scores)
    if avg > max_avg:
        # update maximum average and name of student
        max_avg = avg
        topper = name
    print(f"- Average : {avg:.2f}")
    print(f"- Hobbies : {', '.join(hobbies)}")

print("\n--------------- CLASS TOPPER ANNOUNCEMENT ------------------\n")

# print topper's result
print(f"CLASS TOPPER : {topper} ({max_avg:.2f} Average)\n")

