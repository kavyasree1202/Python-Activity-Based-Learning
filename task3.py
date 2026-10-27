
# University Scholarship Allocation System

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_FAMILY_INCOME = 250000

# Student details:
# [Name, Subject Marks, Attendance, Family Income]

applicants = [
    ["Alice", [85, 90, 80], 95, 150000],
    ["Bob", [78, 82, 75], 85, 200000],
    ["Charlie", [90, 55, 88], 92, 100000],
    ["David", [80, 80, 80], 90, 180000],
    ["Eva", [88, 92, 85], 70, 120000],
    ["Frank", [80, 80, 80], 90, 180000],
    ["Grace", [76, 78, 80], 80, 240000]
]

eligible_students = []
rejected_students = []

# Step 1: Evaluate eligibility
for student in applicants:
    name, marks, attendance, income = student

    aggregate = sum(marks) / len(marks)

    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below minimum")

    if min(marks) < MIN_SUBJECT_MARK:
        reasons.append("Subject mark below minimum")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below minimum")

    if income > MAX_FAMILY_INCOME:
        reasons.append("Family income exceeds limit")

    if not reasons:
        eligible_students.append({
            "name": name,
            "marks": marks,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })
    else:
        rejected_students.append((name, reasons))

# Step 2: Rank eligible students
# Tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Alphabetical order

eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

# Step 3: Display eligible students
print("UNIVERSITY SCHOLARSHIP RESULTS")
print("=" * 65)

print("\nELIGIBLE STUDENTS - RANKING")
print("-" * 65)

if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(f"\nRank: {rank}")
        print("Name:", student["name"])
        print("Aggregate:", round(student["aggregate"], 2))
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])
else:
    print("No eligible applicants found.")

# Step 4: Display rejected students and reasons
print("\nREJECTED APPLICANTS")
print("-" * 65)

if rejected_students:
    for name, reasons in rejected_students:
        print(name, ":", ", ".join(reasons))
else:
    print("No rejected applicants.")

# Step 5: Allocate scholarships
# Example: Only the top 3 eligible students receive scholarships
SCHOLARSHIP_SLOTS = 3

print("\nFINAL SCHOLARSHIP ALLOCATION")
print("-" * 65)

winners = eligible_students[:SCHOLARSHIP_SLOTS]

for rank, student in enumerate(winners, start=1):
    print(f"{rank}. {student['name']} - Scholarship Awarded")

print("\nTotal Applicants:", len(applicants))
print("Eligible Applicants:", len(eligible_students))
print("Rejected Applicants:", len(rejected_students))
print("Scholarships Awarded:", len(winners))
