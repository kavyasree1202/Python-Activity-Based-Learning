
# Student Marks Matrix Analysis

students = ["Alice", "Bob", "Charlie", "David", "Eva"]
subjects = ["Maths", "Science", "English", "Python"]

# Rows represent students; columns represent subjects
marks = [
    [85, 90, 78, 95],
    [60, 55, 65, 70],
    [35, 40, 45, 30],
    [90, 88, 92, 96],
    [70, 75, 80, 85]
]

low_average_threshold = 40

# Row-wise statistics
print("STUDENT-WISE ANALYSIS")
print("-" * 40)

student_averages = []

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    highest = max(marks[i])
    lowest = min(marks[i])

    student_averages.append(average)

    print(f"\nStudent: {students[i]}")
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)

# Identify top performers
highest_average = max(student_averages)

print("\nTOP PERFORMER(S)")
for i in range(len(students)):
    if student_averages[i] == highest_average:
        print(students[i], "- Average:", round(highest_average, 2))

# Column-wise statistics
print("\nSUBJECT-WISE ANALYSIS")
print("-" * 40)

subject_averages = []

for j in range(len(subjects)):
    column_marks = [marks[i][j] for i in range(len(students))]

    total = sum(column_marks)
    average = total / len(students)

    subject_averages.append(average)

    print(f"\nSubject: {subjects[j]}")
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Mark:", max(column_marks))
    print("Lowest Mark:", min(column_marks))

# Detect subjects with low average performance
print("\nSUBJECTS WITH LOW AVERAGE")
found = False
for j in range(len(subjects)):
    if subject_averages[j] < low_average_threshold:
        print(subjects[j], "- Average:",
              round(subject_averages[j], 2))
        found = True

if not found:
    print("No subjects have an average below",
          low_average_threshold)

# Overall class average
all_marks = [mark for row in marks for mark in row]
print("\nOVERALL CLASS AVERAGE:",
      round(sum(all_marks) / len(all_marks), 2))
