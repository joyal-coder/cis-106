# Problem 3: Student Grade Calculator

# Input student demographics and scores
last_name = input("Enter student's last name: ")
midterm = float(input("Enter midterm score (0-100): "))
final_exam = float(input("Enter final exam score (0-100): "))

# Compute total points: 40% midterm and 60% final exam
total_points = (midterm * 0.40) + (final_exam * 0.60)

# Display student last name and total points
print(f"\nStudent: {last_name}")
print(f"Total Exam Points: {total_points:.2f}")
